# WORKFLOW.md

The per-lesson workflow for localizing a course. Follow this for every lesson.

## 0. Identify the course and language

- Find the course ID in `courses/INDEX.md` (e.g. `KO-03`, `JA-01`, `ZH-02`).
- Determine the language and its dialect/script: `ja`, `ko`, or `zh` (Taiwanese vs
  Mainland Mandarin matters — see `courses/zh/_LANGUAGE_NOTES.md`).

## 1. Load the course evidence (do this first)

Before translating anything, load the two context files for the course:

1. `courses/<lang>/_LANGUAGE_NOTES.md`
   — register and speaker habits, art vocabulary, software UI terms, homophone / ASR traps.
2. `courses/<lang>/<course>.md`
   — the course brief: discipline, core concepts, software, traps, voice notes.

These are **priming material, not ground truth.** Confirm any "(verify)" field against
the source material and update the brief. Corrections to evidence should also be reflected
in `glossaries/<id>.tsv` when course-specific vocabulary is involved.

## 2. Read the source for the lesson

Identify the lesson's source file(s) and their format. For the existing KO-03 course
this is:

- Timing source of truth: `Drawing Hacks Transcript/*.ko.srt`
- Aligned Korean reference: `merged_ref/<key>.txt` (`idx <tab> [start --> end] <tab> text`)

Other courses may have a different source format (SRT/transcript, per-language). Use the
course and language notes to decide how to identify the canonical unit boundaries and
timing. See `README.md` for the merge/unit concept used by the pipeline.

## 3. Translate

- Author the English into `translations/<key> <Title>.txt`, **one line per merged unit**.
- Natural, conversational instructor English — warm and direct, not stiff.
- Use the course brief's vocabulary and the language notes' preferred English.
- Handle the course's homophone / ASR traps so source misreads don't leak into the English.
- Keep to the TTS pronunciation rules in `README.md`.

## 4. Build & validate

- Rebuild: `python3 scripts/rebuild_all.py` (or `ba.build(key, lines)` for one lesson).
- Validate: `python3 scripts/validate.py` — must print `OK` (count + timestamp + text
  consistency).
- TTS scan: `python3 scripts/check_tts.py` — should print `0 hazards`.

If `validate.py` throws `units=... vs translations=...`, you changed the line count —
find the fold/split and fix it before proceeding.
