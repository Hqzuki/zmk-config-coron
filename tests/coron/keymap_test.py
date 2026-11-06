from pathlib import Path
import re, json
root=Path(__file__).resolve().parents[2]
s=(root/'config/coron.keymap').read_text()
blocks=re.findall(r"        (\w+) \{.*?\n\s+bindings = <(.*?)>;",s.split('    keymap {')[1],re.S)
assert [n for n,_ in blocks]==['WIN','MAC','NUM','FN','PAN_WIN','PAN_MAC','GESTURE','MOUSE','BLUETOOTH']
for n,b in blocks:
    v=[x.strip() for x in re.findall(r"&\w+(?:\s+(?!&)\S+)*",b)]
    assert len(v)==51,(n,len(v))
    if n=='NUM': assert [v[i] for i in [9,10,11,23,24,25,37,38,39,46]]==['&kp N'+str(i) for i in range(1,10)]+['&kp N0']
    if n=='FN': assert [v[i] for i in [9,10,11,23,24,25,37,38,39,46,49,50]]==['&kp F'+str(i) for i in range(1,13)]
assert len(json.loads((root/'config/coron.json').read_text())['layouts']['default_layout']['layout'])==51
assert 'sensor-bindings' not in s and 'enc_off' not in s
assert 'excluded-positions = <21 22 23 35 36>' in s
assert 'layers = <2 3>' in s
assert s.count('span = <2000>')==2
assert s.count('&df DF_BLE_SEL')==5
for f in ['coron_R.conf','coron_L.conf']:
    assert 'CONFIG_EC11=y' not in (root/'boards/shields/coron'/f).read_text()
print('CoronLP: 9x51 bindings, NUM/FN remap, pointer guard, inertia and encoder-free metadata passed')
