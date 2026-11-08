# Builds index.html: the landing page with every planned day.
# PLAN and LINKS are generated from tools/plan_data.py (the same data fills the study sheet).
import sys, json, html; sys.path.insert(0,sys.argv[1]); from common import *; from quizjs import STORAGE_JS
out=sys.argv[2]
PLAN=json.load(open(sys.argv[1]+'/plan.json'))
# LINKS: day -> list of pages; generated with tools/plan.json from tools/plan_data.py (review=True shows 'Review:')
LINKS=json.load(open(sys.argv[1]+'/links.json'))
body=f'''
<div id="today"></div>
<div class="tools">
  <a class="tl" href="progress.html"><b>Progress</b><span>Every syllabus topic, coloured by how far you have got</span></a>
  <a class="tl" href="flashcards.html"><b>Flashcards</b><span>Learn-by-heart cards, 5 to 10 minutes a day</span><span id="fdue" class="fchip" style="display:none"></span></a>
  <a class="tl" href="exam.html"><b>Exam technique</b><span>Pick a subject: papers, habits that win marks, command terms</span></a>
  <a class="tl" href="german.html"><b>German</b><span>15 minutes a day now; your route to a German-taught degree</span></a>
  <a class="tl" href="{SHEET}"><b>Study sheet</b><span>Daily plan, files and the Error log</span></a>
</div>
<div id="plan"></div>
<style>
.tools{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin:18px 0 6px}}
.tl{{display:block;background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);padding:10px 12px;text-decoration:none;color:var(--ink)}}
.tl b{{display:block;color:var(--indigo)}} .tl span{{font-size:.88rem;color:var(--ink-soft)}}
.wk{{margin-top:26px}} .wk h2{{margin:0 0 8px;font-size:1.25rem}}
.day{{display:grid;grid-template-columns:96px 210px minmax(0,1fr);gap:4px 16px;align-items:baseline;background:var(--card);border:1px solid var(--rule);padding:10px 14px;margin:6px 0}}
.day .d{{font-weight:700;white-space:nowrap}} .day .s{{color:var(--indigo);font-weight:700}} .day .k{{font-size:.92rem;color:var(--ink-soft)}}
.day .g{{grid-column:1 / -1;font-size:.95rem}}
.day .k{{display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}
.day .k.open{{display:block;-webkit-line-clamp:unset;overflow:visible}}
.day .k.clamp{{cursor:pointer}}
.day .g a.op{{display:flex;align-items:center;flex-wrap:wrap;gap:2px 8px;min-height:44px;padding:4px 0;font-weight:600}}
.day .g a.op .pill{{margin-left:0}}
.day .dn{{margin-left:8px}}
details.wk{{background:transparent;border:0;padding:0}} details.wk > summary{{display:flex;align-items:center;min-height:44px;cursor:pointer;font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-size:1.25rem;font-weight:600}}
details.wk > summary .wkn{{font:600 .9rem/1.3 "Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;color:var(--ink-soft);margin-left:10px}}
@media (max-width:700px){{.day{{grid-template-columns:96px minmax(0,1fr)}} .day .k{{grid-column:1 / -1}}}}
.day.today{{border:2px solid var(--amber);background:var(--amber-soft)}}
.pill{{display:inline-block;font-size:.8rem;font-weight:700;padding:1px 7px;border:1px solid currentColor;border-radius:4px;margin-left:6px;vertical-align:1px}}
.p-done{{background:var(--green-soft);color:var(--green-ink)}} .p-soon{{background:var(--card);color:var(--grey)}}
.hero{{background:var(--card);border:1px solid var(--rule);border-left:6px solid var(--amber);padding:14px 16px;margin-top:22px}}
.hero h2{{margin:0 0 6px;font-size:1.3rem}} :root{{--amber-ink:#8A6416;--grey:#5F6B72}}
:focus-visible{{outline:3px solid var(--indigo);outline-offset:2px}}
.fchip{{display:table!important;margin-top:6px;font-size:.85rem!important;font-weight:700;padding:2px 10px;border-radius:4px;background:var(--indigo);color:#fff!important}}
.hero .fl{{margin-top:10px;font-size:.95rem}} .hero .fl a{{font-weight:700}}
.hero .exam{{margin-top:10px;background:var(--amber-soft);border-left:4px solid var(--amber);padding:8px 12px;font-size:.95rem}}
.hero .go{{display:inline-flex;align-items:center;min-height:44px;margin-top:8px;background:var(--indigo);color:#fff;padding:8px 14px;border-radius:6px;text-decoration:none;font-weight:700}}
</style>
'''
script=STORAGE_JS+'''
storageNotice();
var PLAN=__P__, LINKS=__L__;
function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML;}
function quiz(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
var now=new Date(), today=now.getFullYear()+'-'+String(now.getMonth()+1).padStart(2,'0')+'-'+String(now.getDate()).padStart(2,'0');
function lst(iso){var l=LINKS[iso]; return !l?[]:(Array.isArray(l)?l:[l]);}
function scored(l){var q=quiz(l.quiz); return !!(q&&(q.total||q.max));}
function one(l){var q=quiz(l.quiz); var badge=''; if(q&&q.total) badge='<span class="pill p-done">quiz '+(q.best||q.right)+'/'+q.total+'</span>'; else if(q&&q.max) badge='<span class="pill p-done">score '+q.score+'/'+q.max+'</span>'; return '<a class="op" href="'+l.url+'"><span>'+(l.review?'Review: ':'Open: ')+esc(l.label)+'</span>'+badge+'</a>';}
function guideHtml(p){var ls=lst(p.iso); if(!ls.length) return /rest/i.test(p.subject)?'<span class="pill p-soon" style="margin-left:0">rest day</span>':'<span class="pill p-soon" style="margin-left:0">guide coming</span>'; return ls.map(one).join('');}
// today card: today's row, or the next planned day
var cur=PLAN.filter(function(p){return p.iso>=today;})[0];
var t=document.getElementById('today');
if(cur){var isToday=cur.iso===today;
  t.innerHTML='<div class="hero"><div style="font-size:.85rem;font-weight:700;color:var(--amber-ink)">'+(isToday?'TODAY':'NEXT UP')+'</div><h2>'+esc(cur.day)+' '+esc(cur.date)+': '+esc(cur.subject)+'</h2><div>'+esc(cur.task)+'</div>'+
  (lst(cur.iso).length?lst(cur.iso).map(function(l){return '<a class="go" style="margin-right:8px" href="'+l.url+'">'+(l.review?'Review: '+esc(l.label):(isToday?'Open today\\'s guide':'Open the guide'))+'</a>';}).join(''):'<div style="margin-top:8px"><span class="pill p-soon" style="margin-left:0">guide coming</span> Use the files linked on this day in the <a href="__SHEET__">study sheet</a>.</div>')+'</div>';}
// flashcards due today: counted from the saved card schedule (ib-flash-v2), else the last count the flashcards page wrote
function flashDue(){var s=quiz('ib-flash-v2'); if(s&&s.c){var n=0; Object.keys(s.c).forEach(function(k){var c=s.c[k]; if(c&&c.due&&c.due<=today) n++;}); return n;}
  var v=null; try{v=localStorage.getItem('ib-flash-due-count');}catch(e){} return v===null?null:(parseInt(v,10)||0);}
var fd=flashDue();
var flashLine='<div class="fl">'+(fd===null?'<a href="flashcards.html">Flashcards: start today\\'s new cards</a>':'<a href="flashcards.html">Flashcards due today: '+fd+'</a>')+'</div>';
var fe=document.getElementById('fdue'); if(fe&&fd!==null){fe.textContent='Due today: '+fd; fe.style.display='';}
var examNote=(today>='2026-11-23'&&today<='2026-12-04')?'<div class="exam"><b>Exam fortnight:</b> sleep 8 to 9 hours, nothing new the night before a paper, revise from the Error log.</div>':'';
var hero=t.querySelector('.hero'); if(hero) hero.insertAdjacentHTML('beforeend',flashLine+examNote);
if(!cur){t.innerHTML='<div class="hero"><h2>The plan has finished</h2><div>All planned days are done. Check the progress page for what to revise.</div></div>';}
// all days grouped by week; finished weeks are folded away
var weeks=[], byWk={};
PLAN.forEach(function(p){ if(!byWk[p.week]){ byWk[p.week]=[]; weeks.push(p.week); } byWk[p.week].push(p); });
var out='';
weeks.forEach(function(w){ var ds=byWk[w], past=ds.every(function(p){return p.iso<today;});
  var rows=ds.map(function(p){ var cls='day'+(p.iso===today?' today':(p.iso<today?' past':''));
    var done=lst(p.iso).some(scored)?'<span class="pill p-done dn">✓ Done</span>':'';
    return '<div class="'+cls+'" id="d'+p.iso+'"><span class="d">'+esc(p.day)+' '+esc(p.date)+done+'</span><span class="s">'+esc(p.subject)+'</span><span class="k">'+esc(p.task)+'</span><span class="g">'+guideHtml(p)+'</span></div>';}).join('');
  if(past){ var nd=ds.filter(function(p){return lst(p.iso).some(scored);}).length;
    out+='<details class="wk"><summary>'+esc(w)+'<span class="wkn">finished, '+nd+' of '+ds.length+' days with a score</span></summary>'+rows+'</details>'; }
  else out+='<div class="wk"><h2>'+esc(w)+'</h2>'+rows+'</div>'; });
document.getElementById('plan').innerHTML=out;
// long tasks: two lines, tap to show all
[].forEach.call(document.querySelectorAll('.day .k'),function(k){ if(k.scrollHeight<=k.clientHeight+2) return;
  k.classList.add('clamp'); k.setAttribute('role','button'); k.setAttribute('tabindex','0'); k.setAttribute('aria-expanded','false'); k.title='Tap to show the whole task';
  function tog(){ var o=k.classList.toggle('open'); k.setAttribute('aria-expanded',o?'true':'false'); }
  k.addEventListener('click',tog); k.addEventListener('keydown',function(e){ if(e.key==='Enter'||e.key===' '){ e.preventDefault(); tog(); } }); });
// a link like index.html#d2026-11-03 opens the plan at that day
if(/^#d\\d/.test(location.hash)){var el=document.getElementById(location.hash.slice(1)); if(el){var dt=el.closest('details'); if(dt) dt.open=true; el.style.outline='3px solid var(--indigo)'; el.scrollIntoView({block:'center'});}}
'''.replace('__P__',json.dumps(PLAN,ensure_ascii=False)).replace('__L__',json.dumps(LINKS)).replace('__SHEET__',SHEET)
open(out+'/index.html','w').write(page("Jamila IB study plan","index.html","Jamila's IB study plan","Every planned day from Monday 9 November to Friday 4 December 2026. Today's day is highlighted; each day links to its study guide once it is ready.",body,script).replace('<div class="crumb"><a href="index.html">All study pages</a></div>',''))
print("landing ok", len(PLAN), "days")
