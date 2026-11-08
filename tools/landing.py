# Builds index.html: the landing page with every planned day.
# PLAN and LINKS are generated from tools/plan_data.py (the same data fills the study sheet).
import sys, json, html; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
PLAN=json.load(open(sys.argv[1]+'/plan.json'))
# LINKS: day -> list of pages; generated with tools/plan.json from tools/plan_data.py (review=True shows 'Review:')
LINKS=json.load(open(sys.argv[1]+'/links.json'))
body=f'''
<div id="today"></div>
<div class="tools">
  <a class="tl" href="progress.html"><b>Progress</b><span>Every syllabus topic, coloured by how far you have got</span></a>
  <a class="tl" href="flashcards.html"><b>Flashcards</b><span>Learn-by-heart cards, 5 to 10 minutes a day</span></a>
  <a class="tl" href="exam.html"><b>Exam technique</b><span>Pick a subject: papers, habits that win marks, command terms</span></a>
  <a class="tl" href="{SHEET}"><b>Study sheet</b><span>Daily plan, files and the Error log</span></a>
</div>
<div id="plan"></div>
<style>
.tools{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:10px;margin:18px 0 6px}}
.tl{{display:block;background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);padding:10px 12px;text-decoration:none;color:var(--ink)}}
.tl b{{display:block;color:var(--indigo)}} .tl span{{font-size:.88rem;color:var(--ink-soft)}}
.wk{{margin-top:26px}} .wk h2{{margin:0 0 8px;font-size:1.25rem}}
.day{{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;background:var(--card);border:1px solid var(--rule);padding:10px 14px;margin:6px 0}}
.day .d{{min-width:92px;font-weight:700}} .day .s{{min-width:150px;color:var(--indigo);font-weight:700}} .day .k{{flex:1 1 260px;font-size:.92rem;color:var(--ink-soft)}}
.day .g{{flex-basis:100%;font-size:.95rem}}
.day.today{{border:2px solid var(--amber);background:var(--amber-soft)}} .day.past{{opacity:.7}}
.pill{{display:inline-block;font-size:.78rem;font-weight:700;padding:1px 8px;border-radius:999px;margin-left:6px;vertical-align:1px}}
.p-done{{background:var(--green-soft);color:var(--green)}} .p-soon{{background:#EDF0EC;color:var(--grey)}}
.hero{{background:var(--card);border:1px solid var(--rule);border-left:6px solid var(--amber);padding:14px 16px;margin-top:22px}}
.hero h2{{margin:0 0 6px;font-size:1.3rem}} .hero .go{{display:inline-block;margin-top:8px;background:var(--indigo);color:#fff;padding:8px 14px;border-radius:6px;text-decoration:none;font-weight:700}}
</style>
'''
script='''
var PLAN=__P__, LINKS=__L__;
function esc(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML;}
function quiz(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
var now=new Date(), today=now.getFullYear()+'-'+String(now.getMonth()+1).padStart(2,'0')+'-'+String(now.getDate()).padStart(2,'0');
function lst(iso){var l=LINKS[iso]; return !l?[]:(Array.isArray(l)?l:[l]);}
function one(l){var q=quiz(l.quiz); var badge=''; if(q&&q.total) badge='<span class="pill p-done">quiz '+(q.best||q.right)+'/'+q.total+'</span>'; else if(q&&q.max) badge='<span class="pill p-done">score '+q.score+'/'+q.max+'</span>'; return '<a href="'+l.url+'">'+(l.review?'Review: ':'Open: ')+esc(l.label)+'</a>'+badge;}
function guideHtml(p){var ls=lst(p.iso); if(!ls.length) return '<span class="pill p-soon">guide coming</span>'; return ls.map(one).join('<br>');}
// today card: today's row, or the next planned day
var cur=PLAN.filter(function(p){return p.iso>=today;})[0];
var t=document.getElementById('today');
if(cur){var isToday=cur.iso===today;
  t.innerHTML='<div class="hero"><div style="font-size:.85rem;font-weight:700;color:var(--amber)">'+(isToday?'TODAY':'NEXT UP')+'</div><h2>'+esc(cur.day)+' '+esc(cur.date)+': '+esc(cur.subject)+'</h2><div>'+esc(cur.task)+'</div>'+
  (lst(cur.iso).length?lst(cur.iso).map(function(l){return '<a class="go" style="margin-right:8px" href="'+l.url+'">'+(l.review?'Review: '+esc(l.label):(isToday?'Open today\\'s guide':'Open the guide'))+'</a>';}).join(''):'<div style="margin-top:8px"><span class="pill p-soon" style="margin-left:0">guide coming</span> Use the files linked on this day in the <a href="__SHEET__">study sheet</a>.</div>')+'</div>';}
else{t.innerHTML='<div class="hero"><h2>The plan has finished</h2><div>All planned days are done. Check the progress page for what to revise.</div></div>';}
// all days grouped by week
var out='', wk=null;
PLAN.forEach(function(p){ if(p.week!==wk){ if(wk!==null) out+='</div>'; wk=p.week; out+='<div class="wk"><h2>'+esc(wk)+'</h2>'; }
  var cls='day'+(p.iso===today?' today':(p.iso<today?' past':''));
  out+='<div class="'+cls+'" id="d'+p.iso+'"><span class="d">'+esc(p.day)+' '+esc(p.date)+'</span><span class="s">'+esc(p.subject)+'</span><span class="k">'+esc(p.task)+'</span><span class="g">'+guideHtml(p)+'</span></div>';});
document.getElementById('plan').innerHTML=out+'</div>';
// a link like index.html#d2026-11-03 opens the plan at that day
if(location.hash){var el=document.getElementById(location.hash.slice(1)); if(el){el.style.outline='3px solid var(--indigo)'; el.scrollIntoView({block:'center'});}}
'''.replace('__P__',json.dumps(PLAN,ensure_ascii=False)).replace('__L__',json.dumps(LINKS)).replace('__SHEET__',SHEET)
open(out+'/index.html','w').write(page("Jamila IB study plan","index.html","Jamila's IB study plan","Every planned day from Monday 9 November to Friday 4 December 2026. Today's day is highlighted; each day links to its study guide once it is ready.",body,script).replace('<div class="crumb"><a href="index.html">All study pages</a></div>',''))
print("landing ok", len(PLAN), "days")
