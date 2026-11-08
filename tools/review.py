import sys; sys.path.insert(0,sys.argv[1]); from common import *; from quizjs import quiz_js
out=sys.argv[2]
M='../guides/2026-11-04-maths-aa-sl-1.2-1.6.html'; B='../guides/2026-11-05-biology-hl-a1.1-a1.2.html'; N='../guides/2026-11-06-business-sl-1.1-1.6.html'; P='../guides/2026-11-09-psychology-hl-frame-research-methods.html'
Q=[ # (subject, question, options, answer index, why)
("Biology","Sweating cools the body mainly because water has a high",["specific heat capacity","latent heat of vaporisation","cohesion","adhesion"],1,"Evaporating sweat must break hydrogen bonds, which takes a lot of heat from the skin: that is the latent heat of vaporisation. Specific heat capacity is about warming water up, not evaporating it."),
("Maths","An arithmetic sequence has u<sub>1</sub> = 5 and d = −3. Find u<sub>10</sub>.",["−25","−22","−27","32"],1,"u<sub>10</sub> = 5 + 9 × (−3) = −22. −25 uses 10 steps instead of 9; 32 adds instead of subtracting."),
("Business","A firm sells a product for $50. Bought-in materials and services cost $30. Its added value is",["$20","$80","$30","$50"],0,"Added value = selling price − cost of bought-in materials and services = 50 − 30 = $20. It is not profit: wages, rent and profit all come out of it."),
("Maths","Find the sum of the first 10 terms of 2 + 5 + 8 + …",["155","140","170","310"],0,"S<sub>10</sub> = <span class='nw'>10/2 (2 × 2 + 9 × 3)</span> = 5 × 31 = 155. 140 and 170 use 8 or 10 differences instead of 9; 310 forgets to halve."),
("Biology","In DNA, guanine pairs with",["cytosine, held by 3 hydrogen bonds","cytosine, held by 2 hydrogen bonds","thymine, held by 2 hydrogen bonds","adenine, held by 3 hydrogen bonds"],0,"G pairs with C by three hydrogen bonds; A pairs with T by two. A purine always pairs with a pyrimidine."),
("Maths","The 6<sup>th</sup> term of the geometric sequence 81, 27, 9, … is",["1","<span class='frac'><span>1</span><span>3</span></span>","<span class='frac'><span>1</span><span>9</span></span>","3"],1,"r = <span class='frac'><span>1</span><span>3</span></span>, u<sub>6</sub> = 81 × (<span class='frac'><span>1</span><span>3</span></span>)<sup>5</sup> = <span class='frac'><span>81</span><span>243</span></span> = <span class='frac'><span>1</span><span>3</span></span>. <span class='frac'><span>1</span><span>9</span></span> uses the power 6 instead of 5."),
("Business","Which of these is a tertiary sector business?",["A coal mine","A car factory","A bank","A software research lab"],2,"Tertiary = services to people (shops, banks). A mine is primary, a factory secondary, and research and software are quaternary (knowledge)."),
("Maths","The sum to infinity of 81 + 27 + 9 + … is",["121.5","108","243","60.75"],0,"r = <span class='frac'><span>1</span><span>3</span></span>, so S<sub>∞</sub> = <span class='frac'><span>81</span><span>1 − 1/3</span></span> = 81 × <span class='frac'><span>3</span><span>2</span></span> = 121.5. 243 divides by r instead of 1 − r."),
("Biology","Which statement about RNA is correct?",["RNA contains thymine","RNA contains the sugar ribose","RNA is normally double-stranded","RNA contains deoxyribose"],1,"RNA: one strand, ribose, uracil instead of thymine. DNA: two strands, deoxyribose, thymine."),
("Maths","<span class='nw'>Σ from r = 1 to 5</span> of 2<sup>r</sup> equals",["31","62","64","32"],1,"The terms are 2, 4, 8, 16, 32 (start at r = 1, so the first term is 2), total 62. 31 is 1 + 2 + 4 + 8 + 16, starting from 2<sup>0</sup>."),
("Business","Two firms set up a new, separate company that they own together. This is",["a merger","a strategic alliance","a joint venture","a takeover"],2,"A joint venture creates a new business owned jointly. In a strategic alliance the firms cooperate but no new business is created; a merger combines the two firms into one."),
("Maths","The geometric series with first term 1 and ratio <span class='frac'><span>x</span><span>3</span></span> has a sum to infinity when",["|x| &lt; 1","|x| &lt; 3","x &lt; 3","|x| &lt; <span class='frac'><span>1</span><span>3</span></span>"],1,"The condition is |r| &lt; 1, so |x/3| &lt; 1, which is |x| &lt; 3, that is −3 &lt; x &lt; 3. \"x &lt; 3\" forgets the negative side."),
("Biology","How many different base sequences are possible for a stretch of 3 DNA bases?",["12","27","64","81"],2,"4 choices at each position: 4 × 4 × 4 = 4<sup>3</sup> = 64. 12 multiplies 4 × 3; 81 is 3<sup>4</sup>, the wrong way round. This is why codons are triplets: 64 codes are enough for 20 amino acids."),
("Maths","$5000 is invested at 4% compounded annually. Its value after 2 years is",["$5400","$5408","$5416","$5200"],1,"5000 × 1.04<sup>2</sup> = 5000 × 1.0816 = $5408. $5400 is simple interest (4% of the original twice)."),
("Business","Which of these stakeholders is internal?",["Suppliers","Shareholders","The local community","The government"],1,"Internal stakeholders are inside the organisation: employees, managers and directors, and shareholders. The others are external."),
("Maths","A car worth $30 000 loses 20% of its value each year. Its value after 2 years is",["$18 000","$19 200","$24 000","$20 000"],1,"30 000 × 0.8<sup>2</sup> = 30 000 × 0.64 = $19 200. $18 000 takes 20% of the original price twice."),
("Biology","Water climbs up a thin glass tube and forms a meniscus mainly because of",["cohesion alone","adhesion to the glass, with cohesion pulling the following molecules along","surface tension alone","its high specific heat capacity"],1,"Adhesion: water molecules form hydrogen bonds with the polar glass surface, and cohesion drags the molecules behind them up too. This is capillary action, also seen in cell walls and soil."),
("Maths","Which symbol shows that a statement is true for every value of x?",["=","≈","≡","⇒"],2,"≡ means \"is identical to\" (an identity). = holds only for particular values."),
("Business","A sole trader closes with debts larger than the business assets. Who must pay the rest?",["Nobody: the debts are written off","The owner personally, because a sole trader has unlimited liability","Shareholders, up to the amount they invested","The government"],1,"A sole trader has unlimited liability: the owner is personally liable for all business debts. Limited liability (losing at most what you invested) applies to shareholders of companies."),
("Maths","Which completes a valid proof? \"For any integer n, n + (n + 1) = 2n + 1, so the sum of two consecutive integers is …\"",["even, because 2n is even","odd, because 2n is even and adding 1 gives an odd number","odd, because 3 + 4 = 7","sometimes odd, depending on n"],1,"2n is always even, so 2n + 1 is always odd. An example (3 + 4 = 7) is not a proof."),
("Psychology","A study tests whether music helps memory: one randomly allocated group revises with music, the other in silence, then both sit the same test. What is the independent variable?",["The memory test score","Whether there is music while revising","The random allocation","The students' ages"],1,"The IV is what the researcher changes (here two conditions: music or silence). The test score is what is measured, so it is the dependent variable."),
("Psychology","Which of these is a quasi-experiment?",["Participants are randomly allocated to drink coffee or water before a memory test","The memory of 16-year-olds is compared with the memory of 60-year-olds","A coin toss decides which revision method each participant uses","The researcher randomly allocates people to a hot or a cold room"],1,"Age groups already exist, so participants cannot be randomly allocated to them: that makes it a quasi-experiment, which cannot establish cause and effect. The other three use random allocation (a coin toss counts)."),
("Psychology","A researcher puts every student's name in a hat and draws 30 names. This is",["opportunity sampling","random sampling","random allocation","self-selected sampling"],1,"Every member of the population has an equal chance of being picked: random sampling. Random allocation is something else: deciding by chance which condition each chosen participant goes into."),
("Psychology","At HL, Paper 3 (data analysis) is worth what share of the final grade?",["25%","20%","30%","35%"],2,"HL: Paper 1 25%, Paper 2 25%, Paper 3 30%, internal assessment 20%. 35% is Paper 1 or Paper 2 at SL."),
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
<li>24 new questions, maths, biology, business and psychology mixed together. Mixing is harder than doing one topic at a time, and that is the point: it trains you to recognise which method a question needs.</li>
<li>Work each one on paper first, then click. Every answer explains the trap. Do the maths ones without a calculator.</li>
<li>Any you miss go into the Error log, same as during the week.</li></ol></div>
<div class="step"><div class="bh"><b>Step 3 · 10 min</b><span>Flashcards</span></div><ol>
<li>Open the <a href="../flashcards.html">flashcards</a> and go through the "to repeat" and "new" cards until the counts are low.</li></ol></div>
<div class="step"><div class="bh"><b>Step 4 · 10 min</b><span>Progress and next week</span></div><ol>
<li>Look at the <a href="../progress.html">progress page</a>: which topics are still amber or red?</li>
<li>In the study sheet, write the three Error log rules from step 1 in the Notes column of next week's matching subject days, so the next guides can drill them.</li></ol></div>
<p style="font-size:.92rem;color:var(--ink-soft)">This week's guides: <a href="{M}">Maths AA SL 1.2 to 1.6</a>, <a href="{B}">Biology HL A1.1 and A1.2</a> and <a href="{N}">Business Management SL 1.1 to 1.6</a> and <a href="{P}">Psychology HL: course map and research methods</a>.</p>
<section class="quiz" id="quiz"><h2>Mixed quiz: week 1</h2>{qhtml}
  <div class="score" id="score">Score: 0 / {len(Q)} answered 0</div>
</section>
'''
open(out+'/review/2026-11-08-week-1.html','w').write(page("Weekly review: week 1 (Sun 15 Nov 2026)","../index.html","Weekly review: week 1","Sunday 15 November 2026. About an hour (the other two hours today are Biology B1.1): turn this week's mistakes into rules, test yourself on everything mixed together, then plan next week.",body,quiz_js('ib-quiz-review-2026-11-08')))
print(len(Q),"questions")
