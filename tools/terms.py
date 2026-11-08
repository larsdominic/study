#!/usr/bin/env python3
"""Add tap-to-explain words and a "Before you start" box to a guide page.

Usage: python3 tools/terms.py guides/<guide>.html tools/terms/<guide>.json

The JSON file:
{
  "minutes": 6,
  "background": [
    {"title": "What a wave is", "html": "<p>...</p>",
     "link": {"url": "https://www.khanacademy.org/...", "label": "Khan Academy: ..."}}   (link optional)
  ],
  "terms": [
    {"key": "heterogeneous", "match": ["heterogeneous"], "def": "Plain-words explanation (HTML allowed)."}
  ]
}

Safe to run again: it removes what it added before and adds it fresh.
Each term is underlined ONCE per page: at its first use in always-visible text of <main>, else at its
first use in hidden text (closed <details>, quiz explanations). Never inside h1 to h3, links, buttons
(quiz options included), nav, SVG, scripts or the blocks enhance.py adds (warm-up, Today card chips).
The "Before you start" box goes at the start of the plan as "Block 0 · Before you start"
(a <details open>, so it can be folded away): first child of <div class="plan">, else right after the
plan heading, else at the top of <main>.
"""
import json, re, sys, html

START, END = '<!--terms:start-->', '<!--terms:end-->'
CSS = """
/*terms:start*/
.term{border-bottom:2px dotted var(--indigo);cursor:pointer;border-radius:2px}
.term:focus-visible{background:var(--indigo-soft)}
@media (hover:hover){.term:hover{background:var(--indigo-soft)}}
#termbox{display:none;position:fixed;left:10px;right:10px;bottom:10px;max-width:640px;margin:0 auto;background:var(--card);border:2px solid var(--indigo);border-radius:8px;padding:14px 16px 12px;box-shadow:0 8px 28px rgba(0,0,0,.22);z-index:60;max-height:60vh;overflow:auto}
#termbox.on{display:block}
#termbox .tb-h{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
#termbox .tb-h b{font-size:1.1rem;color:var(--indigo)}
#termbox button{font:inherit;border:1px solid var(--rule);background:var(--paper);border-radius:8px;padding:4px 12px;cursor:pointer;flex:none;min-height:44px;min-width:44px}
#termbox .tb-d{margin:8px 0 0;line-height:1.5}
.before.block0{background:var(--card);border:1px solid var(--rule);border-radius:8px;padding:12px 16px;margin:12px 0}
.before > details{background:transparent;border:0;padding:0;margin:0}
.before > details > summary{display:grid;grid-template-columns:32px minmax(0,1fr) auto auto;align-items:center;gap:4px 10px;min-height:44px;list-style:none;cursor:pointer}
.before > details > summary::-webkit-details-marker{display:none}
.before > details > summary::after{content:"Hide";font-size:.85rem;font-weight:600;color:var(--indigo)}
.before > details:not([open]) > summary::after{content:"Show"}
.before .bn{flex:none;display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:var(--indigo);color:#fff;font-weight:700}
.before .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.before .b0t{font-size:1.15rem;font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-weight:600;color:var(--ink)}
.before .bt{white-space:nowrap;font-size:.8rem;font-weight:700;color:var(--ink);background:var(--paper);border:1px solid var(--rule);border-radius:4px;padding:2px 8px}
.before .bgi{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);border-radius:8px;padding:12px 16px;margin:12px 0}
.before .bgi h3{margin:0 0 6px;font-size:1.08rem}
.before .bgi p{margin:6px 0}
.before .bgi svg{max-width:100%;height:auto;display:block;margin:8px auto}
.before .more{font-size:.95rem;color:var(--ink-soft)}
.before .stuck{background:var(--amber-soft);border-radius:8px;padding:10px 14px}
/*terms:end*/
"""
JS = r"""<script>
(function(){
  // tap a dotted word to see what it means
  var T={};
  try{ T=JSON.parse(document.getElementById('terms-data').textContent); }catch(e){ return; }
  var box=document.getElementById('termbox'), bt=box.querySelector('.tb-h b'), bd=box.querySelector('.tb-d');
  function show(el){ var k=el.getAttribute('data-t'); if(!T[k]) return; bt.textContent=T[k].w; bd.innerHTML=T[k].d; box.classList.add('on'); }
  function hide(){ box.classList.remove('on'); }
  document.addEventListener('click',function(e){
    var el=e.target.closest ? e.target.closest('.term') : null;
    if(el){ e.preventDefault(); e.stopPropagation(); show(el); return; }
    if(!box.contains(e.target)) hide();
  },true);
  document.addEventListener('keydown',function(e){
    if(e.key==='Escape') hide();
    if((e.key==='Enter'||e.key===' ') && e.target.classList && e.target.classList.contains('term')){ e.preventDefault(); show(e.target); }
  });
  box.querySelector('button').addEventListener('click',hide);
})();
</script>"""

SKIP = {'script', 'style', 'svg', 'a', 'button', 'title', 'textarea', 'select', 'option',
        'h1', 'h2', 'h3', 'code', 'nav', 'header', 'head', 'summary'}
VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'col', 'source', 'wbr', 'area', 'base'}


def strip_old(t):
    t = re.sub(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', '', t, flags=re.S)
    t = re.sub(r'\n?/\*terms:start\*/.*?/\*terms:end\*/\n?', '', t, flags=re.S)
    # unwrap old term spans
    t = re.sub(r'<span class="term" data-t="[^"]*" tabindex="0" role="button">(.*?)</span>', r'\1', t, flags=re.S)
    return t


def wrap_terms(main, terms):
    # longest variants first so "common difference" wins over "difference"
    pats = []
    for t in terms:
        for m in t['match']:
            pats.append((m, t['key']))
    pats.sort(key=lambda p: -len(p[0]))
    rx = re.compile('|'.join(r'(?<![\w&#-])(' + re.escape(m) + r')(?![\w-])' for m, _ in pats), re.I)
    keys = [k for _, k in pats]
    parts = re.split(r'(<!--.*?-->|<[^>]+>)', main, flags=re.S)
    # stack of (tag name, hidden?) ; text in a closed <details> or a quiz explanation (.why) is hidden
    stack, info, in_enh = [], [], False
    for i, p in enumerate(parts):
        if p.startswith('<!--'):
            if p == '<!--enhance:start-->':
                in_enh = True
            elif p == '<!--enhance:end-->':
                in_enh = False
            continue
        if p.startswith('<'):
            m = re.match(r'<\s*(/)?\s*([a-zA-Z0-9]+)', p)
            if m:
                name = m.group(2).lower()
                if name not in VOID and not p.endswith('/>'):
                    if m.group(1):
                        for j in range(len(stack) - 1, -1, -1):
                            if stack[j][0] == name:
                                del stack[j:]; break
                    else:
                        cls = re.search(r'\bclass="([^"]*)"', p)
                        cls = cls.group(1).split() if cls else []
                        hidden = (name == 'details' and not re.search(r'\sopen\b', p)) or 'why' in cls
                        stack.append((name, hidden))
            continue
        if in_enh or not p.strip() or any(s in SKIP for s, _ in stack):
            continue
        info.append((i, any(h for _, h in stack)))
    used = set()

    def rep(mo):
        idx = next(i for i, g in enumerate(mo.groups()) if g is not None)
        k = keys[idx]
        if k in used:
            return mo.group(0)
        used.add(k)
        return f'<span class="term" data-t="{html.escape(k)}" tabindex="0" role="button">{mo.group(0)}</span>'
    for want_hidden in (False, True):  # first use in visible text, then the rest from hidden text
        for i, hidden in info:
            if hidden == want_hidden:
                parts[i] = rx.sub(rep, parts[i])
    return ''.join(parts)


def before_section(d):
    items = []
    for b in d['background']:
        more = ''
        if b.get('link'):
            more = (f'<p class="more">Want to see it explained another way? '
                    f'<a href="{html.escape(b["link"]["url"])}" target="_blank" rel="noopener">{b["link"]["label"]}</a></p>')
        items.append(f'<div class="bgi"><h3>{b["title"]}</h3>{b["html"]}{more}</div>')
    return (f'{START}<div id="before" class="before block0"><details open>\n'
            f'  <summary><span class="bn" aria-hidden="true">0</span><span class="b0t"><span class="sr">Block 0: </span>Before you start</span>'
            f'<span class="bt">about {d["minutes"]} min</span></summary>\n'
            f'  <p style="margin:10px 0 0">This page builds on the ideas below. Read them first so you do not have to stop later '
            f'(about {d["minutes"]} min, not counted in the blocks below). '
            f'Words with a <span style="border-bottom:2px dotted var(--indigo)">dotted underline</span> anywhere on the page: tap them for a short explanation.</p>\n'
            f'  {"".join(items)}\n'
            f'  <p class="stuck"><b>Still stuck on a word?</b> Do not search for long. Write it in the <b>Error log</b> tab of the study sheet '
            f'starting with "word:" (for example "word: composition") and carry on. It will be explained in the next guide.</p>\n'
            f'</details></div>{END}\n')


def place_before(t, box):
    """Block 0 at the start of the plan."""
    m = re.search(r'<section id="plan"[^>]*>', t)
    if m:
        e = block_end_section(t, m.start())
        pm = re.compile(r'<div class="plan"[^>]*>').search(t, m.end(), e)
        if pm:
            return t[:pm.end()] + box + t[pm.end():]
        hm = re.compile(r'</h2>').search(t, m.end(), e)
        if hm:
            return t[:hm.end()] + box + t[hm.end():]
        return t[:m.end()] + box + t[m.end():]
    m = re.search(r'<main\b[^>]*>', t)
    return t[:m.end()] + box + t[m.end():]


def block_end_section(t, i):
    depth = 0
    for mo in re.compile(r'<(/?)section\b[^>]*>', re.I).finditer(t, i):
        depth += -1 if mo.group(1) else 1
        if depth == 0:
            return mo.end()
    return len(t)


def main(path, jpath):
    t = open(path, encoding='utf-8').read()
    d = json.load(open(jpath, encoding='utf-8'))
    t = strip_old(t)
    # CSS
    t = t.replace('</style>', CSS + '</style>', 1)
    # "Before you start" as Block 0 at the start of the plan (no separate nav link or pointer any more)
    t = place_before(t, before_section(d))
    # "I can" lines are flex boxes: their text must sit in one <span> before words inside can be wrapped
    t = re.sub(r'(<label[^>]*>\s*<input[^>]*>)(?!\s*<span>)(.*?)(</label>)', r'\1<span>\2</span>\3', t, flags=re.S)
    # wrap terms inside <main>
    a, b = t.index('<main'), t.index('</main>')
    t = t[:a] + wrap_terms(t[a:b], d['terms']) + t[b:]
    # data + box + script before </body>
    data = {x['key']: {'w': x.get('word', x['match'][0]), 'd': x['def']} for x in d['terms']}
    blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    tail = (START + '\n<div id="termbox" role="dialog" aria-live="polite"><div class="tb-h"><b></b><button type="button">Close</button></div><p class="tb-d"></p></div>\n'
            f'<script id="terms-data" type="application/json">{blob}</script>\n' + JS + END + '\n')
    i = t.rindex('</body>')
    t = t[:i] + tail + t[i:]
    open(path, 'w', encoding='utf-8').write(t)
    n = t.count('class="term"')
    missing = [x['key'] for x in d['terms'] if f'data-t="{html.escape(x["key"])}"' not in t]
    print(f'{path}: {len(d["terms"])} terms, {n} underlined, {len(d["background"])} background items')
    if missing:
        print('  not found on the page (check spelling or add a variant to "match"):', ', '.join(missing))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
