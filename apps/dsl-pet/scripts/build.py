#!/usr/bin/env python3
from pathlib import Path
import json, plistlib, shutil, subprocess
root=Path(__file__).resolve().parents[1]
assets=root/'assets'
if not assets.is_dir():
 raise SystemExit('Missing apps/dsl-pet/assets. Supply animation assets that you are licensed to use; see the root README.')
required=[assets/'animations.json',assets/'待机.png']
missing=[p for p in required if not p.is_file()]
if missing:
 raise SystemExit('Missing required pet assets: '+', '.join(str(p.relative_to(root.parent.parent)) for p in missing))
manifest=json.loads((assets/'animations.json').read_text())
for a in manifest:
 required=[assets/a['key']/'animation.json',assets/a['key']/'逐帧PNG']
 missing.extend(p for p in required if not p.exists())
 if (assets/a['key']/'逐帧PNG').is_dir():
  missing.extend(assets/a['key']/'逐帧PNG'/f'frame-{n:02d}.png' for n in range(1,a['frame_count']+1) if not (assets/a['key']/'逐帧PNG'/f'frame-{n:02d}.png').is_file())
if missing:
 raise SystemExit('Missing animation assets: '+', '.join(str(p) for p in missing))
app=root/'dist/DSLPet.app';mac=app/'Contents/MacOS';res=app/'Contents/Resources';mac.mkdir(parents=True,exist_ok=True);res.mkdir(parents=True,exist_ok=True)
subprocess.run(['/usr/bin/swiftc','-swift-version','5','-O','-module-cache-path',str(root/'.swift-cache'),*[str(root/'Sources'/f) for f in ['Engine.swift','App.swift','Notices.swift','Reply.swift','main.swift']],'-o',str(mac/'DSLPet')],check=True)
for a in manifest:
 dst=res/'assets'/a['key'];dst.mkdir(parents=True,exist_ok=True)
 shutil.copy2(assets/a['key']/'animation.json',dst/'animation.json')
 shutil.copytree(assets/a['key']/'逐帧PNG',dst/'逐帧PNG',dirs_exist_ok=True)
for n in ['animations.json','待机.png']:shutil.copy2(assets/n,res/'assets'/n)
shutil.copy2(root/'scripts/bridge.py',res/'bridge.py')
shutil.copy2(root/'scripts/reply.py',res/'reply.py')
info={'CFBundleExecutable':'DSLPet','CFBundleIdentifier':'local.chennuo.dsl-pet','CFBundleName':'小 DSL','CFBundleDisplayName':'小 DSL 悬浮桌宠','CFBundleVersion':'10','CFBundleShortVersionString':'0.4.1','CFBundlePackageType':'APPL','LSUIElement':True,'NSHighResolutionCapable':True,'LSMinimumSystemVersion':'13.0'}
with (app/'Contents/Info.plist').open('wb') as f:plistlib.dump(info,f)
subprocess.run(['/usr/bin/codesign','--force','--sign','-',str(app)],check=True)
subprocess.run([str(mac/'DSLPet'),'--self-test',str(res/'assets/animations.json')],check=True)
print(app)
