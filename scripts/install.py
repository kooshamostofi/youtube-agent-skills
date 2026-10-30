"""Install all skills together without overwriting existing folders."""
import argparse
from pathlib import Path
import shutil

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--target',required=True,type=Path)
    a=p.parse_args(); target=a.target.expanduser().resolve()
    root=Path(__file__).resolve().parents[1]
    folders=sorted((root/'skills').glob('yt-*'))
    conflicts=[str(target/d.name) for d in folders if (target/d.name).exists()]
    if conflicts:p.error('Existing destinations; nothing installed: '+', '.join(conflicts))
    target.mkdir(parents=True,exist_ok=True)
    for d in folders:
        out=target/d.name
        shutil.copytree(d,out,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        shutil.copy2(root/'LICENSE',out/'LICENSE')
    print(f'Installed {len(folders)} skills into {target}')
if __name__=='__main__':main()
