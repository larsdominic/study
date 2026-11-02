# Brief for building a study guide page (Jamila, IB Diploma, started late)

Read this whole file before writing anything. It collects every rule Lars has given.

## Who and what
- Jamila, Grade 11, IB Diploma, catching up. About 2 to 3 hours per study day.
- Site: repo `~/ClaudeMe/study` → https://larsdominic.github.io/study/ (GitHub Pages, branch main). Do NOT run git commands; the coordinator commits and pushes.
- Model to copy: `guides/2026-11-04-maths-aa-sl-1.2-1.6.html` (newest standard: copy its CSS, its quiz/ican JavaScript, its plan cards, nav, end block). Also look at `guides/2026-11-03-chemistry-s1.1-s1.3.html`.

## Sources
- Drive folder map with every file ID and question↔mark-scheme pairs: `/Users/I076795/.claude-personal/projects/-Users-I076795-ClaudeMe/memory/reference_ib_drive_map.md`. Drive links have the form `https://drive.google.com/file/d/<ID>/view`.
- Read the actual files with the Google Drive tools (ToolSearch "select:mcp__claude_ai_Google_Drive__read_file_content,mcp__claude_ai_Google_Drive__download_file_content"). Drive is READ-ONLY.
- Official subject guide text already extracted locally (use these for exact syllabus statements):
  - Maths AA: `/private/tmp/claude-501/-Users-I076795-ClaudeMe/72f15993-3922-4df0-aea2-02c19027b8a6/scratchpad/pdf/guide_layout.txt`
  - Chemistry (first assessment 2025): `.../scratchpad/ibchem/guide.txt`
  - Business management (first assessment 2024): `.../scratchpad/ibguide/guide.txt`
  - Biology: NO official guide available. Build from her packs, mark schemes and teacher materials, and show a visible note near the top: "The syllabus wording on this page has not yet been checked against the official IB Biology guide." Add an HTML comment listing what is unverified.
- Web search only to confirm exam formats or common mistakes; never copy text from websites. Never download unauthorised copies of IB papers, mark schemes or textbooks.

## Page structure (all required)
1. Hero banner that IS the content (a diagram or picture that the topic explains), inline SVG.
2. Nav (sticky) whose FIRST link is `<a href="../index.html" style="font-weight:700;color:var(--indigo)">All days</a>`.
3. "How to spend the N hours": 4 step-by-step block cards (`.plan > div` with `.bh` header "Block n · X min" + title, then an `<ol>` of steps, each with minutes in `<span class="t">(n min)</span>`). Each step says exactly what to open (linked), which questions, how to mark (mark scheme, M1/A1 where relevant), and to log mistakes in the Error log. Minutes must add up per block. Then "Files for today" Drive links.
4. One section per syllabus sub-topic: "I can" checklist written from the OFFICIAL statements (official numbering; if the school numbers differ, say so in a small mapping note), explanations, at least one worked example per skill with every step shown, an "Exam trap" callout, a collapsible self-check with answers.
5. Mark what the formula/data booklet gives: green `<span class="fb">In booklet</span>` vs amber `<span class="learn">Learn</span>`, with the visible legend (copy from the maths guide). For Business use "On formula sheet".
6. A 10-question multiple-choice quiz in the subject's exam style, each with an explanation of the trap, scored in the page. The quiz MUST save its result: copy the maths guide's `if(done===qs.length){ ... localStorage ... }` line with the key `ib-quiz-guide-YYYY-MM-DD` (the guide's date).
7. "I can" boxes: unique localStorage key `ib-<subject>-<topics>-ican`, unique `data-k` per box.
8. Closing block: tick the boxes, mark the pack work, write mistakes into the Error log tab of the study sheet, plus the line linking `../flashcards.html`, the exam technique page (`../exam-<subject>.html` if it exists, else `../exam.html`) and `../progress.html`.

## Content rules
- Link every file where it is mentioned (pack, mark scheme, handout, worksheet), not only in the file list.
- Only send her to pack questions the guide does NOT already solve (no duplicates between worked examples/self-checks and the plan's assigned questions). If a file has only answers, say so and explain how to use it.
- Every number and fact must be correct: compute every worked example, self-check and quiz answer (use python). If unsure of a syllabus detail, say so in an HTML comment, never guess.
- British spelling. NO em dashes anywhere. No sentences inside SVG `<text>`: labels only (numbers, symbols, one or two words); explanations go in HTML captions/keys. SVG label font-size at least 22 in a ~700-wide viewBox so they are readable at 390 px.
- Self-contained single HTML file: inline CSS/JS/SVG, no external fonts, scripts or images. Works offline and on a phone.
- Keep formulas from breaking mid-expression: wrap them in `<span class="nw">` (see the maths guide), use `&nbsp;` as thousands separator.
- JavaScript strings: never put an unescaped apostrophe inside a single-quoted JS string.

## Checks before you report back
- `python3 tools/check_layout.py <absolute path to your html>` must print `[width, []] []` for 380, 390, 600, 1000, 1200 (last list = JS errors). Fix anything else.
- Render with Python Playwright (plain `python3`, chromium installed) at 390 and 1000 px, look at the screenshots, fix layout problems.
- Run the quiz once in Playwright: answer all, confirm the score text and that `localStorage['ib-quiz-guide-YYYY-MM-DD']` is set.
- grep the file for "—" (must be 0).

## What to return (plain text)
- File path(s) written.
- The "I can" localStorage key, every data-k with the official topic code it belongs to, and the section anchors (e.g. `#s14`).
- The quiz localStorage key.
- 10 to 25 flashcards as JSON lines: {"id":"<subject letter><nn>","s":"<Subject>","t":"<topic code>","l":"guides/<file>#<anchor>","f":"<front html>","b":"<back html>"} (facts to learn by heart; no em dashes; no apostrophes problems).
- Sources used (Drive file names/IDs), decisions you made, anything unverified or uncertain.
