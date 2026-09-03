# Korean Drawing Course — English Translation & TTS Dub

**Project status: COMPLETE.** All 30 lessons are translated to English and generated
as both an English SRT subtitle file and a TTS-friendly dub script.

This README captures everything learned the hard way during this project so a future
session doesn't have to re-derive it. Read **all** of it before touching this repo.

- [Goal](#goal)
- [Directory map](#directory-map)
- [The rules that matter most](#the-rules-that-matter-most)
- [The pipeline](#the-pipeline)
- [How to regenerate one lesson](#how-to-regenerate-one-lesson)
- [How to validate everything](#how-to-validate-everything)
- [Line counts (authoritative)](#line-counts-authoritative)
- [Canonical English source](#canonical-english-source)
- [Terminology decisions](#terminology-decisions)
- [TTS pronunciation rules — DO THESE FOR EVERY NEW/CONTENT-EDIT](#tts-pronunciation-rules)
- [Gotchas & dead ends](#gotchas--dead-ends)

---

## Goal

The user (a friend of the lecturer) wants to produce **English subtitles** plus an
**English TTS-generated voice dub** for 30 Korean drawing tutorials. Two assets per lesson:

1. `output/<key>.en.srt` — English subtitles, line-for-line matching the Korean timing.
2. `output/<key>.dub.txt` — a line-by-line TTS script in the form
   `[start | end | duration] <English text>`.

**Acceptance criteria:**

- All 30 lessons translated.
- `.en.srt` and `.dub.txt` exist for every lesson.
- Line count in both equals the **merged unit count** of that lesson.
- The timestamps in the dub match the SRT **exactly** (line-for-line).
- The English is **natural, conversational** (reads like a friendly instructor).
- The English is **contextually/semantically clear** (no confusing comments).
- The English is **machine-pronounceable** (see TTS rules below).

## Directory map

| Path | Contents | Editable? |
|------|----------|-----------|
| `Drawing Hacks Transcript/*.ko.srt` | Original Korean SRT subtitles (source of truth for **timing**). | Never edit |
| `processed_text/*.txt` | Korean raw text (spaces stripped) per lesson. | Derived |
| `merged_ref/*.txt` | Korean merged units (`<idx>\t[start --> end]\t<text>`). This is what a translation must line up 1:1 with. | Derived |
| `translations/*.txt` | **The canonical English lines.** One line per merged unit. **THESE ARE EDITED BY HAND.** | **Edit here** |
| `output/<key>.en.srt` | Generated English subtitles. | Generated |
| `output/<key>.dub.txt` | Generated TTS dub script. | Generated |
| `scripts/build_assets.py` | The pipeline: `merge()` + `build()`. The ONLY generation logic. | Edit with care |
| `scripts/rebuild_all.py` | Regenerate every lesson from `translations/`. | Run |
| `scripts/validate.py` | Verify count + timestamp + text consistency for all lessons. | Run |
| `scripts/check_tts.py` | Scan `translations/` for TTS-mangleable text (em dashes, shortcuts, acronyms, ranges). | Run |
| `.gitignore` | Ignores `__pycache__/` and `*.pyc` (from importing `build_assets.py`). | edit if needed |
| `.progress/DONE` | Checklist of the 30 lessons (all `✓`). | Cosmetic |

### The two dirs you must never confuse

- **`translations/`** = what humans/agents author. **Canonical English.**
- **`output/`** = what `build_assets.py` writes. **Regenerable; do not hand-edit.**
- `processed_text/` and `merged_ref/` are **Korean**, not English. Never edit English there.

There is **exactly one** canonical English version per lesson: the file in `translations/`.
Everything in `output/` is generated from it. If you see a discrepancy, fix `translations/`
and rebuild — never patch `output/` by hand.

---

## The rules that matter most

1. **`translations/` is the single source of truth. `output/` is generated.**
2. **Every content edit happens in `translations/`.**
3. **Never change the line count by accident.** A translation file must have exactly
   one line per merged unit. Adding/removing a line breaks the whole lesson's alignment.
4. **Line count drives validation.** `build()` refuses to run if
   `len(units) != len(english_lines)`.
5. **Timestamps are never authored** — they come from the Korean SRT via `merge()`.
   Your only job is to supply the English text. The dub format just re-prints the SRT times.
6. **Tone = conversational / natural.** Plain English descriptions of technical terms.
   No Korean romanization, no parenthetical Korean gloss, no teacher-speak jargon.
7. **TTS-clean text.** See the pronunciation rules.

## The pipeline

`scripts/build_assets.py` contains three functions:

- `parse(fn)` — reads a `.ko.srt`, returns `[(timestamp_text, stripped_text)]`.
  Strips all whitespace inside each Korean cue.
- `merge(cues)` — **this is the important one.** It concatenates consecutive cues *until
  the accumulated text ends in a sentence terminator* (`.?!…`). The result is the list of
  "units" that a translation must map to one-for-one. Each unit gets `start`/`end` from its
  first and last cue.
- `build(video_key, english_lines)` — takes the short key (e.g. `0.1`) and a list of
  English strings (one per merged unit, in order). It:
  1. finds the `.ko.srt` (by key, else by filename prefix),
  2. calls `merge()` to get the canonical unit list,
  3. raises `ValueError` if the counts don't match,
  4. writes `output/<key>.en.srt` and `output/<key>.dub.txt`.

Import it and call `build` directly:

```python
import importlib.util, glob
spec = importlib.util.spec_from_file_location('ba', 'scripts/build_assets.py')
ba = importlib.util.module_from_spec(spec); spec.loader.exec_module(ba)

# Load the canonical English for key 0.2
key = '0.2'
lines = [l.rstrip('\n') for l in open(glob.glob(f'translations/{key} *.txt')[0], encoding='utf-8') if l.strip()]
srt, dub, n = ba.build(key, lines)
print(n)  # 72
```

> **cwd matters.** `build_assets.py` uses the *relative* paths `SRC="Drawing Hacks Transcript"`
> and `OUT="output"`. Run scripts from the repo root (`/home/user/Korean-Course-Conversion`).

## How to regenerate one lesson

```bash
cd /home/user/Korean-Course-Conversion
python3 - <<'PY'
import importlib.util, glob
spec = importlib.util.spec_from_file_location('ba','scripts/build_assets.py')
ba = importlib.util.module_from_spec(spec); spec.loader.exec_module(ba)

key = '1.3'  # change me
lines = [l.rstrip('\n') for l in open(glob.glob(f'translations/{key} *.txt')[0], encoding='utf-8') if l.strip()]
srt, dub, n = ba.build(key, lines)
print(key, '->', n, 'units')
print(srt); print(dub)
PY
```

## How to validate everything

There are three committed scripts. Run them **from the repo root**:

```bash
# Regenerate every lesson's .en.srt + .dub.txt from translations/
python3 scripts/rebuild_all.py

# Verify count + timestamp + text consistency for all 30 lessons
python3 scripts/validate.py        # prints "OK ..." and exits 0 on success

# Scan translations/ for text a TTS engine will mangle
python3 scripts/check_tts.py       # prints "0 hazards" and exits 0 on success
```

`rebuild_all.py` is the safe way to regenerate everything. `validate.py` is the gate you
must pass after any edit; it re-runs `build()` (so it *also* catches count drift) and checks
the three invariants:

- `len(units) == len(translations_lines) == len(srt_cues) == len(dub_lines)`.
- For each line: the dub's `[start | end ...]` equals the SRT cue's `start --> end`.
- For each line: the SRT text equals the dub text (they're the same English, just formatted).

A passing run prints `OK`. If `build()` throws, the lesson's translation count is wrong.

## Line counts (authoritative)

Numbers of **merged units** per lesson (must equal lines in `translations/` and
lines/cues in `output/`). Regenerate with the script above before trusting.

```
0.1  30    0.2  72    1.1 139    1.2  58    1.3 204
2.1 127    2.2 137    2.3 174    2.4 159    3.1 218
3.2 129    3.3 155    4.1 139    4.2 129    4.3 117
5.1 151    5.2 129    5.3 128    5.4  99    5.5  73
6.1 189    6.2 167    6.3 161    7.1 234    7.2 280
7.3 169    8.1 142    8.2 159    8.3 323    9.1  36
```

Total ~4,400 lines. `8.3 Q&A` is the longest; `0.1` and `9.1` are the shortest.

> **Key derivation gotcha.** Lesson keys come from the **numeric prefix** of the filename,
> e.g. `translations/0.2 Ill Introduce My Class.txt` → key `0.2`. The output filenames are
> `0.2.en.srt` / `0.2.dub.txt` (short key only, **not** the full title). When comparing
> translations vs output, map by that first token — a naive glob on the full title fails.

## Canonical English source

The one rule that keeps everything consistent: **`translations/` is canonical; `output/`
is generated.** When reviewing, check `translations/` against `merged_ref/` (Korean) —
never against `output/`. There is no second English version anywhere.

## Terminology decisions

These were scanned corpus-wide and are consistent. Keep them that way.

| Korean | English | Note |
|--------|---------|------|
| 밸류 / value | **value** (88×) | brightness is a synonym (7×) but "value" is dominant; accept both, prefer "value" |
| 양감 | **mass** (29×) / "sense of volume" (4×) | context-dependent; both natural, not standardized to one term. Open decision — ask if it matters. |
| 콘셉트아트 | **concept art** (83×) | vs "key art" (8×); prefer "concept art" |
| 그림자 | **shadow** (32×) | "shadow areas" (1×) ok |
| 하이라이트 | **highlight** (9×) | "lit areas" (4×) ok |
| 라인드로잉 | **line drawing** (27×) | "line art" (1×) ok |

Other terms are uniform: saturation, reflected light, silhouette, midtones, specular,
diffuse, subsurface, raised/recessed (not "embossed/engraved").

**"concretize" was eliminated.** It's jargon; replacements are plain English such as
"make it concrete," "solidify," "get clearer," "define."

### Technical terms → plain English

Never keep Korean with a parenthetical gloss, and don't romanize. E.g.:
- Photoshop features: Free Transform, warp, liquify, Gaussian blur, mixer brush, etc.
- Physics/art: normal (line), angle of incidence/reflection (explain plainly).

## TTS pronunciation rules — DO THESE FOR EVERY NEW/CONTENT-EDIT

If you edit the English, re-scan for these hazards. The rule: **a TTS engine must be able to
read the text aloud without mangling a word.** Concretely:

### 1. No em dashes

`—` breaks phrasing and can cause a pause or glitch. Replace with a period, comma, or colon.
All 30 were converted. Examples:
- `I'm XX years old — is it too late?` → `I'm XX years old. Is it too late?`
- `sense — like design ... — on your own` → `sense, like design ... on your own`

### 2. Keyboard shortcuts written out

Never `Ctrl+Z` / `Shift+L` / `Alt+Ctrl+S` / `Ctrl+Shift+J`. TTS reads `Ctrl` as "cutl" and
`+` as "plus" (or nothing). Spell it out:

| Written | Spoken form |
|---------|-------------|
| `Ctrl+Z` | `Control and Z` |
| `Ctrl+Shift+J` | `Control, Shift, and J` |
| `Alt+Ctrl+S` | `Alt, Control, and S` |
| `Ctrl+J` | `Control and J` |
| `Hold Ctrl` | `Hold Control` |
| `Press ESC` | `Press the Escape key` |
| `Shift+L` | `Shift and L` |

Note the Oxford-style comma before "and" for 3-key combos — it reads cleanly.

### 3. Acronyms — expand the dangerous ones

There is a known-safe allowlist in `scripts/check_tts.py` (`KNOWN_SAFE_CAPS`):

- **Keep (TTS reads fine):** `RGB`, `HSB`, `HSV`, `PNG`, `JPEG`, `BMP`, `CGI`, `OK`, `PC`,
  `HR`, `IKEA`, `COVID`, `XX`, `MMORPG` (MMORPG is in the allowlist for *scan* purposes, but
  it was expanded in the text — see below).
- **Expand / replace:**
  - `CC` → `Creative Cloud` (Photoshop edition, e.g. "Photoshop Creative Cloud 2022")
  - `SF` → `sci-fi`
  - `SNS` → `social media`
  - `MMORPG` → `massively multiplayer online role-playing games`
  - `ESC` → `Escape` (as "the Escape key")

`check_tts.py` flags any all-caps word **not** in the allowlist, so a new unusual acronym
(e.g. an unexpanded one) is surfaced for review rather than silently passing.

### 4. Numbers, ranges, slashes

- `%` reads fine ("percent"). `120%` → "120 percent."
- Chapter shorthand `3-1` reads "three dash one" (awkward). Use `Chapter 3, part 1`.
- Slashes `/` read as "slash." Replace with "and"/"or"/a preposition:
  - `hue/saturation` → `hue and saturation`
  - `brightness/contrast` → `brightness and contrast`
  - `practice/copy-study` → `practice or copy-study`
  - `60% academy / 40% instructor` → `60% for the academy and 40% for the instructor`

### 5. Homographs

Scan contexts for read/live/use — all were verified correct. No ambiguous cases remain.

## Gotchas & dead ends

Things that burned time. Don't repeat them.

1. **The validator's key bug.** Comparing `translations/` to `output/` requires mapping by
   the *numeric prefix* (`0.1`), not the full title. `glob('output/0.1*.srt')` works because
   output files use short keys; `glob('translations/<full title>')` does not. (Fixed; noted in
   "Key derivation gotcha.")

2. **`findgap.py` is misleading.** It counts `.?!…` punctuation, not actual line alignment.
   It cannot diagnose line-count issues. Use content alignment instead. **Do not trust it.**

3. **Stray blank lines in `translations/` break the count.** A translation must be exactly one
   line per unit. `translations/8.2` had 8 blank lines that silently pushed its count to 167
   vs the true 159, causing `ValueError: units=159 vs translations=167`. Filter with
   `if l.strip()` when loading and when validating.

4. **Rhetorical `, right.` is wrong.** Convert to `, right?` (it's a question). This was done
   corpus-wide (3.3, 4.1, 5.5, 6.1, 7.1, 7.2).

5. **Cumulative-sentence drift.** When you hand-translate a long lesson it's easy to
   accidentally fold two Korean units into one English line (or split one into two), and the
   error *accumulates* down the file. This is exactly why `build()` hard-fails on count and why
   the fold-fix history exists (7.2 E20/E23, 6.2 E41/E44, 5.2 E46, 1.3 E60/E102, 3.1 E182,
   4.2 E85, 9.1 E13, 8.3 E50/E194, etc.). **Always re-validate after any content edit.**

6. **`build_assets.py` lives in `/tmp` by default.** `/tmp` is outside the persisted workspace
   root, so it can be lost. The pipeline is mirrored at `scripts/build_assets.py`. Use the
   repo copy.

7. **Relative paths in `build_assets.py`.** It runs against `Drawing Hacks Transcript/` and
   writes to `output/`. Always run from the repo root, or it throws `FileNotFoundError`.

8. **`processed_text/` is a red herring for English.** It's Korean with spaces stripped (for
   readability/alignment checks). Don't edit English there; `merged_ref/` is the aligned
   Korean reference. **Both are Korean.**

9. **Terminology is a consistency, not a correctness, question.** The user is relying on our
   judgment (they can't spot-check), so pick one primary term per concept and stick to it.

10. **Timestamps are derived, never hand-written.** In the `.dub.txt`, the `[start | end | dur]`
    is just a re-print of the SRT cue times. If you "fix" timing by editing the dub you will
    break the match. Always regenerate from source.

## Summary workflow for a future content edit

1. Edit the line in `translations/<key> <Title>.txt` **only.**
2. Re-check the TTS hazards (em dash, shortcuts, acronyms, ranges, slashes).
3. Confirm you did **not** add/remove a line (count must still equal the merged unit count).
4. Rebuild: `ba.build(key, lines)`.
5. Validate: counts equal across translations / srt / dub, and each dub timestamp matches
   its SRT cue timestamp.

If `build()` throws `units=... vs translations=...`, you changed the line count — find the
fold/split and fix it before proceeding.
