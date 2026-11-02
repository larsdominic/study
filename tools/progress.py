import sys, json; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
MATHS=[("SL 1.1","Numbers in scientific form"),("SL 1.2","Arithmetic sequences and series"),("SL 1.3","Geometric sequences and series"),("SL 1.4","Financial applications"),("SL 1.5","Exponents and introduction to logarithms"),("SL 1.6","Simple deductive proof"),("SL 1.7","Rational exponents, laws of logarithms, exponential equations"),("SL 1.8","Sum to infinity"),("SL 1.9","Binomial theorem"),
("SL 2.1","Straight lines"),("SL 2.2","Functions: domain, range, graph"),("SL 2.3","Graphs of functions"),("SL 2.4","Key features of graphs, intersections"),("SL 2.5","Composite and inverse functions"),("SL 2.6","Quadratic functions"),("SL 2.7","Quadratic equations and inequalities, discriminant"),("SL 2.8","Reciprocal and rational functions"),("SL 2.9","Exponential and logarithmic functions"),("SL 2.10","Solving equations"),("SL 2.11","Transformations of graphs"),
("SL 3.1","3D geometry: distance, midpoint, volume, surface area"),("SL 3.2","Right-angled and non-right-angled trigonometry"),("SL 3.3","Applications of trigonometry"),("SL 3.4","Radians, arcs and sectors"),("SL 3.5","The unit circle"),("SL 3.6","Trigonometric identities"),("SL 3.7","Circular functions"),("SL 3.8","Trigonometric equations"),
("SL 4.1","Sampling"),("SL 4.2","Presenting data"),("SL 4.3","Central tendency and spread"),("SL 4.4","Correlation and regression (y on x)"),("SL 4.5","Probability concepts"),("SL 4.6","Venn and tree diagrams, combined events"),("SL 4.7","Discrete random variables"),("SL 4.8","Binomial distribution"),("SL 4.9","Normal distribution"),("SL 4.10","Regression of x on y"),("SL 4.11","Conditional probability and independence"),("SL 4.12","Standardised normal (z) values"),
("SL 5.1","Limits and the derivative"),("SL 5.2","Increasing and decreasing functions"),("SL 5.3","Differentiating ax<sup>n</sup>"),("SL 5.4","Tangents and normals"),("SL 5.5","Introduction to integration, areas"),("SL 5.6","Derivatives of standard functions, chain, product and quotient rules"),("SL 5.7","Second derivative"),("SL 5.8","Maxima, minima, points of inflexion, optimisation"),("SL 5.9","Kinematics"),("SL 5.10","Indefinite integrals, substitution"),("SL 5.11","Definite integrals and areas")]
CHEM=[("S1.1","Particulate nature of matter"),("S1.2","The nuclear atom"),("S1.3","Electron configurations"),("S1.4","Counting particles by mass: the mole"),("S1.5","Ideal gases"),("S2.1","The ionic model"),("S2.2","The covalent model"),("S2.3","The metallic model"),("S2.4","From models to materials"),("S3.1","The periodic table"),("S3.2","Functional groups: organic compounds"),
("R1.1","Measuring enthalpy changes"),("R1.2","Energy cycles in reactions"),("R1.3","Energy from fuels"),("R1.4","Entropy and spontaneity (HL only)"),("R2.1","How much? The amount of chemical change"),("R2.2","How fast? Rate of chemical change"),("R2.3","How far? Extent of chemical change"),("R3.1","Proton transfer reactions"),("R3.2","Electron transfer reactions"),("R3.3","Electron sharing reactions"),("R3.4","Electron-pair sharing reactions")]
# One entry per study guide. ADD A NEW ENTRY FOR EVERY NEW GUIDE (ican keys -> topic code).
GUIDES=[
 dict(subject="Chemistry HL", title="Tue 3 Nov: S1.1 to S1.3", link="guides/2026-11-03-chemistry-s1.1-s1.3.html", ican="ib-chem-s11-13-ican", quiz="ib-quiz-guide-2026-11-03",
      map={"S1.1":["s111","s112","s113"],"S1.2":["s121","s122","s123"],"S1.3":["s131","s132","s133","s134","s135","s136","s137"]},
      anchors={"S1.1":"#s11","S1.2":"#s12","S1.3":"#s13"}),
 dict(subject="Maths AA SL", title="Wed 4 Nov: 1.2 to 1.6", link="guides/2026-11-04-maths-aa-sl-1.2-1.6.html", ican="ib-maths-aa-sl-12-16-ican", quiz="ib-quiz-guide-2026-11-04",
      map={"SL 1.2":["a1","a2","a3","a4"],"SL 1.3":["g1","g2","g3"],"SL 1.8":["i1","i2"],"SL 1.4":["f1","f2","f3","f4"],"SL 1.6":["p1","p2","p3","p4"]},
      anchors={"SL 1.2":"#s12","SL 1.3":"#s13","SL 1.8":"#s18","SL 1.4":"#s14","SL 1.6":"#s16"}),
]
REVIEWS=[dict(title="Week 1 review (Sun 8 Nov)", link="review/2026-11-08-week-1.html", quiz="ib-quiz-review-2026-11-08")]
SUBJECTS=[dict(name="Maths AA SL",topics=MATHS),dict(name="Chemistry HL",topics=CHEM)]
body='''
<div class="card" style="margin-top:24px">
  <b>What the colours mean</b>
  <div style="display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:8px;font-size:.95rem">
    <span><span class="dot" style="background:var(--green)"></span>Secure: every "I can" box ticked and the guide's quiz at 8/10 or better</span>
    <span><span class="dot" style="background:var(--amber)"></span>In progress: some boxes ticked or the quiz done, not yet secure</span>
    <span><span class="dot" style="background:var(--red)"></span>To do: there is a guide, but nothing ticked and no quiz yet</span>
    <span><span class="dot" style="background:#C3C9CD"></span>Not covered yet: no guide for this topic so far</span>
  </div>
  <p style="margin:10px 0 0;font-size:.9rem;color:var(--ink-soft)">This page reads the ticks and quiz scores saved in this browser, so open the guides and this page on the same device. Nothing is sent anywhere.</p>
</div>
<div id="quizzes"></div>
<div id="subjects"></div>
<style>.dot{display:inline-block;width:12px;height:12px;border-radius:50%;margin-right:6px;vertical-align:-1px}
.trow{display:flex;gap:10px;align-items:flex-start;padding:7px 0;border-bottom:1px solid var(--rule)}
.trow .code{min-width:62px;font-weight:700;white-space:nowrap}.trow .name{flex:1}.trow .ev{font-size:.85rem;color:var(--ink-soft);text-align:right}
@media (max-width:600px){.trow{flex-wrap:wrap}.trow .ev{flex-basis:100%;text-align:left;padding-left:20px}}
.sum{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.9rem;margin:4px 0 10px}</style>
'''
script='''
var SUBJECTS=__S__, GUIDES=__G__, REVIEWS=__R__;
function get(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
var COL={g:'var(--green)',a:'var(--amber)',r:'var(--red)',n:'#C3C9CD'};
var info={};
GUIDES.forEach(function(g){var t=get(g.ican)||{}, q=get(g.quiz);
  Object.keys(g.map).forEach(function(code){var ks=g.map[code], n=ks.filter(function(k){return t[k];}).length;
    var best=q?(q.best||q.right):null, tot=q?q.total:null;
    var st = (n===ks.length && q && best>=0.8*tot) ? 'g' : ((n>0||q)?'a':'r');
    info[g.subject+'|'+code]={st:st,ev:n+'/'+ks.length+' ticked'+(q?(' · quiz best '+best+'/'+tot):' · quiz not done'),link:g.link+(g.anchors[code]||'')};});});
var qd=document.getElementById('quizzes'); var h='<h2>Quiz scores</h2><div class="card">';
GUIDES.concat(REVIEWS).forEach(function(g){var q=get(g.quiz); h+='<div class="trow"><div class="name"><a href="'+g.link+(g.ican?'#quiz':'#quiz')+'">'+(g.subject?g.subject+': ':'')+g.title+'</a></div><div class="ev">'+(q?('best '+(q.best||q.right)+'/'+q.total+', last '+q.right+'/'+q.total+' on '+q.date):'not done yet')+'</div></div>';});
qd.innerHTML=h+'</div>';
var sd=document.getElementById('subjects'), out='';
SUBJECTS.forEach(function(s){var c={g:0,a:0,r:0,n:0}, rows='';
  s.topics.forEach(function(t){var i=info[s.name+'|'+t[0]]||{st:'n',ev:'',link:null}; c[i.st]++;
    rows+='<div class="trow"><span class="dot" style="background:'+COL[i.st]+';margin-top:7px"></span><div class="code">'+t[0]+'</div><div class="name">'+(i.link?'<a href="'+i.link+'">'+t[1]+'</a>':t[1])+'</div><div class="ev">'+i.ev+'</div></div>';});
  out+='<h2>'+s.name+'</h2><div class="sum"><span><span class="dot" style="background:var(--green)"></span>'+c.g+' secure</span><span><span class="dot" style="background:var(--amber)"></span>'+c.a+' in progress</span><span><span class="dot" style="background:var(--red)"></span>'+c.r+' to do</span><span><span class="dot" style="background:#C3C9CD"></span>'+c.n+' not covered yet</span></div><div class="card" style="padding-top:4px">'+rows+'</div>';});
sd.innerHTML=out+'<p style="font-size:.9rem;color:var(--ink-soft)">Biology, Business, English and French appear here once they have study guides. Topic codes and order are the official IB ones. Maths AA section names are short summaries of the content of each section, because the IB guide numbers those sections without giving them titles; Chemistry names are the official IB titles.</p>';
'''.replace('__S__',json.dumps(SUBJECTS)).replace('__G__',json.dumps(GUIDES)).replace('__R__',json.dumps(REVIEWS))
open(out+'/progress.html','w').write(page("Progress: IB study","index.html","Progress","Every syllabus topic for each subject, coloured by how far Jamila has got. Tick the \"I can\" boxes in the guides and do the quizzes, and this page updates itself.",body,script))
print("progress ok")
