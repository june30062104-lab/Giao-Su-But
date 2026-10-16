"""Extract the exact final project into a NEW/EMPTY directory; never overwrite work."""
from pathlib import Path,PurePosixPath
import argparse,shutil,stat,zipfile
from check_bundle import check
p=argparse.ArgumentParser();p.add_argument('destination',type=Path);args=p.parse_args()
archive=check();dest=args.destination.expanduser().resolve()
if dest.exists() and (not dest.is_dir() or any(dest.iterdir())):
 p.error('Destination must be a new or empty directory; no files overwritten.')
with zipfile.ZipFile(archive) as z:
 for item in z.infolist():
  name=PurePosixPath(item.filename)
  if name.is_absolute() or '..' in name.parts or '\\' in item.filename or stat.S_ISLNK(item.external_attr>>16):
   p.error('Unsafe archive member: '+item.filename)
 dest.mkdir(parents=True,exist_ok=True)
 for item in z.infolist():
  path=dest/item.filename
  if item.is_dir():path.mkdir(parents=True,exist_ok=True)
  else:
   path.parent.mkdir(parents=True,exist_ok=True)
   with z.open(item) as src,path.open('xb') as out:shutil.copyfileobj(src,out)
print('Project ready:',dest)
print('Next: cd into this directory; npm install; npm run typecheck; npm run studio')
