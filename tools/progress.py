import sys, json; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
MATHS=[("SL 1.1","Numbers in scientific form"),("SL 1.2","Arithmetic sequences and series"),("SL 1.3","Geometric sequences and series"),("SL 1.4","Financial applications"),("SL 1.5","Exponents and introduction to logarithms"),("SL 1.6","Simple deductive proof"),("SL 1.7","Rational exponents, laws of logarithms, exponential equations"),("SL 1.8","Sum to infinity"),("SL 1.9","Binomial theorem"),
("SL 2.1","Straight lines"),("SL 2.2","Functions: domain, range, graph"),("SL 2.3","Graphs of functions"),("SL 2.4","Key features of graphs, intersections"),("SL 2.5","Composite and inverse functions"),("SL 2.6","Quadratic functions"),("SL 2.7","Quadratic equations and inequalities, discriminant"),("SL 2.8","Reciprocal and rational functions"),("SL 2.9","Exponential and logarithmic functions"),("SL 2.10","Solving equations"),("SL 2.11","Transformations of graphs"),
("SL 3.1","3D geometry: distance, midpoint, volume, surface area"),("SL 3.2","Right-angled and non-right-angled trigonometry"),("SL 3.3","Applications of trigonometry"),("SL 3.4","Radians, arcs and sectors"),("SL 3.5","The unit circle"),("SL 3.6","Trigonometric identities"),("SL 3.7","Circular functions"),("SL 3.8","Trigonometric equations"),
("SL 4.1","Sampling"),("SL 4.2","Presenting data"),("SL 4.3","Central tendency and spread"),("SL 4.4","Correlation and regression (y on x)"),("SL 4.5","Probability concepts"),("SL 4.6","Venn and tree diagrams, combined events"),("SL 4.7","Discrete random variables"),("SL 4.8","Binomial distribution"),("SL 4.9","Normal distribution"),("SL 4.10","Regression of x on y"),("SL 4.11","Conditional probability and independence"),("SL 4.12","Standardised normal (z) values"),
("SL 5.1","Limits and the derivative"),("SL 5.2","Increasing and decreasing functions"),("SL 5.3","Differentiating ax<sup>n</sup>"),("SL 5.4","Tangents and normals"),("SL 5.5","Introduction to integration, areas"),("SL 5.6","Derivatives of standard functions, chain, product and quotient rules"),("SL 5.7","Second derivative"),("SL 5.8","Maxima, minima, points of inflexion, optimisation"),("SL 5.9","Kinematics"),("SL 5.10","Indefinite integrals, substitution"),("SL 5.11","Definite integrals and areas")]
# One entry per study guide. ADD A NEW ENTRY FOR EVERY NEW GUIDE (ican keys -> topic code).
GUIDES=[
 dict(subject="Psychology HL", title="Sat 14 Nov: evaluating research and conditioning", link="guides/2026-11-14-psychology-hl-evaluating-research-conditioning.html", ican="ib-psych-hl-eval-cond-ican", quiz="ib-quiz-guide-2026-11-14",
      map={"RM 1": ["d1", "d2", "d3", "t3"], "RM 3": ["r1", "r2", "r3", "t1", "t2", "x1", "x2"], "COG 2": ["cc1", "cc2", "cc3", "cc4"], "COG 7": ["oc1", "oc2", "oc3", "oc4"]},
      anchors={"RM 1": "#designs", "RM 3": "#relval", "COG 2": "#classical", "COG 7": "#operant"}),
 dict(subject="Biology HL", title="Sun 15 Nov: B1.1", link="guides/2026-11-15-biology-hl-b1.1-carbohydrates-lipids.html", ican="ib-bio-b11-ican", quiz="ib-quiz-guide-2026-11-15",
      map={"B1.1": ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13"]},
      anchors={"B1.1": "#b11a"}),
 dict(subject="Psychology HL", title="Mon 16 Nov: SLT, memory, exam technique", link="guides/2026-11-16-psychology-hl-slt-memory-exam-technique.html", ican="ib-psych-hl-slt-mem-ican", quiz="ib-quiz-guide-2026-11-16",
      map={"SOC 10": ["s1", "s2", "s3", "s4", "s5"], "COG 4": ["m1", "m2", "m3", "m4"], "RM 4": ["d1", "d2", "d3", "d4"]},
      anchors={"SOC 10": "#slt", "COG 4": "#mem", "RM 4": "#data"}),
 dict(subject="Biology HL", title="Wed 18 Nov: B1.2 and C1.1", link="guides/2026-11-18-biology-hl-b1.2-c1.1.html", ican="ib-bio-b12-c11-ican", quiz="ib-quiz-guide-2026-11-18",
      map={"B1.2": ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8", "p9", "p10", "p11", "p12"], "C1.1": ["e1", "e2", "e3", "e4", "e5", "e6", "e7", "e8", "e9", "e10", "e11", "e12", "e13", "e14", "e15", "e16", "e17"]},
      anchors={"B1.2": "#b12", "C1.1": "#c11"}),
 dict(subject="Business Management SL", title="Thu 19 Nov: Unit 2, 2.1 to 2.4", link="guides/2026-11-19-business-sl-unit2-hrm.html", ican="ib-business-sl-21-24-ican", quiz="ib-quiz-guide-2026-11-19",
      map={"2.1": ["b21a", "b21b", "b21c", "b21d"], "2.2": ["b22a", "b22b", "b22c"], "2.3": ["b23a", "b23b"], "2.4": ["b24a", "b24b", "b24c", "b24d"]},
      anchors={"2.1": "#s21", "2.2": "#s22", "2.3": "#s23", "2.4": "#s24"}),
 dict(subject="Biology HL", title="Sun 22 Nov: C1.2", link="guides/2026-11-22-biology-hl-c1.2-cell-respiration.html", ican="ib-bio-c12-ican", quiz="ib-quiz-guide-2026-11-22",
      map={"C1.2": ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10", "r11", "r12", "r13", "r14", "r15", "r16", "r17"]},
      anchors={"C1.2": "#c12sl"}),
 dict(subject="Psychology HL", title="Mon 30 Nov: data analysis (Paper 3)", link="guides/2026-11-30-psychology-hl-data-analysis.html", ican="ib-psych-hl-data-ican", quiz="ib-quiz-guide-2026-11-30",
      map={"RM 4": ["p1", "p2", "s1", "s2", "s3", "a1", "h1", "h2", "y1", "g1", "c1", "c2", "r1", "r2", "d1", "d2"]},
      anchors={"RM 4": "#p3"}),
 dict(subject="Psychology HL", title="Mon 9 Nov: course map and research methods", link="guides/2026-11-09-psychology-hl-frame-research-methods.html", ican="ib-psych-hl-frame-rm-ican", quiz="ib-quiz-guide-2026-11-09",
      map={"RM 1":["v1","v2","v3","e1","e2","e3","e4","h1","h2"],"RM 2":["s1","s2","s3"]},
      anchors={"RM 1":"#vars","RM 2":"#samp"}),
 dict(subject="Maths AA SL", title="Tue 17 Nov: 2.2 to 2.5", link="guides/2026-11-10-maths-aa-sl-2.2-2.5.html", ican="ib-maths-aa-sl-22-25-ican", quiz="ib-quiz-guide-2026-11-10",
      map={"SL 2.2":["d1","d2","d3","d4","d5"],"SL 2.3":["s1","s2","s3"],"SL 2.4":["k1","k2","k3"],"SL 2.5":["c1","c2","c3"]},
      anchors={"SL 2.2":"#s22","SL 2.3":"#s23","SL 2.4":"#s24","SL 2.5":"#s25"}),
 dict(subject="Biology HL", title="Wed 11 Nov: A1.1 and A1.2", link="guides/2026-11-05-biology-hl-a1.1-a1.2.html", ican="ib-bio-a11-a12-ican", quiz="ib-quiz-guide-2026-11-05",
      map={"A1.1":["w1","w2","w3","w4","w5","w6","w7","w8"],"A1.2":["n1","n2","n3","n4","n5","n6","n7","n8","n9","n10","n11","n12","n13","n14","n15"]},
      anchors={"A1.1":"#a11","A1.2":"#a12"}),
 dict(subject="Business Management SL", title="Thu 12 Nov: Unit 1, 1.1 to 1.6", link="guides/2026-11-06-business-sl-1.1-1.6.html", ican="ib-business-sl-11-16-ican", quiz="ib-quiz-guide-2026-11-06",
      map={"1.1":["b11a","b11b","b11c","b11d"],"1.2":["b12a","b12b","b12c","b12d"],"1.3":["b13a","b13b","b13c","b13d"],"1.4":["b14a","b14b"],"1.5":["b15a","b15b","b15c","b15d","b15e"],"1.6":["b16a","b16b"]},
      anchors={"1.1":"#s11","1.2":"#s12","1.3":"#s13","1.4":"#s14","1.5":"#s15","1.6":"#s16"}),
 dict(subject="Maths AA SL", title="Tue 10 Nov: 1.2 to 1.6", link="guides/2026-11-04-maths-aa-sl-1.2-1.6.html", ican="ib-maths-aa-sl-12-16-ican", quiz="ib-quiz-guide-2026-11-04",
      map={"SL 1.2":["a1","a2","a3","a4"],"SL 1.3":["g1","g2","g3"],"SL 1.8":["i1","i2"],"SL 1.4":["f1","f2","f3","f4"],"SL 1.6":["p1","p2","p3","p4"]},
      anchors={"SL 1.2":"#s12","SL 1.3":"#s13","SL 1.8":"#s18","SL 1.4":"#s14","SL 1.6":"#s16"}),
]
REVIEWS=[dict(title="Week 1 review (Sun 15 Nov)", link="review/2026-11-08-week-1.html", quiz="ib-quiz-review-2026-11-08"), dict(title="Week 2 review (Sun 22 Nov)", link="review/2026-11-22-week-2.html", quiz="ib-quiz-review-2026-11-22")]
# timed practice pages save {score,max,date} under ib-timed-YYYY-MM-DD
TIMED=[dict(title="Sat 14 Nov: timed set, Maths sequences", link="practice/2026-11-07-timed-maths-sequences.html", key="ib-timed-2026-11-07"),
       dict(title="Sat 21 Nov: mock papers", link="practice/2026-11-21-mock-papers.html", key="ib-timed-2026-11-21")]
BM=[("1.1","What is a business?"),("1.2","Types of business entities"),("1.3","Business objectives"),("1.4","Stakeholders"),("1.5","Growth and evolution"),("1.6","Multinational companies (MNCs)"),
("2.1","Introduction to human resource management"),("2.2","Organizational structure"),("2.3","Leadership and management"),("2.4","Motivation and demotivation"),("2.6","Communication"),
("3.1","Introduction to finance"),("3.2","Sources of finance"),("3.3","Costs and revenues"),("3.4","Final accounts"),("3.5","Profitability and liquidity ratio analysis"),("3.7","Cash flow"),("3.8","Investment appraisal"),
("4.1","Introduction to marketing"),("4.2","Marketing planning"),("4.4","Market research"),("4.5","The seven Ps of the marketing mix"),
("5.1","Introduction to operations management"),("5.2","Operations methods"),("5.4","Location"),("5.5","Break-even analysis")]  # SL sub-topics only (HL-only 2.5, 2.7, 3.6, 3.9, 4.3, 4.6, 5.3, 5.6-5.9 left out)
PSYCH=[('CON 1', 'Concept: Bias'), ('CON 2', 'Concept: Causality'), ('CON 3', 'Concept: Change'), ('CON 4', 'Concept: Measurement'), ('CON 5', 'Concept: Perspective'), ('CON 6', 'Concept: Responsibility'), ('BIO 1', 'Animal research/animal models'), ('BIO 2', 'Biological reductionism'), ('BIO 3', 'Brain imaging techniques'), ('BIO 4', 'Chemical messengers'), ('BIO 5', 'Diathesis-stress model'), ('BIO 6', 'Genetic inheritance'), ('BIO 7', 'Localization of function'), ('BIO 8', 'Neuroplasticity'), ('BIO 9', 'Neurotransmission'), ('COG 1', 'Anchoring bias'), ('COG 2', 'Classical conditioning'), ('COG 3', 'Cognitive load theory'), ('COG 4', 'Cognitive models'), ('COG 5', 'Confirmation bias'), ('COG 6', 'Dual processing theory'), ('COG 7', 'Operant conditioning'), ('COG 8', 'Schema theory'), ('SOC 1', 'Cognitive dissonance'), ('SOC 2', 'Compliance techniques'), ('SOC 3', 'Conformity'), ('SOC 4', 'Cultural dimensions'), ('SOC 5', 'Emic approach'), ('SOC 6', 'Enculturation'), ('SOC 7', 'Etic approach'), ('SOC 8', 'Models of acculturation'), ('SOC 9', 'Social identity theory'), ('SOC 10', 'Social learning theory'), ('RM 1', 'Research methods: types, choosing one, pros and cons, ethics'), ('RM 2', 'Sampling techniques'), ('RM 3', 'Research considerations: generalising, reflexivity, transferability, credibility'), ('RM 4', 'Data analysis and interpretation (studied by all, assessed at HL)'), ('CTX 1', 'Context: Health and well-being'), ('CTX 2', 'Context: Human development'), ('CTX 3', 'Context: Human relationships'), ('CTX 4', 'Context: Learning and cognition'), ('PRAC 1', 'Class practical: experiment'), ('PRAC 2', 'Class practical: interview'), ('PRAC 3', 'Class practical: observation'), ('PRAC 4', 'Class practical: survey'), ('HLX 1', 'HL extension: culture'), ('HLX 2', 'HL extension: motivation'), ('HLX 3', 'HL extension: technology'), ('IA', 'Internal assessment: research proposal')]  # official IB Psychology guide, first assessment 2027 (p19-39, 53); codes are ours, see the key on the page
BIO=[('A1.1', 'Water'), ('A1.2', 'Nucleic acids'), ('A2.1', 'Origins of cells'), ('A2.2', 'Cell structure'), ('A2.3', 'Viruses'), ('A3.1', 'Diversity of organisms'), ('A3.2', 'Classification and cladistics'), ('A4.1', 'Evolution and speciation'), ('A4.2', 'Conservation of biodiversity'), ('B1.1', 'Carbohydrates and lipids'), ('B1.2', 'Proteins'), ('B2.1', 'Membranes and membrane transport'), ('B2.2', 'Organelles and compartmentalization'), ('B2.3', 'Cell specialization'), ('B3.1', 'Gas exchange'), ('B3.2', 'Transport'), ('B3.3', 'Muscle and motility'), ('B4.1', 'Adaptation to environment'), ('B4.2', 'Ecological niches'), ('C1.1', 'Enzymes and metabolism'), ('C1.2', 'Cell respiration'), ('C1.3', 'Photosynthesis'), ('C2.1', 'Chemical signalling'), ('C2.2', 'Neural signalling'), ('C3.1', 'Integration of body systems'), ('C3.2', 'Defence against disease'), ('C4.1', 'Populations and communities'), ('C4.2', 'Transfers of energy and matter'), ('D1.1', 'DNA replication'), ('D1.2', 'Protein synthesis'), ('D1.3', 'Mutation and gene editing'), ('D2.1', 'Cell and nuclear division'), ('D2.2', 'Gene expression'), ('D2.3', 'Water potential'), ('D3.1', 'Reproduction'), ('D3.2', 'Inheritance'), ('D3.3', 'Homeostasis'), ('D4.1', 'Natural selection'), ('D4.2', 'Stability and change'), ('D4.3', 'Climate change')]  # official IB Biology guide, first assessment 2025 (syllabus roadmap, 40 topics)
SUBJECTS=[dict(name="Psychology HL",topics=PSYCH),dict(name="Maths AA SL",topics=MATHS),dict(name="Biology HL",topics=BIO),dict(name="Business Management SL",topics=BM)]
PLAN=json.load(open(sys.argv[1]+'/plan.json'))
LINKS=json.load(open(sys.argv[1]+'/links.json'))
from quizjs import STORAGE_JS
body='''
<div class="card" style="margin-top:24px">
  <b>What the labels mean</b>
  <div class="legend">
    <span><span class="st g">&#10003; Secure</span> every "I can" box ticked, and a quiz score of 80% or more at least 3 days after your first try (so it has stuck, not just been read)</span>
    <span><span class="st a">&#9680; In progress</span> some boxes ticked or the quiz done, not secure yet</span>
    <span><span class="st t">! To do</span> its guide's plan day has come, but nothing ticked and no quiz yet</span>
    <span><span class="st n">&ndash; Not yet</span> no guide for this topic yet, or its plan day is still to come</span>
  </div>
  <p style="margin:10px 0 0;font-size:.9rem;color:var(--ink-soft)">This page reads the ticks and quiz scores saved in this browser, so open the guides and this page on the same device. Nothing is sent anywhere.</p>
</div>
<div id="days"></div>
<div id="quizzes"></div>
<div id="subjects"></div>
<style>:root{--amber-ink:#8A6416;--grey:#5F6B72}
:focus-visible{outline:3px solid var(--indigo);outline-offset:2px}
.legend{display:flex;flex-direction:column;gap:6px;margin-top:8px;font-size:.95rem}
.st{display:inline-block;font-size:.8rem;font-weight:700;padding:1px 8px;border-radius:4px;border:1px solid var(--rule);white-space:nowrap;margin-right:6px;background:var(--card);color:var(--grey)}
.st.g{background:var(--green-soft);border-color:var(--green);color:var(--green)}
.st.a{background:var(--amber-soft);border-color:var(--amber);color:var(--amber-ink)}
.st.t{border-color:var(--grey);color:var(--ink)}
.trow{display:flex;gap:10px;align-items:flex-start;padding:7px 0;border-bottom:1px solid var(--rule)}
.trow .code{min-width:62px;font-weight:700;white-space:nowrap}.trow .name{flex:1}.trow .ev{font-size:.85rem;color:var(--ink-soft);text-align:right}
.trow .st{margin-top:3px;min-width:104px}
@media (max-width:600px){.trow{flex-wrap:wrap}.trow .ev{flex-basis:100%;text-align:left}}
.sum{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.9rem;margin:4px 0 6px}
.bar{display:flex;height:12px;border-radius:4px;overflow:hidden;background:#EDF0EC;border:1px solid var(--rule);margin:0 0 10px}
.bar span{display:block;height:100%}
.bar .g{background:var(--green)} .bar .a{background:var(--amber)} .bar .t{background:var(--grey)}
details.fold summary{cursor:pointer;color:var(--indigo);padding:10px 0;min-height:44px}
.daysdone{font-size:1.1rem}
</style>
'''
script=STORAGE_JS+'''
storageNotice();
var SUBJECTS=__S__, GUIDES=__G__, REVIEWS=__R__, TIMED=__T__, PLAN=__P__, LINKS=__L__;
function get(k){try{return JSON.parse(localStorage.getItem(k)||'null');}catch(e){return null;}}
function pad(n){return (n<10?'0':'')+n;}
var now=new Date(), today=now.getFullYear()+'-'+pad(now.getMonth()+1)+'-'+pad(now.getDate());
function days(a,b){var x=a.split('-'),y=b.split('-');return Math.round((new Date(+y[0],y[1]-1,+y[2])-new Date(+x[0],x[1]-1,+x[2]))/864e5);}
// every finished round: <key>-attempts = [{date,right,total}]; older scores (saved before the history existed) count as one attempt
function attempts(k){var a=get(k+'-attempts'); if(Array.isArray(a)&&a.length) return a;
  var q=get(k); if(q&&q.total&&typeof q.right==='number') return [{date:q.date,right:q.right,total:q.total}];
  if(q&&q.max&&typeof q.score==='number') return [{date:q.date,right:q.score,total:q.max}]; return [];}
function stuck(a){if(!a.length) return false; var first=a.map(function(x){return x.date;}).filter(Boolean).sort()[0]; if(!first) return false;
  return a.some(function(x){return x.total&&x.right>=0.8*x.total&&x.date&&days(first,x.date)>=3;});}
function lst(iso){var l=LINKS[iso]; return !l?[]:(Array.isArray(l)?l:[l]);}
var planDay={}; PLAN.forEach(function(p){lst(p.iso).forEach(function(l){if(!l.review&&!planDay[l.url]) planDay[l.url]=p.iso;});});
var LBL={g:'&#10003; Secure',a:'&#9680; In progress',t:'! To do',n:'&ndash; Not yet'};
function chip(s){return '<span class="st '+s+'">'+LBL[s]+'</span>';}
var info={};
GUIDES.forEach(function(g){var t=get(g.ican)||{}, q=get(g.quiz), at=attempts(g.quiz), pd=planDay[g.link];
  Object.keys(g.map).forEach(function(code){var ks=g.map[code], n=ks.filter(function(k){return t[k];}).length;
    var best=q?(q.best||q.right):null, tot=q?q.total:null;
    var st=(n===ks.length && stuck(at)) ? 'g' : ((n>0||q||at.length)?'a':((!pd||pd<=today)?'t':'n'));
    var ev=n+'/'+ks.length+' ticked'+(q?(' · quiz best '+best+'/'+tot+' ('+at.length+' '+(at.length===1?'try':'tries')+')'):' · quiz not done');
    if(st==='a'&&n===ks.length&&at.length&&!stuck(at)) ev+=' · redo the quiz 3 or more days after your first try';
    if(st==='n'&&pd) ev='guide on '+pd;
    info[g.subject+'|'+code]={st:st,ev:ev,link:g.link+(g.anchors[code]||'')};});});
// days with a page done: any of the day's pages has a score dated on or after that day
var done=0; PLAN.forEach(function(p){ if(lst(p.iso).some(function(l){var q=get(l.quiz); if(q&&q.date&&q.date>=p.iso) return true;
  return attempts(l.quiz).some(function(x){return x.date&&x.date>=p.iso;});})) done++; });
document.getElementById('days').innerHTML='<div class="card daysdone"><b>Days with a page done: '+done+' of '+PLAN.length+'</b><div style="font-size:.88rem;color:var(--ink-soft)">A day counts once you finish the quiz or save the score of one of its pages, on that day or later.</div></div>';
var qd=document.getElementById('quizzes'); var h='<h2>Quiz scores</h2><div class="card">';
function fd(d){if(!d)return '';var m=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],x=d.split('-');return x.length===3?(+x[2])+' '+m[+x[1]-1]:d;}
function firstDay(link){for(var i=0;i<PLAN.length;i++){if(lst(PLAN[i].iso).some(function(l){return !l.review&&l.url===link;}))return PLAN[i].iso;}return '9999';}
GUIDES.concat(REVIEWS).slice().sort(function(a,b){return firstDay(a.link)<firstDay(b.link)?-1:1;}).forEach(function(g){var q=get(g.quiz), at=attempts(g.quiz); h+='<div class="trow"><div class="name"><a href="'+g.link+'#quiz">'+(g.subject?g.subject+': ':'')+g.title+'</a></div><div class="ev">'+(q?('best '+(q.best||q.right)+'/'+q.total+', last '+q.right+'/'+q.total+' on '+fd(q.date)+(at.length>1?', '+at.length+' tries':'')):'not done yet')+'</div></div>';});
TIMED.forEach(function(g){var q=get(g.key); h+='<div class="trow"><div class="name"><a href="'+g.link+'">'+g.title+'</a></div><div class="ev">'+(q?('score '+q.score+'/'+q.max+' on '+fd(q.date)):'not done yet')+'</div></div>';});
qd.innerHTML=h+'</div>';
var sd=document.getElementById('subjects'), out='';
SUBJECTS.forEach(function(s){var c={g:0,a:0,t:0,n:0}, rows='', later='';
  s.topics.forEach(function(t){var i=info[s.name+'|'+t[0]]||{st:'n',ev:'',link:null}; c[i.st]++;
    var r='<div class="trow">'+chip(i.st)+'<div class="code">'+t[0]+'</div><div class="name">'+(i.link?'<a href="'+i.link+'">'+t[1]+'</a>':t[1])+'</div><div class="ev">'+i.ev+'</div></div>';
    if(i.st==='n') later+=r; else rows+=r;});
  var N=s.topics.length, w=function(k){return (100*c[k]/N).toFixed(2)+'%';};
  out+='<h2>'+s.name+(s.partial?' <span style="font-size:.8rem;color:var(--ink-soft);font-family:inherit">(partial list: full topic list once the official Biology guide is in the folder)</span>':'')+'</h2>'+
    '<div class="sum">'+chip('g')+c.g+' '+chip('a')+c.a+' '+chip('t')+c.t+' '+chip('n')+c.n+'</div>'+
    '<div class="bar" role="img" aria-label="'+c.g+' secure, '+c.a+' in progress, '+c.t+' to do, '+c.n+' not yet, out of '+N+'"><span class="g" style="width:'+w('g')+'"></span><span class="a" style="width:'+w('a')+'"></span><span class="t" style="width:'+w('t')+'"></span></div>'+
    '<div class="card" style="padding-top:4px">'+rows+(later?'<details class="fold"'+(rows?'':' open')+'><summary>'+c.n+' topics not covered yet</summary>'+later+'</details>':'')+'</div>';});
sd.innerHTML=out+'<p style="font-size:.9rem;color:var(--ink-soft)">Biology follows the official guide (first assessment 2025). English and French have no topic list here because their courses are skills-based. Topic codes and order are the official IB ones. Maths AA section names are short summaries of the content of each section, because the IB guide numbers those sections without giving them titles; Business Management names are the official IB titles (Business: SL sub-topics only). Psychology follows the official guide (first assessment 2027); its codes are ours: CON = concept, BIO, COG and SOC = biological, cognitive and sociocultural approach, RM = research methodology, CTX = context, PRAC = class practical, HLX = HL extension, IA = internal assessment.</p>';
'''.replace('__S__',json.dumps(SUBJECTS)).replace('__G__',json.dumps(GUIDES)).replace('__R__',json.dumps(REVIEWS)).replace('__T__',json.dumps(TIMED)).replace('__P__',json.dumps(PLAN,ensure_ascii=False)).replace('__L__',json.dumps(LINKS))
open(out+'/progress.html','w').write(page("Progress: IB study","index.html","Progress","Every syllabus topic for each subject, labelled by how far Jamila has got. Tick the \"I can\" boxes in the guides and do the quizzes, and this page updates itself.",body,script))
print("progress ok")
