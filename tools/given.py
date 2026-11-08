# "What you are given vs what you must learn" pages.
# Run from the repo root: python3 tools/given.py tools .
# Sources:
#  Maths: IB Mathematics: analysis and approaches SL formula booklet (first examinations 2021, version 1.0, (c) IBO 2023),
#         Drive 19EX75prXgep28AagsDaWsr3eM6O8rVDV, read from the PDF (pdftotext -layout plus rendered page images, so
#         modulus bars and fractions were checked by eye); IB Maths AA guide (first assessment 2021) SL content statements.
#  Business: IB Business management guide (first assessment 2024, updated July 2024), Drive 1KeX_WVc4uNQe-DdGS_7-1ITxBUqXveWD:
#         Appendices > Formulae (pp. 64 to 65, read from the page images), unit 3, unit 5.5 and the toolkit (figure 5).
# Every worked example was computed with python before being written here.
import sys; sys.path.insert(0, sys.argv[1]); from common import *
out = sys.argv[2]

EXTRA = r'''
  .wrap{max-width:1080px}
  .legend{display:flex;flex-wrap:wrap;gap:8px 20px;background:var(--card);border:1px solid var(--rule);padding:10px 14px;font-size:.92rem;margin:16px 0}
  .fb,.learn{display:inline-block;font-size:.72rem;font-weight:700;padding:1px 7px;border-radius:3px;vertical-align:middle;margin-left:6px;white-space:nowrap;font-family:"Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;letter-spacing:.01em}
  .fb{background:var(--green);color:#fff}
  .learn{background:var(--amber);color:#fff}
  .toc{display:flex;flex-wrap:wrap;gap:8px;margin:18px 0 0;padding:0;list-style:none}
  .toc a{display:inline-block;background:var(--card);border:1px solid var(--rule);padding:5px 12px;border-radius:999px;font-size:.92rem;text-decoration:none}
  .toc a:hover{border-color:var(--indigo)}
  section.topic{margin-top:44px;padding-top:22px;border-top:3px solid var(--ink)}
  section.topic > h2{margin-top:0}
  .cols{display:grid;grid-template-columns:minmax(0,1fr);gap:18px;margin-top:14px}
  @media (min-width:800px){.cols{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}
  .col{background:var(--card);border:1px solid var(--rule);border-top:6px solid var(--green);padding:10px 16px 6px}
  .col.l{border-top-color:var(--amber)}
  .col > h3{margin:4px 0 6px;font-size:1.2rem}
  .col.b > h3{color:var(--green)} .col.l > h3{color:var(--amber)}
  .it{border-top:1px dashed var(--rule);padding:9px 0 10px}
  .col > h3 + .it,.col > .it:first-child{border-top:0}
  .ref{display:inline-block;font-weight:700;color:var(--ink-soft);font-size:.82rem;margin-right:6px;white-space:nowrap}
  .lab{font-size:.95rem;font-weight:600}
  .fm{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;font-size:1.1rem;margin:4px 0 0;line-height:2}
  .fm small{display:block;margin-top:2px;font-family:"Segoe UI","Helvetica Neue",Helvetica,Arial,sans-serif;font-size:.8rem;color:var(--ink-soft);line-height:1.4}
  .eg{font-size:.93rem;color:var(--ink-soft);margin-top:4px;line-height:1.55}
  .eg b{color:var(--ink)}
  .note{font-size:.9rem;color:var(--ink-soft)}
  .wf{font-weight:inherit}
  .rt{display:inline-flex;align-items:flex-start;max-width:100%;vertical-align:top}
  .rt > .ov{min-width:0}
  .ov{display:inline-block;border-top:1px solid currentColor;padding-top:1px;line-height:1.5}
  .intg{font-size:1.35em;vertical-align:middle;line-height:1}
  .lim{display:inline-flex;flex-direction:column;vertical-align:middle;font-size:.72em;line-height:1.05;margin-right:2px;text-align:left}
  .sig{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;line-height:1;margin:0 3px}
  .sig small{font-size:.62em}
  .sig b{font-weight:400;font-size:1.35em;line-height:1.05}
  .grid2{display:grid;grid-template-columns:minmax(0,1fr);gap:14px}
  @media (min-width:800px){.grid2{grid-template-columns:minmax(0,1fr) minmax(0,1fr)}}
  .sheet{background:var(--card);border:1px solid var(--rule);border-left:6px solid var(--green);padding:10px 16px}
  .sheet .fm{margin-bottom:6px}
  .sheet ol{margin:4px 0 0;padding-left:22px;font-size:.95rem} .sheet li{margin:2px 0}
'''

def build(title, h1, intro, body):
    html = page(title, "exam.html", h1, intro, body, crumb_label="Exam technique: all subjects")
    return html.replace("</style>", EXTRA + "</style>", 1)

# ---------- small maths helpers ----------
def fr(a, b): return f'<span class="frac"><span>{a}</span><span>{b}</span></span>'
def sq(x): return f'√<span class="ov">{x}</span>'
def nw(x): return f'<span class="nw">{x}</span>'
def lim(lo, hi): return f'<span class="lim"><span>{hi}</span><span>{lo}</span></span>'
def sig(lo, hi): return f'<span class="sig"><small>{hi}</small><b>Σ</b><small>{lo}</small></span>'
I = lambda s: f'<i>{s}</i>'
u1, un, Sn, d_, r_ = '<i>u</i><sub>1</sub>', '<i>u</i><sub><i>n</i></sub>', '<i>S</i><sub><i>n</i></sub>', '<i>d</i>', '<i>r</i>'
n_ = '<i>n</i>'

def bitem(ref, label, formula):
    return f'<div class="it"><span class="ref">{ref}</span><span class="lab">{label}</span><div class="fm">{formula}</div></div>'

def litem(ref, title, fact, eg):
    return (f'<div class="it"><span class="ref">{ref}</span><span class="lab">{title}</span>'
            f'<div class="fm" style="font-family:inherit;font-size:1rem;line-height:1.6">{fact}</div>'
            f'<div class="eg"><b>Example:</b> {eg}</div></div>')

def topic(anchor, heading, lead, booklet, learn):
    b = ''.join(bitem(*x) for x in booklet)
    l = ''.join(litem(*x) for x in learn)
    return (f'<section class="topic" id="{anchor}"><h2>{heading}</h2><p>{lead}</p><div class="cols">'
            f'<div class="col b"><h3>In the formula booklet <span class="fb">In booklet</span></h3>{b}</div>'
            f'<div class="col l"><h3>Not in the booklet: learn it <span class="learn">Learn</span></h3>{l}</div>'
            f'</div></section>')

# ================= MATHS =================
T1B = [
 ("1.2", "The <i>n</i>th term of an arithmetic sequence", nw(f'{un} = {u1} + ({n_} − 1){d_}')),
 ("1.2", "The sum of <i>n</i> terms of an arithmetic sequence", nw(f'{Sn} = {fr(n_,"2")}(2{u1} + ({n_} − 1){d_})') + ' ; ' + nw(f'{Sn} = {fr(n_,"2")}({u1} + {un})')),
 ("1.3", "The <i>n</i>th term of a geometric sequence", nw(f'{un} = {u1}<i>r</i><sup><i>n</i>−1</sup>')),
 ("1.3", "The sum of <i>n</i> terms of a finite geometric sequence", nw(f'{Sn} = {fr(u1+"(<i>r</i><sup><i>n</i></sup> − 1)","<i>r</i> − 1")}') + ' ' + nw(f'= {fr(u1+"(1 − <i>r</i><sup><i>n</i></sup>)","1 − <i>r</i>")}, <i>r</i> ≠ 1')),
 ("1.8", "The sum of an infinite geometric sequence", nw(f'S<sub>∞</sub> = {fr(u1,"1 − <i>r</i>")}, |<i>r</i>| &lt; 1')),
 ("1.4", "Compound interest", nw(f'<i>FV</i> = <i>PV</i> × (1 + {fr("<i>r</i>","100<i>k</i>")})<sup><i>kn</i></sup>') + '<br><small><i>FV</i> future value, <i>PV</i> present value, <i>n</i> number of years, <i>k</i> number of compounding periods per year, <i>r</i>% nominal annual rate of interest</small>'),
 ("1.5", "Exponents and logarithms", nw('<i>a</i><sup><i>x</i></sup> = <i>b</i> ⇔ <i>x</i> = log<sub><i>a</i></sub><i>b</i>') + '<br><small>where <i>a</i> &gt; 0, <i>b</i> &gt; 0, <i>a</i> ≠ 1</small>'),
 ("1.7", "Exponents and logarithms (the three log laws)", nw('log<sub><i>a</i></sub><i>xy</i> = log<sub><i>a</i></sub><i>x</i> + log<sub><i>a</i></sub><i>y</i>') + '<br>' + nw(f'log<sub><i>a</i></sub>{fr("<i>x</i>","<i>y</i>")} = log<sub><i>a</i></sub><i>x</i> − log<sub><i>a</i></sub><i>y</i>') + '<br>' + nw('log<sub><i>a</i></sub><i>x</i><sup><i>m</i></sup> = <i>m</i> log<sub><i>a</i></sub><i>x</i>')),
 ("1.7", "Change of base (printed in the same 1.7 box, no label)", nw(f'log<sub><i>a</i></sub><i>x</i> = {fr("log<sub><i>b</i></sub><i>x</i>","log<sub><i>b</i></sub><i>a</i>")}')),
 ("1.7", "Exponential and logarithmic functions", nw('<i>a</i><sup><i>x</i></sup> = e<sup><i>x</i> ln <i>a</i></sup>') + ' ; ' + nw('log<sub><i>a</i></sub><i>a</i><sup><i>x</i></sup> = <i>x</i> = <i>a</i><sup>log<sub><i>a</i></sub><i>x</i></sup>') + '<br><small>where <i>a</i>, <i>x</i> &gt; 0, <i>a</i> ≠ 1</small>'),
 ("1.9", "Binomial theorem <i>n</i> ∈ ℕ", nw('(<i>a</i> + <i>b</i>)<sup><i>n</i></sup> = <i>a</i><sup><i>n</i></sup> + <sup><i>n</i></sup>C<sub>1</sub><i>a</i><sup><i>n</i>−1</sup><i>b</i>') + ' ' + nw('+ … + <sup><i>n</i></sup>C<sub><i>r</i></sub><i>a</i><sup><i>n</i>−<i>r</i></sup><i>b</i><sup><i>r</i></sup>') + ' ' + nw('+ … + <i>b</i><sup><i>n</i></sup>') + '<br>' + nw(f'<sup><i>n</i></sup>C<sub><i>r</i></sub> = {fr("<i>n</i>!","<i>r</i>!(<i>n</i> − <i>r</i>)!")}')),
]
T1L = [
 ("SL 1.1", "Scientific notation", nw('<i>a</i> × 10<sup><i>k</i></sup>') + ' with ' + nw('1 ≤ <i>a</i> &lt; 10') + ' and <i>k</i> an integer. Calculator notation such as 5.2E30 scores nothing.',
  nw('0.000 340 2 = 3.402 × 10<sup>−4</sup>')),
 ("SL 1.2", "Finding <i>d</i> and counting terms", nw(f'{d_} = <i>u</i><sub>2</sub> − <i>u</i><sub>1</sub>') + '. With technology the IB still expects you to state the first term and <i>d</i>.',
  '7, 11, 15, … has <i>d</i> = 4, so ' + nw('<i>u</i><sub>20</sub> = 7 + 19 × 4 = 83') + '.'),
 ("SL 1.2, 1.3", "A term from the sum formula", nw(f'{un} = {Sn} − <i>S</i><sub><i>n</i>−1</sub>') + ' (and ' + nw(f'{u1} = <i>S</i><sub>1</sub>') + ').',
  'If ' + nw(f'{Sn} = <i>n</i><sup>2</sup> + 3<i>n</i>') + ', then ' + nw('<i>u</i><sub>5</sub> = <i>S</i><sub>5</sub> − <i>S</i><sub>4</sub> = 40 − 28 = 12') + '.'),
 ("SL 1.2, 1.3", "Sigma notation", 'Substitute each whole number from the bottom value to the top value and add. Number of terms = top − bottom + 1.',
  nw(f'{sig("<i>k</i>=1","4")}(2<i>k</i> + 1) = 3 + 5 + 7 + 9 = 24') + '.'),
 ("SL 1.3", "Finding the common ratio", nw(f'{r_} = {fr("<i>u</i><sub>2</sub>","<i>u</i><sub>1</sub>")}') + ' (any term divided by the one before).',
  '48, 12, 3, … has ' + nw(f'<i>r</i> = {fr("12","48")} = {fr("1","4")}') + '.'),
 ("SL 1.8", "Why the infinite sum exists: say it", 'The booklet prints the condition, but in a "justify" or "explain" part you must write it in words and numbers: "the sum exists because |<i>r</i>| &lt; 1". If <i>r</i> contains <i>x</i>, solve ' + nw('−1 &lt; <i>r</i> &lt; 1') + '.',
  nw('|<i>r</i>| = ¼ &lt; 1') + ', so ' + nw(f'<i>S</i><sub>∞</sub> = {fr("48","1 − ¼")} = 64') + '. If ' + nw(f'<i>r</i> = {fr("2<i>x</i>","3")}') + ', the sum exists for ' + nw(f'−{fr("3","2")} &lt; <i>x</i> &lt; {fr("3","2")}') + '.'),
 ("SL 1.4", "Depreciation", 'Value falls by <i>r</i>% a year: ' + nw('value = <i>PV</i> × (1 − <i>r</i>/100)<sup><i>n</i></sup>') + '. Not printed in this form; on the GDC finance app use a negative I%.',
  'A $20&nbsp;000 car losing 15% a year is worth ' + nw('20&nbsp;000 × 0.85<sup>3</sup> = $12&nbsp;282.50') + ' after 3 years.'),
 ("SL 1.4", "Real value with inflation", 'IB mark schemes usually take the real rate as interest rate minus inflation rate and use that as I%.',
  '$5000 at 4% a year with 2% inflation for 5 years: real rate 2%, ' + nw('5000 × 1.02<sup>5</sup> = $5520.40') + ' in today\'s money.'),
 ("SL 1.5", "Laws of exponents", nw('<i>a</i><sup><i>m</i></sup> × <i>a</i><sup><i>n</i></sup> = <i>a</i><sup><i>m</i>+<i>n</i></sup>') + ', ' + nw('<i>a</i><sup><i>m</i></sup> ÷ <i>a</i><sup><i>n</i></sup> = <i>a</i><sup><i>m</i>−<i>n</i></sup>') + ', ' + nw('(<i>a</i><sup><i>m</i></sup>)<sup><i>n</i></sup> = <i>a</i><sup><i>mn</i></sup>') + ', ' + nw(f'<i>a</i><sup>−<i>n</i></sup> = {fr("1","<i>a</i><sup><i>n</i></sup>")}') + ', ' + nw('<i>a</i><sup>0</sup> = 1') + '.',
  nw('5<sup>3</sup> × 5<sup>−6</sup> = 5<sup>−3</sup>') + ', ' + nw('(2<i>x</i>)<sup>4</sup> = 16<i>x</i><sup>4</sup>') + '.'),
 ("SL 1.5", "ln means base e", nw('log<sub>e</sub><i>x</i> = ln <i>x</i>') + ', and log with no base means base 10. You can only take the log of a positive number.',
  nw('ln e<sup>3</sup> = 3') + ', ' + nw('log 1000 = 3') + '.'),
 ("SL 1.7", "Fractional exponents", nw(f'<i>a</i><sup>1/<i>m</i></sup> = the <i>m</i>th root of <i>a</i>') + ' (the positive root when <i>m</i> is even); ' + nw('<i>a</i><sup><i>p</i>/<i>m</i></sup> = (<i>m</i>th root of <i>a</i>)<sup><i>p</i></sup>') + '.',
  nw('16<sup>3/4</sup> = (4th root of 16)<sup>3</sup> = 2<sup>3</sup> = 8') + '.'),
 ("SL 1.7", "Solving exponential equations", 'Take ln (or log) of both sides, bring the power down with the third log law, then solve.',
  nw('2<sup><i>x</i>−1</sup> = 10') + ' gives ' + nw(f'<i>x</i> − 1 = {fr("ln 10","ln 2")}') + ', so ' + nw('<i>x</i> ≈ 4.32') + '.'),
 ("SL 1.6", "Proof layout (LHS to RHS)", 'Start from one side only, change it step by step, end with "= RHS". Use ≡ for an identity (true for every <i>x</i>). Never work on both sides at once.',
  nw('LHS = (<i>x</i> − 3)<sup>2</sup> + 5') + ' ' + nw('= <i>x</i><sup>2</sup> − 6<i>x</i> + 9 + 5') + ' ' + nw('= <i>x</i><sup>2</sup> − 6<i>x</i> + 14 = RHS') + '.'),
 ("SL 1.9", "Pascal's triangle and picking out one term", 'Row 5 is 1, 5, 10, 10, 5, 1. The term with <i>b</i><sup><i>r</i></sup> uses <sup><i>n</i></sup>C<sub><i>r</i></sub>, which is the (<i>r</i> + 1)th term. Keep the coefficient inside the bracket when you raise it to a power.',
  'Coefficient of <i>x</i><sup>3</sup> in (2 + <i>x</i>)<sup>5</sup>: ' + nw('<sup>5</sup>C<sub>3</sub> × 2<sup>2</sup> = 10 × 4 = 40') + '.'),
]

T2B = [
 ("2.1", "Equations of a straight line", nw('<i>y</i> = <i>mx</i> + <i>c</i>') + ' ; ' + nw('<i>ax</i> + <i>by</i> + <i>d</i> = 0') + ' ; ' + nw('<i>y</i> − <i>y</i><sub>1</sub> = <i>m</i>(<i>x</i> − <i>x</i><sub>1</sub>)')),
 ("2.1", "Gradient formula", nw(f'<i>m</i> = {fr("<i>y</i><sub>2</sub> − <i>y</i><sub>1</sub>","<i>x</i><sub>2</sub> − <i>x</i><sub>1</sub>")}')),
 ("2.6", "Axis of symmetry of the graph of a quadratic function", nw('<i>f</i>(<i>x</i>) = <i>ax</i><sup>2</sup> + <i>bx</i> + <i>c</i> ⇒') + ' ' + nw(f'axis of symmetry is <i>x</i> = −{fr("<i>b</i>","2<i>a</i>")}')),
 ("2.7", "Solutions of a quadratic equation", nw('<i>ax</i><sup>2</sup> + <i>bx</i> + <i>c</i> = 0 ⇒') + ' ' + nw(f'<i>x</i> = {fr("−<i>b</i> ± "+sq("<i>b</i><sup>2</sup> − 4<i>ac</i>"),"2<i>a</i>")}, <i>a</i> ≠ 0')),
 ("2.7", "Discriminant", nw('Δ = <i>b</i><sup>2</sup> − 4<i>ac</i>') + '<br><small>Only the formula. What each sign of Δ means is not printed.</small>'),
]
T2L = [
 ("SL 2.1", "Parallel and perpendicular lines", 'Parallel: ' + nw('<i>m</i><sub>1</sub> = <i>m</i><sub>2</sub>') + '. Perpendicular: ' + nw('<i>m</i><sub>1</sub> × <i>m</i><sub>2</sub> = −1') + ' (negative reciprocal).',
  'A line perpendicular to ' + nw('<i>y</i> = 2<i>x</i> + 1') + ' has gradient ' + nw(f'−{fr("1","2")}') + '.'),
 ("SL 2.2", "Domain, range and inverse", 'Domain = allowed <i>x</i> values, range = output values. An inverse exists only for a one-to-one function; the domain of <i>f</i><sup> −1</sup> is the range of <i>f</i>; its graph is the reflection in <i>y</i> = <i>x</i>.',
  nw(f'<i>f</i>(<i>x</i>) = {sq("2 − <i>x</i>")}') + ' has domain ' + nw('<i>x</i> ≤ 2') + ' and range ' + nw('<i>f</i>(<i>x</i>) ≥ 0') + '.'),
 ("SL 2.5", "Composite and inverse functions", nw('(<i>f</i> ∘ <i>g</i>)(<i>x</i>) = <i>f</i>(<i>g</i>(<i>x</i>))') + ': apply <i>g</i> first. To find <i>f</i><sup> −1</sup>: write <i>y</i> = <i>f</i>(<i>x</i>), swap <i>x</i> and <i>y</i>, make <i>y</i> the subject. ' + nw('(<i>f</i> ∘ <i>f</i><sup> −1</sup>)(<i>x</i>) = <i>x</i>') + '.',
  '<i>f</i>(<i>x</i>) = 2<i>x</i> + 1, <i>g</i>(<i>x</i>) = <i>x</i><sup>2</sup>: ' + nw('(<i>f</i> ∘ <i>g</i>)(3) = <i>f</i>(9) = 19') + '; ' + nw(f'<i>f</i><sup> −1</sup>(<i>x</i>) = {fr("<i>x</i> − 1","2")}') + '.'),
 ("SL 2.6", "The three forms of a quadratic", '<i>y</i>-intercept (0, <i>c</i>). ' + nw('<i>a</i>(<i>x</i> − <i>p</i>)(<i>x</i> − <i>q</i>)') + ': <i>x</i>-intercepts <i>p</i> and <i>q</i>. ' + nw('<i>a</i>(<i>x</i> − <i>h</i>)<sup>2</sup> + <i>k</i>') + ': vertex (<i>h</i>, <i>k</i>). Watch the sign of <i>h</i>.',
  nw('2(<i>x</i> − 3)<sup>2</sup> + 1') + ' has vertex (3, 1); ' + nw('<i>x</i><sup>2</sup> + 6<i>x</i> + 5 = (<i>x</i> + 3)<sup>2</sup> − 4') + ' has vertex (−3, −4).'),
 ("SL 2.7", "What the discriminant tells you", nw('Δ &gt; 0') + ': two distinct real roots. ' + nw('Δ = 0') + ': two equal real roots (one repeated root). ' + nw('Δ &lt; 0') + ': no real roots. "Real roots" (not distinct) means ' + nw('Δ ≥ 0') + '.',
  nw('<i>x</i><sup>2</sup> + 4<i>x</i> + <i>k</i> = 0') + ' has equal roots when ' + nw('16 − 4<i>k</i> = 0') + ', so <i>k</i> = 4.'),
 ("SL 2.7", "Quadratic inequalities", 'Solve the equation first, sketch the parabola, then read off where it is above or below the axis.',
  nw('<i>x</i><sup>2</sup> − <i>x</i> − 6 &lt; 0') + ' ⇒ ' + nw('(<i>x</i> − 3)(<i>x</i> + 2) &lt; 0') + ' ⇒ ' + nw('−2 &lt; <i>x</i> &lt; 3') + '.'),
 ("SL 2.8", "Asymptotes of a rational function", 'For ' + nw(f'{fr("<i>ax</i> + <i>b</i>","<i>cx</i> + <i>d</i>")}') + ': vertical ' + nw(f'<i>x</i> = −{fr("<i>d</i>","<i>c</i>")}') + ', horizontal ' + nw(f'<i>y</i> = {fr("<i>a</i>","<i>c</i>")}') + '. ' + nw(f'<i>y</i> = {fr("1","<i>x</i>")}') + ' is its own inverse.',
  nw(f'<i>f</i>(<i>x</i>) = {fr("2<i>x</i> + 1","<i>x</i> − 3")}') + ' has asymptotes <i>x</i> = 3 and <i>y</i> = 2.'),
 ("SL 2.9", "Exponential and log graphs", nw('<i>y</i> = <i>a</i><sup><i>x</i></sup>') + ' passes through (0, 1) with asymptote <i>y</i> = 0; ' + nw('<i>y</i> = log<sub><i>a</i></sub><i>x</i>') + ' passes through (1, 0) with asymptote <i>x</i> = 0 and needs <i>x</i> &gt; 0. They are inverses (reflections in <i>y</i> = <i>x</i>).',
  nw('<i>y</i> = ln(<i>x</i> − 2)') + ' is defined only for <i>x</i> &gt; 2 and has asymptote <i>x</i> = 2.'),
 ("SL 2.10", "Hidden quadratics", 'Spot <i>a</i><sup>2<i>x</i></sup> = (<i>a</i><sup><i>x</i></sup>)<sup>2</sup>, factorise, then solve each bracket. When no algebra works, use the GDC.',
  nw('e<sup>2<i>x</i></sup> − 5e<sup><i>x</i></sup> + 4 = 0') + ' ⇒ ' + nw('(e<sup><i>x</i></sup> − 1)(e<sup><i>x</i></sup> − 4) = 0') + ' ⇒ <i>x</i> = 0 or ' + nw('<i>x</i> = ln 4') + '.'),
 ("SL 2.11", "Transformations", nw('<i>f</i>(<i>x</i>) + <i>b</i>') + ' up <i>b</i>; ' + nw('<i>f</i>(<i>x</i> − <i>a</i>)') + ' right <i>a</i>; ' + nw('−<i>f</i>(<i>x</i>)') + ' reflect in the <i>x</i>-axis; ' + nw('<i>f</i>(−<i>x</i>)') + ' reflect in the <i>y</i>-axis; ' + nw('<i>p</i> <i>f</i>(<i>x</i>)') + ' vertical stretch, factor <i>p</i>; ' + nw('<i>f</i>(<i>qx</i>)') + ' horizontal stretch, factor ' + nw(fr("1","<i>q</i>")) + '. Order matters.',
  'From <i>y</i> = <i>x</i><sup>2</sup> to ' + nw('<i>y</i> = 3<i>x</i><sup>2</sup> + 2') + ': vertical stretch factor 3, then translate up 2.'),
]

T3B = [
 ("Prior learning", "Area of a parallelogram; of a triangle; of a trapezoid", nw('<i>A</i> = <i>bh</i>') + ' ; ' + nw(f'<i>A</i> = {fr("1","2")}(<i>bh</i>)') + ' ; ' + nw(f'<i>A</i> = {fr("1","2")}(<i>a</i> + <i>b</i>)<i>h</i>')),
 ("Prior learning", "Area and circumference of a circle", nw('<i>A</i> = π<i>r</i><sup>2</sup>') + ' ; ' + nw('<i>C</i> = 2π<i>r</i>')),
 ("Prior learning", "Volume of a cuboid; cylinder; prism", nw('<i>V</i> = <i>lwh</i>') + ' ; ' + nw('<i>V</i> = π<i>r</i><sup>2</sup><i>h</i>') + ' ; ' + nw('<i>V</i> = <i>Ah</i>') + '<br><small><i>A</i> is the area of cross-section</small>'),
 ("Prior learning", "Area of the curved surface of a cylinder", nw('<i>A</i> = 2π<i>rh</i>')),
 ("Prior learning", "Distance and midpoint, two points in 2D", nw(f'<i>d</i> = {sq("(<i>x</i><sub>1</sub> − <i>x</i><sub>2</sub>)<sup>2</sup> + (<i>y</i><sub>1</sub> − <i>y</i><sub>2</sub>)<sup>2</sup>")}') + ' ; ' + nw(f'({fr("<i>x</i><sub>1</sub> + <i>x</i><sub>2</sub>","2")}, {fr("<i>y</i><sub>1</sub> + <i>y</i><sub>2</sub>","2")})')),
 ("3.1", "Distance and midpoint, two points in 3D", f'<span class="rt"><i>d</i>&nbsp;=&nbsp;√<span class="ov">(<i>x</i><sub>1</sub> − <i>x</i><sub>2</sub>)<sup>2</sup> + (<i>y</i><sub>1</sub> − <i>y</i><sub>2</sub>)<sup>2</sup> + (<i>z</i><sub>1</sub> − <i>z</i><sub>2</sub>)<sup>2</sup></span></span>' + ' ; ' + nw(f'({fr("<i>x</i><sub>1</sub> + <i>x</i><sub>2</sub>","2")}, {fr("<i>y</i><sub>1</sub> + <i>y</i><sub>2</sub>","2")}, {fr("<i>z</i><sub>1</sub> + <i>z</i><sub>2</sub>","2")})')),
 ("3.1", "Volume of a right-pyramid; of a right cone", nw(f'<i>V</i> = {fr("1","3")}<i>Ah</i>') + ' ; ' + nw(f'<i>V</i> = {fr("1","3")}π<i>r</i><sup>2</sup><i>h</i>')),
 ("3.1", "Area of the curved surface of a cone", nw('<i>A</i> = π<i>rl</i>') + '<br><small><i>l</i> is the slant height</small>'),
 ("3.1", "Volume of a sphere; surface area of a sphere", nw(f'<i>V</i> = {fr("4","3")}π<i>r</i><sup>3</sup>') + ' ; ' + nw('<i>A</i> = 4π<i>r</i><sup>2</sup>')),
 ("3.2", "Sine rule", nw(f'{fr("<i>a</i>","sin <i>A</i>")} = {fr("<i>b</i>","sin <i>B</i>")} = {fr("<i>c</i>","sin <i>C</i>")}')),
 ("3.2", "Cosine rule", nw('<i>c</i><sup>2</sup> = <i>a</i><sup>2</sup> + <i>b</i><sup>2</sup> − 2<i>ab</i> cos <i>C</i>') + ' ; ' + nw(f'cos <i>C</i> = {fr("<i>a</i><sup>2</sup> + <i>b</i><sup>2</sup> − <i>c</i><sup>2</sup>","2<i>ab</i>")}')),
 ("3.2", "Area of a triangle", nw(f'<i>A</i> = {fr("1","2")}<i>ab</i> sin <i>C</i>')),
 ("3.4", "Length of an arc; area of a sector", nw('<i>l</i> = <i>rθ</i>') + ' ; ' + nw(f'<i>A</i> = {fr("1","2")}<i>r</i><sup>2</sup><i>θ</i>') + '<br><small><i>θ</i> measured in radians</small>'),
 ("3.5", "Identity for tan <i>θ</i>", nw(f'tan <i>θ</i> = {fr("sin <i>θ</i>","cos <i>θ</i>")}')),
 ("3.6", "Pythagorean identity", nw('cos<sup>2</sup><i>θ</i> + sin<sup>2</sup><i>θ</i> = 1')),
 ("3.6", "Double angle identities", nw('sin 2<i>θ</i> = 2 sin <i>θ</i> cos <i>θ</i>') + '<br>' + nw('cos 2<i>θ</i> = cos<sup>2</sup><i>θ</i> − sin<sup>2</sup><i>θ</i>') + ' ' + nw('= 2cos<sup>2</sup><i>θ</i> − 1') + ' ' + nw('= 1 − 2sin<sup>2</sup><i>θ</i>')),
]
T3L = [
 ("SL 3.2", "Right-angled triangles", 'Pythagoras ' + nw('<i>a</i><sup>2</sup> + <i>b</i><sup>2</sup> = <i>c</i><sup>2</sup>') + ' and SOH CAH TOA: ' + nw('sin = opp/hyp') + ', ' + nw('cos = adj/hyp') + ', ' + nw('tan = opp/adj') + '.',
  'Hypotenuse 10, angle 30°: opposite side ' + nw('= 10 sin 30° = 5') + '.'),
 ("SL 3.1", "Hemispheres and total surface areas", 'Only curved surfaces are printed. Add the flat faces yourself. A hemisphere is half a sphere: ' + nw(f'<i>V</i> = {fr("2","3")}π<i>r</i><sup>3</sup>') + ', a solid one has ' + nw('<i>A</i> = 2π<i>r</i><sup>2</sup> + π<i>r</i><sup>2</sup> = 3π<i>r</i><sup>2</sup>') + '.',
  'Solid cone, <i>r</i> = 3, <i>l</i> = 5: ' + nw('15π + 9π = 24π ≈ 75.4') + '. Hemisphere, <i>r</i> = 3: ' + nw('<i>V</i> = 18π ≈ 56.5') + '.'),
 ("SL 3.1", "Angle between a line and a plane", 'Drop a perpendicular from the line to the plane; the angle is in the right-angled triangle formed by the line and its shadow (projection) on the plane.',
  'Box 3 by 4 by 12: base diagonal 5, angle of the space diagonal with the base ' + nw('= tan<sup>−1</sup>(12/5) ≈ 67.4°') + '.'),
 ("SL 3.3", "Bearings, elevation, depression", 'Bearings: clockwise from north, three figures (045°). Elevation and depression are measured from the horizontal.',
  'From 64.3 m away, a 30 m tower has elevation ' + nw('tan<sup>−1</sup>(30/64.3) ≈ 25°') + '.'),
 ("SL 3.4", "Radians", nw('π rad = 180°') + '. Arc and sector formulas only work in radians. Area of a segment = sector − triangle ' + nw(f'= {fr("1","2")}<i>r</i><sup>2</sup><i>θ</i> − {fr("1","2")}<i>r</i><sup>2</sup> sin <i>θ</i>') + '.',
  nw(f'60° = {fr("π","3")}') + '. Segment with <i>r</i> = 6, <i>θ</i> = π/3: ' + nw('6π − 9√3 ≈ 3.26') + '.'),
 ("SL 3.5", "Exact values", '<span class="nw">sin: 0, ½, √2/2, √3/2, 1</span> for 0, π/6, π/4, π/3, π/2. <span class="nw">cos: the same list backwards.</span> <span class="nw">tan: 0, √3/3, 1, √3, undefined.</span>',
  nw('sin(π/3) = √3/2') + ', ' + nw('cos(3π/4) = −√2/2') + ', ' + nw('tan 210° = √3/3') + '.'),
 ("SL 3.5", "Unit circle and quadrants", 'A point on the unit circle is (cos <i>θ</i>, sin <i>θ</i>). Positive in quadrants 1 to 4: all, sin, tan, cos. Symmetries: ' + nw('sin(π − <i>θ</i>) = sin <i>θ</i>') + ', ' + nw('cos(−<i>x</i>) = cos <i>x</i>') + ', ' + nw('sin(π + <i>x</i>) = −sin <i>x</i>') + '.',
  'The line through the origin at angle <i>θ</i> to the positive <i>x</i>-axis is ' + nw('<i>y</i> = <i>x</i> tan <i>θ</i>') + '.'),
 ("SL 3.5", "Ambiguous case of the sine rule", 'Given two sides and an angle not between them, sin <i>B</i> gives two angles, <i>B</i> and 180° − <i>B</i>. Keep both if the angles still add to less than 180°.',
  '<i>A</i> = 30°, <i>a</i> = 6, <i>b</i> = 10: ' + nw('sin <i>B</i> = 0.833') + ', so <i>B</i> ≈ 56.4° or 123.6°.'),
 ("SL 3.6", "Using the identities without finding <i>θ</i>", 'Get the missing ratio from ' + nw('cos<sup>2</sup> + sin<sup>2</sup> = 1') + ', then choose the sign from the quadrant.',
  nw(f'cos <i>x</i> = {fr("3","4")}') + ', <i>x</i> acute: ' + nw(f'sin <i>x</i> = {fr("√7","4")}') + ', ' + nw(f'sin 2<i>x</i> = 2 × {fr("√7","4")} × {fr("3","4")} = {fr("3√7","8")}') + '.'),
 ("SL 3.7", "Graphs of sin, cos, tan", 'For ' + nw('<i>a</i> sin(<i>b</i>(<i>x</i> + <i>c</i>)) + <i>d</i>') + ': amplitude |<i>a</i>|, period ' + nw(f'{fr("2π","<i>b</i>")}') + ' (or 360°/<i>b</i>), shift <i>c</i> to the left, principal axis <i>y</i> = <i>d</i>. tan has period π.',
  nw('<i>y</i> = 3 sin 2<i>x</i> + 1') + ': amplitude 3, period π, maximum 4, minimum −2.'),
 ("SL 3.8", "Solving trig equations in an interval", 'Find the first solution, use symmetry for the second, then add periods until you leave the interval. For sin 2<i>x</i> first double the interval.',
  nw('2 sin <i>x</i> = 1') + ', ' + nw('0 ≤ <i>x</i> ≤ 2π') + ': ' + nw('<i>x</i> = π/6') + ' or ' + nw('5π/6') + '.'),
]

T4B = [
 ("4.2", "Interquartile range", nw('IQR = Q<sub>3</sub> − Q<sub>1</sub>')),
 ("4.3", "Mean, <i>x̄</i>, of a set of data", nw(f'<i>x̄</i> = {fr(sig("<i>i</i>=1","<i>k</i>")+"<i>f</i><sub><i>i</i></sub><i>x</i><sub><i>i</i></sub>","<i>n</i>")}') + ', ' + nw(f'where <i>n</i> = {sig("<i>i</i>=1","<i>k</i>")}<i>f</i><sub><i>i</i></sub>')),
 ("4.5", "Probability of an event <i>A</i>", nw(f'P(<i>A</i>) = {fr("<i>n</i>(<i>A</i>)","<i>n</i>(<i>U</i>)")}')),
 ("4.5", "Complementary events", nw('P(<i>A</i>) + P(<i>A</i>′) = 1')),
 ("4.6", "Combined events", nw('P(<i>A</i> ∪ <i>B</i>) = P(<i>A</i>) + P(<i>B</i>) − P(<i>A</i> ∩ <i>B</i>)')),
 ("4.6", "Mutually exclusive events", nw('P(<i>A</i> ∪ <i>B</i>) = P(<i>A</i>) + P(<i>B</i>)')),
 ("4.6", "Conditional probability", nw(f'P(<i>A</i> | <i>B</i>) = {fr("P(<i>A</i> ∩ <i>B</i>)","P(<i>B</i>)")}')),
 ("4.6", "Independent events", nw('P(<i>A</i> ∩ <i>B</i>) = P(<i>A</i>) P(<i>B</i>)')),
 ("4.7", "Expected value of a discrete random variable <i>X</i>", nw(f'E(<i>X</i>) = {sig("<i>i</i>=1","<i>k</i>")}<i>x</i><sub><i>i</i></sub> P(<i>X</i> = <i>x</i><sub><i>i</i></sub>)')),
 ("4.8", "Binomial distribution <i>X</i> ~ B(<i>n</i>, <i>p</i>): mean and variance", nw('E(<i>X</i>) = <i>np</i>') + ' ; ' + nw('Var(<i>X</i>) = <i>np</i>(1 − <i>p</i>)')),
 ("4.12", "Standardized normal variable", nw(f'<i>z</i> = {fr("<i>x</i> − <i>μ</i>","<i>σ</i>")}')),
]
T4L = [
 ("SL 4.1", "Outliers", 'An outlier is more than ' + nw('1.5 × IQR') + ' from the nearest quartile. Some outliers are real data, some are errors: say which in context.',
  'Q<sub>1</sub> = 10, Q<sub>3</sub> = 18, IQR = 8: outliers are below ' + nw('10 − 12 = −2') + ' or above ' + nw('18 + 12 = 30') + '.'),
 ("SL 4.1", "Data and sampling words", 'Discrete (counted) or continuous (measured). Sampling: simple random, convenience, systematic (every <i>k</i>th), quota, stratified (in proportion to each group).',
  'Stratified sample of 50 from 600 boys and 400 girls: ' + nw('50 × 600/1000 = 30') + ' boys and 20 girls.'),
 ("SL 4.2", "Reading cumulative frequency and box plots", 'Median at <i>n</i>/2, Q<sub>1</sub> at <i>n</i>/4, Q<sub>3</sub> at 3<i>n</i>/4 on the cumulative frequency graph. Mark outliers with a cross. A symmetric box and whiskers suggests the data may be normal.',
  'With 80 values, read the median at a cumulative frequency of 40.'),
 ("SL 4.3", "Grouped data", 'Estimate the mean with mid-interval values. Modal class = class with the highest frequency (equal widths only).',
  'The class 10 ≤ <i>x</i> &lt; 20 uses the mid-interval value 15.'),
 ("SL 4.3", "Standard deviation and variance", 'Found with the GDC only, no formula given. Variance = (standard deviation)<sup>2</sup>.',
  'Standard deviation 1.5 means variance ' + nw('1.5<sup>2</sup> = 2.25') + '.'),
 ("SL 4.3", "Changing every data item", 'Adding <i>c</i>: mean + <i>c</i>, standard deviation unchanged. Multiplying by <i>k</i>: mean × <i>k</i>, standard deviation × <i>k</i> (for positive <i>k</i>).',
  'Mean 12, sd 3. Double then add 5: mean ' + nw('2 × 12 + 5 = 29') + ', sd ' + nw('2 × 3 = 6') + '.'),
 ("SL 4.4", "Correlation and regression", '<i>r</i> from the GDC, ' + nw('−1 ≤ <i>r</i> ≤ 1') + ', only meaningful for linear data. Correlation does not imply causation. The <i>y</i> on <i>x</i> line passes through (<i>x̄</i>, <i>ȳ</i>), predicts <i>y</i> from <i>x</i> only, and extrapolation is unreliable.',
  'For ' + nw('<i>y</i> = 2.5<i>x</i> + 40') + ' (marks against hours): each extra hour adds about 2.5 marks; 40 is the predicted mark for 0 hours.'),
 ("SL 4.10", "Regression line of <i>x</i> on <i>y</i>", 'Use the <i>x</i> on <i>y</i> line (GDC) to predict <i>x</i> from a given <i>y</i>. Do not rearrange the <i>y</i> on <i>x</i> line.',
  'To estimate hours studied from a mark of 70, use the <i>x</i> on <i>y</i> line.'),
 ("SL 4.5", "Expected number of occurrences", nw('expected number = <i>n</i> × P(<i>A</i>)') + '. It need not be a whole number.',
  nw('128 × 0.1 = 12.8') + ' students expected to be absent.'),
 ("SL 4.6", "Mutually exclusive, trees, replacement", 'Mutually exclusive means ' + nw('P(<i>A</i> ∩ <i>B</i>) = 0') + '. "Or" includes both. Multiply along tree branches, add the branches you want. Without replacement the second fraction changes.',
  'Two reds without replacement from 5 red and 3 blue: ' + nw(f'{fr("5","8")} × {fr("4","7")} = {fr("5","14")}') + '.'),
 ("SL 4.11", "Testing for independence", 'Show ' + nw('P(<i>A</i> ∩ <i>B</i>) = P(<i>A</i>)P(<i>B</i>)') + ', or ' + nw('P(<i>A</i> | <i>B</i>) = P(<i>A</i>) = P(<i>A</i> | <i>B</i>′)') + '. Also ' + nw('P(<i>A</i> ∩ <i>B</i>) = P(<i>B</i>)P(<i>A</i> | <i>B</i>)') + '.',
  'P(<i>A</i>) = 0.4, P(<i>B</i>) = 0.5, P(<i>A</i> ∩ <i>B</i>) = 0.2: ' + nw('0.4 × 0.5 = 0.2') + ', so independent.'),
 ("SL 4.7", "Probability distributions", 'The probabilities add up to 1. E(<i>X</i>) = 0 means a fair game when <i>X</i> is the gain.',
  'P(<i>X</i> = <i>x</i>) = 0.1, 0.2, <i>k</i>, 0.3 gives ' + nw('<i>k</i> = 0.4') + '.'),
 ("SL 4.8", "When binomial, and how to use the GDC", 'Fixed number of trials, two outcomes, constant <i>p</i>, independent trials. pdf for "exactly", cdf for "at most". "At least 3" is ' + nw('1 − P(<i>X</i> ≤ 2)') + '. Standard deviation is √Var(<i>X</i>).',
  '<i>X</i> ~ B(10, 0.3): ' + nw('P(<i>X</i> ≥ 3) = 1 − P(<i>X</i> ≤ 2) ≈ 0.617') + '; ' + nw('sd = √2.1 ≈ 1.45') + '.'),
 ("SL 4.9", "Normal distribution facts", 'About 68% within <i>μ</i> ± <i>σ</i>, 95% within <i>μ</i> ± 2<i>σ</i>, 99.7% within <i>μ</i> ± 3<i>σ</i>. Probabilities and inverse normal values come from the GDC; sketch and shade first.',
  '<i>μ</i> = 50, <i>σ</i> = 5: about 95% of values lie between 40 and 60.'),
 ("SL 4.12", "Unknown mean or standard deviation", '<i>z</i> is the number of standard deviations from the mean. Get <i>z</i> from inverse normal with mean 0 and sd 1, then put it into the booklet formula.',
  'P(<i>X</i> &lt; 60) = 0.9, <i>σ</i> = 5: <i>z</i> ≈ 1.2816, so ' + nw('<i>μ</i> = 60 − 1.2816 × 5 ≈ 53.6') + '.'),
]

T5B = [
 ("5.3", "Derivative of <i>x</i><sup><i>n</i></sup>", nw('<i>f</i>(<i>x</i>) = <i>x</i><sup><i>n</i></sup> ⇒ <i>f</i> ′(<i>x</i>) = <i>nx</i><sup><i>n</i>−1</sup>')),
 ("5.6", "Derivative of sin <i>x</i>", nw('<i>f</i>(<i>x</i>) = sin <i>x</i> ⇒ <i>f</i> ′(<i>x</i>) = cos <i>x</i>')),
 ("5.6", "Derivative of cos <i>x</i>", nw('<i>f</i>(<i>x</i>) = cos <i>x</i> ⇒ <i>f</i> ′(<i>x</i>) = −sin <i>x</i>')),
 ("5.6", "Derivative of e<sup><i>x</i></sup>", nw('<i>f</i>(<i>x</i>) = e<sup><i>x</i></sup> ⇒ <i>f</i> ′(<i>x</i>) = e<sup><i>x</i></sup>')),
 ("5.6", "Derivative of ln <i>x</i>", nw(f'<i>f</i>(<i>x</i>) = ln <i>x</i> ⇒ <i>f</i> ′(<i>x</i>) = {fr("1","<i>x</i>")}')),
 ("5.6", "Chain rule", nw('<i>y</i> = <i>g</i>(<i>u</i>), where <i>u</i> = <i>f</i>(<i>x</i>)') + ' ' + nw(f'⇒ {fr("d<i>y</i>","d<i>x</i>")} = {fr("d<i>y</i>","d<i>u</i>")} × {fr("d<i>u</i>","d<i>x</i>")}')),
 ("5.6", "Product rule", nw(f'<i>y</i> = <i>uv</i> ⇒ {fr("d<i>y</i>","d<i>x</i>")} = <i>u</i>{fr("d<i>v</i>","d<i>x</i>")} + <i>v</i>{fr("d<i>u</i>","d<i>x</i>")}')),
 ("5.6", "Quotient rule", nw(f'<i>y</i> = {fr("<i>u</i>","<i>v</i>")} ⇒ {fr("d<i>y</i>","d<i>x</i>")} = ' + fr(f'<i>v</i>{fr("d<i>u</i>","d<i>x</i>")} − <i>u</i>{fr("d<i>v</i>","d<i>x</i>")}', '<i>v</i><sup>2</sup>'))),
 ("5.9", "Acceleration", nw(f'<i>a</i> = {fr("d<i>v</i>","d<i>t</i>")} = {fr("d<sup>2</sup><i>s</i>","d<i>t</i><sup>2</sup>")}')),
 ("5.9", "Distance travelled from <i>t</i><sub>1</sub> to <i>t</i><sub>2</sub>", nw(f'distance = <span class="intg">∫</span>{lim("<i>t</i><sub>1</sub>","<i>t</i><sub>2</sub>")}|<i>v</i>(<i>t</i>)| d<i>t</i>')),
 ("5.9", "Displacement from <i>t</i><sub>1</sub> to <i>t</i><sub>2</sub>", nw(f'displacement = <span class="intg">∫</span>{lim("<i>t</i><sub>1</sub>","<i>t</i><sub>2</sub>")}<i>v</i>(<i>t</i>) d<i>t</i>')),
 ("5.5", "Integral of <i>x</i><sup><i>n</i></sup>", nw(f'∫<i>x</i><sup><i>n</i></sup> d<i>x</i> = {fr("<i>x</i><sup><i>n</i>+1</sup>","<i>n</i> + 1")} + <i>C</i>, <i>n</i> ≠ −1')),
 ("5.5", "Area between a curve <i>y</i> = <i>f</i>(<i>x</i>) and the <i>x</i>-axis, where <i>f</i>(<i>x</i>) &gt; 0", nw(f'<i>A</i> = <span class="intg">∫</span>{lim("<i>a</i>","<i>b</i>")}<i>y</i> d<i>x</i>')),
 ("5.10", "Standard integrals", nw(f'∫{fr("1","<i>x</i>")} d<i>x</i> = ln|<i>x</i>| + <i>C</i>') + ' ; ' + nw('∫sin <i>x</i> d<i>x</i> = −cos <i>x</i> + <i>C</i>') + ' ; ' + nw('∫cos <i>x</i> d<i>x</i> = sin <i>x</i> + <i>C</i>') + ' ; ' + nw('∫e<sup><i>x</i></sup> d<i>x</i> = e<sup><i>x</i></sup> + <i>C</i>')),
 ("5.11", "Area of region enclosed by a curve and <i>x</i>-axis", nw(f'<i>A</i> = <span class="intg">∫</span>{lim("<i>a</i>","<i>b</i>")}|<i>y</i>| d<i>x</i>')),
]
T5L = [
 ("SL 5.1, 5.2", "What the derivative means", 'Gradient of the tangent and rate of change. ' + nw('<i>f</i> ′(<i>x</i>) &gt; 0') + ': increasing; ' + nw('<i>f</i> ′(<i>x</i>) &lt; 0') + ': decreasing.',
  nw('<i>f</i>(<i>x</i>) = <i>x</i><sup>2</sup> − 4<i>x</i>') + ': ' + nw('<i>f</i> ′(<i>x</i>) = 2<i>x</i> − 4 &gt; 0') + ' for <i>x</i> &gt; 2, so increasing there.'),
 ("SL 5.3, 5.6", "Rewrite as powers first", 'Turn roots and fractions into powers of <i>x</i> before using the <i>x</i><sup><i>n</i></sup> rule. A constant multiple stays in front.',
  nw(f'<i>y</i> = {fr("3","<i>x</i><sup>2</sup>")} = 3<i>x</i><sup>−2</sup>') + ' ⇒ ' + nw(f'{fr("d<i>y</i>","d<i>x</i>")} = −6<i>x</i><sup>−3</sup>') + '.'),
 ("SL 5.4", "Tangents and normals", 'Tangent gradient ' + nw('<i>m</i> = <i>f</i> ′(<i>a</i>)') + ', line through (<i>a</i>, <i>f</i>(<i>a</i>)). Normal gradient ' + nw(f'−{fr("1","<i>m</i>")}') + '.',
  '<i>y</i> = <i>x</i><sup>2</sup> at <i>x</i> = 3: tangent ' + nw('<i>y</i> = 6<i>x</i> − 9') + ', normal ' + nw(f'<i>y</i> − 9 = −{fr("1","6")}(<i>x</i> − 3)') + '.'),
 ("SL 5.6", "Chain rule patterns to recognise", nw('e<sup><i>f</i>(<i>x</i>)</sup> → <i>f</i> ′(<i>x</i>)e<sup><i>f</i>(<i>x</i>)</sup>') + '; ' + nw(f'ln <i>f</i>(<i>x</i>) → {fr("<i>f</i> ′(<i>x</i>)","<i>f</i>(<i>x</i>)")}') + '; ' + nw('sin(<i>ax</i> + <i>b</i>) → <i>a</i> cos(<i>ax</i> + <i>b</i>)') + '. Only the general chain rule is printed.',
  nw('<i>y</i> = e<sup><i>x</i><sup>2</sup> + 2</sup>') + ' ⇒ ' + nw(f'{fr("d<i>y</i>","d<i>x</i>")} = 2<i>x</i> e<sup><i>x</i><sup>2</sup> + 2</sup>') + '.'),
 ("Not SL", "Derivative of tan <i>x</i>", 'Not in the SL booklet and not on the SL list (SL 5.6 lists <i>x</i><sup><i>n</i></sup>, sin, cos, e<sup><i>x</i></sup>, ln). It is HL content (AHL 5.15). If an SL question needs it, write tan <i>x</i> = sin <i>x</i>/cos <i>x</i> (in the booklet, 3.5) and use the quotient rule.',
  'Quotient rule gives ' + nw(f'{fr("1","cos<sup>2</sup><i>x</i>")}') + ', which equals 2 at <i>x</i> = π/4.'),
 ("SL 5.7, 5.8", "Stationary points and their nature", 'Solve ' + nw('<i>f</i> ′(<i>x</i>) = 0') + '. ' + nw('<i>f</i> ″ &gt; 0') + ': minimum (concave-up). ' + nw('<i>f</i> ″ &lt; 0') + ': maximum (concave-down). If <i>f</i> ″ = 0, test the sign of <i>f</i> ′ either side.',
  nw('<i>y</i> = <i>x</i><sup>3</sup> − 3<i>x</i>') + ': ' + nw('<i>y</i>′ = 3<i>x</i><sup>2</sup> − 3 = 0') + ' at <i>x</i> = ±1; ' + nw('<i>y</i>″ = 6<i>x</i>') + ' gives a minimum at (1, −2), a maximum at (−1, 2).'),
 ("SL 5.8", "Points of inflexion", nw('<i>f</i> ″(<i>x</i>) = 0') + ' and <i>f</i> ″ changes sign (concavity changes). <i>f</i> ″ = 0 alone is not enough.',
  nw('<i>y</i> = <i>x</i><sup>4</sup>') + ' has <i>y</i>″ = 0 at (0, 0) but no change of sign: it is a minimum, not an inflexion.'),
 ("SL 5.8", "Optimisation", 'Write the quantity in one variable, differentiate, set equal to 0, check it is a maximum or minimum, answer the question asked.',
  'Rectangle with perimeter 20: ' + nw('<i>A</i> = <i>x</i>(10 − <i>x</i>)') + ', ' + nw('<i>A</i>′ = 10 − 2<i>x</i> = 0') + ', <i>x</i> = 5, largest area 25.'),
 ("SL 5.9", "Velocity and speed", nw(f'<i>v</i> = {fr("d<i>s</i>","d<i>t</i>")}') + ' is not printed (only <i>a</i> is). Speed = |<i>v</i>|. At rest when <i>v</i> = 0; changes direction when <i>v</i> changes sign.',
  nw('<i>s</i> = <i>t</i><sup>3</sup> − 6<i>t</i><sup>2</sup>') + ' ⇒ ' + nw('<i>v</i> = 3<i>t</i><sup>2</sup> − 12<i>t</i>') + ', at rest when <i>t</i> = 0 or 4.'),
 ("SL 5.5", "Finding the constant <i>C</i>", 'Integrate, then substitute the given point to find <i>C</i>.',
  nw(f'{fr("d<i>y</i>","d<i>x</i>")} = 3<i>x</i><sup>2</sup> + <i>x</i>') + ', <i>y</i> = 10 at <i>x</i> = 1 ⇒ ' + nw(f'<i>y</i> = <i>x</i><sup>3</sup> + {fr("1","2")}<i>x</i><sup>2</sup> + 8.5') + '.'),
 ("SL 5.10", "Integrals of (<i>ax</i> + <i>b</i>) composites", 'Integrate as usual and divide by <i>a</i>: ' + nw(f'∫cos(<i>ax</i> + <i>b</i>) d<i>x</i> = {fr("1","<i>a</i>")}sin(<i>ax</i> + <i>b</i>) + <i>C</i>') + ', same for e<sup><i>ax</i>+<i>b</i></sup> and ' + nw(f'{fr("1","<i>ax</i> + <i>b</i>")}') + '.',
  nw(f'<i>f</i> ′(<i>x</i>) = cos(2<i>x</i> + 3) ⇒ <i>f</i>(<i>x</i>) = {fr("1","2")}sin(2<i>x</i> + 3) + <i>C</i>') + '.'),
 ("SL 5.10", "Reverse chain rule (inspection)", 'If the derivative of the inside bracket is (a multiple of) the factor outside, integrate the bracket as a power.',
  nw(f'∫2<i>x</i>(<i>x</i><sup>2</sup> + 1)<sup>4</sup> d<i>x</i> = {fr("(<i>x</i><sup>2</sup> + 1)<sup>5</sup>","5")} + <i>C</i>') + '.'),
 ("SL 5.11", "Definite integrals by hand", nw(f'<span class="intg">∫</span>{lim("<i>a</i>","<i>b</i>")}<i>g</i> ′(<i>x</i>) d<i>x</i> = <i>g</i>(<i>b</i>) − <i>g</i>(<i>a</i>)') + ' (no +<i>C</i>).',
  nw('<span class="intg">∫</span>' + lim('0','2') + '(3<i>x</i><sup>2</sup> + 1) d<i>x</i> = [<i>x</i><sup>3</sup> + <i>x</i>]' + lim('0','2') + ' = 10') + '.'),
 ("SL 5.11", "Areas below the axis and between curves", 'An integral below the <i>x</i>-axis is negative: split at the roots and add the sizes. Between curves: ' + nw('∫(top − bottom) d<i>x</i>') + ', which is not printed.',
  nw('<span class="intg">∫</span>' + lim('0','2') + '(<i>x</i><sup>2</sup> − 4) d<i>x</i> = −16/3') + ', so the area is 16/3. Between <i>y</i> = <i>x</i> and <i>y</i> = <i>x</i><sup>2</sup>: ' + nw('<span class="intg">∫</span>' + lim('0','1') + '(<i>x</i> − <i>x</i><sup>2</sup>) d<i>x</i> = 1/6') + '.'),
]

TOPICS = (topic("t1", "Topic 1: Number and algebra", "Sequences, finance, exponents and logs, binomial expansion.", T1B, T1L)
  + topic("t2", "Topic 2: Functions", "Lines, quadratics, function language, graphs and transformations. The booklet gives only five lines here, so most of this topic is learned.", T2B, T2L)
  + topic("t3", "Topic 3: Geometry and trigonometry", 'The booklet starts this topic with a "Prior learning" box of basic areas and volumes. No exact values and no unit circle facts are printed.', T3B, T3L)
  + topic("t4", "Topic 4: Statistics and probability", "Most of this topic is done on the GDC, so the learn column is mostly about which button and which words.", T4B, T4L)
  + topic("t5", "Topic 5: Calculus", "The booklet gives the standard derivatives and integrals; using them (tangents, stationary points, areas) is all learned. The booklet prints 5.9 before 5.5 and 5.10: that is its real order.", T5B, T5L))

maths_body = f'''
<div class="legend" aria-label="Legend for the formula markers">
  <span><span class="fb" style="margin-left:0">In booklet</span> printed in the formula booklet you get in both papers: know how to use it, no need to memorise it</span>
  <span><span class="learn" style="margin-left:0">Learn</span> not in the booklet: you must remember it</span>
</div>
<p>Left column: exactly what the SL formula booklet prints, with its own section numbers and labels (they match the official syllabus numbers, so 1.8 sits next to 1.3). Right column: what the official syllabus expects you to know that the booklet does not print, each with a one-line example. <a href="{DRIVE('19EX75prXgep28AagsDaWsr3eM6O8rVDV')}">Open the booklet</a> next to this page the first time you read it.</p>
<div class="tip"><b>Five surprises.</b> Change of base <b>is</b> in the booklet (1.7). The <sup><i>n</i></sup>C<sub><i>r</i></sub> formula <b>is</b> in the booklet (1.9). The discriminant formula is printed but <b>not</b> what Δ &gt; 0, = 0, &lt; 0 mean. Velocity <i>v</i> = d<i>s</i>/d<i>t</i> is <b>not</b> printed (only acceleration). Exact trig values, laws of exponents and standard deviation are <b>not</b> printed.</div>
<ul class="toc">
  <li><a href="#t1">1 Number and algebra</a></li><li><a href="#t2">2 Functions</a></li><li><a href="#t3">3 Geometry and trigonometry</a></li><li><a href="#t4">4 Statistics and probability</a></li><li><a href="#t5">5 Calculus</a></li>
</ul>
{TOPICS}
<p class="note" style="margin-top:28px">Sources: the IB Mathematics: analysis and approaches SL formula booklet (first examinations 2021, version 1.0), <a href="{DRIVE('19EX75prXgep28AagsDaWsr3eM6O8rVDV')}">in your folder</a>, checked against the printed pages; the "learn" items come from the SL content statements in the <a href="{DRIVE('19usrPWgR-_yAbEtM2QeF8vHtOR691ZXw')}">IB Maths AA subject guide</a>. Exam habits: <a href="exam-maths-aa-sl.html">Exam technique: Maths AA SL</a>.</p>
'''
maths_comment = '''<!-- given-maths-aa-sl: built by tools/given.py.
Booklet: IB Maths AA SL formula booklet, first examinations 2021, version 1.0 (c) IBO 2023, Drive 19EX75prXgep28AagsDaWsr3eM6O8rVDV.
Read from the PDF with pdftotext -layout AND the rendered page images, because the Drive text loses modulus bars
(|r| < 1 in 1.8, |v(t)| in 5.9, ln|x| in 5.10, |y| in 5.11) and fraction bars. All five were confirmed on the images.
Uncertain / judgement calls:
 - SL 1.4 real value: "real rate = interest rate minus inflation rate" is the approximation used in IB mark schemes as far as I know;
   the guide only says "Calculate the real value of an investment with an interest rate and an inflation rate". Exact method
   (divide by 1.02^5) gives 5509.80 instead of 5520.40 for the example.
 - SL 3.5 quadrant mnemonic (all, sin, tan, cos) is standard teaching, not guide wording.
 - Derivative of tan x: SL 5.6 lists only x^n, sin x, cos x, e^x, ln x; tan x is in AHL 5.15.
-->
'''

html = build("Given or learn: Maths AA SL", "Given or learn: Maths AA SL",
             "For every SL topic: what the formula booklet gives you, and what you must carry in your head.", maths_body)
html = html.replace("<main", maths_comment + "<main", 1)
open(out + '/given-maths-aa-sl.html', 'w').write(html)

# ================= BUSINESS MANAGEMENT =================
def sheet(name, formula, steps):
    li = ''.join(f'<li>{s}</li>' for s in steps)
    return f'<div class="sheet"><span class="lab">{name}</span> <span class="fb">On formula sheet</span><div class="fm">{formula}</div><div class="eg"><b>Worked example</b></div><ol>{li}</ol></div>'

case = 'Harbour Bikes Ltd (made-up figures): sales revenue $500&nbsp;000, cost of sales $300&nbsp;000, expenses $120&nbsp;000, current assets $90&nbsp;000 (of which stock $30&nbsp;000), current liabilities $60&nbsp;000, non-current liabilities $150&nbsp;000, equity $250&nbsp;000.'
SHEET_ITEMS = [
 ("Gross profit margin (GPM)", f'GPM = {fr("gross profit","sales revenue")} × 100%',
  ['Gross profit = sales revenue − cost of sales = ' + nw('$500&nbsp;000 − $300&nbsp;000 = $200&nbsp;000'),
   nw(f'GPM = {fr("200&nbsp;000","500&nbsp;000")} × 100% = 40%')]),
 ("Profit margin", f'profit margin = {fr("profit before interest and tax","sales revenue")} × 100%',
  ['Profit before interest and tax = gross profit − expenses = ' + nw('$200&nbsp;000 − $120&nbsp;000 = $80&nbsp;000'),
   nw(f'Profit margin = {fr("80&nbsp;000","500&nbsp;000")} × 100% = 16%')]),
 ("Return on capital employed (ROCE)", f'ROCE = {fr("profit before interest and tax","capital employed")} × 100%' + '<br><small>where capital employed = non-current liabilities + equity (printed on the sheet)</small>',
  ['Capital employed = ' + nw('$150&nbsp;000 + $250&nbsp;000 = $400&nbsp;000'),
   nw(f'ROCE = {fr("80&nbsp;000","400&nbsp;000")} × 100% = 20%')]),
 ("Current ratio", f'current ratio = {fr("current assets","current liabilities")}',
  [nw(f'{fr("90&nbsp;000","60&nbsp;000")} = 1.5') + ', written 1.5 or 1.5:1 (no % sign)']),
 ("Acid test (quick) ratio", f'acid test ratio = {fr("current assets − stock","current liabilities")}',
  [nw('$90&nbsp;000 − $30&nbsp;000 = $60&nbsp;000'), nw(f'{fr("60&nbsp;000","60&nbsp;000")} = 1.0') + ' (1:1)']),
 ("Average rate of return (ARR)", f'ARR = {fr("(total returns − capital cost) ÷ years of use","capital cost")} × 100%',
  ['A machine costs $100&nbsp;000 and brings total returns of $140&nbsp;000 over 5 years.',
   'Average yearly profit = ' + nw('($140&nbsp;000 − $100&nbsp;000) ÷ 5 = $8000'),
   nw(f'ARR = {fr("8000","100&nbsp;000")} × 100% = 8% a year')]),
]
sheet_html = ''.join(sheet(*x) for x in SHEET_ITEMS)

def lgroup(title, items, anchor):
    l = ''.join(litem(*x) for x in items)
    return f'<section class="topic" id="{anchor}"><h2>{title}</h2><div class="col l" style="margin-top:12px">{l}</div></section>'

import re as _re
def nw(x):
    # BM learn items: keep short expressions on one line, let long word formulas wrap (they cannot fit a 390 px screen)
    vis = _re.sub(r'<[^>]+>', '', _re.sub(r'&[a-z]+;', ' ', x))
    return f'<span class="nw">{x}</span>' if len(vis) <= 30 else f'<span class="wf">{x}</span>'

FIN = [
 ("3.1", "Capital vs revenue expenditure", 'Capital expenditure buys non-current assets that last more than a year. Revenue expenditure pays day-to-day running costs.',
  'A $30&nbsp;000 delivery van is capital expenditure; its fuel and the driver wages are revenue expenditure.'),
 ("3.2", "Internal sources of finance", '<b>Personal funds</b> (sole traders): the owner&rsquo;s own savings. <b>Retained profit</b>: profit kept in the business after tax and dividends. <b>Sale of assets</b>: selling things the business owns but no longer needs.',
  'A bakery owner puts in $8000 of savings; later the firm sells an unused warehouse for $250&nbsp;000.'),
 ("3.2", "External sources: shares, loans, overdrafts, trade credit", '<b>Share capital</b>: money from selling shares in a company (never repaid, but owners lose some control). <b>Loan capital</b>: borrowed for a fixed period, repaid with interest. <b>Overdraft</b>: the bank lets the account go below zero up to a limit; short term, high interest. <b>Trade credit</b>: buy from suppliers now, pay later.',
  'A 5-year $60&nbsp;000 bank loan for a van; a café gets coffee beans now and pays the supplier in 30 days.'),
 ("3.2", "External sources: crowdfunding, leasing, microfinance, business angels", '<b>Crowdfunding</b>: small amounts from many people, usually online. <b>Leasing</b>: paying regularly to use an asset owned by someone else. <b>Microfinance providers</b>: small loans to people on low incomes who cannot get bank loans. <b>Business angels</b>: wealthy individuals who invest their own money in a small business for a share of it, often with advice.',
  'A start-up raises $40&nbsp;000 from 800 online backers; a market trader gets a $500 microloan; an angel invests $100&nbsp;000 for 20% of a tech firm.'),
 ("3.2", "Short or long term (AO3)", 'Match the finance to its use: short-term needs (stock, a cash gap) suit overdrafts and trade credit; long-term assets suit loans, share capital or leasing. Judge cost, control, risk and the size of the business.',
  'Financing a new factory with an overdraft is a poor match; a long-term loan or share issue fits better.'),
 ("3.3", "Types of cost and total revenue", '<b>Fixed</b> costs do not change with output (rent). <b>Variable</b> costs rise with output (materials). <b>Direct</b> costs belong to one product (its ingredients). <b>Indirect/overhead</b> costs are shared (office salaries). ' + nw('Total revenue = price × quantity sold') + '; revenue streams are the different sources of income.',
  nw('2000 bikes × $15 rental = $30&nbsp;000') + ' total revenue from the rental stream.'),
 ("3.4", "Profit and loss account layout", 'Sales revenue − cost of sales = gross profit; − expenses = profit before interest and tax; − interest = profit before tax; − tax = profit for the period; − dividends = retained profit.',
  'Harbour Bikes: PBIT $80&nbsp;000, interest $10&nbsp;000, tax 20%: profit before tax $70&nbsp;000, tax $14&nbsp;000, profit for period $56&nbsp;000; after $20&nbsp;000 dividends, retained profit $36&nbsp;000.'),
 ("3.4", "Balance sheet and intangible assets", 'Total assets − total liabilities = net assets = total equity (share capital + retained earnings). Intangible assets have no physical form: goodwill, patents, copyrights, trademarks, brands.',
  'Harbour Bikes: net assets $250&nbsp;000 = total equity $250&nbsp;000. (Its capital employed of $400&nbsp;000 also counts the $150&nbsp;000 of non-current liabilities, so do not mix the two up.)'),
 ("3.5", "Reading the ratios (not printed)", 'Higher margins and ROCE are better; compare with past years and competitors. Common textbook guide: current ratio about 1.5 to 2, acid test about 1. Strategies (AO3): raise prices, cut costs, sell assets, chase debtors.',
  'Harbour Bikes: current ratio 1.5 and acid test 1.0 look healthy; GPM 40% versus profit margin 16% shows expenses take 24% of revenue.'),
 ("3.7", "Cash flow and working capital", 'Profit is not cash. ' + nw('Working capital = current assets − current liabilities') + '. In a cash flow forecast: ' + nw('net cash flow = cash inflows − cash outflows') + ', ' + nw('closing balance = opening balance + net cash flow') + ', and the closing balance is next month&rsquo;s opening balance.',
  'Opening $5000, inflows $12&nbsp;000, outflows $14&nbsp;500: net cash flow −$2500, closing balance $2500. Harbour Bikes working capital ' + nw('= $90&nbsp;000 − $60&nbsp;000 = $30&nbsp;000') + '.'),
 ("3.8", "Payback period (not printed)", 'Time for the net cash flows to repay the cost. Count whole years, then ' + nw('months = amount still needed ÷ that year&rsquo;s net cash flow × 12') + '.',
  'Cost $50&nbsp;000, net cash flows $20&nbsp;000, $20&nbsp;000, $15&nbsp;000: after 2 years $10&nbsp;000 is still needed, ' + nw('10&nbsp;000 ÷ 15&nbsp;000 × 12 = 8 months') + ', so 2 years 8 months.'),
]
BE = [
 ("5.5", "Contribution", nw('Contribution per unit = price − variable cost per unit') + '. ' + nw('Total contribution = contribution per unit × units sold') + ' (= total revenue − total variable costs).',
  'Price $25, variable cost $15 per unit: contribution $10 per unit; 5500 units give total contribution $55&nbsp;000.'),
 ("5.5", "Break-even quantity", nw(f'Break-even quantity = {fr("fixed costs","contribution per unit")}') + '. Round <b>up</b> to a whole unit. Break-even revenue = break-even quantity × price.',
  'Fixed costs $40&nbsp;000: ' + nw('40&nbsp;000 ÷ 10 = 4000 units') + ', break-even revenue ' + nw('4000 × $25 = $100&nbsp;000') + '.'),
 ("5.5", "Profit or loss", nw('Profit = total contribution − fixed costs') + ' (= total revenue − total costs).',
  'At 5500 units: ' + nw('$55&nbsp;000 − $40&nbsp;000 = $15&nbsp;000') + ' profit.'),
 ("5.5", "Margin of safety", nw('Margin of safety = actual output − break-even quantity') + ' (in units, or multiply by price for revenue). Negative means a loss.',
  nw('5500 − 4000 = 1500 units') + ' (or $37&nbsp;500 of sales).'),
 ("5.5", "Target profit output and target price", 'Target profit output = ' + fr('fixed costs + target profit','contribution per unit') + '<br>Target price = ' + fr('fixed costs + target profit','quantity') + ' + variable cost per unit',
  'Target profit $20&nbsp;000: ' + nw('(40&nbsp;000 + 20&nbsp;000) ÷ 10 = 6000 units') + '. To make it on 5000 units: ' + nw('60&nbsp;000 ÷ 5000 + 15 = $27') + '.'),
 ("5.5", "Changes in price or cost", 'Recalculate the contribution, then the break-even quantity. A higher price or lower variable cost lowers break-even; higher fixed costs raise it. On the chart, redraw the line that changed.',
  'Price up to $27: contribution $12, break-even ' + nw('40&nbsp;000 ÷ 12 = 3333.3') + ', so 3334 units.'),
 ("5.5", "Break-even chart and limitations", 'Units on the <i>x</i>-axis, $ on the <i>y</i>-axis. Fixed costs: horizontal line. Total costs: start at fixed costs. Total revenue: start at 0. Break-even where total revenue meets total costs. Limitations (AO3): assumes everything made is sold, straight-line costs and revenue, one product, and a static price.',
  'Label the break-even point, the margin of safety and the profit and loss areas on every chart.'),
]
TOOL = [
 ("Toolkit", "SWOT analysis", 'Strengths and weaknesses are <b>internal</b>; opportunities and threats are <b>external</b>. Shows where a business stands before a decision.',
  'Strength: loyal customers. Threat: a new competitor opens next door.'),
 ("Toolkit", "Ansoff matrix", 'Growth options by product (existing or new) and market (existing or new): market penetration, product development, market development, diversification. Risk rises towards diversification.',
  'Selling existing bikes in a new country is market development.'),
 ("Toolkit", "STEEPLE analysis", 'External factors: Social, Technological, Economic, Environmental, Political, Legal, Ethical.',
  'A new e-bike subsidy is Political (or Economic); a rise in interest rates is Economic.'),
 ("Toolkit", "BCG matrix", 'Products by market growth (vertical) and relative market share (horizontal): stars (high, high), cash cows (low growth, high share), question marks (high growth, low share), dogs (low, low).',
  'A best-selling bike in a mature market is a cash cow: use its cash to fund question marks.'),
 ("Toolkit", "Business plan", 'A document setting out the business idea, objectives, marketing, operations, human resources and finance (forecasts). Used to plan and to persuade lenders and investors.',
  'A bank asks for a business plan with a cash flow forecast before granting a loan.'),
 ("Toolkit", "Decision trees", 'Square = decision, circle = chance node with probabilities adding to 1. Expected value = Σ (probability × outcome); subtract the cost of the option; pick the highest net value.',
  'Launch: ' + nw('0.6 × $500&nbsp;000 + 0.4 × $100&nbsp;000 = $340&nbsp;000') + '; minus cost $200&nbsp;000 gives $140&nbsp;000.'),
 ("Toolkit", "Descriptive statistics", 'Mean, mode, median, bar charts, pie charts, infographics, quartiles, standard deviation. Use them to summarise data from the case and say what they show.',
  'Weekly sales 12, 15, 15, 20, 38: mean 20, median 15, mode 15; the mean is pulled up by one strong week.'),
 ("Toolkit", "Circular business models", 'Five types: circular supply models, resource recovery models, product life extension models, sharing models, product service system models.',
  'Repairing and reselling used bikes is product life extension; renting bikes by the hour is a sharing model.'),
]

bm_body = f'''
<div class="legend" aria-label="Legend for the formula markers">
  <span><span class="fb" style="margin-left:0">On formula sheet</span> printed on the sheet you get in the exam: know how to use it</span>
  <span><span class="learn" style="margin-left:0">Learn</span> not on the sheet: you must remember it</span>
</div>
<ul class="toc">
  <li><a href="#sheet">On the formula sheet</a></li><li><a href="#fin">Finance: learn it</a></li><li><a href="#be">Break-even: learn it</a></li><li><a href="#tool">Toolkit: learn it</a></li>
</ul>
<section class="topic" id="sheet"><h2>On the formula sheet (SL)</h2>
<p>The IB guide says a copy of these formulae is provided in the exam. For SL you only need these six. All worked examples use one company so you can see how the ratios connect: {case}</p>
<div class="grid2">{sheet_html}</div>
<div class="tip"><b>Ignore the HL lines.</b> The same appendix also lists stock turnover, debtor days, creditor days, gearing ratio, NPV, capacity utilisation rate and productivity rate, plus a discount table. These are HL only and are not examined at SL.</div>
</section>
{lgroup("Finance (unit 3): learn it", FIN, "fin")}
{lgroup("Break-even analysis (5.5): learn it", BE, "be")}
{lgroup("The SL toolkit: learn what each tool shows", TOOL, "tool")}
<p class="note" style="margin-top:28px">Sources: the IB Business management guide, first assessment 2024 (updated July 2024), <a href="{DRIVE('1KeX_WVc4uNQe-DdGS_7-1ITxBUqXveWD')}">in your folder</a>: Appendices: Formulae; unit 3 (Finance and accounts); 5.5 Break-even analysis; the business management toolkit (figure 5). Exam habits: <a href="exam-business-management-sl.html">Exam technique: Business Management SL</a>.</p>
'''
bm_comment = '''<!-- given-business-management-sl: built by tools/given.py.
Formula sheet: guide Appendices > Formulae (pp. 64 to 65), read from the page images: SL/HL = GPM, profit margin, ROCE (with capital employed),
current ratio, acid test ratio, ARR. HL only = stock turnover (times/days), debtor days, creditor days, gearing, NPV, capacity utilisation,
productivity, discount table. 5.5 break-even is all SL (checked on the page image: not in bold). Contribution as a TOOL (make or buy,
contribution and absorption costing) is HL only, but "total contribution versus contribution per unit" in 5.5 is SL.
Uncertain / not in the guide wording (from standard textbook practice, please check against the class textbook):
 - The P&L layout lines (profit before interest and tax, interest, profit before tax, tax, profit for period, dividends, retained profit)
   and the balance sheet identity: the guide lists "Profit and loss account" and "Balance sheet" only; layout follows the usual IB textbook format.
 - Intangible asset examples (goodwill, patents, copyrights, trademarks, brands): guide says only "Different types of intangible assets".
 - Ratio benchmarks (current ratio about 1.5 to 2, acid test about 1) are textbook rules of thumb, not IB wording.
 - Payback month formula and break-even "round up" are standard practice, not guide wording.
 - Whether the printed exam sheet for SL papers also shows the HL formulae is not stated; the page says to ignore them either way.
 - Definitions of sources of finance and toolkit tools are my summaries; the guide only lists the names.
-->
'''
html = build("Given or learn: Business Management SL", "Given or learn: Business Management SL",
             "The six formulas on the SL formula sheet with worked examples, then the finance, break-even and toolkit facts that are not on it.", bm_body)
html = html.replace("<main", bm_comment + "<main", 1)
open(out + '/given-business-management-sl.html', 'w').write(html)
print("given ok")
