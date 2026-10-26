"""Reconstruct the already signed APK using only public release bytes."""
import base64,gzip,hashlib,json,sys,time,urllib.request
from pathlib import Path

d=json.loads(Path('release.json').read_text())
assert d['baseUrl']=='https://github.com/lintopino-dotcom/SPM-Browser-Updates/releases/download/v19.10.0/SPM-Browser-19.10.0.apk'
old=Path(sys.argv[1]).read_bytes() if len(sys.argv)>1 else urllib.request.urlopen(d['baseUrl'],timeout=60).read()
assert hashlib.sha256(old).hexdigest()==d['baseSha256']=='cfdd90e41078a9c7307cc36ea54c9bf719c5d98f3eb6daf899b8a9fc6d008163'
chunks=[]
for c in json.loads(gzip.decompress(base64.b64decode(d['patchGzipBase64'],validate=True))):
 if c[0]=='copy':
  assert 0<=c[1]<=len(old) and 0<=c[2]<=len(old)-c[1]
  chunks.append(old[c[1]:c[1]+c[2]])
 else:
  assert c[0]=='data'
  chunks.append(base64.b64decode(c[1],validate=True))
apk=b''.join(chunks)
assert hashlib.sha256(apk).hexdigest()==d['apkSha256']=='11cc310db6c53a724521466c432e9552a8520eb0885914fff935a5c52861e6fe'
assert len(apk)==d['apkSize']==14709870
assert d['apkName']=='SPM-Browser-19.10.1.apk'
envelope=d['manifest'];payload=base64.b64decode(envelope['payload'],validate=True);p=json.loads(payload)
assert p['versionCode']==88 and p['versionName']=='19.10.1'
assert p['packageName']=='com.sonyplaystationmodding.browser.classic'
assert p['apkSize']==len(apk) and p['sha256']==d['apkSha256']
assert p['apkUrl']=='https://github.com/lintopino-dotcom/SPM-Browser-Updates/releases/download/v19.10.1/SPM-Browser-19.10.1.apk'
assert p['expiresAt']>time.time()*1000
Path(d['apkName']).write_bytes(apk)
Path('manifest.json').write_text(json.dumps(envelope,indent=2))
Path('manifest.payload').write_bytes(payload)
Path('manifest.sig').write_bytes(base64.b64decode(envelope['signature'],validate=True))
print('Exact APK and signed manifest reconstructed and hashes verified')
