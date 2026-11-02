import sys, json, html, re; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
M='guides/2026-11-04-maths-aa-sl-1.2-1.6.html'; C='guides/2026-11-03-chemistry-s1.1-s1.3.html'
# (id, subject, topic, link, front, back)  -- add cards for every new guide here
cards=[
("m01","Maths","SL 1.2",M+"#s12","How do you test whether a sequence is arithmetic?","Check the differences are equal: u<sub>2</sub> − u<sub>1</sub> = u<sub>3</sub> − u<sub>2</sub>. That constant is d."),
("m02","Maths","SL 1.2",M+"#s12","n<sup>th</sup> term of an arithmetic sequence","u<sub>n</sub> = u<sub>1</sub> + (n − 1)d (in the formula booklet). n − 1 steps, not n."),
("m03","Maths","SL 1.2",M+"#s12","Sum of the first n terms of an arithmetic sequence (two forms)","S<sub>n</sub> = n/2 (2u<sub>1</sub> + (n − 1)d) = n/2 (u<sub>1</sub> + u<sub>n</sub>) (both in the booklet)."),
("m04","Maths","SL 1.2",M+"#s12","How many terms in a sigma sum from r = a to r = b?","b − a + 1. From r = 3 to r = 12 is 10 terms, not 9."),
("m05","Maths","SL 1.2",M+"#s12","You are given S<sub>n</sub>. How do you find u<sub>n</sub> and u<sub>1</sub>?","u<sub>n</sub> = S<sub>n</sub> − S<sub>n−1</sub>, and u<sub>1</sub> = S<sub>1</sub>."),
("m06","Maths","SL 1.2",M+"#s12","Simple interest: arithmetic or geometric?","Arithmetic: the same amount is added every year (for example 5000 + 189n)."),
("m07","Maths","SL 1.2",M+"#s12","Data is nearly but not exactly arithmetic. How do you model it?","Approximate d by the average step: (last − first) ÷ (number of gaps). Predictions far outside the data are less reliable."),
("m08","Maths","SL 1.3",M+"#s13","How do you test whether a sequence is geometric?","Check the ratios are equal: u<sub>2</sub>/u<sub>1</sub> = u<sub>3</sub>/u<sub>2</sub>. That constant is r."),
("m09","Maths","SL 1.3",M+"#s13","n<sup>th</sup> term of a geometric sequence","u<sub>n</sub> = u<sub>1</sub>r<sup>n−1</sup> (in the booklet)."),
("m10","Maths","SL 1.3",M+"#s13","Sum of the first n terms of a geometric sequence","S<sub>n</sub> = u<sub>1</sub>(r<sup>n</sup> − 1)/(r − 1) = u<sub>1</sub>(1 − r<sup>n</sup>)/(1 − r), r ≠ 1 (in the booklet)."),
("m11","Maths","SL 1.3",M+"#s13","Two terms of a geometric sequence are given. Fastest way to find r?","Divide them: u<sub>5</sub>/u<sub>2</sub> = r<sup>3</sup>. Remember r<sup>2</sup> = 3 gives r = ±√3."),
("m12","Maths","SL 1.3",M+"#s13","Grows by 2.5% a year. Multiplier? After n years or in year n?","× 1.025. After n years: × 1.025<sup>n</sup>. In year n when year 1 is the start: × 1.025<sup>n−1</sup>."),
("m13","Maths","SL 1.8",M+"#s18","Sum to infinity and its condition","S<sub>∞</sub> = u<sub>1</sub>/(1 − r), only if |r| &lt; 1 (in the booklet). Always write the check."),
("m14","Maths","SL 1.8",M+"#s18","First term of the sum from r = 1 of 5(1/4)<sup>r</sup>?","Put r = 1: 5 × 1/4 = 5/4, not 5."),
("m15","Maths","SL 1.8",M+"#s18","Ball dropped from h, each bounce reaches r of the last. Total distance?","h + 2 × hr/(1 − r). The first drop counts once, every later height twice."),
("m16","Maths","SL 1.4",M+"#s14","Compound interest formula","FV = PV × (1 + r/(100k))<sup>kn</sup> (in the booklet). k = 1 yearly, 2 half-yearly, 4 quarterly, 12 monthly."),
("m17","Maths","SL 1.4",M+"#s14","Depreciation by r% a year for n years","Value = original × (1 − r/100)<sup>n</sup>."),
("m18","Maths","SL 1.4",M+"#s14","Real value of an investment with inflation i% a year","Divide the nominal value by (1 + i/100)<sup>n</sup>. Quick method: use the rate r − i."),
("m19","Maths","SL 1.4",M+"#s14","GDC financial app: the sign rule","PV and FV must have opposite signs (money paid in is negative)."),
("m20","Maths","SL 1.6",M+"#s16","= or ≡ ?","= is true for some values (x + 2 = 5). ≡ is true for every value (an identity)."),
("m21","Maths","SL 1.6",M+"#s16","How to lay out an LHS to RHS proof","Start from one side only, change it step by step, reach the other side, write \"= RHS\" and a concluding sentence."),
("m22","Maths","SL 1.6",M+"#s16","Algebraic form of an even and of an odd integer","Even 2k, odd 2k + 1. Two different odd numbers: 2a + 1 and 2b + 1."),
("m23","Maths","Exam","exam-maths-aa-sl.html","Command term \"Write down\"","Obtain the answer, usually by extracting information. Little or no calculation; working does not need to be shown."),
("m24","Maths","Exam","exam-maths-aa-sl.html","Command term \"Hence\"","Use the preceding work to obtain the required result. Another method scores nothing."),
("m25","Maths","Exam","exam-maths-aa-sl.html","Paper 1 and Paper 2: calculator?","Paper 1: no calculator. Paper 2: GDC required. Both 90 minutes, 80 marks."),
("c01","Chemistry","S1.1",C+"#s11","Element, compound, mixture","Element: one kind of atom, cannot be broken down chemically. Compound: different elements chemically bonded in a fixed ratio. Mixture: not chemically bonded, no fixed ratio, separable by physical methods."),
("c02","Chemistry","S1.1",C+"#s11","Homogeneous vs heterogeneous mixture","Homogeneous: uniform composition, one phase (salt water, air). Heterogeneous: not uniform, more than one phase (sand in water)."),
("c03","Chemistry","S1.1",C+"#s11","The six separation techniques in the IB guide","Solvation, filtration, recrystallisation, evaporation, distillation, paper chromatography."),
("c04","Chemistry","S1.1",C+"#s11","What property does each use: distillation, filtration, paper chromatography?","Distillation: boiling point. Filtration: particle size (insoluble solid). Chromatography: different attraction to the stationary and mobile phase."),
("c05","Chemistry","S1.1",C+"#s11","Name the six changes of state","Melting, freezing, vaporisation (evaporation and boiling), condensation, sublimation (solid to gas), deposition (gas to solid)."),
("c06","Chemistry","S1.1",C+"#s11","Why does temperature stay constant while a liquid boils?","Energy goes into overcoming forces between particles (potential energy rises), not into kinetic energy, so average kinetic energy and temperature stay the same."),
("c07","Chemistry","S1.1",C+"#s11","What does temperature in kelvin measure? Convert °C to K.","The average kinetic energy of the particles. T(K) = T(°C) + 273."),
("c08","Chemistry","S1.2",C+"#s12","Relative mass and charge of proton, neutron, electron","Proton 1, +1. Neutron 1, 0. Electron negligible (1/1836), −1."),
("c09","Chemistry","S1.2",C+"#s12","In the nuclear symbol, what are A and Z?","A (top left): mass number = protons + neutrons. Z (bottom left): atomic number = protons."),
("c10","Chemistry","S1.2",C+"#s12","Electrons in an ion","Z − charge. Fe<sup>3+</sup>: 26 − 3 = 23. Cl<sup>−</sup>: 17 + 1 = 18."),
("c11","Chemistry","S1.2",C+"#s12","Isotopes: definition, and why the same chemistry?","Atoms of the same element with different numbers of neutrons. Same chemistry because they have the same number and arrangement of electrons; different mass, so different physical properties."),
("c12","Chemistry","S1.2",C+"#s12","Relative atomic mass from abundances","A<sub>r</sub> = Σ(isotope mass × % abundance) ÷ 100. If the abundances do not add to 100, divide by their total."),
("c13","Chemistry","S1.2",C+"#s12","(HL) Mass spectrum: what do peak position and height tell you?","Position (m/z) identifies the isotope; height gives its relative abundance."),
("c14","Chemistry","S1.3",C+"#s13","Continuous vs line spectrum","Continuous: all wavelengths, no gaps. Line: only certain wavelengths, separate lines on a dark background."),
("c15","Chemistry","S1.3",C+"#s13","Why is the hydrogen line spectrum evidence for energy levels?","Only certain photon energies are emitted, so electrons can only have certain (discrete) energies. The lines converge because the levels converge."),
("c16","Chemistry","S1.3",C+"#s13","Hydrogen: falls to n = 1, n = 2, n = 3 give which region?","n = 1: ultraviolet. n = 2: visible. n = 3: infrared."),
("c17","Chemistry","S1.3",C+"#s13","Maximum electrons in main level n, and in s, p, d, f","2n<sup>2</sup>. s 2, p 6, d 10, f 14."),
("c18","Chemistry","S1.3",C+"#s13","Aufbau, Pauli, Hund in one line each","Aufbau: fill lowest energy first. Pauli: max 2 electrons per orbital, opposite spins. Hund: single electrons with parallel spins in degenerate orbitals before pairing."),
("c19","Chemistry","S1.3",C+"#s13","Configurations of Cr and Cu","Cr [Ar] 4s<sup>1</sup> 3d<sup>5</sup>. Cu [Ar] 4s<sup>1</sup> 3d<sup>10</sup>."),
("c20","Chemistry","S1.3",C+"#s13","Transition metal ions lose which electrons first?","4s, even though 4s filled first. Fe<sup>2+</sup> is [Ar] 3d<sup>6</sup>."),
("c21","Chemistry","S1.3",C+"#s13","(HL) Definition of first ionisation energy","The minimum energy to remove one mole of electrons from one mole of gaseous atoms to form one mole of gaseous 1+ ions. M(g) → M<sup>+</sup>(g) + e<sup>−</sup>."),
("c22","Chemistry","S1.3",C+"#s13","(HL) What does the convergence limit correspond to?","Ionisation: the electron is removed completely (n = ∞)."),
("c23","Chemistry","S1.3",C+"#s13","(HL) First IE across a period and down a group","Across: increases (nuclear charge up, shielding about the same). Down: decreases (outer electron further away and more shielded)."),
("c24","Chemistry","S1.3",C+"#s13","(HL) The two dips in first IE across period 2","B lower than Be (removing a higher-energy p electron). O lower than N (removing the first paired p electron; pair repulsion)."),
("c25","Chemistry","S1.3",C+"#s13","(HL) How do successive IEs give the group?","Count the electrons removed before the first big jump: that is the number of outer electrons, so the group."),
("c26","Chemistry","Exam","exam-chemistry-hl.html","Paper 1A: wrong answers?","40 multiple-choice questions and no marks deducted for wrong answers, so never leave one blank."),
("n01","Business","1.1","guides/2026-11-06-business-sl-1.1-1.6.html#s11","Name the four sectors of the economy with one example each","Primary: takes natural resources (farm, mine). Secondary: manufacturing and construction (factory). Tertiary: services to people (shop, bank). Quaternary: knowledge and information (software, research)."),
("n02","Business","1.1","guides/2026-11-06-business-sl-1.1-1.6.html#s11","Added value","Selling price minus the cost of bought-in materials and services. Wages, rent and profit come out of it, so it is <b>not</b> profit."),
("n03","Business","1.1","guides/2026-11-06-business-sl-1.1-1.6.html#s11","Entrepreneur vs intrapreneur","Entrepreneur: spots an opportunity, organises the resources and takes the risk of starting a business. Intrapreneur: an employee who acts entrepreneurially inside an existing organisation, using its resources."),
("n04","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","Limited vs unlimited liability","Unlimited: the owner is personally liable for all business debts (sole traders, most partners). Limited: shareholders can lose at most what they invested."),
("n05","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","Privately held vs publicly held company","Both have limited liability and are in the private sector. Privately held: shares sold privately, with the other owners agreeing. Publicly held: shares sold to the general public on a stock exchange."),
("n06","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","Cooperative: main features","Owned and run by its members (workers, customers or producers), usually one member one vote; profits shared among members or reinvested. A for-profit social enterprise."),
("n07","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","NGO","Non-governmental organisation: a non-profit social enterprise, independent of government, run for a cause; funded by donations, grants and fundraising; any surplus goes to the cause."),
("n08","Business","1.3","guides/2026-11-06-business-sl-1.1-1.6.html#s13","Vision statement vs mission statement","Vision: the long-term ideal future the organisation wants to reach. Mission: its purpose now, what it does, for whom and what it values."),
("n09","Business","1.3","guides/2026-11-06-business-sl-1.1-1.6.html#s13","Strategic vs tactical objectives","Strategic: long term, whole organisation, set by senior managers. Tactical: shorter term, one department or area, helps achieve a strategic objective."),
("n10","Business","1.3","guides/2026-11-06-business-sl-1.1-1.6.html#s13","Corporate social responsibility (CSR)","Acting in the interests of society and the environment <b>beyond</b> what the law requires, and taking responsibility for the effects of the business."),
("n11","Business","1.4","guides/2026-11-06-business-sl-1.1-1.6.html#s14","Internal vs external stakeholders","Internal: employees, managers and directors, shareholders. External: customers, suppliers, lenders, government, local community, pressure groups, competitors."),
("n12","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Average cost formula (is it on the formula sheet?)","Average cost = total cost &divide; output. Not on the formula sheet: learn it."),
("n13","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Six internal economies of scale","Purchasing (bulk buying), technical, financial, marketing, managerial, risk-bearing."),
("n14","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","External economies of scale vs external growth","External economies: lower average costs because the whole industry or area grows. External growth: growing by joining with or working through other firms (M&amp;As, takeovers, joint ventures, alliances, franchising)."),
("n15","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Joint venture vs strategic alliance","Joint venture: firms create a new, separate business they own together. Strategic alliance: firms cooperate but stay independent, and no new business is created."),
("n16","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Merger vs acquisition vs takeover","Merger: two firms agree to combine into one. Acquisition: one firm buys a controlling interest in another, with its agreement. Takeover: a hostile acquisition, against the wishes of the target managers."),
("n17","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Franchising: who pays whom?","The franchisee pays the franchisor an initial fee plus royalties (a share of sales) for the right to use its brand and system."),
("n18","Business","1.6","guides/2026-11-06-business-sl-1.1-1.6.html#s16","MNC, home country and host country","MNC: a company with its head office in one country that produces in more than one country. Home country: where the head office is. Host country: any other country where it operates."),
]
for c in cards: assert "—" not in c[4]+c[5]
data=[dict(id=a,s=b,t=t,l=l,f=f,b=bk) for a,b,t,l,f,bk in cards]
# Anki import file: front<TAB>back<TAB>tags
with open(out+'/flashcards-anki.txt','w') as fh:
    fh.write("#separator:tab\n#html:true\n#tags column:3\n")
    for a,s,t,l,f,bk in cards:
        fh.write(f"{f}\t{bk}\tIB::{s} {t.replace(' ','_')}\n")
body='''
<div class="card" style="margin-top:24px">
  <p style="margin:0 0 8px"><b>How to use:</b> read the question, answer it out loud or on paper, then press <b>Show answer</b>. Press <b>Again</b> if you were wrong or slow, <b>Got it</b> if you knew it. "Again" cards come back first next time. Your progress is saved on this device.</p>
  <div id="filters" style="display:flex;flex-wrap:wrap;gap:6px"></div>
</div>
<div id="stats" style="font-size:.92rem;color:var(--ink-soft);margin:8px 2px"></div>
<div class="card" id="box" style="min-height:220px">
  <div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;font-size:.85rem;color:var(--ink-soft)"><span id="meta"></span><a id="src" href="#">open the section</a></div>
  <p id="front" style="font-size:1.25rem;font-weight:600;margin:14px 0"></p>
  <div id="back" style="display:none;border-top:1px solid var(--rule);padding-top:12px;font-size:1.08rem"></div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:16px">
    <button id="show" class="fb">Show answer</button>
    <button id="again" class="fb" style="display:none;background:var(--red-soft);border-color:var(--red)">Again</button>
    <button id="got" class="fb" style="display:none;background:var(--green-soft);border-color:var(--green)">Got it</button>
  </div>
</div>
<p style="font-size:.92rem;color:var(--ink-soft)">Prefer Anki? Download <a href="flashcards-anki.txt" download>flashcards-anki.txt</a> and use File, Import in Anki. <button id="reset" class="fb" style="font-size:.85rem;padding:3px 10px;margin-left:6px">Reset progress</button></p>
<style>.fb{font:inherit;padding:8px 16px;border-radius:6px;border:1px solid var(--rule);background:#F3F5F2;color:var(--ink);cursor:pointer}.fb.on{background:var(--indigo);color:#fff;border-color:var(--indigo)}</style>
'''
script='''
var CARDS=__DATA__;
var KEY='ib-flash-v1', st={}; try{st=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
var subj='All', cur=null, queue=[];
function save(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(e){}}
function box(c){return (st[c.id]&&st[c.id].b)||0;}
function pool(){return CARDS.filter(function(c){return subj==='All'||c.s===subj;});}
function build(){var p=pool();
  // never-seen and "again" cards first, then by box, keep list order inside a box
  queue=p.slice().sort(function(a,b){var sa=st[a.id]?1:0, sb=st[b.id]?1:0; var ka=st[a.id]?box(a)+1:0, kb=st[b.id]?box(b)+1:0; return ka-kb;});
}
function stats(){var p=pool(),again=0,learning=0,known=0,fresh=0;p.forEach(function(c){if(!st[c.id])fresh++;else if(box(c)===0)again++;else if(box(c)<3)learning++;else known++;});
  document.getElementById('stats').textContent=p.length+' cards: '+fresh+' new, '+again+' to repeat, '+learning+' learning, '+known+' known (3 correct in a row)';}
function next(){if(!queue.length)build(); cur=queue.shift();
  document.getElementById('meta').textContent=cur.s+' · '+cur.t;
  var a=document.getElementById('src'); a.href=cur.l;
  document.getElementById('front').innerHTML=cur.f; var bk=document.getElementById('back'); bk.innerHTML=cur.b; bk.style.display='none';
  document.getElementById('show').style.display=''; document.getElementById('again').style.display='none'; document.getElementById('got').style.display='none'; stats();}
document.getElementById('show').onclick=function(){document.getElementById('back').style.display='block';this.style.display='none';document.getElementById('again').style.display='';document.getElementById('got').style.display='';};
document.getElementById('again').onclick=function(){st[cur.id]={b:0,d:Date.now()};save();queue.splice(Math.min(3,queue.length),0,cur);next();};
document.getElementById('got').onclick=function(){var b=box(cur);st[cur.id]={b:Math.min(3,(st[cur.id]?b:0)+1),d:Date.now()};save();next();};
document.getElementById('reset').onclick=function(){if(confirm('Forget all flashcard progress on this device?')){st={};save();build();next();}};
var subs=['All'];CARDS.forEach(function(c){if(subs.indexOf(c.s)<0)subs.push(c.s);});
var fl=document.getElementById('filters');subs.forEach(function(s){var b=document.createElement('button');b.className='fb'+(s===subj?' on':'');b.textContent=s;b.onclick=function(){subj=s;[].forEach.call(fl.children,function(x){x.classList.toggle('on',x===b);});build();next();};fl.appendChild(b);});
build();next();
'''.replace('__DATA__',json.dumps(data,ensure_ascii=False))
open(out+'/flashcards.html','w').write(page("Flashcards: IB study","index.html","Flashcards","The things to learn by heart from each study guide: formulas, definitions and exam rules. Five to ten minutes a day beats an hour once a week.",body,script))
print(len(cards),"cards")
