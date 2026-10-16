"""Check the portable skill's immutable reference project without network/dependencies."""
from pathlib import Path
import hashlib,json,re,zipfile
ROOT=Path(__file__).resolve().parents[1]
def check():
 p=json.loads((ROOT/'assets/profile.json').read_text())
 archive=ROOT/p['projectArchive']['path']
 if hashlib.sha256(archive.read_bytes()).hexdigest()!=p['projectArchive']['sha256']:
  raise ValueError('Reference archive SHA-256 mismatch')
 with zipfile.ZipFile(archive) as z:
  for name,digest in p['projectArchive']['fileHashes'].items():
   if hashlib.sha256(z.read(name)).hexdigest()!=digest:raise ValueError('Changed fixture: '+name)
  m=json.loads(z.read('project/final-minute-timeline.json'))
  assert m['duration']==p['golden']['durationSeconds']
  assert len(m['shots'])==p['golden']['shotCount']
  assert len(m['soundEffects'])==p['golden']['sfxPlacements']
  assert len(m['voiceEnvelope'])==p['golden']['frames']
 for doc in [ROOT/'SKILL.md',*(ROOT/'references').glob('*.md')]:
  for target in re.findall(r'\]\(([^)]+)\)',doc.read_text()):
   if '://' not in target and not (doc.parent/target.split('#')[0]).exists():raise ValueError('Broken link: '+target)
 print('Bundle OK: reference hash, source hashes, 62.4s/1872 frames, 18 shots, 32 SFX, local links.')
 return archive
if __name__=='__main__':check()
