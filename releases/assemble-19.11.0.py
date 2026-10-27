"""Reconstruct an already signed APK from public bytes; no signing key used."""
import base64,gzip,hashlib,json,sys,time,urllib.request
from pathlib import Path
d=json.loads(Path('release.json').read_text())
assert d['baseUrl']=='https://github.com/lintopino-dotcom/SPM-Browser-Updates/releases/download/v19.10.1/SPM-Browser-19.10.1.apk'
old=Path(sys.argv[1]).read_bytes() if len(sys.argv)>1 else urllib.request.urlopen(d['baseUrl'],timeout=60).read()
assert hashlib.sha256(old).hexdigest()==d['baseSha256']=='11cc310db6c53a724521466c432e9552a8520eb0885914fff935a5c52861e6fe'
chunks=[]
for c in json.loads(gzip.decompress(base64.b64decode(d['patchGzipBase64'],validate=True))):
 if c[0]=='copy':
  assert 0<=c[1]<=len(old) and 0<=c[2]<=len(old)-c[1]
  chunks.append(old[c[1]:c[1]+c[2]])
 else:
  assert c[0]=='data'
  chunks.append(base64.b64decode(c[1],validate=True))
apk=b''.join(chunks)
assert hashlib.sha256(apk).hexdigest()==d['apkSha256']=='3154284414c7d1eec1100a4c9afbcf90df734c856c8a85a0b75c95971c8f2488'
assert len(apk)==d['apkSize']==28879643
assert d['apkName']=='SPM-Browser-19.11.0.apk'
envelope=d['manifest'];payload=base64.b64decode(envelope['payload'],validate=True);p=json.loads(payload)
assert p['versionCode']==89 and p['versionName']=='19.11.0'
assert p['packageName']=='com.sonyplaystationmodding.browser.classic'
assert p['apkSize']==len(apk) and p['sha256']==d['apkSha256']
assert p['apkUrl']=='https://github.com/lintopino-dotcom/SPM-Browser-Updates/releases/download/v19.11.0/SPM-Browser-19.11.0.apk'
assert p['expiresAt']>time.time()*1000
Path(d['apkName']).write_bytes(apk)
Path('manifest.json').write_text(json.dumps(envelope,indent=2))
Path('manifest.payload').write_bytes(payload)
Path('manifest.sig').write_bytes(base64.b64decode(envelope['signature'],validate=True))
print('Exact signed APK and manifest reconstructed and hashes verified')
