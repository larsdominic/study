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

## Learning extras (8 Nov): warm-up, quiz history, spaced flashcards
- `python3 tools/enhance.py guides/*.html practice/*.html review/*.html` adds, between `<!--enhance:start-->` and `<!--enhance:end-->` (safe to rerun; rerun after new flashcards or plan changes):
  - "Warm-up from earlier days (8 min)": 5 flashcard questions picked at build time from `flash.py` (3 from guides planned 1 to 3 days before the page's plan day, 2 from 7 or more days before, topped up from any earlier guide; same day, same pick). It sits in the Today card (pages with a "Today you will be able to" box or numbered blocks); otherwise it fills `<div id="warmup"></div>` if the page has one, else goes at the top of `<main>`. First day: a short note instead.
  - the quiz extras from `quizjs.py` (`ENGINE`): "How sure are you? Guessed / Unsure / Sure" on every question, "3 of 10" counters, ✓/✗ labels on answers, "Log these first" (sure but wrong first), "Try again (shuffled)" (question and option order, `data-a` moves with the right option), self-mark menus on `.written[data-max]` items.
  - the "cannot save" notice (`storageOK()`), placed under the top bar.
  - the shared site layer (below) and the Today card.

## Site layer (8 Nov, UX review `ib-notes/research/ux-review.md`)
- `common.py` holds `SITE_CSS`, `SITE_JS`, `site_bar(depth)`, `site_head()`, `site_tail()` and `block_open(n, title, time)`. `page()` puts them into every generated page; `enhance.py` puts them into guides, practice and review pages. All of it sits between enhance markers, and the CSS comes after the page's own CSS so it wins.
- What it gives: a sticky 44 px top bar "← Today · Flashcards · Progress · Sheet"; the guide section menu as one sideways row of 44 px links with the current section marked (`aria-current`); visible focus everywhere (`:focus-visible`, 3 px indigo, gold on the dark header); `--amber-ink:#8A6416`, `--grey:#5F6B72`, `--green-ink:#256B43` for text; one badge system (Learn = solid amber, In booklet / formula sheet = neutral outline, Apply = indigo outline, HL = purple outline, green only for done); radii 4 and 8 px; text at most 68ch wide; header title first, picture at most 34% of the screen height (30% on phones); 44 px targets; print CSS; `color-scheme: light` (dark mode not done yet).
- Timed blocks: guide `.plan` blocks ("Block 1 · 25 min" + title) and `.step` blocks with that header become numbered `.block` cards at load time; `review.py` and `timed.py` write `.block` cards directly (`block_open`). Each block gets a "Block done" tick saved in `ib-<file name>-blocks` = `{n: date}`. Teaching sections linked from a block get "Block n · " in their kicker.
- Today card (enhance.py): at the top of `<main>`, the page's own "Today you will be able to" box is MOVED in (its old place keeps `<!--enhance:origin-->`; a rerun puts it back first), then chips to the warm-up, Block 0 and each block (ids `b1`..`bn` are added to the blocks if missing), then the warm-up.
- terms.py: "Before you start" is "Block 0 · Before you start" at the start of the plan (an open `<details>`); each word is underlined once per page (first visible use), never in headings, links, buttons, nav or summaries. `check_terms.py` tests all of that.
- `check_layout.py` ignores elements inside rows that scroll sideways on purpose (overflow-x auto), and always reports a page wider than the screen.

## Run order after changing tools or pages (from the repo root)
1. `python3 tools/build_plan.py` (only if `plan_data.py` changed)
2. the generators: `for g in landing progress flash exam exam_bm exam_psych given review review2 timed; do python3 tools/$g.py tools .; done`
3. `for j in tools/terms/*.json; do b=$(basename $j .json); f=$(ls guides/$b.html practice/$b.html 2>/dev/null | head -1); [ -n "$f" ] && python3 tools/terms.py $f $j; done`
4. `python3 tools/enhance.py guides/*.html practice/*.html review/*.html`
5. checks: `python3 tools/check_terms.py <abs path>` (pages with terms) and `python3 tools/check_layout.py <abs path>`
- The page's own quiz script still scores the first round and saves `ib-quiz-…` as `{right,total,date,best}` (unchanged). New keys: `<quizkey>-attempts` = `[{date,right,total}]` (local dates; timed pages keep one entry per day), `<quizkey>-written` = `{itemId: mark}`.
- `quiz_js(key)` (generated pages) is the same engine running the whole quiz.
- Flashcards: state `ib-flash-v2` = `{c:{id:{b,last,due}}, nd, nn}`; boxes 0 to 4, intervals 0 (Again: today), 1, 3, 7, 14 days; a card unlocks on its guide's first plan day in `links.json`; at most 10 new a day; old `ib-flash-v1` boxes are moved across once. `ib-flash-due-count` = cards due today (the landing page counts from `ib-flash-v2` itself when it can).
- Progress: Secure = every "I can" box ticked and an attempt at 80% or more at least 3 days after the first attempt. "! To do" = plan day reached, untouched; "– Not yet" = no guide or plan day still to come (folded away). "Days with a page done" = plan days where one of its pages has a score dated that day or later.
