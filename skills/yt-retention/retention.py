"""Analyze two-column retention data with explicit units; no causal verdicts."""
import argparse, csv, json, math, sys
from pathlib import Path

def load_csv(path, x_unit, y_unit, duration=None):
    if x_unit != 'seconds' and (duration is None or duration <= 0):
        raise ValueError('Percent/fraction positions require positive --duration')
    rows=[]
    with open(path,encoding='utf-8-sig',newline='') as f:
        for line,r in enumerate(csv.reader(f),1):
            if not r or not any(c.strip() for c in r): continue
            if len(r)!=2: raise ValueError(f'Line {line}: expected exactly two columns')
            try: x,y=(float(c.strip().rstrip('%')) for c in r)
            except ValueError:
                if line==1: continue
                raise ValueError(f'Line {line}: invalid numeric data')
            if not all(math.isfinite(v) for v in (x,y)) or x<0 or y<0:
                raise ValueError(f'Line {line}: negative or nonfinite value')
            if x_unit=='percent':
                if x>100: raise ValueError('Position percent exceeds 100')
                x=x*duration/100
            elif x_unit=='fraction':
                if x>1: raise ValueError('Position fraction exceeds 1')
                x=x*duration
            if y_unit=='fraction': y*=100
            if duration is not None and x>duration+1e-6: raise ValueError('Position exceeds duration')
            if rows and x<=rows[-1][0]: raise ValueError('Positions must strictly increase')
            rows.append((x,y))
    if len(rows)<2: raise ValueError('At least two data points required')
    return rows

def interpolate(rows,t):
    for (a,y),(b,z) in zip(rows,rows[1:]):
        if a<=t<=b: return y+(z-y)*(t-a)/(b-a)
    raise ValueError('Time outside observed range')

def analyze(rows,opening=30):
    if opening<=0: raise ValueError('Opening seconds must be positive')
    start_t,start=rows[0]; end_t=min(opening,rows[-1][0])
    opening_change=None
    if start_t==0 and end_t>0: opening_change=start-interpolate(rows,end_t)
    drops=[{'from_seconds':a,'to_seconds':b,'drop_percentage_points':round(y-z,4),
            'rate_pp_per_second':round((y-z)/(b-a),6)}
           for (a,y),(b,z) in zip(rows,rows[1:]) if y>z]
    drops.sort(key=lambda r:r['rate_pp_per_second'],reverse=True)
    mid_start=max(opening,start_t)
    mid_rate=((interpolate(rows,mid_start)-rows[-1][1])/(rows[-1][0]-mid_start)
              if rows[-1][0]>mid_start else None)
    return {'points':len(rows),'observed_start_seconds':start_t,'observed_end_seconds':rows[-1][0],
            'opening_end_seconds':end_t,'opening_drop_percentage_points':None if opening_change is None else round(opening_change,4),
            'opening_covers_30_seconds':start_t==0 and rows[-1][0]>=30,
            'largest_decline_intervals':drops[:5], 'net_after_opening_pp_per_second':mid_rate,
            'caution':'Interval changes are descriptive, not exact exit times or causal diagnoses. Opening needs time zero; short coverage is partial.'}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('csv');p.add_argument('--x-unit',required=True,choices=['seconds','percent','fraction'])
    p.add_argument('--y-unit',required=True,choices=['percent','fraction'])
    p.add_argument('--duration',type=float);p.add_argument('--opening-seconds',type=float,default=30)
    p.add_argument('--transcript');p.add_argument('--json',action='store_true')
    a=p.parse_args()
    try:
        if a.duration is not None and (not math.isfinite(a.duration) or a.duration<=0): raise ValueError('Invalid duration')
        rows=load_csv(a.csv,a.x_unit,a.y_unit,a.duration); out=analyze(rows,a.opening_seconds)
        if a.transcript:
            sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'yt-edit'))
            from deadair import load
            cues=load(a.transcript)
            for d in out['largest_decline_intervals']:
                d['transcript']=' '.join(t for s,e,t in cues if s<=d['to_seconds'] and e>=d['from_seconds'])
    except (ValueError,OSError,KeyError,TypeError) as e: p.error(str(e))
    print(json.dumps(out,ensure_ascii=False,indent=2))
if __name__=='__main__': main()
