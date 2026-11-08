import sys, json; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
MATHS=[("SL 1.1","Numbers in scientific form"),("SL 1.2","Arithmetic sequences and series"),("SL 1.3","Geometric sequences and series"),("SL 1.4","Financial applications"),("SL 1.5","Exponents and introduction to logarithms"),("SL 1.6","Simple deductive proof"),("SL 1.7","Rational exponents, laws of logarithms, exponential equations"),("SL 1.8","Sum to infinity"),("SL 1.9","Binomial theorem"),
("SL 2.1","Straight lines"),("SL 2.2","Functions: domain, range, graph"),("SL 2.3","Graphs of functions"),("SL 2.4","Key features of graphs, intersections"),("SL 2.5","Composite and inverse functions"),("SL 2.6","Quadratic functions"),("SL 2.7","Quadratic equations and inequalities, discriminant"),("SL 2.8","Reciprocal and rational functions"),("SL 2.9","Exponential and logarithmic functions"),("SL 2.10","Solving equations"),("SL 2.11","Transformations of graphs"),
("SL 3.1","3D geometry: distance, midpoint, volume, surface area"),("SL 3.2","Right-angled and non-right-angled trigonometry"),("SL 3.3","Applications of trigonometry"),("SL 3.4","Radians, arcs and sectors"),("SL 3.5","The unit circle"),("SL 3.6","Trigonometric identities"),("SL 3.7","Circular functions"),("SL 3.8","Trigonometric equations"),
("SL 4.1","Sampling"),("SL 4.2","Presenting data"),("SL 4.3","Central tendency and spread"),("SL 4.4","Correlation and regression (y on x)"),("SL 4.5","Probability concepts"),("SL 4.6","Venn and tree diagrams, combined events"),("SL 4.7","Discrete random variables"),("SL 4.8","Binomial distribution"),("SL 4.9","Normal distribution"),("SL 4.10","Regression of x on y"),("SL 4.11","Conditional probability and independence"),("SL 4.12","Standardised normal (z) values"),
("SL 5.1","Limits and the derivative"),("SL 5.2","Increasing and decreasing functions"),("SL 5.3","Differentiating ax<sup>n</sup>"),("SL 5.4","Tangents and normals"),("SL 5.5","Introduction to integration, areas"),("SL 5.6","Derivatives of standard functions, chain, product and quotient rules"),("SL 5.7","Second derivative"),("SL 5.8","Maxima, minima, points of inflexion, optimisation"),("SL 5.9","Kinematics"),("SL 5.10","Indefinite integrals, substitution"),("SL 5.11","Definite integrals and areas")]
# One entry per study guide. ADD A NEW ENTRY FOR EVERY NEW GUIDE (ican keys -> topic code).
GUIDES=[
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
REVIEWS=[dict(title="Week 1 review (Sun 15 Nov)", link="review/2026-11-08-week-1.html", quiz="ib-quiz-review-2026-11-08")]
# timed practice pages save {score,max,date} under ib-timed-YYYY-MM-DD
TIMED=[dict(title="Sat 14 Nov: timed set, Maths sequences", link="practice/2026-11-07-timed-maths-sequences.html", key="ib-timed-2026-11-07"),
       dict(title="Sat 21 Nov: mock papers", link="practice/2026-11-21-mock-papers.html", key="ib-timed-2026-11-21")]
BM=[("1.1","What is a business?"),("1.2","Types of business entities"),("1.3","Business objectives"),("1.4","Stakeholders"),("1.5","Growth and evolution"),("1.6","Multinational companies (MNCs)"),
("2.1","Introduction to human resource management"),("2.2","Organizational structure"),("2.3","Leadership and management"),("2.4","Motivation and demotivation"),("2.6","Communication"),
("3.1","Introduction to finance"),("3.2","Sources of finance"),("3.3","Costs and revenues"),("3.4","Final accounts"),("3.5","Profitability and liquidity ratio analysis"),("3.7","Cash flow"),("3.8","Investment appraisal"),
("4.1","Introduction to marketing"),("4.2","Marketing planning"),("4.4","Market research"),("4.5","The seven Ps of the marketing mix"),
("5.1","Introduction to operations management"),("5.2","Operations methods"),("5.4","Location"),("5.5","Break-even analysis")]  # SL sub-topics only (HL-only 2.5, 2.7, 3.6, 3.9, 4.3, 4.6, 5.3, 5.6-5.9 left out)
PSYCH=[('CON 1', 'Concept: Bias'), ('CON 2', 'Concept: Causality'), ('CON 3', 'Concept: Change'), ('CON 4', 'Concept: Measurement'), ('CON 5', 'Concept: Perspective'), ('CON 6', 'Concept: Responsibility'), ('BIO 1', 'Animal research/animal models'), ('BIO 2', 'Biological reductionism'), ('BIO 3', 'Brain imaging techniques'), ('BIO 4', 'Chemical messengers'), ('BIO 5', 'Diathesis-stress model'), ('BIO 6', 'Genetic inheritance'), ('BIO 7', 'Localization of function'), ('BIO 8', 'Neuroplasticity'), ('BIO 9', 'Neurotransmission'), ('COG 1', 'Anchoring bias'), ('COG 2', 'Classical conditioning'), ('COG 3', 'Cognitive load theory'), ('COG 4', 'Cognitive models'), ('COG 5', 'Confirmation bias'), ('COG 6', 'Dual processing theory'), ('COG 7', 'Operant conditioning'), ('COG 8', 'Schema theory'), ('SOC 1', 'Cognitive dissonance'), ('SOC 2', 'Compliance techniques'), ('SOC 3', 'Conformity'), ('SOC 4', 'Cultural dimensions'), ('SOC 5', 'Emic approach'), ('SOC 6', 'Enculturation'), ('SOC 7', 'Etic approach'), ('SOC 8', 'Models of acculturation'), ('SOC 9', 'Social identity theory'), ('SOC 10', 'Social learning theory'), ('RM 1', 'Research methods: types, choosing one, pros and cons, ethics'), ('RM 2', 'Sampling techniques'), ('RM 3', 'Research considerations: generalising, reflexivity, transferability, credibility'), ('RM 4', 'Data analysis and interpretation (studied by all, assessed at HL)'), ('CTX 1', 'Context: Health and well-being'), ('CTX 2', 'Context: Human development'), ('CTX 3', 'Context: Human relationships'), ('CTX 4', 'Context: Learning and cognition'), ('PRAC 1', 'Class practical: experiment'), ('PRAC 2', 'Class practical: interview'), ('PRAC 3', 'Class practical: observation'), ('PRAC 4', 'Class practical: survey'), ('HLX 1', 'HL extension: culture'), ('HLX 2', 'HL extension: motivation'), ('HLX 3', 'HL extension: technology'), ('IA', 'Internal assessment: research proposal')]  # official IB Psychology guide, first assessment 2027 (p19-39, 53); codes are ours, see the key on the page
BIO=[("A1.1","Water"),("A1.2","Nucleic acids")]  # PARTIAL: only topics with guides so far; replace with the full official list once the IB Biology guide is in the folder
SUBJECTS=[dict(name="Psychology HL",topics=PSYCH),dict(name="Maths AA SL",topics=MATHS),dict(name="Biology HL",topics=BIO,partial=True),dict(name="Business Management SL",topics=BM)]
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
var SUBJECTS=__S__, GUIDES=__G__, REVIEWS=__R__, TIMED=__T__;
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
TIMED.forEach(function(g){var q=get(g.key); h+='<div class="trow"><div class="name"><a href="'+g.link+'">'+g.title+'</a></div><div class="ev">'+(q?('score '+q.score+'/'+q.max+' on '+q.date):'not done yet')+'</div></div>';});
qd.innerHTML=h+'</div>';
var sd=document.getElementById('subjects'), out='';
SUBJECTS.forEach(function(s){var c={g:0,a:0,r:0,n:0}, rows='';
  s.topics.forEach(function(t){var i=info[s.name+'|'+t[0]]||{st:'n',ev:'',link:null}; c[i.st]++;
    rows+='<div class="trow"><span class="dot" style="background:'+COL[i.st]+';margin-top:7px"></span><div class="code">'+t[0]+'</div><div class="name">'+(i.link?'<a href="'+i.link+'">'+t[1]+'</a>':t[1])+'</div><div class="ev">'+i.ev+'</div></div>';});
  out+='<h2>'+s.name+(s.partial?' <span style="font-size:.8rem;color:var(--ink-soft);font-family:inherit">(partial list: full topic list once the official Biology guide is in the folder)</span>':'')+'</h2><div class="sum"><span><span class="dot" style="background:var(--green)"></span>'+c.g+' secure</span><span><span class="dot" style="background:var(--amber)"></span>'+c.a+' in progress</span><span><span class="dot" style="background:var(--red)"></span>'+c.r+' to do</span><span><span class="dot" style="background:#C3C9CD"></span>'+c.n+' not covered yet</span></div><div class="card" style="padding-top:4px">'+rows+'</div>';});
sd.innerHTML=out+'<p style="font-size:.9rem;color:var(--ink-soft)">Biology shows only the topics studied so far; English and French appear once their official subject guides are in the folder. Topic codes and order are the official IB ones. Maths AA section names are short summaries of the content of each section, because the IB guide numbers those sections without giving them titles; Business Management names are the official IB titles (Business: SL sub-topics only). Psychology follows the official guide (first assessment 2027); its codes are ours: CON = concept, BIO, COG and SOC = biological, cognitive and sociocultural approach, RM = research methodology, CTX = context, PRAC = class practical, HLX = HL extension, IA = internal assessment.</p>';
'''.replace('__S__',json.dumps(SUBJECTS)).replace('__G__',json.dumps(GUIDES)).replace('__R__',json.dumps(REVIEWS)).replace('__T__',json.dumps(TIMED))
open(out+'/progress.html','w').write(page("Progress: IB study","index.html","Progress","Every syllabus topic for each subject, coloured by how far Jamila has got. Tick the \"I can\" boxes in the guides and do the quizzes, and this page updates itself.",body,script))
print("progress ok")
