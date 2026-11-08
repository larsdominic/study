#!/usr/bin/env python3
"""Test the tap-to-explain words on a guide page.
Usage: python3 tools/check_terms.py <absolute path to guide html> [screenshot.png]
Checks: every term is underlined exactly once, never inside a button, link, h1 to h3, nav or summary;
every tap shows its definition; the termbox Close button is at least 44 x 44 px; "Before you start"
is Block 0: the first block of the plan (when the page has a plan), a <details> that is open by default.
Prints problems; the last line is OK or FAIL."""
import sys, os, json
from collections import Counter
from playwright.sync_api import sync_playwright
path = os.path.abspath(sys.argv[1]); shot = sys.argv[2] if len(sys.argv) > 2 else None
bad = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 390, 'height': 800})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + path)
    # Block 0 before anything is opened by the test
    b0 = pg.evaluate("""()=>{const b=document.getElementById('before'); if(!b) return null;
      const d=b.querySelector(':scope > details'); const plan=document.getElementById('plan');
      let first=null; if(plan){ const box=plan.querySelector('.plan'); first=box?box.firstElementChild:null; }
      return {details:!!d, open:!!(d&&d.open), title:d?d.querySelector('summary').textContent:'',
              inPlan:plan?plan.contains(b):null, first:first?first===b:null, hasPlanBox:!!(plan&&plan.querySelector('.plan'))};}""")
    if not b0: bad.append('no Before you start section')
    else:
        if not b0['details'] or not b0['open']: bad.append('Before you start is not an open <details> (Block 0, open by default)')
        if 'Block 0' not in b0['title'] or 'Before you start' not in b0['title']: bad.append('Before you start is not titled "Block 0 · Before you start"')
        if b0['inPlan'] is False: bad.append('Before you start is not inside the plan section')
        if b0['hasPlanBox'] and not b0['first']: bad.append('Before you start is not the first block of the plan')
    pg.eval_on_selector_all('details', 'els=>els.forEach(d=>d.open=true)')  # words inside closed self-checks count too
    data = json.loads(pg.inner_text('#terms-data') or '{}') if pg.query_selector('#terms-data') else {}
    if not data: bad.append('no terms data on the page')
    keys = pg.eval_on_selector_all('.term', 'els=>els.map(e=>e.dataset.t)')
    missing = sorted(set(data) - set(keys))
    if missing: bad.append('terms never underlined: ' + ', '.join(missing))
    twice = sorted(k for k, n in Counter(keys).items() if n > 1)
    if twice: bad.append('underlined more than once (first use only): ' + ', '.join(twice))
    unknown = sorted(set(keys) - set(data))
    if unknown: bad.append('underlined but no definition: ' + ', '.join(unknown))
    inside = pg.eval_on_selector_all('.term', "els=>els.filter(e=>e.closest('button,a,h1,h2,h3,nav,summary')).map(e=>e.textContent)")
    if inside: bad.append('term inside a button, link, heading, nav or summary: ' + ', '.join(inside))
    flex = pg.eval_on_selector_all('.term', "els=>els.filter(e=>/flex|grid/.test(getComputedStyle(e.parentElement).display)).map(e=>e.textContent)")
    if flex: bad.append('term is a direct child of a flex/grid box (breaks layout): ' + ', '.join(flex))
    seen, hidden = set(), []
    for k in dict.fromkeys(keys):
        els = [e for e in pg.query_selector_all(f'.term[data-t="{k}"]') if e.is_visible()]
        if not els: hidden.append(k); continue
        seen.add(k); el = els[0]
        el.scroll_into_view_if_needed(); el.click(timeout=5000)
        on = pg.eval_on_selector('#termbox', 'e=>e.classList.contains("on")')
        txt = pg.inner_text('#termbox .tb-d')
        if not on or not txt.strip(): bad.append(f'tap on "{k}" did not show a definition')
        if len(seen) == 1:
            bb = pg.query_selector('#termbox .tb-h button').bounding_box()
            if not bb or bb['width'] < 44 or bb['height'] < 44: bad.append(f'termbox Close button smaller than 44 x 44 px: {bb}')
        pg.click('#termbox button')
    if hidden: print('note: only in hidden text (quiz answers), not tapped:', ', '.join(hidden))
    if shot:
        el = pg.query_selector('.term'); el.scroll_into_view_if_needed(); el.click(); pg.screenshot(path=shot)
    if errs: bad.append('JS errors: ' + '; '.join(errs))
    print(f'{len(data)} terms, {len(keys)} underlined, {len(seen)} tapped')
for x in bad: print(' -', x)
print('FAIL' if bad else 'OK')
