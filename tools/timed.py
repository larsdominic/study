# Timed practice pages (Saturday sets and mock papers).
# Run from the repo root: python3 tools/timed.py tools .
# Each page: crumb, intro, "Before you start", countdown timer(s), questions, "Mark it",
# score entry saved to localStorage 'ib-timed-YYYY-MM-DD' as {score, max, date, items}, Error log steps.
import sys, os
sys.path.insert(0, sys.argv[1]); from common import *
out = sys.argv[2]
os.makedirs(out + '/practice', exist_ok=True)

GDOC = lambda i: f'https://docs.google.com/document/d/{i}/edit'
# Drive IDs (from the Drive map, 2 Nov 2026)
M_PACK = DRIVE('1V3p4Y01JZwk-t3oGevgKyf5KzY8Kj1kf'); M_MS = DRIVE('1_hgaTyeVEmk8O4pm8H4E86H7Kp7VsBQZ')
M_FB = DRIVE('1yofdn_7Gu3pb2O5G6iHhrXVgRUQ1Qldz')
BT_Q = DRIVE('13LgqwVvlh2mMyONXTCfLCQFK6YHub8IF'); BT_A = DRIVE('1DPChl8qQvp6OeEuFGL0LN2AwUlt0BFOd')
WOC = DRIVE('19665yTxY6MkADedj2PvO-o0JKmE_yQeF')
STD_SOL = DRIVE('1x2mKoF4Nj0YWStNWQd6kwp6dzr8y8KoV'); R21_HO = DRIVE('1TAYUtJuBRPfFFDx83it0Xl14lGn-sx-4')
LP_TASK = GDOC('1cyauXBdiIVs5cH8AI-b4MTVe2_RpGEXIDfkCsrlo8Kk'); VTP = GDOC('1JcbnbbYzezkn4WONBbGmhMqPm7Fx7UE__bsN45fkxc4')
EE_FOLDER = 'https://drive.google.com/drive/folders/1IrGGlBxw5M16BDi4OFg60SbLcaYl1Zd0'
Q1 = DRIVE('183UXkkDOuRylI5n6vU2jLntfpblOAX7b'); FA1P1 = DRIVE('1PyUubsdFfMqX9EnS9ymPrr6jOizFpWcT')
FA1P2MS = DRIVE('1U5rjK07YmiJS4EeiWaUjRx3qX-hs6kCl'); BIO_MS = DRIVE('16z2TwiUy5JZkPv-Hqi4AD6R5H_6wYBiw')
NYT = 'https://www.nytimes.com/2020/10/01/learning/40-more-intriguing-photos-to-make-students-think.html'
MG = '../guides/2026-11-04-maths-aa-sl-1.2-1.6.html'; CG = '../guides/2026-11-03-chemistry-s1.1-s1.3.html'

EXTRA = r'''
  .timer{background:var(--card);border:1px solid var(--rule);border-top:6px solid var(--indigo);padding:16px;margin:16px 0;text-align:center}
  .timer .tlabel{font-weight:700;margin-bottom:2px}
  .timer .tdisp{font:700 4.2rem/1.1 "SF Mono",Menlo,Consolas,monospace;letter-spacing:.02em;margin:6px 0;color:var(--ink);font-variant-numeric:tabular-nums}
  .timer .tstat{color:var(--ink-soft);font-size:.95rem;min-height:1.5em}
  .timer .tbtns{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:10px}
  .timer button,.btn{font:inherit;font-weight:700;padding:10px 20px;border-radius:6px;border:1px solid var(--indigo);background:var(--indigo);color:#fff;cursor:pointer;min-width:96px}
  .timer button.sec,.btn.sec{background:#fff;color:var(--indigo)}
  .timer button:disabled{opacity:.4;cursor:default}
  .timer.low{border-top-color:var(--amber)} .timer.low .tdisp{color:var(--amber)}
  .timer.up{border-top-color:var(--red);background:var(--red-soft)} .timer.up .tdisp{color:var(--red)} .timer.up .tstat{color:var(--red);font-weight:700}
  details{background:var(--card);border:1px solid var(--rule);padding:10px 14px;margin:10px 0}
  summary{cursor:pointer;font-weight:600} details[open] summary{margin-bottom:8px}
  .score-t input{font:inherit;width:4.6em;padding:4px 6px;border:1px solid var(--grey);border-radius:4px}
  .score-t td{vertical-align:middle}
  .saved{font-weight:700;margin:6px 0 0}
  .miss{background:var(--red-soft);border-left:5px solid var(--red);padding:12px 16px;margin:14px 0}
  .ok{background:var(--green-soft);border-left:5px solid var(--green);padding:12px 16px;margin:14px 0}
  .card ul,.card ol{margin:4px 0;padding-left:22px} .card li{margin:4px 0}
  .muted{color:var(--ink-soft);font-size:.92rem}
  @media (max-width:600px){.timer .tdisp{font-size:3.4rem}}
'''

JS = r'''(function(){
  var PAGE="__PAGE__";
  var store=true; try{localStorage.setItem("_t","1");localStorage.removeItem("_t");}catch(e){store=false;}
  function load(k){ if(!store) return null; try{ return JSON.parse(localStorage.getItem(k)); }catch(e){ return null; } }
  function save(k,v){ if(!store) return; try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} }
  function pad(n){ return (n<10?"0":"")+n; }
  function fmt(ms){ var s=Math.ceil(Math.max(ms,0)/1000); return pad(Math.floor(s/60))+":"+pad(s%60); }
  var ac=null;
  function unlock(){ try{ if(!ac){ var C=window.AudioContext||window.webkitAudioContext; if(C) ac=new C(); } if(ac&&ac.state==="suspended") ac.resume(); }catch(e){} }
  function beep(){ if(!ac) return; try{ var t0=ac.currentTime+0.05; for(var i=0;i<3;i++){ var o=ac.createOscillator(), g=ac.createGain(); o.frequency.value=880; o.connect(g); g.connect(ac.destination); var t=t0+i*0.5; g.gain.setValueAtTime(0.0001,t); g.gain.exponentialRampToValueAtTime(0.3,t+0.02); g.gain.exponentialRampToValueAtTime(0.0001,t+0.35); o.start(t); o.stop(t+0.4); } }catch(e){} }
  var timers=[]; var baseTitle=document.title;
  // The timer stores the moment it was started (Date.now()), never a tick count,
  // so it stays correct when the phone screen sleeps or the page is reloaded.
  document.querySelectorAll(".timer").forEach(function(el){
    var t={el:el, dur:parseInt(el.getAttribute("data-sec"),10)*1000, key:"ib-timer-"+PAGE+"-"+el.getAttribute("data-id"),
      st:{start:null, used:0, alerted:false},
      disp:el.querySelector(".tdisp"), stat:el.querySelector(".tstat"),
      bStart:el.querySelector(".tstart"), bPause:el.querySelector(".tpause"), bReset:el.querySelector(".treset")};
    var s=load(t.key); if(s && typeof s.used==="number") t.st=s;
    t.bStart.addEventListener("click",function(){ unlock(); if(t.st.start) return; t.st.start=Date.now(); save(t.key,t.st); render(t); });
    t.bPause.addEventListener("click",function(){ if(!t.st.start) return; t.st.used+=Date.now()-t.st.start; t.st.start=null; save(t.key,t.st); render(t); });
    t.bReset.addEventListener("click",function(){ t.st={start:null, used:0, alerted:false}; save(t.key,t.st); render(t); });
    timers.push(t);
  });
  function used(t){ return t.st.used+(t.st.start?Date.now()-t.st.start:0); }
  function render(t){
    var r=t.dur-used(t), running=!!t.st.start;
    t.bStart.disabled=running; t.bPause.disabled=!running;
    t.bStart.textContent=(t.st.used>0&&!running&&r>0)?"Resume":"Start";
    if(r>0){
      t.el.classList.remove("up"); t.el.classList.toggle("low", r<=300000);
      t.disp.textContent=fmt(r);
      if(running){ var end=new Date(Date.now()+r); t.stat.textContent="Running. Ends at "+pad(end.getHours())+":"+pad(end.getMinutes())+"."; }
      else t.stat.textContent=t.st.used>0?"Paused.":"Ready. Press Start when you turn the paper over.";
    } else {
      t.el.classList.remove("low"); t.el.classList.add("up"); t.disp.textContent="00:00";
      t.stat.textContent="Time is up. Pens down."+(running?" Over by "+fmt(-r)+".":"");
      if(!t.st.alerted){ t.st.alerted=true; save(t.key,t.st); beep(); try{ if(navigator.vibrate) navigator.vibrate([400,200,400]); }catch(e){} }
    }
  }
  function all(){ var up=false; timers.forEach(function(t){ render(t); if(t.st.start && used(t)>=t.dur) up=true; }); document.title=(up?"Time is up | ":"")+baseTitle; }
  all(); setInterval(all,250);
  document.addEventListener("visibilitychange",all); window.addEventListener("focus",all); window.addEventListener("pageshow",all);

  // score entry: one row per item; total saved as {score, max, date, items}
  var KEY="ib-timed-"+PAGE, rows=document.querySelectorAll(".score-t tr[data-item]"), out=document.getElementById("saved");
  function maxOf(r){ var m=r.querySelector(".mx"); return parseFloat(m.tagName==="INPUT"?m.value:m.getAttribute("data-max")); }
  function today(){ var d=new Date(); return d.getFullYear()+"-"+pad(d.getMonth()+1)+"-"+pad(d.getDate()); }
  function show(rec){ out.textContent=rec?("Saved on this device: "+rec.score+" / "+rec.max+" ("+Math.round(100*rec.score/rec.max)+"%), "+rec.date+"."):"Nothing saved yet. Rows you leave empty do not count."; }
  function saveScore(){
    var items={}, sc=0, mx=0, any=false;
    rows.forEach(function(r){ var v=r.querySelector(".sc").value, m=maxOf(r);
      if(v!=="" && !isNaN(parseFloat(v)) && m>0){ var x=Math.min(Math.max(parseFloat(v),0),m); if(x!==parseFloat(v)) r.querySelector(".sc").value=x; items[r.getAttribute("data-item")]={s:x,m:m}; sc+=x; mx+=m; any=true; } });
    if(!any){ if(store){ try{ localStorage.removeItem(KEY); }catch(e){} } show(null); return; }
    var rec={score:sc, max:mx, date:today(), items:items}; save(KEY,rec); show(rec);
  }
  var rec=load(KEY);
  if(rec && rec.items){ rows.forEach(function(r){ var it=rec.items[r.getAttribute("data-item")]; if(it){ r.querySelector(".sc").value=it.s; var m=r.querySelector(".mx"); if(m.tagName==="INPUT") m.value=it.m; } }); }
  show(rec && rec.items ? rec : null);
  rows.forEach(function(r){ r.querySelectorAll("input").forEach(function(i){ i.addEventListener("change",saveScore); }); });
  document.getElementById("savebtn").addEventListener("click",saveScore);
  if(!store) out.textContent="This browser is not letting the page save (private mode?). Write your score on paper.";
})();'''

def timer(tid, label, sec, note=''):
    m, s = divmod(sec, 60)
    return (f'<div class="timer" data-id="{tid}" data-sec="{sec}"><div class="tlabel">{label}</div>'
            f'<div class="tdisp" aria-live="off">{m:02d}:{s:02d}</div><div class="tstat">Ready.</div>'
            f'<div class="tbtns"><button class="tstart">Start</button><button class="tpause sec">Pause</button><button class="treset sec">Reset</button></div></div>'
            + (f'<p class="muted">{note}</p>' if note else ''))

def score_table(rows):
    tr = ''
    for iid, label, mx, editable in rows:
        mcell = (f'<input class="mx" type="number" min="1" step="1" value="{mx}" aria-label="maximum marks for {label}">' if editable
                 else f'<span class="mx" data-max="{mx}">{mx}</span>')
        tr += f'\n<tr data-item="{iid}"><td>{label}</td><td><input class="sc" type="number" min="0" max="{mx}" step="1" inputmode="numeric" aria-label="marks gained, {label}"></td><td>{mcell}</td></tr>'
    return (f'<div class="tablewrap"><table class="score-t"><tr><th>Item</th><th>Marks gained</th><th>Out of</th></tr>{tr}</table></div>'
            '<p><button class="btn" id="savebtn">Save score</button></p><p class="saved" id="saved"></p>')

def errlog(extra=''):
    return f'''<div class="step"><div class="bh"><b>Error log</b><span>about 10 min</span></div><ol>
<li>Open the <a href="{SHEET}">study sheet</a>, <b>Error log</b> tab.</li>
<li>Write one row for every mark you lost: the date, the subject, the question (for example "{{q}}"), what went wrong, and the rule that fixes it.</li>
<li>Say what kind of mistake it was: <b>did not know it</b> (go back to the guide or handout), <b>wrong method</b>, <b>careless slip</b> (copying, signs, units) or <b>ran out of time</b>. Four careless slips in one set is a pattern worth a rule of its own.</li>
<li>Timing: write down which question you were on when the timer ended. If you finished in extra time, how many minutes did it take? Speed problems and knowledge problems need different fixes.</li>
{extra}</ol></div>'''

def build(fname, title, h1, intro, body, page_date):
    html = page(title, '../index.html', h1, intro, body, JS.replace('__PAGE__', page_date), crumb_label='All days')
    html = html.replace('</style>', EXTRA + '</style>', 1)
    assert '\u2014' not in html, fname
    open(out + '/practice/' + fname, 'w').write(html)
    print('wrote practice/' + fname)

# ---------------------------------------------------------------- 1. Maths, Sat 7 Nov
u = lambda n: f'u<sub>{n}</sub>'; S = lambda n: f'S<sub>{n}</sub>'
body1 = f'''
<h2>Before you start</h2>
<div class="card"><ul>
<li><b>Paper and pen</b>, plus a pencil and ruler. Write on paper, not on screen.</li>
<li><b>No calculator.</b> Put it in another room. Maths AA Paper 1 is the no-calculator paper, and every question below can be done by hand.</li>
<li><b>Formula booklet: yes.</b> You get it in every IB maths exam. Open the <a href="{M_FB}">formula booklet</a> at the sequences page ({u('n')}, {S('n')} and {S('∞')} for arithmetic and geometric sequences are all there).</li>
<li><b>The question paper:</b> the <a href="{M_PACK}">sequences and series practice pack</a> (on screen or printed). Do <b>not</b> open the mark scheme until the timer has ended.</li>
<li><b>How long:</b> 40 minutes on the timer, then about 15 minutes to mark and 10 minutes for the Error log. About 65 minutes in all.</li>
<li>Phone on silent. You can keep this page open on the phone: the timer works offline and stays correct if the screen locks (it counts from the time you pressed Start).</li>
</ul></div>

<h2>Timer</h2>
{timer('maths', 'Maths sequences, no calculator', 2400, 'Why 40 minutes: Paper 1 gives 90 minutes for 80 marks, about 67.5 seconds a mark. 35 marks × 67.5 s = 2362.5 s, which is 39 min 22.5 s, rounded up to 40 minutes.')}

<h2>The questions</h2>
<p>All from the <a href="{M_PACK}">practice pack</a>. Work in this order. If you are stuck for more than two minutes, leave a gap and move on: that is exam technique, not giving up.</p>
<div class="tablewrap"><table>
<tr><th>Pack question</th><th>What it is about</th><th>Marks</th></tr>
<tr><td>4</td><td>Find {u(1)} and d from {u(7)} = 6 and {u(6)} + {u(12)} = 24</td><td>5</td></tr>
<tr><td>11</td><td>{u(10)} = 16 and {S(25)} = 100: find k with {u('k')} = 0</td><td>6</td></tr>
<tr><td>16</td><td><span class="nw">{S('n')} = pn<sup>2</sup> − qn</span> with {S(5)} = 65 and {S(6)} = 96: find p, q and {u(6)}</td><td>7</td></tr>
<tr><td>20</td><td>{u(1)} = 0.6, {u(4)} = 0.15, then a probability table</td><td>6</td></tr>
<tr><td>31, parts (c) to (g) only</td><td>Fuel pumped into a tank each hour (arithmetic sequence)</td><td>11</td></tr>
<tr><th colspan="2">Total</th><th>35</th></tr></table></div>
<div class="tip"><b>Read this first.</b> Question 20 (b) uses a probability table. The only fact you need is that the probabilities in the table add up to 1 (you meet this properly in Topic 4). In question 31, skip parts (a) and (b): they need a calculator. Start at (c) and use the volume 624&nbsp;000 m<sup>3</sup> that part (b) gives you.</div>
<p class="muted">Why these questions: Wednesday's <a href="{MG}">sequences guide</a> already uses most of the pack. Of the questions it does not use, only 20 and 31 (c) to (g) work without a calculator: 6, 29 and 31 (a) to (b) need a GDC, and 25 needs logarithms, which you have not covered yet. So the set also repeats three of Wednesday's no-calculator homework questions (4, 11 and 16). Do them again from a blank page without looking at Wednesday's work. Getting them right a second time, and faster, is the point.</p>
<p>Write every step. Most marks are for method (M1), so a correct method with a slip in the arithmetic still scores.</p>

<h2>Mark it</h2>
<div class="step"><div class="bh"><b>Marking</b><span>about 15 min</span></div><ol>
<li>When the timer ends, draw a line under your work. If you want to finish a question, carry on in a different colour: anything after the line scores 0 in an exam, but it shows you what you know.</li>
<li>Open the <a href="{M_MS}">mark scheme</a> at questions 4, 11, 16, 20 and 31 (c) to (g). Go line by line.</li>
<li>How to read it: <b>M1</b> is a method mark, <b>A1</b> a mark for a correct answer or line, <b>R1</b> a mark for a reason (31 (g) needs the sentence comparing the total with 624&nbsp;000 m<sup>3</sup>). Marks in brackets, like <b>(M1)</b> or <b>(A1)</b>, can be given even if that line is missing, when a later correct answer shows you must have done it. <b>AG</b> means "answer given": no extra mark, you only have to reach it. <b>ft</b> (follow through) means you keep later marks if you used an earlier wrong answer correctly.</li>
<li>In question 20 (b) the table entries are {u('n')} divided by k (the PDF shows them as fractions).</li>
<li>Add up your marks per question and enter them below.</li></ol></div>
<details><summary>Quick check: final answers (worked out again by hand and with Python)</summary>
<ul>
<li>4: {u(1)} = −12, d = 3</li>
<li>11: d = −4, {u(1)} = 52, k = 14</li>
<li>16: p = 3, q = 2, {u(6)} = 31</li>
<li>20: d = −0.15, k = 1.5</li>
<li>31: (c) d = −1800; (d) {u(13)} = 23&nbsp;400 m<sup>3</sup>; (e) n = 26, so the pump worked for 25 hours; (f) {S(8)} = 309&nbsp;600 m<sup>3</sup>; (g) {S(25)} = 585&nbsp;000 m<sup>3</sup>, which is less than 624&nbsp;000 m<sup>3</sup>, so the tank is never full.</li>
</ul><p class="muted">Use the mark scheme for the marks; this list only tells you whether the final answer was right.</p></details>

<h2>Your score</h2>
{score_table([('q4','Question 4',5,False),('q11','Question 11',6,False),('q16','Question 16',7,False),('q20','Question 20',6,False),('q31','Question 31 (c) to (g)',11,False)])}

<h2>Error log</h2>
{errlog('<li>If you lost marks on 4, 11 or 16 again, write "repeat" in the row. A mistake made twice is a habit: turn its rule into a flashcard.</li>').replace('{q}','Seq pack 16 (a)')}
<p>Also on the study site: the <a href="{MG}">sequences guide</a> for anything you could not do, the <a href="../flashcards.html">flashcards</a>, <a href="../exam-maths-aa-sl.html">exam technique for Maths AA</a> and your <a href="../progress.html">progress page</a>.</p>
'''
build('2026-11-07-timed-maths-sequences.html', 'Timed set: Maths sequences, no calculator (Sat 7 Nov 2026)',
      'Timed set: Maths sequences (no calculator)',
      'Saturday 7 November 2026. 40 minutes under exam conditions: five questions (35 marks) from your sequences pack, no calculator, then mark them with the mark scheme and log your mistakes.',
      body1, '2026-11-07')

# ---------------------------------------------------------------- 2. Chemistry, Sat 14 Nov
WOC_DATA = [(1, 24.53, 25.55, 25.21), (2, 25.10, 26.61, 26.10), (3, 24.87, 26.91, 26.22), (4, 25.34, 27.83, 26.99), (5, 24.96, 27.97, 26.95)]
Ar = {'H': 1.01, 'O': 16.00, 'S': 32.07, 'Cu': 63.55}
MC = round(Ar['Cu'] + Ar['S'] + 4 * Ar['O'], 2); MW = round(2 * Ar['H'] + Ar['O'], 2)
proc = []
for t, c, h, a in WOC_DATA:
    mh = round(h - c, 2); ma = round(a - c, 2); mw = round(h - a, 2)
    na = ma / MC; nw = mw / MW; proc.append((t, mh, ma, mw, na, nw, nw / na, 100 * 0.02 / mw + 100 * 0.02 / ma))
mean_x = sum(p[6] for p in proc) / 5
assert (MC, MW) == (159.62, 18.02) and abs(mean_x - 4.5047) < 1e-3
raw_rows = ''.join(f'<tr><td>{t}</td><td>{c:.2f}</td><td>{h:.2f}</td><td>{a:.2f}</td></tr>' for t, c, h, a in WOC_DATA)
sig = lambda v: f'{v:.3g}'
key_rows = ''.join(f'<tr><td>{t}</td><td>{mh:.2f}</td><td>{ma:.2f}</td><td>{mw:.2f}</td><td>{sig(na)}</td><td>{sig(nw)}</td><td>{x:.2f}</td><td>{ux:.1f}%</td></tr>' for t, mh, ma, mw, na, nw, x, ux in proc)
CU = 'CuSO<sub>4</sub>'; HY = 'CuSO<sub>4</sub>·5H<sub>2</sub>O'; XH = 'CuSO<sub>4</sub>·xH<sub>2</sub>O'; W2 = 'H<sub>2</sub>O'
body2 = f'''
<h2>Before you start</h2>
<div class="card"><ul>
<li><b>Paper and pen</b>, a ruler, and one sheet of graph or squared paper (for the graph in set B).</li>
<li><b>Calculator: yes.</b> Both IB chemistry papers allow one.</li>
<li><b>Data booklet:</b> use your school copy of the IB chemistry data booklet (it is not in the Drive folder). If you do not have it, these are the relative atomic masses you need today, to two decimal places as in the booklet: H 1.01, C 12.01, O 16.00, S 32.07, Ca 40.08, Cu 63.55.</li>
<li><b>Open:</b> the <a href="{BT_Q}">back titration concept check</a> and the <a href="{WOC}">water of crystallisation worksheet</a>. Keep the <a href="{BT_A}">answers</a> closed until the first timer ends.</li>
<li><b>How long:</b> set A 18 min 20 s, set B 45 min, plus about 25 minutes for marking and the Error log. About 1.5 hours with a short break. The English and EE tasks at the bottom are not timed.</li>
<li>The timers work offline and keep the right time if the phone screen locks.</li>
</ul></div>
<p class="muted">Revise first if you need to: R2.1 <a href="{R21_HO}">stoichiometry handout</a> and the <a href="{STD_SOL}">standard solutions slides</a> (titration calculations).</p>

<h2>Set A: back titration concept check</h2>
{timer('chem-bt', 'Set A: back titration, 11 marks', 1100, 'Why 18 min 20 s: HL Paper 2 gives 150 minutes for 90 marks, which is 100 seconds a mark. 11 marks × 100 s = 1100 s.')}
<p>Open the <a href="{BT_Q}">back titration concept check</a> and answer every part, (a) to (g), 11 marks. It is one question about eggshell: excess hydrochloric acid reacts with the calcium carbonate, and the acid left over is titrated with sodium hydroxide. Show every step with units; the marks are for the working.</p>
<div class="tip"><b>The idea in one line.</b> acid reacted with the solid = acid added − acid left over (found by the titration). Then use the equation ratio to get from moles of HCl to moles of CaCO<sub>3</sub>.</div>

<h3>Mark set A</h3>
<div class="step"><div class="bh"><b>Marking</b><span>about 8 min</span></div><ol>
<li>Open the <a href="{BT_A}">answers</a>. They are written like a mark scheme: [1] next to each mark point, and the notes in italics say what else is accepted.</li>
<li>Note the rules it uses: forgetting to divide cm<sup>3</sup> by 1000 is penalised only once in (a) and (b); in (d) one mark is for the right formulas and one for balancing; in (f) the percentage can be anything from 79.8% to 81.5%.</li>
<li>I recalculated every number in the answers and they are right: 5.44 × 10<sup>−3</sup>, 2.38 × 10<sup>−3</sup>, 3.06 × 10<sup>−3</sup> and 1.53 × 10<sup>−3</sup> mol; 0.153 g; 81.4% or 81.5% (depending on whether you round the mass first).</li></ol></div>

<h2>Set B: water of crystallisation worksheet</h2>
{timer('chem-woc', 'Set B: water of crystallisation, 45 min', 2700, 'This one is not an exam paper, so it has no marks to convert. 45 minutes: about 25 for the write-up sections and 20 for the calculations.')}
<p>The <a href="{WOC}">worksheet</a> is not a question sheet: it is the write-up template for the practical where you heat hydrated copper(II) sulfate, {XH}, to find x. It has headings (research question, background, method, risk assessment, results tables, graph, conclusion) but no numbers and no answer sheet. So the timed task is:</p>
<ol>
<li><b>About 25 min:</b> write the <b>Background</b>, the <b>Method</b> (with variables, how you know dehydration is complete, repeats) and the <b>risk assessment</b> table, in note form, following the prompts in the worksheet.</li>
<li><b>About 20 min:</b> process the practice data below with <b>Method A</b> (x for each trial, then a mean) and <b>Method B</b> (a graph of moles of water against moles of {CU}; the gradient is x). Then answer the research question: how close is your x to the accepted value of 5, and why is it different?</li>
</ol>
<p>If you did this practical in class, use your own results for part 2 instead.</p>
<h3>Practice data (made up for this exercise, not real results)</h3>
<div class="tablewrap"><table>
<tr><th>Trial</th><th>Crucible + lid / g ± 0.01</th><th>Crucible + lid + hydrated salt / g ± 0.01</th><th>Crucible + lid + residue after heating / g ± 0.01</th></tr>
{raw_rows}</table></div>
<p class="muted">Two small slips in the worksheet, so they do not confuse you: the "Choose your data-analysis approach" box says "hydrated cobalt(II) chloride", but everything else in the worksheet is about copper(II) sulfate; and the results table row "Mass of hydrated CuSO4.H2O" means {XH}.</p>

<h3>Mark set B</h3>
<p>There is no answer sheet in the folder, so here is my own worked key. Every number was calculated in Python and checked by hand. Mark yourself with the 10-point checklist at the end of the key.</p>
<details><summary>Worked answer key: water of crystallisation (open after the timer)</summary>
<p><b>Values used:</b> relative atomic masses to two decimal places as in the IB data booklet: Cu 63.55, S 32.07, O 16.00, H 1.01.</p>
<ul>
<li><span class="nw">M({CU})</span> = <span class="nw">63.55 + 32.07</span> <span class="nw">+ 4 × 16.00</span> = <span class="nw">159.62 g mol<sup>−1</sup></span></li>
<li><span class="nw">M({W2})</span> = <span class="nw">2 × 1.01 + 16.00</span> = <span class="nw">18.02 g mol<sup>−1</sup></span></li>
<li>If x = 5: <span class="nw">M({HY})</span> = <span class="nw">159.62 + 5 × 18.02</span> = <span class="nw">249.72 g mol<sup>−1</sup></span>, so water is <span class="nw">90.10 ÷ 249.72 = 36.08%</span> of the mass.</li>
<li>Equation: <span class="nw">{HY}(s) →</span> <span class="nw">{CU}(s) + 5{W2}(g)</span>. Blue crystals turn to a white powder.</li>
</ul>
<p><b>Method A, trial 1 step by step:</b></p>
<ol>
<li>mass of hydrated salt = 25.55 − 24.53 = 1.02 g</li>
<li>mass of anhydrous {CU} = 25.21 − 24.53 = 0.68 g</li>
<li>mass of water lost = 25.55 − 25.21 = 0.34 g</li>
<li>n({CU}) = 0.68 ÷ 159.62 = 0.00426 mol; n({W2}) = 0.34 ÷ 18.02 = 0.0189 mol</li>
<li>x = n({W2}) ÷ n({CU}) = 0.0189 ÷ 0.00426 = 4.43 (from the unrounded moles; dividing the rounded ones gives 4.44, also fine)</li>
</ol>
<div class="tablewrap"><table>
<tr><th>Trial</th><th>Hydrated / g</th><th>Anhydrous / g</th><th>Water / g</th><th>n({CU}) / mol</th><th>n({W2}) / mol</th><th>x</th><th>% uncertainty in x</th></tr>
{key_rows}</table></div>
<ul>
<li><b>Mean x = 4.50</b> (4.51 if you average the rounded values; either is fine). Two or three significant figures are justified, because the smallest masses have only two.</li>
<li><b>Uncertainty:</b> each mass is a difference of two readings, so ±0.02 g. % uncertainty in x = % uncertainty in the water mass + % uncertainty in the anhydrous mass. Trial 1: <span class="nw">0.02 ÷ 0.34 = 5.9%</span> plus <span class="nw">0.02 ÷ 0.68 = 2.9%</span>, so 8.8%. The bigger samples (trial 5, 3.0%) are more precise.</li>
<li><b>Percentage error</b> of the mean: <span class="nw">(4.50 − 5) ÷ 5 × 100 = −9.9%</span>, about −10%.</li>
<li><b>Method B:</b> plot n({W2}) (y) against n({CU}) (x). The best-fit line has a gradient of about 4.6 (4.58 by least squares) and passes very close to the origin (intercept −0.0005 mol). Gradient = moles of water per mole of {CU} = x. Accept 4.4 to 4.7 from a hand-drawn line. (The worksheet mentions a "mass fraction": if you plot mass of water against mass of {CU} instead, the gradient is 0.517, and x = 0.517 × 159.62 ÷ 18.02 = 4.58, the same answer.)</li>
<li><b>Conclusion:</b> x ≈ 4.5, about 10% below the literature value of 5. The error (10%) is larger than the random uncertainty (3% to 9%), so random error cannot explain it: there is a systematic error.</li>
<li><b>Most likely cause:</b> incomplete dehydration. Water left in the residue makes the residue too heavy and the water lost too small, so x comes out too low. Fix: heat, cool and weigh again until two masses agree within 0.01 g (heating to constant mass).</li>
<li><b>Other errors and their direction:</b> the anhydrous salt absorbing water from the air while it cools makes x too low (cool it in a desiccator, with the lid on); solid spitting out of the crucible makes x too high (lid partly on, heat gently at first); heating far too strongly can decompose {CU} further (the residue goes grey or black), which also makes x too high.</li>
</ul>
<p><b>Background should cover:</b> what water of crystallisation is; the formula {XH} and that x is a whole number of water molecules per formula unit; the dehydration equation and colour change; the assumption that all mass lost is water and the residue is pure anhydrous {CU}; how x = n({W2}) ÷ n({CU}).</p>
<p><b>Method should cover:</b> independent variable (initial mass of hydrated salt, for Method B), dependent variable (mass lost), controls (same balance, same crucible and lid, same heating method); weigh the empty crucible and lid, add salt, weigh, heat gently then strongly, cool in a desiccator, weigh, repeat to constant mass; at least five trials. Risk table: copper(II) sulfate is harmful if swallowed and irritates eyes and skin (goggles, wash hands); hot crucible (tongs, let it cool); copper compounds are toxic to aquatic life, so collect the residue for disposal and do not pour it down the sink.</p>
<p><b>Self-check, 1 point each (10 in total):</b> (1) balanced equation; (2) both molar masses right; (3) masses of water and anhydrous salt for all five trials; (4) moles for all five trials; (5) x for each trial between 4.4 and 4.6; (6) a mean of about 4.5 with sensible significant figures; (7) a graph with labelled axes and a gradient of 4.4 to 4.7; (8) percentage error about −10%; (9) incomplete dehydration named as the main cause, with the direction (x too low); (10) one realistic improvement (heat to constant mass, or cool in a desiccator).</p>
</details>

<h2>Your score</h2>
{score_table([('backtitration','Set A: back titration concept check',11,False),('woc','Set B: water of crystallisation (self-check points)',10,False)])}

<h2>Error log</h2>
{errlog('<li>For set B, log any step of the calculation you could not do without the key, and any section of the write-up you left empty.</li>').replace('{q}','Back titration (e)')}

<h2>Not timed: English learner portfolio entry</h2>
<div class="step"><div class="bh"><b>About 35 min</b><span>100 Photographs That Changed the World</span></div><ol>
<li>Open the <a href="{LP_TASK}">learner portfolio entry instructions</a>.</li>
<li>Put in the entry: the photograph your group worked on (image, or a description if you cannot attach it), your original caption, the global issue with a one-sentence explanation of the connection, and the real historical caption.</li>
<li>Write the reflection, 150 to 250 words: what changed between your caption and the real one, and what that shows about how word choice and framing shape meaning; which global issue field it fits (culture, identity and community; politics, power and justice; art, creativity and imagination; science, technology and environment; beliefs, values and education); and whether it could help your Individual Oral.</li>
<li>Tag it: Non-literary texts, Global Issues, Framing &amp; Perspective. Keep the focus on language choices and meaning, not a summary of the lesson.</li>
<li>If you missed the lesson where groups chose photographs, ask the English teacher which photograph to use.</li></ol></div>

<h2>Not timed: Extended Essay, subject and three research questions</h2>
<div class="step"><div class="bh"><b>About 30 min</b><span>EE planning</span></div><ol>
<li>Choose the EE subject. Most students pick a subject they take and enjoy, ideally one where they already know how to find sources or collect data. Write two sentences on why.</li>
<li>Write three candidate research questions in that subject. A good one is a real question (not "describe ..."), narrow enough for 4,000 words, and answerable with sources or data you can actually get.</li>
<li>Test each: Is it focused? Can it be argued, with more than one possible answer? Can you name two sources or a data method for it today? Is it safe and ethical? Cross out or rewrite any that fail.</li>
<li>Save the three questions in your <a href="{EE_FOLDER}">EE folder</a> on Drive (it is empty now). You will agree one with your supervisor on Saturday 21 November.</li></ol></div>
<p>Also on the study site: the <a href="{CG}">chemistry guide for S1.1 to S1.3</a>, <a href="../flashcards.html">flashcards</a>, <a href="../exam-chemistry-hl.html">exam technique for Chemistry HL</a> and your <a href="../progress.html">progress page</a>.</p>
'''
build('2026-11-14-timed-chemistry-titration.html', 'Timed set: Chemistry titration (Sat 14 Nov 2026)',
      'Timed set: Chemistry titration and back titration',
      'Saturday 14 November 2026. Two timed chemistry sets (a back titration question and the water of crystallisation worksheet with practice data), each marked straight afterwards. Then two untimed tasks: an English learner portfolio entry and choosing your Extended Essay subject.',
      body2, '2026-11-14')

# ---------------------------------------------------------------- 3. Mock papers, Sat 21 Nov
FA1_KEY = [('1', 'D', 'M(C<sub>60</sub>) = 60 × 12.01 = 720.6 g mol<sup>−1</sup>; 720.6 ÷ (6.0 × 10<sup>23</sup>) = 1.2 × 10<sup>−21</sup> g'),
 ('2', 'D', '10 cm<sup>3</sup> of A reacted with 20 cm<sup>3</sup> of B to give 10 cm<sup>3</sup> of product: A + 2B → AB<sub>2</sub>'),
 ('3', 'A', 'pV = nRT is constant at fixed T and n: a horizontal line'),
 ('4', 'A', '2s paired; the two 2p electrons in separate orbitals with parallel spins (Hund)'),
 ('5', 'C', 'big jump after the 3rd electron: 3 outer electrons, Al'),
 ('6', 'B', 'molecular formula = actual number of each atom (A is the empirical formula)'),
 ('7', 'A', 'masses of Zn and oxide give % composition and empirical formula; zinc oxide is ionic (a lattice, not molecules), so it has no molecular formula'),
 ('8', 'A', 'M = mRT ÷ pV with p in kPa, V in dm<sup>3</sup> (0.220) and T in K (290)'),
 ('9', 'C', '2n<sup>2</sup> = 2 × 16 = 32'),
 ('10', 'B', 'S has one paired 3p orbital, and the repulsion makes it easier to remove an electron'),
 ('11', 'A', 'period number = highest occupied level n, and level n has n sub-levels; outer electrons come from the group'),
 ('12', 'D', 'all three are single-phase mixtures (pentane and hexane mix, ethanol and water mix)'),
 ('13', 'B', 'emission: electrons fall to lower levels and release photons'),
 ('14', 'B', '2.67 ÷ 267.21 = 9.99 × 10<sup>−3</sup> mol; × 223.20 = 2.23 g of PbO'),
 ('15', 'A', 'n(HCl) = 0.0100 mol; 0.02 mol Zn would need 0.04 mol HCl, so HCl is limiting; H<sub>2</sub> = 0.0100 ÷ 2 = 0.005 mol'),
 ('16', 'B', 'N 5.6 g ÷ 14.01 = 0.40; O 3.2 ÷ 16.00 = 0.20; ratio 2 : 1, N<sub>2</sub>O'),
 ('17', 'C', '71x + 69(1 − x) = 69.72 gives x = 0.36, so <sup>69</sup>Ga is 64%, about 60%'),
 ('18', 'A', 'big jump after the 3rd electron: group 13'),
 ('19', 'C', 'the dumbbell (figure-of-eight) shape'),
 ('20', 'B', '2− means two electrons gained')]
fa1rows = ''.join(f'<tr><td>{q}</td><td><b>{a}</b></td><td>{w}</td></tr>' for q, a, w in FA1_KEY)
body3 = f'''
<p style="margin-top:22px">Up to five papers today (four if the Formative Assessment 1 Paper 2 questions do not arrive). Do not sit them all in one go. A plan that works: <b>morning</b> chemistry (Quiz 1, a 10 minute break, Formative Assessment 1 Paper 1, and Paper 2 after another break if you have it), marking each straight away; <b>afternoon</b> Biology, then the English analysis. Each paper has its own timer below; pause it only for a real interruption.</p>

<h2>Before you start</h2>
<div class="card"><ul>
<li><b>Paper and pen</b>, pencil, ruler. Answer on paper.</li>
<li><b>Calculator: yes</b> for chemistry and biology. Not needed for English.</li>
<li><b>Chemistry data booklet:</b> required for the chemistry papers (the Formative Assessment 1 front page says so). It is not in the Drive folder, so use your school copy.</li>
<li><b>Files:</b> <a href="{Q1}">Quiz 1 Paper 2 HL</a>, <a href="{FA1P1}">Formative Assessment 1 Paper 1A and 1B HL</a>, <a href="{BIO_MS}">Biology Grade 11 combined paper HL</a> (the original, not the "(duplicate)" copy), and for English the <a href="{NYT}">New York Times photo collection</a> linked in your <a href="{VTP}">visual thinking assignment</a>.</li>
<li><b>Sticky notes or strips of paper</b> to cover answers (see "What is missing" below), or ask someone to do it before you start.</li>
<li><b>How long:</b> about 3 hours of papers (nearly 4 with Formative Assessment 1 Paper 2), plus about an hour of marking and Error log over the day.</li>
<li>The timers work offline and keep the right time if the phone screen locks.</li>
</ul></div>

<h2>What is missing, and what to do about it</h2>
<div class="ok"><b>Quiz 1 Paper 2 HL: complete.</b> The questions are on pages 1 to 3 and the mark scheme is on page 4 of the same file. Stop before page 4. Two oddities: question 2 (b) (ii) says "in 5(e)" and the mark scheme labels question 2 as e, f(i), f(ii). The question was taken from an old IB paper where it was question 5: read "5(e)" as your answer to 2 (a), and e, f(i), f(ii) as 2 (a), (b)(i), (b)(ii).</div>
<div class="miss"><b>Formative Assessment 1 Paper 1A and 1B HL: no mark scheme in the folder, and the copy is not clean.</b> The Drive copy already has handwritten working and circled answers on it. What to do: on Monday 16 November ask your chemistry teacher for a clean copy and the mark scheme. If you get no clean copy, print the annotated one and cover the handwriting and highlights with sticky notes before you start, or simply sit it as a re-sit and note in the Error log that you had seen the answers. To mark it without the official scheme, use my key below: I worked out all 20 Paper 1A answers myself and they match the circled answers on the copy. For Paper 1B I give the points I would expect, but the school mark scheme decides.</div>
<div class="miss"><b>Formative Assessment 1 Paper 2 HL: the mark scheme is there, the question paper is not.</b> The file is a set of mark scheme extracts from IB past papers (May 2021 and May 2022 HL Paper 2). Ask your chemistry teacher for the question paper on Monday 16 November. <b>Do not read the mark scheme before you have the questions</b>: that would spoil the paper. No questions by Saturday? Skip this paper and leave its score row empty (it then does not count).</div>
<div class="miss"><b>Biology Grade 11 combined paper HL: the only file is the mark scheme, but it contains every question.</b> Each question (with its diagrams) is followed straight away by a grey "Markscheme" box with the answer. Before you start, print it and cover every grey box with a sticky note, or on screen scroll with a sheet of paper held over everything below the question you are on. No time is printed on it.</div>

<h2>1. Chemistry Quiz 1 Paper 2 HL (12 marks)</h2>
{timer('chem-quiz1', 'Chemistry Quiz 1 Paper 2 HL', 1200, 'The paper prints no time. At HL Paper 2 pace (150 minutes for 90 marks, 100 seconds a mark): 12 marks = 20 minutes.')}
<p><a href="{Q1}">Quiz 1 Paper 2 HL</a>: question 1 (chlorine: electron configuration, radius, mass spectrum, 7 marks) and question 2 (titration of vinegar with KOH and a systematic error, 5 marks).</p>
<div class="step"><div class="bh"><b>Mark it</b><span>about 10 min</span></div><ol>
<li>Turn to page 4 of the same file: that is the mark scheme. A ✓ is one mark. Words in «» are not needed for the mark; OR gives alternatives.</li>
<li>Check 1 (a)(i) carefully: the full configuration is required, a condensed one like [Ne] 3s<sup>2</sup> 3p<sup>5</sup> gets 0.</li>
<li>Question 2 (a): 0.02075 dm<sup>3</sup> × 1.00 = 0.0208 mol, ÷ 0.02500 dm<sup>3</sup> = 0.830 mol dm<sup>−3</sup> (I checked this). Two marks for the right final answer.</li></ol></div>

<h2>2. Formative Assessment 1 Paper 1A and 1B HL (30 marks)</h2>
{timer('chem-fa1-p1', 'FA1 Paper 1A and 1B HL', 3000, 'Time from the front page: 50 minutes for 30 marks (20 multiple choice, 10 written). Calculator and data booklet required.')}
<p><a href="{FA1P1}">Formative Assessment 1 Paper 1A and 1B HL</a> (S1.1 to S1.5; questions 14 and 15, reacting masses and the limiting reactant, are R2.1). Paper 1A: 20 multiple-choice questions. Paper 1B: one data-based question about separating sand, salt and iron (10 marks).</p>
<div class="step"><div class="bh"><b>Mark it</b><span>about 10 min</span></div><ol>
<li>If your teacher gave you the mark scheme, use that. Otherwise use the key below.</li>
<li>Paper 1A: one mark each. Paper 1B: give yourself a mark only for a point that matches one in the key or says the same thing in other words.</li>
<li>Ask your teacher about any 1B answer you are unsure of.</li></ol></div>
<details><summary>Answer key Paper 1A (my own, checked; not the school mark scheme)</summary>
<div class="tablewrap"><table><tr><th>Q</th><th>Answer</th><th>Why</th></tr>{fa1rows}</table></div>
<p class="muted">Relative atomic masses used: C 12.01, O 16.00, N 14.01, Pb 207.20. Question 11 is the least clear-cut: A is the intended answer, because a period-n element fills level n, which has n sub-levels.</p></details>
<details><summary>Expected points Paper 1B (my own; the school mark scheme decides)</summary>
<ul>
<li>(a) [4] One mark per step: pull out the iron filings with a magnet; add water and stir until the salt dissolves; filter, so the sand stays on the filter paper (rinse and dry it); evaporate or crystallise the filtrate to get the salt.</li>
<li>(b) [1] iron <span class="nw">2.17 ÷ 5.62 × 100 = 38.6%</span>; sand <span class="nw">1.98 ÷ 5.62 × 100 = 35.2%</span>.</li>
<li>(c) [2] Error: the separated solids were still wet, or carried other material (for example sand stuck to the iron, or the iron oxidised), so 2.17 + 1.98 + 1.80 = 5.95 g is more than 5.62 g. Reduce it: dry each solid to constant mass (heat, weigh, repeat until the mass stops changing) before weighing.</li>
<li>(d) [1] The hypothesis judged by how much space the iron took up, but iron is much denser than sand and salt, so a small volume of iron has a large mass.</li>
<li>(e) [2] Fractional distillation; the two liquids have different boiling points (methanol about 65 °C, butan-1-ol about 118 °C).</li>
</ul></details>

<h2>3. Formative Assessment 1 Paper 2 HL (only if you have the questions)</h2>
{timer('chem-fa1-p2', 'FA1 Paper 2 HL', 3000, 'The mark scheme totals 29 marks (counted from its Total column; one row shows no total and is counted as 1). At HL Paper 2 pace that is 48 min 20 s; 50 minutes matches the Paper 1 of the same assessment.')}
<div class="step"><div class="bh"><b>Mark it</b><span>about 10 min</span></div><ol>
<li>Use the <a href="{FA1P2MS}">FA1 Paper 2 HL mark scheme</a>. Its question numbers come from the original past papers, so match the parts by their content.</li>
<li>The "Out of" box for this paper below can be changed: if your question paper shows a different total, type that in.</li></ol></div>

<h2>4. Biology Grade 11 combined paper HL (30 marks)</h2>
{timer('bio-combined', 'Biology combined paper 1A, 1B and 2 HL', 2160, 'No time is printed, so 1.2 minutes a mark: 30 marks = 36 minutes.')}
<p><a href="{BIO_MS}">Grade 11 combined paper HL</a> (A1.1 water, A1.2 nucleic acids, B1.1 carbohydrates and lipids, B1.2 proteins, plus two questions, 7 and 8, on cell respiration, C1.2): questions 1 to 10 are multiple choice (10 marks), questions 11 to 14 are written (20 marks). Cover the grey answer boxes first.</p>
<div class="step"><div class="bh"><b>Mark it</b><span>about 10 min</span></div><ol>
<li>Uncover the grey boxes one at a time. For written answers each mark point ends with a semicolon; "OWTTE" means "or words to that effect", so your wording can differ if the meaning is the same.</li>
<li>Do not go over the mark shown in brackets: question 12 (b) is worth [2] even though its notes mention 3 marks.</li>
<li>Names must be in full where the scheme says so (11 (a)(i): "thymine", not "T").</li></ol></div>

<h2>5. English: one Paper 1 style analysis</h2>
{timer('eng-p1', 'English Paper 1 style analysis, one text', 4050, 'HL Paper 1 is 2 hours 15 minutes for two texts, so one text gets 67 min 30 s (about 10 minutes of that for reading, annotating and planning).')}
<div class="step"><div class="bh"><b>The task</b><span>67 min 30 s</span></div><ol>
<li>Choose one photograph from the <a href="{NYT}">New York Times collection</a> (a different one from your visual thinking assignment), or a print advert you can see in full.</li>
<li>Use a guiding question as in the exam, for example: "How does the photographer use composition and framing to shape the viewer's response?" or "How do the image and the words in this advert work together to persuade its audience?"</li>
<li>Write a guided analysis: an introduction with your overall reading, then paragraphs that each make a point about a technique (framing, angle, focus, colour, layout, typography, slogan), quote or describe the evidence, and explain its effect on the audience. End with a short conclusion.</li></ol></div>
<div class="step"><div class="bh"><b>Mark it</b><span>about 10 min</span></div><ol>
<li>A Paper 1 analysis is marked out of 20: four criteria worth 5 each (A understanding and interpretation, B analysis and evaluation, C focus and organisation, D language).</li>
<li>Give yourself a rough mark per criterion, then hand it to your English teacher for a real mark. Enter the teacher's mark when you have it.</li></ol></div>
<!-- Unverified: the English A criteria names and 5 marks each are from memory of the Language and Literature guide (first assessment 2021); no English subject guide is in the Drive folder. The 2 h 15 min HL timing was confirmed in published exam-format summaries. -->

<h2>Your scores</h2>
<p class="muted">Leave a row empty if you did not sit that paper; it then does not count in the total.</p>
{score_table([('chem-quiz1','Chemistry Quiz 1 Paper 2 HL',12,False),('chem-fa1-1a','FA1 Paper 1A (multiple choice)',20,False),('chem-fa1-1b','FA1 Paper 1B',10,False),('chem-fa1-p2','FA1 Paper 2 (if you had the questions)',29,True),('bio-combined','Biology combined paper HL',30,False),('eng-p1','English Paper 1 analysis (teacher or self mark)',20,False)])}

<h2>Error log</h2>
{errlog('<li>Add the papers to the Error log by subject. Then pick the three topics where you lost most marks today: they go first in next week&apos;s plan.</li>').replace('{q}','FA1 Paper 1A Q11')}

<h2>Not timed: Extended Essay</h2>
<div class="step"><div class="bh"><b>Meeting</b><span>agree the research question</span></div><ol>
<li>Take the three research questions from Saturday 14 November to your supervisor.</li>
<li>Ask: which is the most focused? Does it fit the subject&apos;s EE requirements? Is 4,000 words enough, or too much? What should you read or do first?</li>
<li>Write the agreed question and the next steps in a document in your <a href="{EE_FOLDER}">EE folder</a> straight after the meeting.</li></ol></div>
<p>Also on the study site: <a href="../flashcards.html">flashcards</a>, <a href="../exam-chemistry-hl.html">exam technique for Chemistry HL</a>, <a href="../exam.html">exam technique</a> and your <a href="../progress.html">progress page</a>.</p>
'''
build('2026-11-21-mock-papers.html', 'Mock papers: Chemistry, Biology, English (Sat 21 Nov 2026)',
      'Mock papers: Chemistry, Biology and English',
      'Saturday 21 November 2026. Sit Chemistry Quiz 1 and Formative Assessment 1 under timed conditions, then the Biology Grade 11 combined paper and one English Paper 1 style analysis. Mark each straight away and log your mistakes. Then agree your Extended Essay research question with your supervisor.',
      body3, '2026-11-21')
