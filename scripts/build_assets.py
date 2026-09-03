import os, re, sys, json

SRC="Drawing Hacks Transcript"
OUT="output"
os.makedirs(OUT, exist_ok=True)

def parse(fn):
    raw=open(fn,encoding='utf-8').read().replace('\r\n','\n').replace('\r','\n')
    blocks=re.split(r'\n\s*\n', raw)
    cues=[]
    for b in blocks:
        lines=[l for l in b.split('\n') if l.strip()]
        if not lines: continue
        if re.match(r'^\d+$', lines[0].strip()): lines=lines[1:]
        ts=None
        if lines and re.match(r'^\d{2}:\d{2}:\d{2}', lines[0].strip()): ts=lines[0].strip(); lines=lines[1:]
        if ts and lines:
            txt=' '.join(l.strip() for l in lines); txt=re.sub(r'\s+','',txt)
            cues.append((ts,txt))
    return cues

def ts_to_ms(t):
    h,m,rest=t.split(':'); s,ms=rest.split(','); return int(h)*3600000+int(m)*60000+int(s)*1000+int(ms)
def ms_to_ts(ms):
    ms=max(0,int(ms)); h=ms//3600000; ms%=3600000; m=ms//60000; ms%=60000; s=ms//1000; ms%=1000
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'

SENT_END=set('.?!…')

def merge(cues):
    units=[]; cur=[]; cur_start=None; cur_end=None
    for ts,txt in cues:
        m=re.match(r'^(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})$', ts)
        s,e=ts_to_ms(m.group(1)), ts_to_ms(m.group(2))
        if not cur: cur_start=s; cur=[txt]
        else: cur.append(txt)
        cur_end=e
        if txt and txt[-1] in SENT_END:
            units.append({'start':cur_start,'end':cur_end,'text':''.join(cur)}); cur=[]; cur_start=None
    if cur: units.append({'start':cur_start,'end':cur_end,'text':''.join(cur)})
    return units

def build(video_key, english_lines):
    """english_lines: list of english strings, one per merged unit (same order)."""
    fn = os.path.join(SRC, f'{video_key}.ko.srt')
    if not os.path.exists(fn):
        # find
        cands=[f for f in os.listdir(SRC) if f.startswith(video_key) and f.endswith('.ko.srt')]
        if not cands: raise FileNotFoundError(video_key)
        fn=os.path.join(SRC,cands[0])
    units=merge(parse(fn))
    if len(units)!=len(english_lines):
        raise ValueError(f'{video_key}: units={len(units)} vs translations={len(english_lines)}')
    base = video_key.replace(' ','_')
    # SRT
    srt=[]
    for i,(u,en) in enumerate(zip(units,english_lines),1):
        srt.append(str(i))
        srt.append(f'{ms_to_ts(u["start"])} --> {ms_to_ts(u["end"])}')
        srt.append(en)
        srt.append('')
    srt_path=os.path.join(OUT,f'{base}.en.srt')
    open(srt_path,'w',encoding='utf-8').write('\n'.join(srt))
    # Dub script (speaker+timing+line)
    dub=[]
    for i,(u,en) in enumerate(zip(units,english_lines),1):
        dur=u['end']-u['start']
        dub.append(f"[{ms_to_ts(u['start'])} | {ms_to_ts(u['end'])} | {dur/1000:.0f}s] {en}")
    dub_path=os.path.join(OUT,f'{base}.dub.txt')
    open(dub_path,'w',encoding='utf-8').write('\n'.join(dub))
    return srt_path, dub_path, len(units)

if __name__=='__main__':
    print("module loaded")
