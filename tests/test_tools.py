import importlib.util,json,os,subprocess,sys,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SK=ROOT/'skills'
def module(skill,file):
    spec=importlib.util.spec_from_file_location(file,SK/skill/(file+'.py'))
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
class Tools(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.d=Path(self.temp.name)
    def tearDown(self):self.temp.cleanup()
    def run_tool(self,skill,file,*args,ok=True):
        env=dict(os.environ,PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1')
        p=subprocess.run([sys.executable,str(SK/skill/file),*map(str,args)],capture_output=True,text=True,encoding='utf-8',env=env)
        if ok:self.assertEqual(p.returncode,0,p.stderr)
        else:self.assertNotEqual(p.returncode,0)
        return p
    def test_retention_units_and_interpolation(self):
        for unit,scale in [('seconds',1),('percent',100/60),('fraction',1/60)]:
            f=self.d/'r.csv';f.write_text('position,retention\n'+'\n'.join(f'{x*scale},{100-x}' for x in range(0,61,5)))
            out=json.loads(self.run_tool('yt-retention','retention.py',f,'--x-unit',unit,'--y-unit','percent','--duration',60).stdout)
            self.assertAlmostEqual(out['opening_drop_percentage_points'],30)
        m=module('yt-retention','retention');self.assertEqual(m.analyze([(0,100),(20,80),(40,60)])['opening_drop_percentage_points'],30)
    def test_retention_reject_ambiguous_and_unsorted(self):
        f=self.d/'r.csv';f.write_text('x,y\n0,100\n30,80\n20,70')
        self.run_tool('yt-retention','retention.py',f,ok=False)
        self.run_tool('yt-retention','retention.py',f,'--x-unit','seconds','--y-unit','percent',ok=False)
    def test_retention_fraction_replay_missing_zero(self):
        m=module('yt-retention','retention');f=self.d/'r.csv';f.write_text('x,y\n0,1.2\n1,1.0')
        rows=m.load_csv(f,'fraction','fraction',60);self.assertEqual(rows,[(0,120),(60,100)])
        self.assertIsNone(m.analyze([(5,100),(40,70)])['opening_drop_percentage_points'])
    def test_transcript_list_and_object(self):
        for obj in [[{'start':0,'end':2,'text':'hello'}],{'segments':[{'start':0,'end':2,'text':'hello'}]}]:
            f=self.d/'t.json';f.write_text(json.dumps(obj));out=json.loads(self.run_tool('yt-edit','deadair.py',f,'--json').stdout);self.assertEqual(out['duration'],2)
    def test_srt_vtt_chapters(self):
        for ext in ['srt','vtt']:
            f=self.d/('t.'+ext)
            cues='\n\n'.join(f'{i+1}\n00:00:{i*10:02d}.000 --> 00:00:{i*10+9:02d}.000\nScene topic number {i}' for i in range(6))
            f.write_text(('WEBVTT\n\n' if ext=='vtt' else '')+cues)
            out=json.loads(self.run_tool('yt-chapters','chapters.py',f,'--target',3,'--json').stdout);self.assertTrue(out['valid']);self.assertEqual(len(out['chapters']),3)
    def test_title_no_number_penalty_and_four_words(self):
        out=json.loads(self.run_tool('yt-package','title.py','--title','Maya Sees Tomorrow','--thumb','NOT WHAT SHE EXPECTED','--json').stdout)[0]
        keys=[x[0] for x in out['issues']];self.assertNotIn('no-number',keys);self.assertIn('thumb-length',keys)
    def test_hook_and_swipe(self):
        h=json.loads(self.run_tool('yt-script','hookscore.py','--hook','Why did Maya see tomorrow before the phone rang?','--json').stdout);self.assertEqual(len(h),1)
        f=self.d/'v.json';f.write_text(json.dumps([{'channel':'A','title':'Test','views':v,'url':'https://example.com'} for v in [10,20,30,100]]))
        o=json.loads(self.run_tool('yt-viral','swipe.py',f,'--min',2,'--json').stdout);self.assertEqual(o['outliers'][0]['multiple'],4)
        f.write_text('[{"channel":"A","title":"No views"}]');self.run_tool('yt-viral','swipe.py',f,ok=False)
    def test_skill_links_and_metadata(self):
        import re
        self.assertEqual(len(list(SK.glob('*/SKILL.md'))),11)
        for p in SK.glob('*/SKILL.md'):
            text=p.read_text(encoding='utf-8');self.assertTrue(text.startswith('---\nname: '+p.parent.name));self.assertNotIn('~/.claude',text)
            for link in re.findall(r'\]\(([^)]+)\)',text):self.assertTrue((p.parent/link).is_file(),link)
        self.assertEqual(json.loads((ROOT/'plugin.json').read_text())['name'],'youtube-agent-skills')
if __name__=='__main__':unittest.main(verbosity=2)
