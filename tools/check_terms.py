#!/usr/bin/env python3
"""Test the tap-to-explain words on a guide page.
Usage: python3 tools/check_terms.py <absolute path to guide html> [screenshot.png]
Prints problems; the last line is OK or FAIL."""
import sys, os, json
from playwright.sync_api import sync_playwright
path = os.path.abspath(sys.argv[1]); shot = sys.argv[2] if len(sys.argv) > 2 else None
bad = []
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width': 390, 'height': 800})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + path)
    pg.eval_on_selector_all('details', 'els=>els.forEach(d=>d.open=true)')  # words inside closed self-checks count too
    data = json.loads(pg.inner_text('#terms-data') or '{}') if pg.query_selector('#terms-data') else {}
    if not data: bad.append('no terms data on the page')
    if not pg.query_selector('#before'): bad.append('no Before you start section')
    keys = pg.eval_on_selector_all('.term', 'els=>els.map(e=>e.dataset.t)')
    missing = sorted(set(data) - set(keys))
    if missing: bad.append('terms never underlined: ' + ', '.join(missing))
    unknown = sorted(set(keys) - set(data))
    if unknown: bad.append('underlined but no definition: ' + ', '.join(unknown))
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
        pg.click('#termbox button')
    if hidden: print('note: only in hidden text (quiz answers), not tapped:', ', '.join(hidden))
    if shot:
        el = pg.query_selector('.term'); el.scroll_into_view_if_needed(); el.click(); pg.screenshot(path=shot)
    if errs: bad.append('JS errors: ' + '; '.join(errs))
    print(f'{len(data)} terms, {len(keys)} underlined, {len(seen)} tapped')
for x in bad: print(' -', x)
print('FAIL' if bad else 'OK')
