# Generators for the study-site extra pages

## The plan (8 Nov 2026 restart: Chemistry dropped, Psychology HL added, clean slate from Mon 9 Nov)
- `plan_data.py` is the single source for every day from 9 Nov to 4 Dec: subject, task, Drive files (new IDs after the 8 Nov re-upload, or checked free web pages) and the site pages for that day (`review=True` marks a revisit). The same data filled the study sheet (Daily plan tab, links in columns K to Y, site link in column Z).
- `python3 tools/build_plan.py` writes `plan.json` and `links.json`; then run `landing.py`.
- `exam_psych.py` → `exam-psychology-hl.html` (from the official Psychology guide, first assessment 2027).

Run from the repo root: `python3 tools/<script>.py tools .` (first argument: this folder, second: output root).

- `flash.py` → `flashcards.html` + `flashcards-anki.txt`. Add cards for every new guide (the "Learn" items).
- `progress.py` → `progress.html`. Add a `GUIDES` entry for every new guide (its "I can" localStorage key, quiz key, and which `data-k` boxes belong to which topic). New subject: add its official topic list to `SUBJECTS`.
- `review.py` → the weekly review page. Copy it for each new Sunday (new file name, new quiz key, questions from that week's guides), then add the review to `REVIEWS` in `progress.py`.
- `exam.py` → the exam technique pages. Add one per new subject, from that subject's official guide (assessment outline + glossary of command terms).
- `check_layout.py <file.html>` → overflow check at 380 to 1200 px (needs Python Playwright).

Every guide's quiz saves `ib-quiz-guide-YYYY-MM-DD` in localStorage; every guide's "I can" boxes save under their own key. The progress page reads both.

## Background words (4 Nov)
- `tools/terms/<guide>.json` holds the tap-to-explain words and the "Before you start" box for each guide; `python3 tools/terms.py guides/<guide>.html tools/terms/<guide>.json` adds them to the page (safe to rerun). `python3 tools/check_terms.py <abs path>` tests them. How to write them: `tools/TERMS_BRIEF.md`.
