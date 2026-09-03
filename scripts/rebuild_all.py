#!/usr/bin/env python3
"""Regenerate every lesson's .en.srt + .dub.txt from translations/.

Run from the repo root:
    cd /home/user/Korean-Course-Conversion
    python3 scripts/rebuild_all.py
"""
import os, re, glob, sys
import importlib.util

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

spec = importlib.util.spec_from_file_location('ba', os.path.join(REPO, 'scripts', 'build_assets.py'))
ba = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ba)


def key_of(path):
    return os.path.basename(path).split(' ', 1)[0]


def trans_lines(text):
    return [l.rstrip('\n') for l in text.split('\n') if l.strip()]


def main():
    fails = 0
    for f in sorted(glob.glob('translations/*.txt')):
        key = key_of(f)
        lines = trans_lines(open(f, encoding='utf-8').read())
        try:
            srt, dub, n = ba.build(key, lines)
            print(f'{key:>4}  {n:>3} units  ->  {os.path.basename(srt)}')
        except Exception as e:
            print(f'{key:>4}  FAILED: {e}')
            fails += 1
    print()
    if fails:
        print(f'{fails} lesson(s) failed to build')
        return 1
    print('all lessons rebuilt OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
