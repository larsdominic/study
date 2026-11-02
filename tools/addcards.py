# Append flashcards from a JSON-lines file into tools/flash.py (skips ids already present).
import sys, json, re
src, flash = sys.argv[1], 'tools/flash.py'
s=open(flash).read(); added=0
lines=[json.loads(l) for l in open(src) if l.strip()]
block=''
for c in lines:
    if f'("{c["id"]}",' in s: continue
    for k in ('f','b'): assert '—' not in c[k]
    block+='(%s,%s,%s,%s,%s,%s),\n' % tuple(json.dumps(c[k],ensure_ascii=False) for k in ('id','s','t','l','f','b')); added+=1
marker='\n]\nfor c in cards:'
assert marker in s
s=s.replace(marker,'\n'+block.rstrip('\n')+marker if block else marker,1)
open(flash,'w').write(s); print('added',added)
