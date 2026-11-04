# Brief: background words and ideas for a guide page

Why: Jamila (IB Diploma, Grade 11, started late) worked through the 3 Nov chemistry guide and had to stop many times to look up words, for example "heterogeneous". The guide did define it ("regions with different composition and more than one phase"), but with more words she did not know. She may have missed parts of the Grade 9 and 10 course in each subject. Goal: she can work through a guide without leaving the page.

Do NOT run git. Do not change the guide's teaching content by hand; everything goes through the JSON file and `tools/terms.py`.

## What you produce
`tools/terms/<guide file name without .html>.json`, then run
`python3 tools/terms.py guides/<guide>.html tools/terms/<guide>.json` (from the repo root `~/ClaudeMe/study`). The tool is safe to run again after edits.

Format (see the docstring in tools/terms.py):
```
{"minutes": 6,
 "background": [{"title": "...", "html": "<p>...</p>", "link": {"url": "...", "label": "..."}}],
 "terms": [{"key": "heterogeneous", "word": "heterogeneous", "match": ["heterogeneous"], "def": "..."}]}
```

## Step 1: find the gaps
Read the WHOLE guide text (prose, tables, worked examples, self-check answers, exam traps, plan; the quiz questions live in the script, read those too) as a student who has NOT done this subject's Grade 9 and 10 course. List:
- every subject word that is used without being explained first, or explained only with other hard words (chemistry: phase, composition, immiscible, solvent, solute, kinetic energy, frequency, ion; maths: integer, coefficient, expression, substitute, sigma; business: stakeholder, revenue, liability; biology: polymer, monomer, hydrogen bond);
- general academic words a 16-year-old may not know (deduce, derive, hence, constituent, subsequent, viable);
- IB command terms used on the page (state, outline, explain, describe, deduce, evaluate, show that, hence...): give the official IB meaning in plain words;
- symbols and notation used without explanation (Σ, ∞, ≈, ∝, subscripts like u_n, units like mol dm^-3).
Typical size: 30 to 70 terms. Include a term even if the page explains it later, when it is USED before that explanation.

## Step 2: definitions ("def")
- 1 to 3 short sentences, at most about 40 words, in everyday words. Add a tiny example where it helps ("Oil on water is two phases.").
- Never explain a word with another hard word. If you must use one, that word must also be a term in your list.
- Correct for IB at this level and consistent with how the guide uses it. If a word has an everyday meaning and a subject meaning, give the subject meaning.
- British spelling. No em dashes. HTML allowed (<b>, <i>, <sub>, <sup>), nothing else.
- "match": every form that appears on the page (singular, plural, -ing, capitalised forms are matched automatically). Avoid very short or very common matches that would underline the wrong thing (e.g. do not match "term" in a maths guide where "term" is used constantly unless that IS a gap; do not match "mass" inside "mass number" if both are terms: the tool prefers the longest match).
- "key": lowercase, unique.

## Step 3: "Before you start" box ("background")
4 to 8 ideas the topic builds on that a word definition cannot carry (for example chemistry: "Atoms, elements and the periodic table", "Energy and frequency of light"; maths: "Substituting into a formula", "Indices: what 2^5 and 2^-1 mean"; business: "What a business is for"; biology: "What a molecule and a bond are").
- Each: a title and 60 to 150 words of HTML (<p>, <ul>, <b>, <sub>, <sup>, a small table). A small inline SVG is allowed only if it really helps: labels only (no sentences), font-size at least 22 in a ~700 wide viewBox, use the page's CSS colours (var(--indigo) etc.).
- Plain words, correct, no em dashes.
- "minutes": realistic reading time for the box (usually 5 to 10).
- Optional "link": ONLY for an idea that text cannot carry well (moving or 3D things, a skill that needs practice). ONLY a specific lesson page on Khan Academy (khanacademy.org) or BBC Bitesize (bbc.co.uk/bitesize). You MUST open the URL (WebFetch, load it with ToolSearch "select:WebFetch") and confirm it loads and teaches exactly that idea at a suitable level. If you cannot confirm it, leave the link out. Never link anything else.

Notes on the tool: words inside the "I can" checkbox lines ARE underlined (their text is put in a <span> first). Headings, links, buttons, the hero and SVG are never underlined. Words that appear only inside quiz answers (hidden until answered) are fine; check_terms.py lists them as a note.

## Step 4: check
- `python3 tools/terms.py ...` prints how many terms were underlined and lists any term not found on the page: fix the "match" or drop the term.
- `python3 tools/check_terms.py <absolute path to the guide> <scratchpad>/x.png` must end with OK.
- `python3 tools/check_layout.py <absolute path to the guide>` must print `[width, []] []` for every width.
- Look at the screenshot. Also take a 390 px screenshot of the #before section (Python Playwright, plain python3) and look at it.
- `grep -c "—"` on the guide and on your JSON: must be 0.
- Save screenshots in the scratchpad, never in the repo.

## What to return (plain text)
The JSON path, number of terms and background items, the list of terms (key only), any links you added with what you confirmed, anything you were unsure about.
