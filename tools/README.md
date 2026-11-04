# Generators for the study-site extra pages

Run from the repo root: `python3 tools/<script>.py tools .` (first argument: this folder, second: output root).

- `flash.py` → `flashcards.html` + `flashcards-anki.txt`. Add cards for every new guide (the "Learn" items).
- `progress.py` → `progress.html`. Add a `GUIDES` entry for every new guide (its "I can" localStorage key, quiz key, and which `data-k` boxes belong to which topic). New subject: add its official topic list to `SUBJECTS`.
- `review.py` → the weekly review page. Copy it for each new Sunday (new file name, new quiz key, questions from that week's guides), then add the review to `REVIEWS` in `progress.py`.
- `exam.py` → the exam technique pages. Add one per new subject, from that subject's official guide (assessment outline + glossary of command terms).
- `check_layout.py <file.html>` → overflow check at 380 to 1200 px (needs Python Playwright).

Every guide's quiz saves `ib-quiz-guide-YYYY-MM-DD` in localStorage; every guide's "I can" boxes save under their own key. The progress page reads both.

## Background words (4 Nov)
- `tools/terms/<guide>.json` holds the tap-to-explain words and the "Before you start" box for each guide; `python3 tools/terms.py guides/<guide>.html tools/terms/<guide>.json` adds them to the page (safe to rerun). `python3 tools/check_terms.py <abs path>` tests them. How to write them: `tools/TERMS_BRIEF.md`.
