"""Validate timing/media paths for a NEW composition, without fixture-specific counts."""
from pathlib import Path
import argparse,json,math
p=argparse.ArgumentParser();p.add_argument('manifest',type=Path);p.add_argument('--public',required=True,type=Path);a=p.parse_args()
m=json.loads(a.manifest.read_text());duration=m['duration'];fps=m['profile']['fps'];public=a.public.resolve()
def require(ok,msg):
 if not ok:raise ValueError(msg)
def media(src):
 path=(public/src).resolve();require(path.is_relative_to(public),'Media escapes public/: '+src);require(path.is_file(),'Missing media: '+src)
require(isinstance(duration,(int,float)) and math.isfinite(duration) and duration>0,'Invalid duration')
require(isinstance(fps,(int,float)) and math.isfinite(fps) and fps>0,'Invalid fps')
shots=m['shots'];require(bool(shots),'No shots');cursor=0;ids=set()
for s in shots:
 require(s['id'] not in ids,'Duplicate shot id');ids.add(s['id'])
 require(abs(s['start']-cursor)<1e-6,'Gap or overlap at '+s['id'])
 require(math.isfinite(s['end']) and s['end']>s['start'],'Invalid end at '+s['id']);cursor=s['end']
require(abs(cursor-duration)<1e-6,'Shots do not cover duration');media(m['audio'])
for fx in m.get('soundEffects',[]):
 require(0<=fx['time']<duration,'SFX outside duration');media(fx['src'])
 require(0<=fx.get('volume',1)<=1,'Invalid SFX gain')
for name,t in m.get('events',{}).items():require(isinstance(t,(int,float)) and 0<=t<duration,'Event outside duration: '+name)
for cue in m.get('cues',[]):require(0<=cue['start']<cue['end']<=duration+1e-6,'Cue outside duration; trim excerpt explicitly')
if 'voiceEnvelope' in m:
 require(len(m['voiceEnvelope'])==round(duration*fps),'Wrong envelope frame count')
 require(all(isinstance(x,(int,float)) and math.isfinite(x) and x>=0 for x in m['voiceEnvelope']),'Invalid envelope')
print(f'OK: {len(shots)} shots; {duration}s; {round(duration*fps)} frames; media/events/cues valid.')
