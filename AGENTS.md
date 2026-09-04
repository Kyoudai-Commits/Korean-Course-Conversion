# AGENTS.md

Guidance for AI agents working in this repository.

## Repository purpose

This repo localizes a growing set of drawing / illustration courses recorded in Japanese,
Korean, and Mandarin Chinese. For each course we produce English subtitles and a
TTS-friendly dub script, translating unit-by-unit into natural, conversational instructor
English.

The existing, proven pipeline for the one fully-built course (KO-03 "Drawing Hacks") is
documented in detail in `README.md` — read it before touching any code or content. It
covers the `translations/` → `output/` build, the line-count rules, the TTS pronunciation
rules, and validation. The general rules there (single source of truth, one line per
merged unit, TTS-clean text, always re-validate) apply to every course you localize, even
if a future course has a different source format.

## Course- and lesson-specific evidence

Localization quality depends heavily on course- and lesson-specific context: the
instructor's register, their recurring vocabulary, the homophone / ASR traps for that
language, the exact software UI terms shown on screen, and the course's discipline. That
evidence is stored in `courses/`:

```
courses/
  INDEX.md                     # course index + platform notes
  _TEMPLATE.md                 # template for a new course brief
  <lang>/_LANGUAGE_NOTES.md    # per-language register, vocabulary, UI terms, ASR traps
  <lang>/<course>.md           # per-course context brief (ID, instructor, concepts)
```

**Before starting any lesson of a course:**

1. Load the language notes for that course's language:
   `courses/<lang>/_LANGUAGE_NOTES.md`
2. Load the course brief, matched by ID in `courses/INDEX.md`:
   `courses/<lang>/<course>.md`

Treat both as **priming material, not ground truth.** Fields marked "(verify)" were not
confirmed against the course materials — confirm them from the first lesson and update
the brief. When a brief or language note is corrected, update the course's glossary at
`glossaries/<id>.tsv` (accumulated, evidence-based) if course-specific vocabulary changed.

## Directory map (high level)

| Path | Contents | Editable? |
|------|----------|-----------|
| `courses/` | Course index, template, per-language notes, per-course briefs. | Edit to refine evidence |
| `translations/<key> <Title>.txt` | **Canonical English lines**, one per merged unit. | **Edit here** |
| `merged_ref/<key>.txt` | Aligned Korean reference (source for a single course). | Derived |
| `output/<key>.en.srt` / `<key>.dub.txt` | Generated subtitles / dub script. | Generated |
| `scripts/` | Pipeline + validation scripts. | Edit with care |
| `README.md` | Full pipeline documentation. | Edit with care |

## Golden rules

- `translations/` is the single source of truth; `output/` is generated. Edit only
  `translations/`, then rebuild.
- Never change a translation's line count by accident (it breaks alignment).
- Follow the TTS pronunciation rules in `README.md` (no em dashes, spell out shortcuts,
  expand dangerous acronyms, avoid slashes/awkward ranges).
- Validate after any content edit: `python3 scripts/validate.py` and
  `python3 scripts/check_tts.py` (run from the repo root).
