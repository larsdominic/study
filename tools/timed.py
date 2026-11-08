# Timed practice pages (Saturday sets and mock papers).
# Run from the repo root: python3 tools/timed.py tools .
# Each page: crumb, intro, "Before you start", countdown timer(s), questions, "Mark it",
# score entry saved to localStorage 'ib-timed-YYYY-MM-DD' as {score, max, date, items}, Error log steps.
import sys, os
sys.path.insert(0, sys.argv[1]); from common import *
out = sys.argv[2]
os.makedirs(out + '/practice', exist_ok=True)

# Drive IDs (new upload, 8 Nov 2026; titles from the 8 Nov rename map)
M_PACK = DRIVE('1HUMbO0pFdie-qUVSvB5vzkLBLLErWCnL'); M_MS = DRIVE('13_E6OeummnBtiEB9_BRN9tZCKe2HhilT')
M_FB = DRIVE('19EX75prXgep28AagsDaWsr3eM6O8rVDV')
BIO_MS = DRIVE('1-fhyVSaXdMn9DuMLD5SWpO5TV37zB8eW')   # combined paper HL: questions inside the mark scheme
MOCK_Q = DRIVE('1S-X8BUmQiUTuiLWlr382zDg1dFsjcyLW'); MOCK_MS = DRIVE('1bS3dMIiu8HZOnYBdk5U3FvWgjHS5gJLe')
EN_GUIDE = DRIVE('1Sk7GD4FmWcB_crdej9xiSiWgg1iFySKR'); EN_MODEL = DRIVE('1mSfhzzcuxkvOuk33g9wqVY3xyNvbx7nP')
EN_BIG5 = DRIVE('1vXYq3D89JG8VLj2LIBcx1qnC-8RECXus')
PS_GUIDE = DRIVE('1Khqsn6PrxoS5UXAEKBpu5G_XG5Viyvtq'); PS_SPEC = DRIVE('1KoOk8IT670o-bbr1HKc-Nw2Kub_Gf1Mr')
PS_EX01 = DRIVE('1PRhaPPsIOqIk3SR-hFoj-ihbJioLIbcv'); PS_LC02 = DRIVE('18G55fgHqH329URQeM2Ykm0o_JpWRWZsf')
PS_RM04 = DRIVE('1flZ_D46k42AkC-ctI-Syh2qtVWKygnG1'); PS_RM06 = DRIVE('1upA3pwuiQj7stqZapW62OuZ9wedazOW-')
PS_MEAS = DRIVE('1exoZh04Ac6Wym__lOYzQ8CuMHCfVtALC')
CFP = 'https://www.cartooningforpeace.org/en/'   # checked 8 Nov 2026: opens (200)
MG = '../guides/2026-11-04-maths-aa-sl-1.2-1.6.html'

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
<li>Say what kind of mistake it was: <b>did not know it</b> (go back to the guide or handout), <b>wrong method</b>, <b>careless slip</b> (copying, signs, units), <b>ran out of time</b> or <b>ask teacher</b> (you still do not understand the mark scheme). Four careless slips in one set is a pattern worth a rule of its own.</li>
<li>Timing: write down which question you were on when the timer ended. If you finished in extra time, how many minutes did it take? Speed problems and knowledge problems need different fixes.</li>
<li><b>Fix-it:</b> rewrite one answer where you lost marks so it would now get full marks, using the mark scheme.</li>
{extra}</ol></div>'''

def build(fname, title, h1, intro, body, page_date):
    html = page(title, '../index.html', h1, intro, body, JS.replace('__PAGE__', page_date), crumb_label='All days')
    html = html.replace('</style>', EXTRA + '</style>', 1)
    assert '\u2014' not in html, fname
    open(out + '/practice/' + fname, 'w').write(html)
    print('wrote practice/' + fname)

# ---------------------------------------------------------------- 1. Maths, Sat 14 Nov (file name and score key keep 7 Nov)
u = lambda n: f'u<sub>{n}</sub>'; S = lambda n: f'S<sub>{n}</sub>'
body1 = f'''
<h2>Before you start</h2>
<div class="card"><ul>
<li><b>Paper and pen</b>, plus a pencil and ruler. Write on paper, not on screen.</li>
<li><b>No calculator.</b> Put it in another room. Maths AA Paper 1 is the no-calculator paper, and every question below can be done by hand.</li>
<li><b>Formula booklet: yes.</b> You get it in every IB maths exam. Open the <a href="{M_FB}">formula booklet</a> (Drive file "REF - Maths AA SL Formula Booklet (official).pdf") at the sequences page ({u('n')}, {S('n')} and {S('∞')} for arithmetic and geometric sequences are all there).</li>
<li><b>The question paper:</b> the <a href="{M_PACK}">sequences and series practice pack</a> (Drive file "1.2-1.4 + 1.8 Sequences and Series (school 1.2-1.5) - Practice Questions (IB Questionbank).pdf"; on screen or printed). Do <b>not</b> open the <a href="{M_MS}">mark scheme</a> (the file with the same name ending "- Mark Scheme (IB Questionbank).pdf") until the timer has ended.</li>
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
<p class="muted">Why these questions: Tuesday's <a href="{MG}">sequences guide</a> (10 November) already uses most of the pack. Of the questions it does not use, 20, 28 and 31 (c) to (g) work without a calculator (28 is left for extra practice): 6, 29 and 31 (a) to (b) need a GDC, and 25 needs logarithms, which you have not covered yet. So the set also repeats question 11 from Tuesday's guide and questions 4 and 16 from its "more practice" list. Do them again from a blank page without looking at Tuesday's work. Getting them right a second time, and faster, is the point.</p>
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
{errlog('<li>If you lost marks on a question you had already done (11, and 4 or 16 if you did them as extra practice on Tuesday), write "repeat" in the row. A mistake made twice is a habit: turn its rule into a flashcard.</li>').replace('{q}','Seq pack 16 (a)')}
<p>Also on the study site: the <a href="{MG}">sequences guide</a> for anything you could not do, the <a href="../flashcards.html">flashcards</a>, <a href="../exam-maths-aa-sl.html">exam technique for Maths AA</a> and your <a href="../progress.html">progress page</a>.</p>
'''
build('2026-11-07-timed-maths-sequences.html', 'Timed set: Maths sequences, no calculator (Sat 14 Nov 2026)',
      'Timed set: Maths sequences (no calculator)',
      'Saturday 14 November 2026. 40 minutes under exam conditions: five questions (35 marks) from your sequences pack, no calculator, then mark them with the mark scheme and log your mistakes.',
      body1, '2026-11-07')

# ---------------------------------------------------------------- 2. Mock papers, Sat 21 Nov
# Saturday = 4 h: 2 h timed practice (Biology, English) + 2 h Psychology (audit 4.2, Session 4).
# Minutes per block (each block must add up to 120)
BIO_MIN, BIO_MARK = 36, 10          # combined paper: 30 marks x 1.2 min a mark = 36 min
EN_READ, EN_PLAN, EN_WRITE, EN_CHECK, EN_MARK = 10, 10, 40, 7, 7   # HL timing per text from the class revision guide, step 7
EN_MIN = EN_READ + EN_PLAN + EN_WRITE + EN_CHECK
assert BIO_MIN == round(30 * 1.2) and EN_MIN == 67 and BIO_MIN + BIO_MARK + EN_MIN + EN_MARK == 120
PS_P1, PS_RM, PS_P3, PS_MARK, PS_FIX = 40, 25, 20, 25, 10
MK_P1, MK_RM, MK_P3 = 10, 8, 7
BRK1, BRK2 = 15, 10          # break between the two halves; second break inside the Psychology half
assert MK_P1 + MK_RM + MK_P3 == PS_MARK
P3_READ = 6.5; assert PS_P3 == 9 * 1.5 + P3_READ   # 9 marks at about 1.5 min a mark + reading sources 1 and 2
RM_READ, RM_Q5, RM_Q6, RM_MEAS = 3, 6, 6, 10
assert RM_READ + RM_Q5 + RM_Q6 + RM_MEAS == PS_RM and PS_P1 + PS_RM + PS_P3 + PS_MARK + PS_FIX == 120
P1_PACE = 90 / 35; P3_PACE = 105 / 30          # official minutes per mark (guide: P1 1 h 30 for 35 marks, P3 1 h 45 for 30)
assert round(P3_PACE * 9, 1) == 31.5 and round(P1_PACE * 16, 1) == 41.1
# Optional Biology mock selection (biology audit, Sat 21 Nov proposal) without the C1.2 questions:
# C1.2 is learnt on Sun 22 Nov, after this paper. Marks read from the question paper.
# Every one of these is also a question in the HL topical packs (same SaveMyExams bank): pack = (topic, HL pack question).
MOCK = [('22', 'B1.2', 8, ('B1.2', '6')), ('29', 'B1.2', 7, ('B1.2', '7')), ('25', 'B1.1', 6, None),
        ('28', 'B1.1', 6, ('B1.1', '4')), ('35', 'C1.1', 6, ('C1.1', '6')), ('48', 'C1.1', 12, ('C1.1', '9'))]
MOCK_MCQ = [('26', 'B1.1', ('B1.1', '3')), ('31', 'B1.2', ('B1.2', '8')), ('32', 'B1.1', ('B1.1', '5')),
            ('38', 'C1.1', ('C1.1', '7')), ('39', 'C1.1', ('C1.1', '8')), ('41', 'B1.1', ('B1.1', '6'))]
MOCK_MARKS = sum(m for _, _, m, _ in MOCK) + len(MOCK_MCQ)
MOCK_SEC = round(MOCK_MARKS * 1.2 * 60)
assert MOCK_MARKS == 51 and MOCK_SEC == 3672
packref = lambda pk: f'{pk[0]} HL pack question {pk[1]}' if pk else 'not in the HL packs'
mock_rows = ''.join(f'<tr><td>{q}</td><td>{t}</td><td>{m}</td><td>{packref(pk)}</td></tr>' for q, t, m, pk in MOCK)
mock_rows += (f'<tr><td>{", ".join(q for q, _, _ in MOCK_MCQ)} (multiple choice)</td><td>B1.1, B1.2, C1.1</td><td>{len(MOCK_MCQ)}</td><td>'
              + '; '.join(f'{q} = {packref(pk)}' for q, _, pk in MOCK_MCQ) + '</td></tr>')
mock_rows += f'<tr><th colspan="2">Total</th><th>{MOCK_MARKS}</th><th></th></tr>'
# P3 specimen source 2 (read from the specimen resource booklet): max, median, mean, SD, min; box plot min, Q1, median, Q3, max
HS = dict(mx=21, med=10, mean=11.6, sd=3.87, mn=7, q1=9, q3=14); NS = dict(mx=25, med=15, mean=17.64, sd=4.48, mn=12, q1=14, q3=21)
d_mean = round(NS['mean'] - HS['mean'], 2); d_med = NS['med'] - HS['med']
r_hs = HS['mx'] - HS['mn']; r_ns = NS['mx'] - NS['mn']; iqr_hs = HS['q3'] - HS['q1']; iqr_ns = NS['q3'] - NS['q1']
assert (d_mean, d_med, r_hs, r_ns, iqr_hs, iqr_ns) == (6.04, 5, 14, 13, 5, 7)
# score table: one row per marked item
SC_BIO = [('bio-combined', 'Biology combined paper, questions 1 to 6 and 9 to 14', 28, False),
          ('bio-combined-c12', 'Biology combined paper, questions 7 and 8 (C1.2)', 2, False)]
SC_EN = [('eng-p1', 'English Paper 1 cartoon analysis (self or teacher mark)', 20, False)]
SC_PS = [('psy-p1a', 'Psychology Paper 1 (a): classical conditioning', 4, False), ('psy-p1b', 'Psychology Paper 1 (b): dog trainers, operant conditioning', 6, False),
         ('psy-p1c', 'Psychology Paper 1 (c): specimen Q4, social learning theory', 6, False), ('psy-rm-q5', 'Evaluating research task Q5', 4, False),
         ('psy-rm-q6', 'Evaluating research task Q6', 4, False), ('psy-p2-meas', 'Paper 2 style: measurement in your experiment', 4, False),
         ('psy-p3-q1', 'Psychology specimen Paper 3 Q1', 3, False), ('psy-p3-q2', 'Psychology specimen Paper 3 Q2', 6, False)]
SC_MOCK = [(f'bio-mock-{q}', f'Optional: Biology mock Q{q} ({t})', m, False) for q, t, m, _ in MOCK] + \
          [('bio-mock-mcq', 'Optional: Biology mock multiple choice (' + ', '.join(q for q, _, _ in MOCK_MCQ) + ')', len(MOCK_MCQ), True)]
tot = lambda rows: sum(r[2] for r in rows)
T_BIO, T_EN, T_PS, T_MOCK = tot(SC_BIO), tot(SC_EN), tot(SC_PS), tot(SC_MOCK)
assert (T_BIO, T_EN, T_PS, T_MOCK) == (30, 20, 37, 51) and T_PS == 4 + 6 + 6 + 4 + 4 + 4 + 3 + 6
T_DAY = T_BIO + T_EN + T_PS; T_ALL = T_DAY + T_MOCK
assert (T_DAY, T_ALL) == (87, 138)

body3 = f'''
<p style="margin-top:22px">Four hours of work today, with two breaks. <b>First two hours:</b> timed practice, the Biology combined paper and one English Paper 1 style analysis of a satirical cartoon. <b>Second two hours:</b> timed Psychology practice. Mark each part straight after its timer, while you still remember your thinking.</p>
<div class="blocks">
{block_open('1', 'Timed practice: Biology and English', f'{BIO_MIN + BIO_MARK + EN_MIN + EN_MARK} min')}<p>Biology combined paper ({BIO_MIN}) and marking ({BIO_MARK}); English cartoon analysis ({EN_MIN}) and self-check ({EN_MARK}).</p></div>
<div class="brkc"><b>Break · about {BRK1} min.</b> Get up, eat, no screens.</div>
{block_open('2a', 'Psychology, part 1', f'{PS_P1 + PS_RM} min')}<p>Paper 1 Sections A and B ({PS_P1}); research methods ({PS_RM}).</p></div>
<div class="brkc"><b>Break 2 · {BRK2} min.</b> Stand up, drink water, look out of a window, no phone.</div>
{block_open('2b', 'Psychology, part 2', f'{PS_P3 + PS_MARK + PS_FIX} min')}<p>Paper 3 questions 1 and 2 ({PS_P3}); marking with the markbands ({PS_MARK}); Fix-it: rewrite your weakest answer to the top markband ({PS_FIX}).</p></div>
</div>
<p class="muted">Work time, breaks not counted: {BIO_MIN + BIO_MARK + EN_MIN + EN_MARK + PS_P1 + PS_RM + PS_P3 + PS_MARK + PS_FIX} minutes, plus about 10 minutes for the Error log at the end.</p>

<h2>Before you start</h2>
<div class="card"><ul>
<li><b>Paper and pen</b>, pencil, ruler. Answer on paper.</li>
<li><b>Calculator:</b> yes for Biology. Not needed for English or Psychology.</li>
<li><b>Biology:</b> the <a href="{BIO_MS}">Grade 11 combined paper HL</a> (Drive file "Combined Paper Grade 11 HL (1A-1B-2, 30 marks) - Mark Scheme with Questions.pdf"), with the answer boxes covered (see below).</li>
<li><b>English:</b> one satirical cartoon you have <b>not</b> seen before, chosen by someone else (see section 2), plus your class <a href="{EN_GUIDE}">Paper 1 satirical cartoons revision guide</a> and the <a href="{EN_MODEL}">Horsey model response</a> for the self-check afterwards. Read the Horsey model before today (it was on the plan for Friday 13 November), not during the timed part.</li>
<li><b>Psychology:</b> the <a href="{PS_SPEC}">specimen papers</a> (Drive file "REF - Specimen papers 1, 2 and 3 with markschemes (official, first assessment 2027).pdf"), the <a href="{PS_EX01}">21 September exam practice sheet</a> and the <a href="{PS_RM04}">evaluating research task</a>. The specimen file has each markscheme straight after its paper: do not scroll into a markscheme before the marking block.</li>
<li><b>Sticky notes or strips of paper</b> to cover answers, or ask someone to do it before you start.</li>
<li>The timers work offline and keep the right time if the phone screen locks.</li>
</ul></div>

<div class="miss"><b>Biology Grade 11 combined paper HL: the only file is the mark scheme, but it contains every question.</b> Each question (with its diagrams) is followed straight away by a grey "Markscheme" box with the answer. Before you start, print it and cover every grey box with a sticky note, or on screen scroll with a sheet of paper held over everything below the question you are on. No time is printed on it.</div>

<h2>1. Biology Grade 11 combined paper HL (30 marks)</h2>
{timer('bio-combined', 'Biology combined paper 1A, 1B and 2 HL', BIO_MIN * 60, 'No time is printed, so 1.2 minutes a mark: 30 marks = 36 minutes.')}
<p><a href="{BIO_MS}">Grade 11 combined paper HL</a> (A1.1 water, A1.2 nucleic acids, B1.1 carbohydrates and lipids, B1.2 proteins, C1.1 enzymes in question 12, and two questions, 7 and 8, on cell respiration, C1.2): questions 1 to 10 are multiple choice (10 marks), questions 11 to 14 are written (20 marks). Cover the grey answer boxes first.</p>
<div class="tip"><b>Questions 7 and 8.</b> They are on cell respiration (C1.2), which you learn on Sunday 22 November. Try them anyway: they are one mark each, and a reasoned guess is good practice. They have their own score row, so you can see them separately.</div>
<div class="step"><div class="bh"><b>Mark it</b><span>about {BIO_MARK} min</span></div><ol>
<li>Uncover the grey boxes one at a time. For written answers each mark point ends with a semicolon; "OWTTE" means "or words to that effect", so your wording can differ if the meaning is the same.</li>
<li>Do not go over the mark shown in brackets: question 12 (b) is worth [2] even though its notes mention 3 marks.</li>
<li>Names must be in full where the scheme says so (11 (a)(i): "thymine", not "T").</li>
<li>Write one Error log row for every mark you lost (see the Error log at the end).</li></ol></div>

<h2>2. English A: one Paper 1 style cartoon analysis (20 marks)</h2>
<p>Paper 1 gives you unseen non-literary texts, and a satirical cartoon is one possible text type. Today you write one full analysis under time, using what you practised in your class <a href="{EN_GUIDE}">Paper 1 satirical cartoons revision guide</a> ("Paper 1 Satirical Cartoons - Revision Guide (research workbook).docx") and the <a href="{EN_MODEL}">Horsey "Modern Life" model response</a> ("Paper 1 Satirical Cartoons - Horsey Modern Life - Model Response and Answers (20 of 20).docx") as your model.</p>
<div class="step"><div class="bh"><b>Get the cartoon ready</b><span>before today</span></div><ol>
<li>Ask someone at home to choose <b>one</b> satirical (editorial) cartoon you have not seen, with no violent or graphic images, for example from <a href="{CFP}">Cartooning for Peace</a> or the Pulitzer Prize winners for Illustrated Reporting and Commentary (both are on the research list in your revision guide). Not one from your own cartoon bank (step 6): those you have already analysed.</li>
<li>They save or print it with the cartoonist, the publication and the date, and do not show it to you before the timer starts.</li>
<li>They write a guiding question on the back in the same form as the Horsey one: "How does the cartoonist use visual and linguistic features to comment on [the issue]?" If the cartoon has no words, "visual features" alone.</li></ol></div>
{timer('eng-p1', 'English Paper 1 style analysis, one cartoon', EN_MIN * 60, f'Your revision guide (step 7) gives HL Paper 1 as 2 hours 15 minutes for two texts, and suggests per text: read and annotate {EN_READ} min, plan {EN_PLAN} min, write {EN_WRITE} min, check {EN_CHECK} min. That is {EN_MIN} minutes.')}
<div class="step"><div class="bh"><b>The task</b><span>{EN_MIN} min</span></div><ol>
<li><b>Read and annotate</b> <span class="t">({EN_READ} min)</span>. Read the guiding question first. Note the audience, the purpose and the target of the satire. Annotate the cartoon with the Big 5 (audience, purpose and context; content and theme; tone, mood and register; style; structure and layout) from your <a href="{EN_BIG5}">Big 5 slides</a>, and the conventions from steps 2 to 4 of the revision guide: caricature, exaggeration, symbolism, juxtaposition, scale and placement, caption, labels, irony, colour.</li>
<li><b>Plan</b> <span class="t">({EN_PLAN} min)</span>. Write a one-sentence thesis that answers the guiding question. Choose 3 or 4 points and group them by argument, not in the order you noticed them. The Horsey model groups them as: the contrast between the figures; the central object and setting; the language and tone; words and image working together.</li>
<li><b>Write</b> <span class="t">({EN_WRITE} min)</span>. Introduction: text type, cartoonist, publication, date, audience, purpose, then your thesis. Each body paragraph in PEEL, using the step 5 chain from the revision guide: spot it, explain it, the effect on the reader, the link to the purpose. Never stop at naming a technique. Conclusion: judge how well the cartoon works, not only what it means. The Horsey notes say 600 to 800 focused words can reach the top bands.</li>
<li><b>Check</b> <span class="t">({EN_CHECK} min)</span>. Fix errors, sharpen your terms, and check that every topic sentence goes back to the guiding question.</li></ol></div>
<div class="step"><div class="bh"><b>Self-check</b><span>about {EN_MARK} min</span></div><ol>
<li>Fill in the "Check yourself against the criteria" table at the end of the revision guide (step 7): for A understanding and interpretation, B analysis and evaluation, C focus and organisation, D language, tick Not yet, Nearly or Secure.</li>
<li>Compare with "What lifts this response to the top band" in the Horsey file. Tick each one you did: analysis, not description (every observation followed by "which suggests" or "so that"); words and image read together; one or two points most students would miss; a conclusion that evaluates.</li>
<li>Underline your thesis and each topic sentence: do they all answer the guiding question (C)? Circle the subject terms you used (D) and compare with the Horsey ones (juxtaposition, lexis, semantic field, bathos, passive voice).</li>
<li>Give yourself a rough mark out of 5 for each criterion, using the Horsey 5 out of 5 notes as the top. Enter the total out of 20 below, then hand the analysis to your English teacher and replace your mark with theirs when you get it.</li>
<li>Write the weakest criterion in the Error log, with one thing you will do differently next time.</li></ol></div>
<p class="muted">Where these figures come from: the 2 hours 15 minutes, 20 marks per text, 5 marks per criterion and the criteria A to D are from your class revision guide (step 7) and the Horsey model, and match the official IB Language A: language and literature guide (first assessment 2021; Paper 1 is unchanged in the 2026 version).</p>

<h2>3. Psychology: timed practice (37 marks)</h2>
<p>This is the fourth Psychology session: no notes, under time. The structure of each paper comes from the official guide (<a href="{PS_GUIDE}">IB Psychology guide, first assessment 2027</a>): Paper 1 is 1 hour 30 minutes for 35 marks (Section A two 4-mark questions, Section B two 6-mark questions applied to an unseen situation, Section C one 15-mark essay); Paper 2 Section A has four questions on your class practicals (4, 4, 6 and 6 marks); Paper 3 (HL only) is 1 hour 45 minutes for 30 marks, with questions of 3, 6, 6 and 15 marks on a set of sources.</p>

<h3>Paper 1 Sections A and B (16 marks)</h3>
{timer('psy-p1', 'Psychology Paper 1, Sections A and B', PS_P1 * 60, f'Your 21 September practice sheet allows 10 minutes for a 4-marker and 15 for a 6-marker: 10 + 15 + 15 = 40 minutes. The official pace is 90 minutes for 35 marks, so 16 marks would be {P1_PACE * 16:.1f} minutes.')}
<div class="step"><div class="bh"><b>Three questions</b><span>{PS_P1} min</span></div><ol>
<li><b>(a) [4]</b> "Describe classical conditioning with reference to one example." From the <a href="{PS_EX01}">21 September exam practice sheet</a>. You wrote this on Monday 16 November: do it again from a blank page, without looking at Monday&apos;s answer. Move on at 10 minutes.</li>
<li><b>(b) [6]</b> The dog-trainer question on the same sheet: "Explain how dog trainers might use operant conditioning principles to teach specific behaviours or reduce problematic behaviours in dogs." Read the short scenario above it first. Move on at 25 minutes.</li>
<li><b>(c) [6]</b> <a href="{PS_SPEC}">Specimen Paper 1</a>, question 4 (Section B, human development): as the school psychologist, explain how social learning theory could be used to promote empathy or prosocial behaviour among children. Stop at 40 minutes.</li></ol></div>

<h3>Research methods (12 marks)</h3>
{timer('psy-rm', 'Psychology research methods', PS_RM * 60, f'Plan: {RM_READ} min to re-read the study, {RM_Q5} min for Q5, {RM_Q6} min for Q6, {RM_MEAS} min for the 4-mark Paper 2 style question. The class task allowed 20 to 25 minutes for all six questions open book; the official pace (90 minutes for 35 marks) gives a 4-mark question about 10 minutes.')}
<div class="step"><div class="bh"><b>Two tasks</b><span>{PS_RM} min</span></div><ol>
<li><a href="{PS_RM04}">Evaluating research task</a> ("RM04 Research methodology - Evaluating research, breathing study - Application task (class).docx"): re-read Ms Patel&apos;s breathing study, then answer <b>Q5 [4]</b> (reliability and construct validity of her anxiety questionnaire, and one improvement) and <b>Q6 [4]</b> (her claim about "all IB students", with population validity and ecological validity). This time with no notes.</li>
<li><b>Paper 2 Section A style [4]:</b> "Explain the concept of measurement in relation to your class practical." This is a question from your <a href="{PS_RM06}">class practical planning template</a>. If you did not take part in the class experiment, use a simple experiment you can describe, for example "Does background music affect how many words people remember?". Cover how the independent and dependent variables were operationalised, how they were measured, and one limitation of that measurement.</li></ol></div>

<p class="ok"><b>Break 2 · {BRK2} minutes.</b> Stand up, drink water, look out of a window. No phone. Then Paper 3.</p>

<h3>Paper 3 (HL): questions 1 and 2 (9 marks)</h3>
{timer('psy-p3', 'Psychology specimen Paper 3, Q1 and Q2', PS_P3 * 60, f'The official pace is 105 minutes for 30 marks, so 9 marks would be {P3_PACE * 9:.1f} minutes, but that time includes reading all five sources for question 4. You only need sources 1 and 2: about 1.5 minutes a mark (9 × 1.5 = {9 * 1.5} minutes) plus {P3_READ} minutes to read them, so {PS_P3} minutes.')}
<div class="step"><div class="bh"><b>Two questions</b><span>{PS_P3} min</span></div><ol>
<li>In the <a href="{PS_SPEC}">specimen file</a>, find the Paper 3 question paper (it has source 1, a bar chart, and the four questions) and the resource booklet that follows it (source 2 is a table and a box plot).</li>
<li><b>Q1 [3]</b> "Explain one issue that limits the interpretation of the data in source 1." Only your first issue counts, so pick one and explain it fully.</li>
<li><b>Q2 [6]</b> "Analyse the findings from source 2 and state a conclusion linked to the claim that the use of technology in education may have a negative effect on the mental health of students." Use the numbers, and end with a conclusion that is clearly linked to them.</li>
<li>Leave questions 3 and 4 for another day.</li></ol></div>

<h3>Mark it with the markbands</h3>
<div class="step"><div class="bh"><b>Marking</b><span>{PS_MARK} min</span></div><ol>
<li><b>Paper 1 (a), (b), (c)</b> <span class="t">({MK_P1} min)</span>. The markbands are at the start of the specimen Paper 1 markscheme (also guide pages 45 to 46). Section A, out of 4: 1 to 2 limited knowledge, the example is relevant but not explained; 3 to 4 detailed knowledge, the example is relevant and explained. Section B, out of 6: 1 to 2 limited; 3 to 4 some detail, mostly accurate, application partly developed; 5 to 6 accurate and detailed, application well developed. For (a) also check the PEEL word guide on the <a href="{PS_EX01}">practice sheet</a> and the "examiner would be looking for" notes in the <a href="{PS_LC02}">classical conditioning slides</a>; for (b) the three Identify, Explain, Apply cycles on the same sheet; for (c) the notes under question 4 in the specimen markscheme (you must suggest a strategy, not only describe the theory).</li>
<li><b>Research methods</b> <span class="t">({MK_RM} min)</span>. There is no mark scheme for the evaluating research task in your Drive, so use my points below. For the measurement question use the official markband for Paper 2 Section A question 2 (guide pages 47 to 48): 1 to 2 the concept is relevant but limited, with some links to the practical; 3 to 4 the concept is well developed, with clear and detailed links.</li>
<li><b>Paper 3</b> <span class="t">({MK_P3} min)</span>. Specimen Paper 3 markscheme (also guide page 50): Q1 gives 1 if the issue is identified, 2 if clearly described, 3 if explained. Q2: 1 to 2 limited or inaccurate analysis; 3 to 4 accurate but lacking detail, with an unclear link to the conclusion; 5 to 6 analysed in detail, with a conclusion explicitly linked to the findings.</li>
<li>Write one Error log row for every mark you lost, with its type: did not know, wrong method, slip, time or ask teacher.</li></ol></div>
<div class="step"><div class="bh"><b>Fix-it</b><span>{PS_FIX} min</span></div><ol>
<li>Pick your weakest Psychology answer: the one with the lowest mark compared with its maximum (for example 2 out of 6 is weaker than 2 out of 4).</li>
<li>Rewrite it on a fresh page so that it meets the <b>top</b> markband, using the descriptors above as a checklist. Section A: detailed knowledge, and an example that is relevant <b>and explained</b>. Section B: accurate and detailed knowledge, and an application that is well developed (every paragraph goes back to the dogs or the children in the question). Paper 3 Q2: findings analysed in detail, with numbers, and a conclusion explicitly linked to them. Research methods: each point tied to Ms Patel&apos;s study.</li>
<li>Check it against the <a href="../exam-psychology-hl.html#annotated">annotated model answers</a> on the exam technique page: can you say which descriptor each of your sentences earns?</li>
<li>Write your three weakest points in the Error log. They are what you fix first in the exam window.</li></ol></div>
<details><summary>My points for the evaluating research task, Q5 and Q6 (not the teacher&apos;s mark scheme)</summary>
<p><b>Q5 [4]:</b> one mark for each point that is explained and tied to Ms Patel&apos;s study.</p>
<ul>
<li>Reliability: she wrote the 5-item questionnaire herself and never tested it, for example by giving it twice to the same students to see if the scores stay the same (test-retest). So we do not know if it gives consistent scores.</li>
<li>Construct validity: we do not know whether the items measure exam anxiety, the construct, rather than general stress or mood; it was never compared with an established, already tested anxiety measure.</li>
<li>The students knew the aim, so their answers may show what they think she wants to hear, which also weakens what the scores mean.</li>
<li>Improvement: use an established anxiety scale, or pilot her questionnaire, check test-retest reliability and compare its scores with an established scale.</li>
</ul>
<p><b>Q6 [4]:</b> about 2 marks for population validity and 2 for ecological validity, each 1 for the problem with evidence from the study and 1 for what it means for her claim.</p>
<ul>
<li>Population validity: 24 volunteers (self-selected through a library poster) from one Grade 11 class in one school, all her own students. Volunteers may be more interested in breathing exercises or more anxious, so the sample does not represent "all IB students".</li>
<li>Ecological validity: a mock exam at school is quite close to real life, which is a strength, but a mock has lower stakes than a real IB exam, and the exercise was led by the students&apos; own teacher, so the effect may be different in real exams.</li>
<li>Judgement: the claim is far too broad. At most the study suggests the exercise might help these students in this setting, and the word "cause" is not justified while order effects and her own marking are not controlled.</li>
</ul></details>
<details><summary>Numbers from specimen source 2, worked out to check your Q2 analysis (open after the timer)</summary>
<ul>
<li>25 students in each group; scores out of 30, and higher means better mental health.</li>
<li>Mean: {HS['mean']} with high screen time against {NS['mean']} with no screen time, so {d_mean} points lower. Median: {HS['med']} against {NS['med']}, so {d_med} lower.</li>
<li>Standard deviation: {HS['sd']} against {NS['sd']}, so the no screen time scores are a little more spread out.</li>
<li>Range: {HS['mx']} − {HS['mn']} = {r_hs} and {NS['mx']} − {NS['mn']} = {r_ns}, about the same.</li>
<li>Box plot: the middle half of the high screen time group runs from {HS['q1']} to {HS['q3']} and of the no screen time group from {NS['q1']} to {NS['q3']}, so the two boxes only meet at {HS['q3']}.</li>
</ul><p class="muted">The markscheme decides the marks. A strong conclusion also says what the data cannot show: one day and one task only.</p></details>

<h2>Optional: Biology mock paper selection ({MOCK_MARKS} marks)</h2>
<p><b>Not part of today&apos;s four hours.</b> Do this only if you have a spare slot before the exam window starts on Monday 23 November. It uses the <a href="{MOCK_Q}">mock exam practice questions</a> ("Mock Exam Grade 11 Practice - Questions (SaveMyExams).pdf"), marked with the <a href="{MOCK_MS}">mock exam mark scheme</a> ("Mock Exam Grade 11 Practice - Mark Scheme (SaveMyExams).pdf"). You need graph paper for question 48 and a calculator.</p>
{timer('bio-mock', 'Biology mock selection', MOCK_SEC, f'1.2 minutes a mark, as for the combined paper: {MOCK_MARKS} marks × 1.2 = {MOCK_MARKS * 1.2:.1f} minutes.')}
<div class="tablewrap"><table>
<tr><th>Mock question</th><th>Topic</th><th>Marks</th><th>Also in your topical packs as</th></tr>
{mock_rows}</table></div>
<div class="tip"><b>Seen it already?</b> The mock and your HL topical packs come from the same question bank, so most of these questions are also in the packs (last column). If you already did one of them on a Biology day, skip it here and leave its row empty (for the multiple choice row, lower its "Out of" box instead): a question you have seen is not a test. The cell respiration (C1.2) questions of the mock are left out, because you learn C1.2 on Sunday 22 November.</div>
<div class="step"><div class="bh"><b>Mark it</b><span>about 15 min</span></div><ol>
<li>Open the <a href="{MOCK_MS}">mark scheme</a> only after the timer. Give a mark only for a point that matches the scheme or says the same thing in other words.</li>
<li>Question 29 has one mark for clarity of communication: give it only if your answer is clear and in a logical order.</li>
<li>Write one Error log row for every mark you lost.</li></ol></div>

<h2>Your scores</h2>
<p class="muted">Leave a row empty if you did not do that part; it then does not count in the total. Today&apos;s papers add up to {T_BIO} (Biology) + {T_EN} (English) + {T_PS} (Psychology) = {T_DAY} marks; with the optional Biology selection ({T_MOCK}) the maximum is {T_ALL}.</p>
{score_table(SC_BIO + SC_EN + SC_PS + SC_MOCK)}

<h2>Error log</h2>
{errlog('<li>Add today&apos;s papers to the Error log by subject. Then pick the three topics where you lost most marks: they go first in the exam window plan.</li>').replace('{q}', 'Bio combined Q12 (b)')}
<p>Also on the study site: <a href="../flashcards.html">flashcards</a>, <a href="../exam.html">exam technique</a> and your <a href="../progress.html">progress page</a>.</p>
'''
build('2026-11-21-mock-papers.html', 'Mock papers: Biology, English, Psychology (Sat 21 Nov 2026)',
      'Mock papers: Biology, English and Psychology',
      'Saturday 21 November 2026. Four hours: two hours of timed practice (the Biology Grade 11 combined paper and one English Paper 1 style cartoon analysis), then two hours of timed Psychology practice. Mark each part straight away with the mark schemes and markbands, and log your mistakes.',
      body3, '2026-11-21')
