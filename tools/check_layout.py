"""Overflow check at 380 to 1200 px: python3 tools/check_layout.py <absolute path to page.html>
Prints, per width: width [page scrollWidth, [elements sticking out of their box]] [JS errors].
Clean output is `width [width, []] []` for every width.
Elements inside a deliberate sideways-scroll container (overflow-x auto or scroll, for example the
section menu, the top bar or .tablewrap) are not counted: that row scrolls on purpose. A page that is
wider than the screen is always reported (scrollWidth > width)."""
import sys
from playwright.sync_api import sync_playwright
url = "file://" + sys.argv[1]
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (380, 390, 600, 1000, 1200):
        pg = b.new_page(viewport={"width": w, "height": 900}); errs = []
        pg.on("pageerror", lambda e: errs.append(str(e))); pg.goto(url)
        bad = pg.evaluate("""()=>{const out=[];
          const scroller=el=>{for(let a=el.parentElement;a&&a!==document.body;a=a.parentElement){const o=getComputedStyle(a).overflowX; if(o==='auto'||o==='scroll') return true;} return false;};
          document.querySelectorAll('body *').forEach(el=>{
          const r=el.getBoundingClientRect(); if(!r.width) return; let par=el.parentElement; if(!par) return;
          while(par && getComputedStyle(par).display.startsWith('inline')) par=par.parentElement;
          if(el.closest('svg') && el.tagName.toLowerCase()!=='svg') return;
          if(el.closest('.tablewrap') || scroller(el)) return;
          const pr=par.getBoundingClientRect(); const cs=getComputedStyle(par);
          const right=pr.right-parseFloat(cs.paddingRight)+1, left=pr.left+parseFloat(cs.paddingLeft)-1;
          if(r.right>right+0.5 || r.left<left-0.5) out.push(el.tagName+'.'+el.className+' '+Math.round(r.right-right)+'px '+(el.textContent||'').trim().slice(0,30));});
          const sw=document.documentElement.scrollWidth;
          if(sw>window.innerWidth) out.unshift('PAGE WIDER THAN SCREEN by '+(sw-window.innerWidth)+'px');
          return [sw, out.slice(0,8)];}""")
        print(w, bad, errs)
    b.close()
