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
Each term is underlined at its first appearance in every section of <main>
(not inside headings, links, buttons, SVG or scripts).
"""
import json, re, sys, html

START, END = '<!--terms:start-->', '<!--terms:end-->'
CSS = """
/*terms:start*/
.term{border-bottom:2px dotted var(--indigo);cursor:pointer;border-radius:2px}
.term:hover,.term:focus{background:var(--indigo-soft);outline:none}
#termbox{display:none;position:fixed;left:10px;right:10px;bottom:10px;max-width:640px;margin:0 auto;background:var(--card);border:2px solid var(--indigo);border-radius:12px;padding:14px 16px 12px;box-shadow:0 8px 28px rgba(0,0,0,.22);z-index:60;max-height:60vh;overflow:auto}
#termbox.on{display:block}
#termbox .tb-h{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
#termbox .tb-h b{font-size:1.1rem;color:var(--indigo)}
#termbox button{font:inherit;border:1px solid var(--rule);background:var(--paper);border-radius:8px;padding:4px 12px;cursor:pointer;flex:none}
#termbox .tb-d{margin:8px 0 0;line-height:1.5}
.before .bgi{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);border-radius:10px;padding:12px 16px;margin:12px 0}
.before .bgi h3{margin:0 0 6px;font-size:1.08rem}
.before .bgi p{margin:6px 0}
.before .bgi svg{max-width:100%;height:auto;display:block;margin:8px auto}
.before .more{font-size:.95rem;color:var(--ink-soft)}
.before .stuck{background:var(--amber-soft);border-radius:10px;padding:10px 14px}
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
        'h1', 'h2', 'h3', 'code', 'nav', 'header', 'head'}
VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'col', 'source', 'wbr', 'area', 'base'}


def strip_old(t):
    t = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', t, flags=re.S)
    t = re.sub(r'\n?/\*terms:start\*/.*?/\*terms:end\*/\n?', '\n', t, flags=re.S)
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
    stack, used, out = [], set(), []
    for p in parts:
        if p.startswith('<!--'):
            out.append(p); continue
        if p.startswith('<'):
            m = re.match(r'<\s*(/)?\s*([a-zA-Z0-9]+)', p)
            if m:
                name = m.group(2).lower()
                if name == 'section' and not m.group(1):
                    used = set()  # a new section: underline each word once again
                if name not in VOID and not p.endswith('/>'):
                    if m.group(1):
                        # close the nearest matching open tag
                        for i in range(len(stack) - 1, -1, -1):
                            if stack[i] == name:
                                del stack[i:]; break
                    else:
                        stack.append(name)
            out.append(p); continue
        if any(s in SKIP for s in stack) or not p.strip():
            out.append(p); continue

        def rep(mo):
            idx = next(i for i, g in enumerate(mo.groups()) if g is not None)
            k = keys[idx]
            if k in used:
                return mo.group(0)
            used.add(k)
            return f'<span class="term" data-t="{html.escape(k)}" tabindex="0" role="button">{mo.group(0)}</span>'
        out.append(rx.sub(rep, p))
    return ''.join(out)


def before_section(d):
    items = []
    for b in d['background']:
        more = ''
        if b.get('link'):
            more = (f'<p class="more">Want to see it explained another way? '
                    f'<a href="{html.escape(b["link"]["url"])}" target="_blank" rel="noopener">{b["link"]["label"]}</a></p>')
        items.append(f'<div class="bgi"><h3>{b["title"]}</h3>{b["html"]}{more}</div>')
    return (f'{START}<section id="before" class="before">\n'
            f'  <h2 style="margin-top:28px">Before you start (about {d["minutes"]} min)</h2>\n'
            f'  <p style="margin:10px 0 0">This page builds on the ideas below. Read them first so you do not have to stop later. '
            f'Words with a <span style="border-bottom:2px dotted var(--indigo)">dotted underline</span> anywhere on the page: tap them for a short explanation.</p>\n'
            f'  {"".join(items)}\n'
            f'  <p class="stuck"><b>Still stuck on a word?</b> Do not search for long. Write it in the <b>Error log</b> tab of the study sheet '
            f'starting with "word:" (for example "word: composition") and carry on. It will be explained in the next guide.</p>\n'
            f'</section>{END}\n\n')


def main(path, jpath):
    t = open(path, encoding='utf-8').read()
    d = json.load(open(jpath, encoding='utf-8'))
    t = strip_old(t)
    # CSS
    t = t.replace('</style>', CSS + '</style>', 1)
    # nav link after "All days"
    t = re.sub(r'(<a href="\.\./index\.html"[^>]*>All days</a>)', r'\1' + START + '<a href="#before">Before you start</a>' + END, t, count=1)
    # the box before the plan, and a pointer in the plan intro
    t = t.replace('<section id="plan">', before_section(d) + '<section id="plan">', 1)
    t = re.sub(r'(<section id="plan">.*?</h2>)', r'\1' + START + f'<p style="margin:10px 0 0"><b>First:</b> read <a href="#before">Before you start</a> (about {d["minutes"]} min). It is not counted in the blocks below.</p>' + END, t, count=1, flags=re.S)
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
