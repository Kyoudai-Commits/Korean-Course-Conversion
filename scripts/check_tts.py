#!/usr/bin/env python3
"""Scan translations/ for text that a TTS engine will mangle.

Run from the repo root:
    cd /home/user/Korean-Course-Conversion
    python3 scripts/check_tts.py
"""
import os, re, glob, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(REPO)

# (regex, human label, fix hint)
RULES = [
    (r'—',                    'em-dash',        'use a period, comma, or colon'),
    (r'\bCtrl\b|\bCtrl\+',    'bare "Ctrl"',    'write "Control"'),
    (r'[A-Za-z]\+[A-Za-z]',   'shortcut "+"',   'write "Control and Z" / "Control, Shift, and J"'),
    (r'\bAlt\+|\bShift\+',    'shortcut Alt/+', 'spell out with "and"'),
    (r'\bESC\b',              '"ESC"',          'write "Escape"'),
    (r'\bMMORPG\b',           'MMORPG',          'write "massively multiplayer online role-playing games"'),
    (r'\bSF\b',               '"SF"',           'write "sci-fi"'),
    (r'\bCC\b',               '"CC"',           'write "Creative Cloud"'),
    (r'\bSNS\b',              '"SNS"',          'write "social media"'),
    (r'[0-9]-[0-9]',          'numeric range',  'write "Chapter 3, part 1"'),
    # Acronyms that TTS is known to mangle. Anything NOT here is assumed TTS-safe.
    (r'\b(?:CC|SF|SNS|MMORPG|ESC)\b', 'risky acronym', 'expand: CC->Creative Cloud, SF->sci-fi, SNS->social media, MMORPG->massively multiplayer online role-playing games, ESC->Escape'),
]

# All-caps strings that are safe to leave as-is (TTS reads them fine).
# Everything else all-caps gets flagged as a candidate for review.
KNOWN_SAFE_CAPS = {
    'PC', 'RGB', 'HSB', 'HSV', 'PNG', 'JPEG', 'BMP', 'CGI', 'OK', 'HR',
    'IKEA', 'COVID', 'XX', 'MMORPG',
}

def main():
    hits = 0
    files = sorted(glob.glob('translations/*.txt'))
    print(f'scanning {len(files)} translation files\n')
    for f in files:
        for lineno, line in enumerate(open(f, encoding='utf-8'), 1):
            line = line.rstrip('\n')
            for pat, label, hint in RULES:
                if re.search(pat, line):
                    print(f'{os.path.basename(f)}:{lineno}  [{label}]  {line.strip()[:90]}')
                    print(f'    -> {hint}')
                    hits += 1
                    break  # one label per line
            else:
                # Flag any all-caps word that is NOT in the known-safe set.
                for word in re.findall(r'\b[A-Z]{2,}\b', line):
                    if word not in KNOWN_SAFE_CAPS:
                        print(f'{os.path.basename(f)}:{lineno}  [unreviewed all-caps "{word}"]  {line.strip()[:90]}')
                        print('    -> check whether a TTS engine reads this correctly')
                        hits += 1
    print(f'\n{len(files)} files, {hits} hazards'
          + ('\nOK: no hazards' if hits == 0 else '\nREVIEW the hits above'))
    return 0 if hits == 0 else 1

if __name__ == '__main__':
    sys.exit(main())
