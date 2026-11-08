# shared head/CSS for the study-site extra pages (each output file stays self-contained)
CSS = r'''
  :root{--paper:#F5F7F4;--ink:#1E2A33;--ink-soft:#4A5862;--rule:#D6DCD8;--indigo:#2F47A6;--indigo-soft:#E6EAF7;--amber:#B8761A;--amber-soft:#FBF1DF;--green:#2E7D4F;--green-soft:#E3F2E8;--red:#B23A3A;--red-soft:#F8E4E4;--grey:#5F6B72;--amber-ink:#8A6416;--card:#FFFFFF}
  *{box-sizing:border-box}
  body{margin:0;background:var(--paper);color:var(--ink);font:17px/1.6 "Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;overflow-wrap:break-word}
  h1,h2,h3{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;line-height:1.2;margin:0 0 .4em;font-weight:600}
  h1{font-size:2.1rem} h2{font-size:1.5rem;margin-top:1.6em} h3{font-size:1.15rem;margin-top:1.4em}
  p{margin:0 0 1em} a{color:var(--indigo)}
  sup,sub{line-height:0}
  .wrap{max-width:820px;margin:0 auto;padding:0 20px 80px}
  .top{background:#0B0F1A;color:#fff;padding:26px 0 22px}
  .top h1{color:#fff} .top p{color:#C9D1E6;max-width:660px;margin-bottom:0}
  .top .crumb{font-size:.9rem;margin-bottom:8px} .top .crumb a{color:#F2C46D}
  table{border-collapse:collapse;width:100%;margin:12px 0 20px;font-size:.95rem;background:var(--card)}
  th,td{border:1px solid var(--rule);padding:8px 10px;text-align:left;vertical-align:top}
  th{background:#EDF0EC}
  .tablewrap{overflow-x:auto;-webkit-overflow-scrolling:touch}
  .card{background:var(--card);border:1px solid var(--rule);padding:14px 16px;margin:12px 0}
  .tip{background:var(--amber-soft);border-left:5px solid var(--amber);padding:12px 16px;margin:18px 0}
  .tip b:first-child{color:var(--amber-ink)}
  .step{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);padding:12px 16px;margin:12px 0}
  .step .bh{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 12px;margin-bottom:4px}
  .step .bh b{font-size:1.15rem;font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif}
  .step .bh span{font-weight:700;color:var(--indigo)}
  .step ol{margin:6px 0 0;padding-left:22px} .step li{margin:4px 0}
  .t{color:var(--ink-soft);font-size:.88rem;white-space:nowrap}
  .tag{display:inline-block;font-size:.72rem;font-weight:700;padding:1px 7px;border-radius:4px;color:#fff;vertical-align:middle;white-space:nowrap}
  .quiz .q{background:var(--card);border:1px solid var(--rule);padding:14px 16px;margin:12px 0}
  .quiz .q > p{font-weight:600;margin-bottom:8px}
  .quiz .subj{display:inline-block;font-size:.75rem;font-weight:700;color:var(--indigo);background:var(--indigo-soft);padding:1px 7px;border-radius:4px;margin-right:6px;vertical-align:middle}
  .quiz button{display:block;width:100%;text-align:left;background:#F3F5F2;border:1px solid var(--rule);padding:8px 12px;margin:6px 0;border-radius:6px;font:inherit;cursor:pointer;color:var(--ink)}
  .quiz button:focus-visible{border-color:var(--indigo)}
  @media (hover:hover){.quiz button:hover{border-color:var(--indigo)}}
  .quiz button.right{background:var(--green-soft);border-color:var(--green)}
  .quiz button.wrong{background:var(--red-soft);border-color:var(--red)}
  .quiz .why{display:none;margin-top:8px;font-size:.95rem;color:var(--ink-soft)}
  .quiz .q.done .why{display:block}
  .score{font-weight:700;margin-top:14px}
  .frac{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:.92em;line-height:1.15;margin:0 2px}
  .frac>span:first-child{border-bottom:1px solid currentColor;padding:0 3px}
  .frac>span:last-child{padding:0 3px}
  .nw{white-space:nowrap}
  @media (max-width:600px){h1{font-size:1.7rem}body{font-size:16px}th,td{padding:6px}}
'''
def page(title, crumb, h1, intro, body, script="", crumb_label="All study pages"):
    depth = '../' if crumb.startswith('../') else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{CSS}</style>
{site_head()}
</head>
<body>
{site_bar(depth)}
<header class="top"><div class="wrap" style="padding-bottom:0">
  <div class="crumb"><a href="{crumb}">{crumb_label}</a></div>
  <h1>{h1}</h1>
  <p>{intro}</p>
</div></header>
<main class="wrap">
{body}
</main>
{('<script>'+script+'</script>') if script else ''}
{site_tail()}
</body>
</html>
'''
DRIVE=lambda i:f'https://drive.google.com/file/d/{i}/view'
SHEET='https://docs.google.com/spreadsheets/d/1svykHaPDhtPFnzkO6tdNk8GPLWyd8tOh6IAV-9gwkJQ/edit'


# ---------------------------------------------------------------- shared site layer (UX review 8 Nov 2026)
# Used by page() above and by tools/enhance.py (hand-written guides). Everything sits between
# <!--enhance:start--> and <!--enhance:end--> so enhance.py can remove it and add it fresh.
# The CSS comes after the page's own CSS so it wins.
SITE_START, SITE_END = '<!--enhance:start-->', '<!--enhance:end-->'
SANS = '"Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif'
SITE_CSS = r"""
:root{--amber-ink:#8A6416;--grey:#5F6B72;--purple:#6A3D9A;--green-ink:#256B43;--r-sm:4px;--r:8px}
/* top bar: back to today, flashcards, progress, sheet */
.sitebar{position:sticky;top:0;z-index:30;height:44px;background:var(--paper);box-shadow:0 1px 0 var(--rule)}
.sitebar .sb{max-width:820px;height:44px;margin:0 auto;padding:0 10px;display:flex;align-items:stretch;gap:2px;overflow-x:auto;scrollbar-width:none;white-space:nowrap}
.sitebar .sb::-webkit-scrollbar{display:none}
.sitebar a{flex:none;display:flex;align-items:center;min-height:44px;padding:0 10px;color:var(--indigo);text-decoration:none;font:600 .95rem/1 __SANS__;border-radius:var(--r-sm)}
.sitebar a.sb-home{font-weight:700}
@media (hover:hover){.sitebar a:hover{background:var(--indigo-soft)}}
/* guide section menu: one row that scrolls sideways, 44 px targets, current section marked */
nav.toc{top:44px;z-index:29}
nav.toc .wrap{display:flex;flex-wrap:nowrap;gap:2px;overflow-x:auto;-webkit-overflow-scrolling:touch;scrollbar-width:none;white-space:nowrap;padding:0 10px}
nav.toc .wrap::-webkit-scrollbar{display:none}
nav.toc a{flex:none;display:flex;align-items:center;min-height:44px;padding:12px 10px;line-height:1.2;border-radius:0}
nav.toc a[href$="index.html"]{display:none}
nav.toc a[aria-current]{color:var(--indigo);font-weight:700;background:var(--indigo-soft);box-shadow:inset 0 -3px 0 var(--indigo)}
[id]{scroll-margin-top:56px}
html:has(nav.toc) [id]{scroll-margin-top:100px}
/* focus: always visible */
:focus-visible{outline:3px solid var(--indigo)!important;outline-offset:2px!important}
header.hero :focus-visible,header.top :focus-visible{outline-color:#F2C46D!important}
/* readable text */
main p,main li,.why{max-width:68ch}
@media (max-width:600px){.wrap{padding-left:16px;padding-right:16px}}
small{font-size:max(12px,.8em)}
.sig small{font-size:max(12px,.62em)}
/* hero: title first, then the picture (at most 30% of the screen height, as wide as the text column),
   so the title and the Today card share the first screen; long intro paragraphs fold to 3 lines (tap to read) */
header.hero{display:flex;flex-direction:column}
header.hero > .wrap{order:-1;width:100%}
header.hero > svg,header.hero > img{max-height:30vh;max-width:780px;margin:14px auto 0}
header.hero p.fold{position:relative;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden;cursor:pointer}
header.hero p.fold::after{content:"more";position:absolute;right:0;bottom:0;padding:0 2px 0 28px;background:linear-gradient(90deg,rgba(11,15,26,0),#0B0F1A 22px);color:#F2C46D;font-weight:700}
header.hero .wrap > p ~ p.fold{-webkit-line-clamp:2}
header.hero p.fold.open{display:block;-webkit-line-clamp:unset}
header.hero p.fold.open::after{content:none}
@media (max-width:600px){header.hero > svg,header.hero > img{max-height:28vh} header.hero .meta{font-size:.85rem;gap:0 14px}}
/* contrast: amber and grey text */
body .tip b:first-child,body .src > b:first-child,body .star,body .col.l > h3,body .timer.low .tdisp{color:var(--amber-ink)}
/* one badge system: Learn = solid amber; Given / in booklet = neutral outline; Apply = indigo outline; HL = purple outline; green = done */
.badge,.fb,.learn,.tag,span.hl,.quiz .subj,.written .wsubj,.wsubj,.pill,.soon{display:inline-block;font:700 .8rem/1.4 __SANS__;letter-spacing:.01em;padding:1px 7px;border:1px solid currentColor;border-radius:var(--r-sm);background:var(--card);vertical-align:middle;white-space:nowrap}
.learn,.badge.learn{background:var(--amber-ink);border-color:var(--amber-ink);color:#fff}
.fb,.badge.apply{color:var(--indigo);border-color:var(--indigo)}
.fb.given,.badge.given,.tag,.quiz .subj,.written .wsubj,.wsubj,.badge.subj{color:var(--ink);border-color:var(--grey)}
span.hl,.badge.hl{color:var(--purple);border-color:var(--purple)}
.pill{margin-left:6px}
.p-done,.badge.done{color:var(--green-ink);border-color:var(--green);background:var(--green-soft)}
.p-soon,.soon{color:var(--grey);border-color:var(--grey)}
/* radii: 4 px small things, 8 px boxes */
.today,.goals,.able,.todaycard,#termbox,.before .bgi,.before .stuck,.quiz button,.go,.notice,.btn,.timer button,.tl,.chip,.plan > div,.step,.block{border-radius:var(--r)}
/* 44 px targets */
.go{min-height:44px;display:inline-flex;align-items:center}
main details>summary{min-height:44px;display:flex;align-items:center;cursor:pointer}
ul.files a,.files li>a{display:inline-flex;align-items:center;min-height:44px}
input[type=number],input[type=text],select{min-height:44px}
#box a#src,a.src{display:inline-flex;align-items:center;min-height:44px}
#termbox .tb-h button{min-height:44px;min-width:44px}
.top .crumb{display:flex;flex-wrap:nowrap;align-items:center;gap:0 6px;overflow-x:auto;scrollbar-width:none;white-space:nowrap;margin-bottom:2px}
.top .crumb::-webkit-scrollbar{display:none}
.top .crumb a{flex:none;display:inline-flex;align-items:center;min-height:44px;padding-right:4px}
/* timed blocks: one card for guide plans, review steps and mock plans */
.plan > div,.block,.step{background:var(--card);border:1px solid var(--rule);padding:12px 16px}
.plan > div.brk{background:var(--green-soft);border-color:var(--green)}
.bh{display:flex;flex-wrap:wrap;align-items:center;gap:4px 10px;margin-bottom:4px}
.block > .bh{display:grid;grid-template-columns:32px minmax(0,1fr) auto;gap:4px 10px;align-items:center}
.plan .bh .bn,.step .bh .bn,.bh .bn{flex:none;display:inline-flex;align-items:center;justify-content:center;width:32px;height:32px;border-radius:50%;background:var(--indigo);color:#fff;font:700 1rem/1 __SANS__}
.plan .bh > b,.step .bh > b,.bh > b{font-size:1.15rem;line-height:1.25;font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;color:var(--ink)}
.plan .bh .bt,.step .bh .bt,.bh .bt{flex:none;display:inline-block;font:700 .8rem/1.4 __SANS__;color:var(--ink);background:var(--paper);border:1px solid var(--rule);border-radius:var(--r-sm);padding:2px 8px}
.bdone{display:flex;align-items:center;gap:10px;min-height:44px;margin:8px 0 0;padding-top:4px;border-top:1px solid var(--rule);font-weight:600;color:var(--ink-soft);cursor:pointer;max-width:none}
.bdone input{width:20px;height:20px;margin:0;flex:none;accent-color:var(--green)}
.block.is-done{border-color:var(--green)} .block.is-done .bn{background:var(--green)} .block.is-done .bdone{color:var(--green-ink)}
.blocks{display:grid;gap:10px;margin:16px 0}
.blocks > .block p{margin:4px 0 0}
.brkc{background:var(--green-soft);border:1px solid var(--green);border-radius:var(--r);padding:8px 16px}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* Today card on guides: goals, plan chips, warm-up */
.todaycard{background:var(--card);border:2px solid var(--indigo);padding:14px 16px 6px;margin:20px 0 10px}
.todaycard .tc-goals > *{background:transparent!important;border:0!important;padding:0!important;margin:0!important;box-shadow:none!important;border-radius:0!important}
.todaycard .tc-goals h2,.todaycard .tc-goals h3,.todaycard .tc-goals > * > p:first-child,.todaycard .tc-goals > * > b:first-child{display:block;font:600 1.25rem/1.25 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;color:var(--ink);margin:0 0 6px}
.todaycard .tc-goals ol,.todaycard .tc-goals ul{margin:0;padding-left:22px}
.todaycard .tc-goals li{margin:3px 0}
.todaycard .tc-plan{margin:0 0 12px;padding-bottom:12px;border-bottom:1px solid var(--rule)}
@media (max-width:600px){.todaycard .chips{display:grid;grid-template-columns:1fr 1fr;gap:6px}.todaycard .chip{padding:4px 10px;font-size:.9rem}.todaycard .chip.c0{grid-column:1 / -1}}
.todaycard .tc-h{font-weight:700;margin:0 0 6px}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{display:inline-flex;align-items:center;gap:4px;min-height:44px;padding:4px 12px;border:1px solid var(--indigo);background:var(--card);color:var(--indigo);text-decoration:none;font-size:.95rem;line-height:1.2}
.chip b{font-weight:700}
.chip.done{border-color:var(--green);color:var(--green-ink);background:var(--green-soft)}
.chip.done::before{content:"\2713";font-weight:700}
.todaycard .warmup{border:0;border-top:1px solid var(--rule);border-radius:0;padding:12px 0 4px;margin:12px 0 0;background:transparent}
.todaycard .tc-plan + .warmup{border-top:0;margin-top:0;padding-top:0}
.todaycard .warmup h2{font-size:1.15rem}
.sitebar + .notice{margin:8px max(16px,calc((100% - 780px) / 2))}
@media print{.sitebar,.notice,#termbox,.go,.chips,.bdone{display:none!important}nav.toc{position:static}.quiz button{display:list-item}.todaycard{border-width:1px}}
""".replace('__SANS__', SANS)

# runs once per page: highlights the current section in the menu, numbers the timed blocks and keeps
# "Block done" ticks in localStorage '<page>-blocks' (page = file name without .html, prefixed ib-)
SITE_JS = r"""(function(){
  if(window.__ibSite) return; window.__ibSite=1;
  var PAGE='ib-'+((location.pathname.split('/').pop()||'index').replace(/\.html?$/,''));
  var BK=PAGE+'-blocks';
  function get(){ try{ var v=JSON.parse(localStorage.getItem(BK)||'null'); return v&&typeof v==='object'?v:{}; }catch(e){ return {}; } }
  function put(v){ try{ localStorage.setItem(BK,JSON.stringify(v)); }catch(e){} }
  // guide plan blocks "Block 1 · 25 min" + title -> numbered card with a time chip
  [].forEach.call(document.querySelectorAll('.plan > div:not(.brk), .step'),function(d){
    var bh=d.querySelector(':scope > .bh'); if(!bh || bh.querySelector('.bn')) return;
    var b=bh.querySelector('b'); var m=b && /^\s*Block\s+(\d+[a-z]?)\s*[·.:-]\s*(.+?)\s*$/i.exec(b.textContent); if(!m) return;
    var s=bh.querySelector('span'); var title=s?s.innerHTML:'';
    d.classList.add('block'); d.setAttribute('data-n',m[1]);
    bh.innerHTML='<span class="bn" aria-hidden="true">'+m[1]+'</span><b><span class="sr">Block '+m[1]+': </span>'+(title||('Block '+m[1]))+'</b><span class="bt">'+m[2]+'</span>';
    // teaching sections linked from this block get a kicker "Block n · ..."
    [].forEach.call(d.querySelectorAll('a[href^="#"]'),function(a){
      var t=document.getElementById(a.getAttribute('href').slice(1)); if(!t) return;
      var k=t.querySelector(':scope > .kicker'); if(!k || k.getAttribute('data-bk')) return;
      k.setAttribute('data-bk',m[1]); k.insertAdjacentHTML('afterbegin','<span class="bk">Block '+m[1]+' · </span>');
    });
  });
  // long hero intro paragraphs fold to 3 lines; tap to read them all
  [].forEach.call(document.querySelectorAll('header.hero .wrap > p'),function(p){
      if(p.textContent.length<160) return;
      p.classList.add('fold'); if(p.scrollHeight<=p.clientHeight+2){ p.classList.remove('fold'); return; }
      p.setAttribute('role','button'); p.setAttribute('tabindex','0'); p.setAttribute('aria-expanded','false');
      function tog(e){ if(e && e.target && e.target.closest && e.target.closest('a,.term')) return; var o=p.classList.toggle('open'); p.setAttribute('aria-expanded',o?'true':'false'); }
      p.addEventListener('click',tog); p.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); tog(); } });
  });
  // keep the Today card on the first screen: shrink the header picture (not below 18% of the screen height) if needed
  (function(){ var art=document.querySelector('header.hero > svg, header.hero > img'), card=document.querySelector('.todaycard');
    if(!art || !card) return; var vh=window.innerHeight, over=card.getBoundingClientRect().top+window.pageYOffset-(vh-70);
    if(over>0){ var h=art.getBoundingClientRect().height; art.style.maxHeight=Math.max(0.18*vh,h-over)+'px'; } })();
  // "Block done" ticks
  var st=get();
  [].forEach.call(document.querySelectorAll('.block'),function(d,i){
    if(d.querySelector(':scope > .bdone')) return;
    var n=d.getAttribute('data-n')||String(i+1);
    var l=document.createElement('label'); l.className='bdone';
    l.innerHTML='<input type="checkbox"> Block done';
    var c=l.querySelector('input'); c.checked=!!st[n]; d.classList.toggle('is-done',c.checked);
    c.addEventListener('change',function(){ var s=get(); if(c.checked) s[n]=new Date().toISOString().slice(0,10); else delete s[n]; put(s); d.classList.toggle('is-done',c.checked); chips(); });
    d.appendChild(l);
  });
  function chips(){ var s=get(); [].forEach.call(document.querySelectorAll('.chip[data-n]'),function(a){ a.classList.toggle('done',!!s[a.getAttribute('data-n')]); }); }
  chips();
  // current section in the menu
  var nav=document.querySelector('nav.toc .wrap'); if(!nav || !('IntersectionObserver' in window)) return;
  var links={}, secs=[];
  [].forEach.call(nav.querySelectorAll('a[href^="#"]'),function(a){ var el=document.getElementById(a.getAttribute('href').slice(1)); if(el){ links[el.id]=a; secs.push(el); } });
  // the current section is the last one whose top has passed under the two bars; the observer (and a
  // throttled scroll check, for long sections) only decides when to look again
  function mark(){ var best=null; secs.forEach(function(el){ if(el.getBoundingClientRect().top<=120) best=el; });
    Object.keys(links).forEach(function(id){ links[id].removeAttribute('aria-current'); });
    if(best){ var a=links[best.id]; a.setAttribute('aria-current','location');
      var l=a.offsetLeft-nav.offsetLeft, r=l+a.offsetWidth; if(l<nav.scrollLeft+8 || r>nav.scrollLeft+nav.clientWidth-8) nav.scrollLeft=Math.max(0,l-40); } }
  secs.sort(function(a,b){ return (a.compareDocumentPosition(b)&2)?1:-1; });
  var io=new IntersectionObserver(mark,{rootMargin:'-100px 0px -55% 0px'});
  var tick=false; window.addEventListener('scroll',function(){ if(tick) return; tick=true; requestAnimationFrame(function(){ tick=false; mark(); }); },{passive:true});
  secs.forEach(function(el){ io.observe(el); });
})();"""


def block_open(n, title, time, extra_id=None):
    """Opening of a numbered timed block card (close it with </div>). The site layer adds the "Block done" tick."""
    bid = extra_id or f'b{n}'
    return (f'<div class="block" id="{bid}" data-n="{n}"><div class="bh"><span class="bn" aria-hidden="true">{n}</span>'
            f'<b><span class="sr">Block {n}: </span>{title}</b><span class="bt">{time}</span></div>')


def site_bar(depth=''):
    """The sticky top bar. depth: '' for pages in the site root, '../' for guides/, practice/, review/."""
    return (SITE_START + f'<nav class="sitebar" aria-label="Study site"><div class="sb">'
            f'<a class="sb-home" href="{depth}index.html#today">← Today</a>'
            f'<a href="{depth}flashcards.html">Flashcards</a>'
            f'<a href="{depth}progress.html">Progress</a>'
            f'<a href="{SHEET}">Sheet</a></div></nav>' + SITE_END)


def site_head():
    return SITE_START + '<meta name="color-scheme" content="light"><style>' + SITE_CSS + '</style>' + SITE_END


def site_tail():
    return SITE_START + '<script>' + SITE_JS + '</script>' + SITE_END
