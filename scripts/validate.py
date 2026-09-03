#!/usr/bin/env python3
"""Validate the English deliverables against the Korean source.

Checks, per lesson:
  - translations line count == merged unit count
  - output .en.srt cue count == unit count and == .dub.txt line count
  - each .dub.txt [start | end | dur] matches its .en.srt cue timestamp
  - each .en.srt text == corresponding .dub.txt text

Exit code 0 on success, 1 if any mismatch. Prints every problem.

Run from the repo root:
    cd /home/user/Korean-Course-Conversion
    python3 scripts/validate.py
"""
import os, re, sys, glob
import importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

spec = importlib.util.spec_from_file_location('ba', os.path.join(REPO, 'scripts', 'build_assets.py'))
ba = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ba)


def key_of(path):
    """Numeric prefix of a translations filename -> lesson key ('0.2')."""
    return os.path.basename(path).split(' ', 1)[0]


def trans_lines(text):
    return [l.rstrip('\n') for l in text.split('\n') if l.strip()]


def parse_srt(path):
    raw = open(path, encoding='utf-8').read().split('\n')
    cues = []
    i = 0
    while i < len(raw):
        if (i + 2 < len(raw) and re.match(r'^\d+$', raw[i].strip())
                and ' --> ' in raw[i + 1]):
            cues.append((raw[i + 1].strip(), raw[i + 2].strip()))
            i += 4
        else:
            i += 1
    return cues


def parse_dub(path):
    out = []
    for l in open(path, encoding='utf-8'):
        l = l.rstrip('\n')
        if not l.strip():
            continue
        m = re.match(r'^\[([^\]|]+) \| ([^\]|]+) \| ([^\]]+)\] (.+)$', l)
        if not m:
            out.append((None, None, None, l))
            continue
        out.append((m.group(1).strip(), m.group(2).strip(), m.group(3).strip(), m.group(4).strip()))
    return out


def main():
    trans = {}
    for f in sorted(glob.glob('translations/*.txt')):
        trans[key_of(f)] = trans_lines(open(f, encoding='utf-8').read())

    bad = []
    fails = 0

    for key, lines in trans.items():
        # Rebuild from source to confirm count + regenerate output.
        # build() raises ValueError on count mismatch.
        try:
            srt_path, dub_path, n = ba.build(key, lines)
        except Exception as e:
            bad.append((key, 'build failed', str(e)))
            fails += 1
            continue

        srt_cues = parse_srt(srt_path)
        dub_cues = parse_dub(dub_path)

        if len(srt_cues) != n:
            bad.append((key, f'srt cues {len(srt_cues)} != units {n}')); fails += 1
        if len(dub_cues) != n:
            bad.append((key, f'dub lines {len(dub_cues)} != units {n}')); fails += 1

        for i, (s_ts, s_txt) in enumerate(srt_cues):
            if i >= len(dub_cues):
                break
            d_start, d_end, _dur, d_txt = dub_cues[i]
            s_start, s_end = s_ts.split(' --> ')
            if (s_start, s_end) != (d_start, d_end):
                bad.append((key, f'line {i}: ts {s_ts} != dub {d_start}|{d_end}')); fails += 1
            if s_txt.rstrip() != d_txt.rstrip():
                bad.append((key, f'line {i}: text differs')); fails += 1

    print(f'checked {len(trans)} lessons')
    if bad:
        print(f'FAILURES: {fails}')
        for b in bad:
            print('  ', b)
        return 1
    print('OK: every lesson count + timestamp + text consistent')
    return 0


if __name__ == '__main__':
    sys.exit(main())
