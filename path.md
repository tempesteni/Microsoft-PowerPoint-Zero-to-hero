# path.md: How This Package Was Built

Process documentation for the PowerPoint Zero to Hero package, written so anyone can rebuild or extend it.

## The Strategy

Same proven "study guide strategy" as the Microsoft-Excel-Zero-to-hero package: modules + quizzes + cheat sheets + practice artifacts + flashcards + multi-length study plans, packaged publish-ready with verification gates.

## Build Phases

1. **Scaffold** - 16 folders, planned content map (8 modules + projects + sources + study plan + 4 support folders + sample-decks).
2. **Study plans first** - 5 learner-selectable tracks (12/8/6/4/2 weeks) + progress tracker. Pace varies, content does not.
3. **Module research + writing** - 8 modules + 6 project briefs via parallel AI subagents (2 rounds: research-capped round, then skip-research fast path after timeouts proved research was the bottleneck).
4. **Supporting materials** - 8 quizzes (15 MC + 5 practical each, 70-pt scale), 4 cheat sheets, 120 Anki flashcards, 10 deck-build briefs, fix-this-deck challenge (20 planted issues, answer key).
5. **Sample decks** - 7 real .pptx artifacts (starter, pitch, data report, animated demo, training w/ notes, .potx template, deliberately-broken fix-me). Mix of AI-subagent builds and deterministic python-pptx/pptxgenjs generator scripts (kept in sample-decks/ so learners can study how the decks were generated).
6. **Verification gate** - files (33 checked, 0 empty), links (57 URLs curl-tested; 11 dead/typo'd found, all repaired and re-verified), content (0 em dashes, module cross-refs, consistency), security (0 tokens/wallets/real emails).
7. **Visual QA** - LibreOffice headless render (7 PDFs, 63 slide images), per-deck contact sheets, fresh-eyes AI visual inspection with fix loop.
8. **Docs** - README (comprehensive, inline AI setup guides), this file, CONTRIBUTORS, HOW-TO-USE-WITH-AI.

## Key Decisions

- **5 study plan lengths in one file** instead of 5 separate plans: learner picks a track; content stays identical.
- **Sample decks as first-class teaching artifacts** with walkthroughs, not screenshots: learners open and reverse-engineer real files.
- **The fix-me deck plants exactly 20 issues** matching the challenge answer key (7 design, 5 content, 4 accessibility, 4 technical).
- **Generators shipped alongside decks** (build_sample05.py, build_fixme.py, build_sample06.py): automation is itself a Module 8 lesson.
- **Animations via XML injection** (Morph transitions, Bounce entrances, trigger timing) since pptxgenjs/python-pptx cannot author motion: deck files carry real animation data.
- **Skip-research fast path** for authoring: web research was the timeout bottleneck; deep-link guessing was banned (Microsoft GUID URLs 404); all external URLs verified at the gate instead.

## Toolchain

pptxgenjs (npm) + python-pptx + markitdown + LibreOffice headless + poppler (pdftoppm) + Pillow (contact sheets). All run locally on Linux: no Microsoft Office required to build or verify.

## Extending

New module: drop `NN-topic/NN-topic.md` with the metadata block + self-contained `##` sections, then add its quiz, flashcards, and study-plan references. Re-run the link gate (curl every URL) before publishing.
