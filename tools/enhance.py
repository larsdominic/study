#!/usr/bin/env python3
"""Add the learning extras to guide, practice and review pages.

Usage: python3 tools/enhance.py guides/<page>.html practice/<page>.html review/<page>.html ...

Adds (safe to run again: it removes its own blocks between <!--enhance:start--> and
<!--enhance:end--> and adds them fresh):
  1. "Warm-up from earlier days (8 min)": 5 flashcard questions from earlier guides, chosen now
     (at build time) from the cards in tools/flash.py: 3 from guides planned 1 to 3 days before this
     page's plan day, 2 from guides 7 or more days before, topped up from any earlier guide. Same
     date gives the same choice. Goes into <div id="warmup"></div> if the page has one, else right
     after the "Today you will be able to" box, else at the top of <main>.
  2. The quiz extras (tools/quizjs.py ENGINE): Sure / Guessing per question, "Log these first" list,
     <key>-attempts history, "Try again (shuffled)", self-mark menus on .written[data-max] items.
     The page's own quiz script still scores the first round and saves its key as before.
  3. Phone nav: the sticky section menu is one row that scrolls sideways below 600 px.
  4. A notice under the top bar when this browser cannot save progress (storageOK() in quizjs.py).
  5. The shared site layer from tools/common.py (UX review 8 Nov): sticky top bar (Today, Flashcards,
     Progress, Sheet), section menu as one sideways row with the current section marked, visible focus,
     contrast tokens, one badge system, 44 px targets, numbered timed blocks with "Block done" ticks
     (localStorage 'ib-<file name>-blocks'), print CSS, <meta name="color-scheme" content="light">.
  6. A "Today" card at the top of <main>: the page's own "Today you will be able to" box is MOVED into it
     (its old place keeps <!--enhance:origin-->, and a rerun puts it back first), chips that jump to each
     timed block ("Block 1 · 25 min"; ids b1..bn are added to the blocks if missing; "Block 0 · Before
     you start" when terms.py added it) and the warm-up. Pages with neither a goals box nor numbered
     blocks keep the warm-up where it was before (warmup div, or top of <main>).
  Badges "In booklet" / "On formula sheet" get the class "given" (neutral outline instead of indigo "Apply").

Dates come from tools/links.json (first non-review day the page is planned for), else from the
date in the file name. Rerun after adding flashcards or changing the plan.
"""
import ast, datetime, html, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from quizjs import ENGINE, STORAGE_JS, CSS as QUIZ_CSS  # noqa: E402
from common import SITE_CSS, SITE_JS, site_bar  # noqa: E402

START, END = '<!--enhance:start-->', '<!--enhance:end-->'
STRIP = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
MOVED_A, MOVED_B, ORIGIN = '<!--enhance:moved-->', '<!--enhance:/moved-->', '<!--enhance:origin-->'
MOVED = re.compile(re.escape(MOVED_A) + r'(.*?)' + re.escape(MOVED_B), re.S)
SHEET = 'https://docs.google.com/spreadsheets/d/1svykHaPDhtPFnzkO6tdNk8GPLWyd8tOh6IAV-9gwkJQ/edit'

CSS = '''
.warmup{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--amber);padding:12px 16px 4px;margin:24px 0}
.warmup h2{margin:0 0 6px;font-size:1.3rem}
.warmup .wu-how{font-size:.95rem;color:var(--ink-soft);margin:0 0 8px}
.warmup ol{margin:0;padding-left:24px}
.warmup li{margin:10px 0}
.warmup .wu-m{font-size:.8rem;color:var(--ink-soft)}
.warmup .wu-f{font-weight:600}
.warmup details{margin-top:4px}
.warmup summary{cursor:pointer;color:var(--indigo);font-size:.92rem}
.warmup .wu-b{border-top:1px solid var(--rule);margin-top:6px;padding-top:6px}
.warmup .wu-b a{font-size:.88rem;margin-left:6px;white-space:nowrap}
.warmup .wu-foot{font-size:.92rem;margin:12px 0 8px}
''' + QUIZ_CSS + SITE_CSS


def _val(n, env):
    """Strings, lists, tuples, names and + only (enough for M + "#s12" in the cards list)."""
    if isinstance(n, ast.Constant):
        return n.value
    if isinstance(n, ast.Name):
        return env[n.id]
    if isinstance(n, (ast.List, ast.Tuple)):
        v = [_val(x, env) for x in n.elts]
        return v if isinstance(n, ast.List) else tuple(v)
    if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Add):
        return _val(n.left, env) + _val(n.right, env)
    raise ValueError('unsupported')


def load_cards():
    """The cards list from tools/flash.py, read without running the script."""
    tree = ast.parse(open(os.path.join(HERE, 'flash.py')).read())
    env = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                env[node.targets[0].id] = _val(node.value, env)
            except (ValueError, KeyError):
                pass
    return env['cards']


LINKS = json.load(open(os.path.join(HERE, 'links.json')))
PLAN = {p['iso']: p for p in json.load(open(os.path.join(HERE, 'plan.json')))}


def first_dates():
    """page url -> first plan day (a non-review entry wins over a review one)."""
    first, anyd = {}, {}
    for iso in sorted(LINKS):
        ls = LINKS[iso] if isinstance(LINKS[iso], list) else [LINKS[iso]]
        for l in ls:
            anyd.setdefault(l['url'], iso)
            if not l.get('review'):
                first.setdefault(l['url'], iso)
    for u, d in anyd.items():
        first.setdefault(u, d)
    return first


FIRST = first_dates()


def rel_url(path):
    p = os.path.abspath(path).split(os.sep)
    return '/'.join(p[-2:])


def page_date(path):
    r = rel_url(path)
    if r in FIRST:
        return FIRST[r]
    m = re.search(r'(\d{4}-\d\d-\d\d)', os.path.basename(path))
    return m.group(1) if m else None


def quiz_key(path, t):
    r = rel_url(path)
    for iso in LINKS:
        for l in (LINKS[iso] if isinstance(LINKS[iso], list) else [LINKS[iso]]):
            if l['url'] == r and l.get('quiz'):
                return l['quiz']
    m = re.search(r'''['"](ib-quiz-[a-z0-9-]+)['"]''', t)
    if m:
        return m.group(1)
    m = re.search(r'PAGE\s*=\s*"(\d{4}-\d\d-\d\d)"', t)
    if m and 'ib-timed-' in t:
        return 'ib-timed-' + m.group(1)
    return None


def pick(cards, pdate):
    if not pdate:
        return []
    pd = datetime.date.fromisoformat(pdate)
    items = []
    for c in cards:
        d = FIRST.get(c[3].split('#')[0])
        if not d or not c[3].startswith(('guides/', 'practice/', 'review/')):
            continue
        gap = (pd - datetime.date.fromisoformat(d)).days
        if gap >= 1:
            items.append((gap, d, c))
    rng = random.Random(pdate)
    recent = [x for x in items if 1 <= x[0] <= 3]
    old = [x for x in items if x[0] >= 7]
    chosen = rng.sample(recent, min(3, len(recent))) + rng.sample(old, min(2, len(old)))
    rest = [x for x in items if x not in chosen]
    chosen += rng.sample(rest, min(5 - len(chosen), len(rest)))
    rng.shuffle(chosen)
    return chosen


def day_label(iso):
    p = PLAN.get(iso)
    if p:
        return f"{p['day']} {p['date']}"
    d = datetime.date.fromisoformat(iso)
    return d.strftime('%a ') + str(d.day) + d.strftime(' %b')


def warmup_html(path, with_id):
    pdate = page_date(path)
    chosen = pick(load_cards(), pdate)
    sid = (f' id="{with_id}"' if isinstance(with_id, str) else ' id="warmup"') if with_id else ''
    h = [f'<section class="warmup"{sid} aria-label="Warm-up from earlier days">',
         '<h2>Warm-up from earlier days (8 min)</h2>']
    if not chosen:
        h.append('<p class="wu-how">From tomorrow this box asks you 5 questions from earlier days. Answering from memory is what makes things stick.</p>')
    else:
        h.append('<p class="wu-how">Answer from memory before you read on: write the answer on paper, then tap to check it.</p><ol>')
        depth = '../' if rel_url(path).count('/') else ''
        for gap, d, c in chosen:
            _id, subj, topic, link, front, back = c
            h.append(f'<li><div class="wu-m">{html.escape(subj)} · {html.escape(topic)} · from {day_label(d)}</div>'
                     f'<div class="wu-f">{front}</div>'
                     f'<details><summary>Write the answer on paper, then tap</summary>'
                     f'<div class="wu-b">{back} <a href="{depth}{link}">open the section</a></div></details></li>')
        h.append('</ol>')
    h.append(f'<p class="wu-foot">Missed one? Put it in the <a href="{SHEET}">Error log</a>.</p></section>')
    return '\n'.join(h)


def block_end(t, i):
    """End index of the element whose opening tag starts at i (simple tag balance)."""
    m = re.match(r'<([a-zA-Z0-9]+)', t[i:])
    tag = m.group(1).lower()
    depth = 0
    for mo in re.compile(r'<(/?)' + tag + r'\b[^>]*>', re.I).finditer(t, i):
        depth += -1 if mo.group(1) else 1
        if depth == 0:
            return mo.end()
    return -1


def place_warmup(t, path):
    m = re.search(r'(<div id="warmup"[^>]*>)\s*(</div>)', t)
    if m:
        return t[:m.end(1)] + START + warmup_html(path, False) + END + t[m.start(2):], 'warmup div'
    p = t.find('Today you will be able to')
    if p >= 0:
        for mo in reversed(list(re.finditer(r'<(div|section|aside)\b[^>]*>', t[:p]))):
            e = block_end(t, mo.start())
            if e > p:
                return t[:e] + START + '\n' + warmup_html(path, True) + '\n' + END + '\n' + t[e:], 'after "Today you will be able to"'
    m = re.search(r'<main\b[^>]*>', t)
    if m:
        return t[:m.end()] + START + '\n' + warmup_html(path, True) + '\n' + END + '\n' + t[m.end():], 'top of main'
    m = re.search(r'</header>', t)
    e = m.end() if m else re.search(r'<body[^>]*>', t).end()
    return t[:e] + START + '\n' + warmup_html(path, True) + '\n' + END + '\n' + t[e:], 'after header'


def unmove(t):
    """Put a goals box that an earlier run moved into the Today card back where it was."""
    m = MOVED.search(t)
    if not m:
        return t.replace(ORIGIN, '')
    box = m.group(1)
    t = t[:m.start()] + t[m.end():]
    return t.replace(ORIGIN, box, 1) if ORIGIN in t else t


def goals_box(t):
    """(start, end) of the element holding "Today you will be able to", or None."""
    body = t.find('<body')
    p = t.find('Today you will be able to', body if body >= 0 else 0)
    if p < 0:
        return None
    for mo in reversed(list(re.finditer(r'<(div|section|aside|header)\b[^>]*>', t[:p]))):
        if re.match(r'<header class="(hero|top)"', mo.group(0)):
            return None
        e = block_end(t, mo.start())
        if e > p:
            return mo.start(), e
    return None


def find_blocks(t):
    """Numbered timed blocks: list of dicts n, mins, pos (index right after '<tag'), attrs, id.
    Three markups: guide plans (<div><div class="bh"><b>Block 1 · 25 min</b>), the .block cards of
    review.py / timed.py (<span class="bn">1</span> ... <span class="bt">25 min</span>), and
    <h2>Block 1. Title (15 min)</h2> on the revision pages."""
    pats = [
        (re.compile(r'<(div)\b([^>]*)>\s*<div class="bh">\s*<b>\s*Block\s+(\d+[a-z]?)\s*·\s*([^<]+?)\s*</b>'), 3, 4),
        (re.compile(r'<(div)\b([^>]*\bclass="block\b[^>]*)>\s*<div class="bh">\s*<span class="bn"[^>]*>([^<]+)</span>.*?<span class="bt">([^<]+)</span>', re.S), 3, 4),
        (re.compile(r'<(h2)\b([^>]*)>\s*Block\s+(\d+)[.:]\s*[^<]*?\((?:[^()<]*?,\s*)?(\d+\s*min)\)\s*</h2>'), 3, 4),
    ]
    for rx, gn, gm in pats:
        out, seen = [], set()
        for m in rx.finditer(t):
            n = m.group(gn).strip()
            if n in seen:
                continue
            seen.add(n)
            idm = re.search(r'\bid="([^"]+)"', m.group(2))
            out.append({'n': n, 'mins': m.group(gm).strip(), 'pos': m.start() + 1 + len(m.group(1)),
                        'id': idm.group(1) if idm else None})
        if out:
            return out
    return []


def add_block_ids(t, blocks):
    """Give blocks without an id the id b<n> (unless that id is taken). Works from the end so positions hold."""
    for b in sorted(blocks, key=lambda x: -x['pos']):
        if b['id']:
            continue
        bid = 'b' + b['n']
        if f'id="{bid}"' in t:
            bid = 'block-' + b['n']
        t = t[:b['pos']] + f' id="{bid}"' + t[b['pos']:]
        b['id'] = bid
    return t


def today_card(t, path):
    """Build the Today card at the top of <main>. Returns (text, where) or None when the page has
    neither a goals box nor numbered blocks."""
    box = goals_box(t)
    blocks = find_blocks(t)
    if not box and not blocks:
        return None
    m = re.search(r'<main\b[^>]*>', t)
    if not m:
        return None
    goals = ''
    if box:
        s, e = box
        goals = t[s:e]
        t = t[:s] + ORIGIN + t[e:]
    t = add_block_ids(t, find_blocks(t))
    blocks = find_blocks(t)
    chips = []
    if 'id="before"' in t:
        chips.append('<a class="chip c0" href="#before"><b>Block 0</b> · Before you start</a>')
    chips.append('<a class="chip" href="#wu"><b>Warm-up</b> · 8 min</a>')
    for b in blocks:
        chips.append(f'<a class="chip" href="#{b["id"]}" data-n="{html.escape(b["n"])}"><b>Block {html.escape(b["n"])}</b> · {html.escape(b["mins"])}</a>')
    plan = ('<div class="tc-plan"><p class="tc-h">Today: tap a block to jump to it</p>'
            '<div class="chips">' + ''.join(chips) + '</div></div>')
    # chips first (so the plan is in reach on the first screens), then the goals box, then the warm-up
    head = START + '\n<section class="todaycard" aria-label="Today">' + plan + ('<div class="tc-goals">' if goals else '') + END
    tail = (START + ('</div>' if goals else '') + '\n' + warmup_html(path, 'wu') + '\n</section>' + END + '\n')
    mid = (MOVED_A + goals + MOVED_B) if goals else ''
    m = re.search(r'<main\b[^>]*>', t)
    t = t[:m.end()] + head + mid + tail + t[m.end():]
    return t, 'Today card' + (' (goals box moved in)' if goals else ' (no goals box)') + f', {len(blocks)} block chips'


GIVEN = re.compile(r'<span class="fb"((?:\s[^>]*)?)>(\s*(?:In (?:the )?booklet|On (?:the )?formula sheet|Given))')


def enhance(path):
    t = open(path, encoding='utf-8').read()
    t = unmove(t)
    t = STRIP.sub('', t)
    key = quiz_key(path, t)
    t = GIVEN.sub(lambda m: f'<span class="fb given"{m.group(1)}>{m.group(2)}', t)
    r = today_card(t, path)
    if r:
        t, where = r
    else:
        t, where = place_warmup(t, path)
    t = t.replace('</head>', START + '<meta name="color-scheme" content="light"><style>' + CSS + '</style>' + END + '\n</head>', 1)
    parent = os.path.basename(os.path.dirname(os.path.abspath(path)))
    depth = '../' if parent in ('guides', 'practice', 'review') else ''
    mb = re.search(r'<body\b[^>]*>', t)
    t = t[:mb.end()] + site_bar(depth) + '\n' + t[mb.end():]
    js = (STORAGE_JS + ENGINE + '\nstorageNotice();\nibQuizEnhance(' + json.dumps({'key': key, 'own': False}) + ');\n'
          + SITE_JS + '\n')
    i = t.rfind('</body>')
    t = t[:i] + START + '<script>' + js + '</script>' + END + '\n' + t[i:]
    open(path, 'w', encoding='utf-8').write(t)
    print(f'{path}: warm-up {where} (plan day {page_date(path)}), quiz key {key}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for p in sys.argv[1:]:
        enhance(p)
