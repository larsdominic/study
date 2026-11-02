import sys; sys.path.insert(0,sys.argv[1]); from common import *; from quizjs import quiz_js
out=sys.argv[2]
M='../guides/2026-11-04-maths-aa-sl-1.2-1.6.html'; C='../guides/2026-11-03-chemistry-s1.1-s1.3.html'
Q=[ # (subject, question, options, answer index, why)
("Chemistry","Which of these is a homogeneous mixture?",["Sand in water","Air","Oil and water","Granite"],1,"Air has the same composition throughout and one phase. The others have visible regions with different composition (heterogeneous)."),
("Maths","An arithmetic sequence has u<sub>1</sub> = 5 and d = −3. Find u<sub>10</sub>.",["−25","−22","−27","32"],1,"u<sub>10</sub> = 5 + 9 × (−3) = −22. −25 uses 10 steps instead of 9; 32 adds instead of subtracting."),
("Chemistry","Which technique separates the dyes in a sample of ink?",["Filtration","Distillation","Paper chromatography","Evaporation"],2,"The dyes are attracted differently to the paper (stationary phase) and the solvent (mobile phase), so they move different distances."),
("Maths","Find the sum of the first 10 terms of 2 + 5 + 8 + …",["155","140","170","310"],0,"S<sub>10</sub> = <span class='nw'>10/2 (2 × 2 + 9 × 3)</span> = 5 × 31 = 155. 140 and 170 use 8 or 10 differences instead of 9; 310 forgets to halve."),
("Chemistry","−73 °C in kelvin is",["−346 K","346 K","200 K","73 K"],2,"T(K) = T(°C) + 273 = −73 + 273 = 200 K. Kelvin temperatures are never negative."),
("Maths","The 6<sup>th</sup> term of the geometric sequence 81, 27, 9, … is",["1","<span class='frac'><span>1</span><span>3</span></span>","<span class='frac'><span>1</span><span>9</span></span>","3"],1,"r = <span class='frac'><span>1</span><span>3</span></span>, u<sub>6</sub> = 81 × (<span class='frac'><span>1</span><span>3</span></span>)<sup>5</sup> = <span class='frac'><span>81</span><span>243</span></span> = <span class='frac'><span>1</span><span>3</span></span>. <span class='frac'><span>1</span><span>9</span></span> uses the power 6 instead of 5."),
("Chemistry","How many protons, neutrons and electrons are in <sup>27</sup>Al<sup>3+</sup>? (Z = 13)",["13, 14, 16","13, 14, 10","14, 13, 10","13, 27, 10"],1,"13 protons; 27 − 13 = 14 neutrons; 13 − 3 = 10 electrons. A 3+ ion has lost electrons, not gained them."),
("Maths","The sum to infinity of 81 + 27 + 9 + … is",["121.5","108","243","60.75"],0,"r = <span class='frac'><span>1</span><span>3</span></span>, so S<sub>∞</sub> = <span class='frac'><span>81</span><span>1 − 1/3</span></span> = 81 × <span class='frac'><span>3</span><span>2</span></span> = 121.5. 243 divides by r instead of 1 − r."),
("Chemistry","An element is 90% mass 20 and 10% mass 22. Its relative atomic mass is",["21.0","20.0","20.2","20.8"],2,"(20 × 90 + 22 × 10) ÷ 100 = 2020 ÷ 100 = 20.2. It must lie close to the more abundant isotope (20). 21.0 is a plain average that ignores abundance."),
("Maths","<span class='nw'>Σ from r = 1 to 5</span> of 2<sup>r</sup> equals",["31","62","64","32"],1,"The terms are 2, 4, 8, 16, 32 (start at r = 1, so the first term is 2), total 62. 31 is 1 + 2 + 4 + 8 + 16, starting from 2<sup>0</sup>."),
("Chemistry","Which transition in a hydrogen atom emits visible light?",["n = 2 to n = 1","n = 4 to n = 2","n = 5 to n = 3","n = 1 to n = 2"],1,"Falls to n = 2 give the visible lines. Falls to n = 1 give ultraviolet, falls to n = 3 give infrared, and n = 1 to n = 2 is absorption, not emission."),
("Maths","The geometric series with first term 1 and ratio <span class='frac'><span>x</span><span>3</span></span> has a sum to infinity when",["|x| &lt; 1","|x| &lt; 3","x &lt; 3","|x| &lt; <span class='frac'><span>1</span><span>3</span></span>"],1,"The condition is |r| &lt; 1, so |x/3| &lt; 1, which is |x| &lt; 3, that is −3 &lt; x &lt; 3. \"x &lt; 3\" forgets the negative side."),
("Chemistry","The maximum number of electrons in the n = 3 energy level is",["8","9","18","32"],2,"2n<sup>2</sup> = 2 × 9 = 18 (3s, 3p and 3d). 8 is a common confusion with the period length; 9 is the number of orbitals."),
("Maths","$5000 is invested at 4% compounded annually. Its value after 2 years is",["$5400","$5408","$5416","$5200"],1,"5000 × 1.04<sup>2</sup> = 5000 × 1.0816 = $5408. $5400 is simple interest (4% of the original twice)."),
("Chemistry","The condensed electron configuration of Fe<sup>2+</sup> (Z = 26) is",["[Ar] 4s<sup>2</sup> 3d<sup>4</sup>","[Ar] 3d<sup>6</sup>","[Ar] 4s<sup>2</sup> 3d<sup>6</sup>","[Ar] 4s<sup>1</sup> 3d<sup>5</sup>"],1,"Fe is [Ar] 4s<sup>2</sup> 3d<sup>6</sup>, and transition metal ions lose the 4s electrons first, leaving [Ar] 3d<sup>6</sup>."),
("Maths","A car worth $30 000 loses 20% of its value each year. Its value after 2 years is",["$18 000","$19 200","$24 000","$20 000"],1,"30 000 × 0.8<sup>2</sup> = 30 000 × 0.64 = $19 200. $18 000 takes 20% of the original price twice."),
("Chemistry","How many unpaired electrons does a nitrogen atom have?",["1","2","3","5"],2,"2p<sup>3</sup>: by Hund's rule the three p electrons occupy separate orbitals with parallel spins, so all three are unpaired."),
("Maths","Which symbol shows that a statement is true for every value of x?",["=","≈","≡","⇒"],2,"≡ means \"is identical to\" (an identity). = holds only for particular values."),
("Chemistry","(HL) Successive ionisation energies (kJ mol<sup>−1</sup>) of an element: 800, 2427, 3660, 25026, 32827. Its group is",["1","2","13","15"],2,"The big jump comes after the 3<sup>rd</sup> electron, so there are three outer electrons: group 13 (this is boron)."),
("Maths","Which completes a valid proof? \"For any integer n, n + (n + 1) = 2n + 1, so the sum of two consecutive integers is …\"",["even, because 2n is even","odd, because 2n is even and adding 1 gives an odd number","odd, because 3 + 4 = 7","sometimes odd, depending on n"],1,"2n is always even, so 2n + 1 is always odd. An example (3 + 4 = 7) is not a proof."),
]
qhtml=''
for i,(s,q,opts,a,why) in enumerate(Q,1):
    b=''.join(f'\n    <button>{o}</button>' for o in opts)
    qhtml+=f'\n  <div class="q" data-a="{a}"><p><span class="subj">{s}</span>{i}. {q}</p>{b}\n    <div class="why">{why}</div></div>\n'
EL=SHEET
body=f'''
<div class="step" style="margin-top:24px"><div class="bh"><b>Step 1 · 15 min</b><span>Error log: find your top 3</span></div><ol>
<li>Open the <a href="{EL}">study sheet</a>, Error log tab, and read every row from this week.</li>
<li>Group mistakes that have the same cause (for example "used n instead of n − 1" twice counts as one repeat).</li>
<li>Pick the <b>three</b> causes that came up most, or cost the most marks. For each one write a one-line rule on a card or sticky note (for example "u<sub>n</sub> has n − 1 steps").</li>
<li>Redo one question from the Error log for each of the three, without looking at the answer.</li></ol></div>
<div class="step"><div class="bh"><b>Step 2 · 25 min</b><span>Mixed quiz (below)</span></div><ol>
<li>20 new questions, maths and chemistry mixed together. Mixing is harder than doing one topic at a time, and that is the point: it trains you to recognise which method a question needs.</li>
<li>Work each one on paper first, then click. Every answer explains the trap. Use a calculator for the chemistry ones if you like; do the maths ones without.</li>
<li>Any you miss go into the Error log, same as during the week.</li></ol></div>
<div class="step"><div class="bh"><b>Step 3 · 10 min</b><span>Flashcards</span></div><ol>
<li>Open the <a href="../flashcards.html">flashcards</a> and go through the "to repeat" and "new" cards until the counts are low.</li></ol></div>
<div class="step"><div class="bh"><b>Step 4 · 10 min</b><span>Progress and next week</span></div><ol>
<li>Look at the <a href="../progress.html">progress page</a>: which topics are still amber or red?</li>
<li>In the study sheet, write the three Error log rules from step 1 in the Notes column of next week's matching subject days, so the next guides can drill them.</li></ol></div>
<p style="font-size:.92rem;color:var(--ink-soft)">This week's guides: <a href="{C}">Chemistry S1.1 to S1.3</a> and <a href="{M}">Maths AA SL 1.2 to 1.6</a>. Biology, Business and English join the review once they have guides.</p>
<section class="quiz" id="quiz"><h2>Mixed quiz: week 1</h2>{qhtml}
  <div class="score" id="score">Score: 0 / {len(Q)} answered 0</div>
</section>
'''
open(out+'/review/2026-11-08-week-1.html','w').write(page("Weekly review: week 1 (Sun 8 Nov 2026)","../index.html","Weekly review: week 1","Sunday 8 November 2026. About an hour: turn this week's mistakes into rules, test yourself on everything mixed together, then plan next week.",body,quiz_js('ib-quiz-review-2026-11-08')))
print(len(Q),"questions")
