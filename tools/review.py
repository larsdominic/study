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
N_OLD=len(Q); assert N_OLD==24
# Psychology session 2 (Sat 14 Nov): evaluating research, classical and operant conditioning.
# Checked against ~/ClaudeMe/ib-notes/research/psychology-audit.md (Session 2 plan, class files #4 Skittles worksheet
# "buzzer + Skittle, salivation", #7 operant slides "positive/negative reinforcement and punishment", RM01 slides 60-148
# "counterbalancing") and psych-glossary.json ("reinforcement increases a behaviour, punishment decreases it").
NEW=[
(6,("Psychology","In your class Skittles experiment, a buzzer sounded just before each Skittle was eaten. After several pairings, students salivated when they heard the buzzer alone. Salivating at the buzzer alone is the",["unconditioned response","conditioned response","conditioned stimulus","neutral stimulus"],1,"It is a learned response to the buzzer, so it is the conditioned response (CR). The buzzer is now the conditioned stimulus (CS); before the pairings it was a neutral stimulus. Salivating at the Skittle itself is the unconditioned response (UCR): nobody had to learn it.")),
(15,("Psychology","A student's parents stop nagging her about homework as soon as she has finished it, and she starts doing her homework earlier. In operant conditioning this is",["positive reinforcement","negative reinforcement","positive punishment","negative punishment"],1,"Something unpleasant (the nagging) is taken away when she does the behaviour, and the behaviour increases: negative reinforcement. Reinforcement always makes a behaviour more likely, punishment less likely. \"Negative\" means something is taken away, not that it is bad.")),
(23,("Psychology","In a repeated measures experiment, half the participants do condition A first and then B; the other half do B first and then A. This is done to control",["order effects, such as practice or tiredness","participant variables (differences between the people in two groups)","researcher bias","sampling bias"],0,"This is counterbalancing. In repeated measures the same people do both conditions, so participant variables are already controlled. The risk is that doing one condition first (practice, boredom, tiredness) changes the scores in the second; counterbalancing spreads these order effects evenly over both conditions.")),
]
for pos,item in NEW: Q.insert(pos,item)
assert len(Q)==N_OLD+3 and all(0<=a<len(o) for _,_,o,a,_ in Q)
assert all(len(set(o))==len(o) for _,_,o,_,_ in Q)   # no duplicate options, so exactly one button is right
qhtml=''
for i,(s,q,opts,a,why) in enumerate(Q,1):
    b=''.join(f'\n    <button>{o}</button>' for o in opts)
    qhtml+=f'\n  <div class="q" data-a="{a}"><p><span class="subj">{s}</span>{i}. {q}</p>{b}\n    <div class="why">{why}</div></div>\n'

# ---- three written items (self-marked; not part of the saved quiz score)
W=[('psy','Psychology',4,'Paper 1 Section A style',
 '<p><b>Describe operant conditioning with reference to one example.</b> [4]</p>',
 '''<p><b>Model answer</b> (written for this site, not an official IB answer):</p>
<p>Operant conditioning is learning through the consequences of a behaviour: a behaviour followed by reinforcement becomes more likely, and a behaviour followed by punishment becomes less likely. Positive reinforcement adds something pleasant, such as a reward; negative reinforcement takes away something unpleasant; both make the behaviour more frequent. Punishment adds something unpleasant or takes away something pleasant, so the behaviour becomes less frequent. For example, a teacher gives a disruptive student a merit point every lesson he stays in his seat. Because staying seated is now followed by a reward he values (positive reinforcement), he links the behaviour with its consequence and stays in his seat more often.</p>
<p><b>Check it against the official markband</b> (Paper 1 Section A, IB Psychology guide p45):</p>
<ul><li>1 to 2 marks: "limited knowledge"; the example "is relevant but is not explained".</li>
<li>3 to 4 marks: "detailed knowledge"; the example "is relevant and explained".</li></ul>
<p><b>Tick list:</b> learning through consequences? reinforcement increases, punishment decreases? positive and negative used correctly ("negative" = taken away)? <b>one</b> example (only the first counts)? the example says <b>how</b> the consequence changes the behaviour? All five: 4. Example named but not explained: 2 at most.</p>'''),
('bus','Business',4,'Paper 1 style, short case',
 '''<p><i>FreshBowl sells salads from 5 outlets in one city. The owners plan to open 15 more over the next two years, so the chain will have 20 outlets.</i></p>
<p><b>Explain two internal economies of scale FreshBowl could gain from this growth.</b> [4]</p>''',
 '''<p><b>Model answer</b> (written for this site, not an official IB answer):</p>
<p><b>Purchasing economies.</b> With 20 outlets FreshBowl buys far more vegetables, bowls and packaging, so suppliers give bulk discounts. Each salad then costs less to make: its average cost falls.</p>
<p><b>Marketing economies.</b> One advertising campaign or one ordering app can now be spread over the sales of 20 outlets instead of 5, so the marketing cost of each salad sold falls.</p>
<p><b>How to mark it</b> (the 1 + 1 pattern from your <a href="__N__">Business guide</a>'s worked examples; not an official mark scheme): for each economy, 1 mark for naming a correct type, 1 mark for explaining it with FreshBowl's case (outlets, salads, ingredients) and saying it lowers <b>average</b> cost. Financial (cheaper loans for a bigger firm) or managerial (specialist managers) economies, explained with the case, also score. Writing "costs go down" without "per salad" or "average" loses the second mark.</p>'''),
('bio','Biology',3,'short written answer',
 '<p><b>Explain why glucose dissolves in water but olive oil does not.</b> [3]</p>',
 '''<p><b>Mark points</b> (written for this site in the style of your class mark schemes, one mark per point, max 3; not an official IB mark scheme, and the IB Biology guide is not in your folder):</p>
<ul><li>water molecules are polar (δ− oxygen, δ+ hydrogens);</li>
<li>glucose is polar / has many -OH groups, so it forms hydrogen bonds with water / is hydrophilic;</li>
<li>water molecules surround each glucose molecule, so it dissolves;</li>
<li>oil is non-polar / hydrophobic, so it is not attracted to water and cannot form hydrogen bonds with it (it stays as a separate layer);</li></ul>
<p>See A1.1 "Water as a solvent" in your <a href="__B__">Biology guide</a> if you missed one.</p>''')]
T_W=sum(w[2] for w in W); assert T_W==11
whtml=''
for k,subj,mx,kind,qtext,model in W:
    model=model.replace('__N__',N).replace('__B__',B)
    whtml+=f'''
<div class="written card" id="w-{k}" data-k="{k}" data-max="{mx}"><p class="wh"><span class="wsubj">{subj}</span> {kind}, {mx} marks</p>
{qtext}
<details><summary>Show model answer (only after you have written yours on paper)</summary>{model}</details></div>'''

# ---- timings (one hour; the 3-minute break sits between blocks 2 and 3)
BD, BD_CHECK = 5, 3
QZ = 22
BRK = 3
W_WRITE, W_MARK = 13, 4
EL = 10
BLOCKS = [BD + BD_CHECK, QZ, BRK, W_WRITE + W_MARK, EL]
assert sum(BLOCKS) == 60, BLOCKS
G=[('Psychology, Mon 9 Nov',P,'course map, command terms, research methods: variables, experiments, hypotheses, sampling'),
   ('Maths, Tue 10 Nov',M,'sequences, series, sigma notation, compound interest, proof'),
   ('Biology, Wed 11 Nov',B,'A1.1 water, A1.2 nucleic acids'),
   ('Business, Thu 12 Nov',N,'Unit 1, 1.1 to 1.6'),
   ('English, Fri 13 Nov','../guides/2026-11-13-english-a-hl-paper1-satirical-cartoons.html','Paper 1, satirical cartoons'),
   ('Psychology, Sat 14 Nov','../guides/2026-11-14-psychology-hl-evaluating-research-conditioning.html','evaluating research, classical and operant conditioning')]
glist=''.join(f'<li><b>{d}</b>: {t}' + (f' (<a href="{u}">guide</a>)' if u else ' (no guide page: check against the list below)') + '</li>' for d,u,t in G)
EXTRA_CSS='''<style>
.quiz .q:not(.done) .subj{display:none}
.written .wh{font-weight:700;margin-bottom:6px}
.written details{background:#F7F8F6;border:1px solid var(--rule);padding:8px 12px;margin:10px 0}
.written summary{cursor:pointer;font-weight:600}
.written ul{padding-left:22px}
.stuck{background:var(--amber-soft);border-left:5px solid var(--amber);padding:10px 16px;margin:14px 0}
.star{color:var(--amber-ink);font-weight:700}
.brk{text-align:center;font-weight:700;color:var(--green);background:var(--green-soft);padding:10px;margin:16px 0}
</style>'''
body=f'''{EXTRA_CSS}
<div class="card" style="margin-top:24px"><b>How the hour goes:</b> {BLOCKS[0]} min brain dump, {QZ} min mixed quiz, a {BRK}-minute break, {W_WRITE + W_MARK} min on three written questions, {EL} min Error log and Fix-it. That is {sum(BLOCKS)} minutes.<br>
<span class="star">★</span> steps are extras. <b>Short on time: skip ★ steps, still do the quiz.</b></div>
<div class="stuck"><b>Stuck?</b> Look at the worked example in that day's guide, then redo its self-check. Still stuck after 10 minutes? Log it as "ask teacher" in the Error log and move on.</div>

{block_open(1,'Brain dump on a blank page',f'{BLOCKS[0]} min')}<ol>
<li><b>{BD} min, no notes, page scrolled away.</b> Take a blank sheet. Write the six headings below, and under each one write every "I can" line you remember from that day, in your own words (key words are enough).<ul>{glist}</ul></li>
<li><b>{BD_CHECK} min, check.</b> Open each guide and compare with its green "I can" boxes. Tick what you had; add what you missed in a different colour. The missed lines are your weak spots for the quiz.</li>
<li><span class="star">★ If time:</span> add one example under each line you missed.</li></ol>
</div>

{block_open(2,'Mixed quiz (below)',f'{QZ} min')}<ol>
<li>{len(Q)} questions from Maths, Biology, Business and Psychology, mixed together (English is in the brain dump). <b>The subject label is hidden until you answer.</b> Before you click, write in the margin which subject and which rule or method the question needs (for example "Maths: u<sub>n</sub> = u<sub>1</sub> + (n − 1)d"). Spotting the method is the skill an exam tests; mixing trains it.</li>
<li>Work each one on paper first, then click. Every answer explains the trap. Do the maths ones without a calculator.</li>
<li><span class="star">★ If time:</span> any you got right by guessing count as wrong for the Error log.</li></ol></div>

<p class="brk">{BRK}-minute break: stand up, drink water, look out of a window. No phone.</p>

{block_open(3,f'Three written exam questions ({T_W} marks)',f'{W_WRITE + W_MARK} min')}<ol>
<li><b>{W_WRITE} min:</b> write all three on paper, page scrolled away. About 5 min each for the 4-mark ones, 3 min for the Biology one.</li>
<li><b>{W_MARK} min:</b> open each "Show model answer", mark yours with the tick list and choose your mark in the "My mark" menu under the question. It saves on this device.</li>
<li><span class="star">★ If time:</span> underline in your answer the words that earned each mark.</li></ol></div>
<section id="written"><h2>Written questions</h2>
<p style="font-size:.92rem;color:var(--ink-soft)">Psychology markband wording is from the official IB Psychology guide (first assessment 2027). The Business and Biology mark points are written for this site, not taken from an official IB mark scheme.</p>
{whtml}
</section>

{block_open(4,'Error log and Fix-it',f'{EL} min')}<ol>
<li>Open the <a href="{SHEET}">study sheet</a>, Error log tab. Write one row for every mark you lost today (quiz and written), with its type: <b>did not know</b>, <b>wrong method</b>, <b>slip</b>, <b>time</b> or <b>ask teacher</b>.</li>
<li>Read this week's rows too. Group mistakes with the same cause and pick the <b>three</b> that came up most or cost the most marks. Write each as a one-line rule (for example "u<sub>n</sub> has n − 1 steps"). In the Notes column of next week's matching subject days, write the rule, so the next guides drill it.</li>
<li><b>Fix-it:</b> take one written answer where you lost marks and rewrite it to full marks, using the model answer's tick list but your own words. Then close the page and redo that day's self-check from memory, and write the rule.</li>
<li><span class="star">★ If time:</span> redo one old Error log question for each of the three rules, without looking at the answer.</li></ol></div>
<div class="card"><b>After the hour</b> (<span class="star">★</span>, or in today's planning hour): open the <a href="../flashcards.html">flashcards</a> for the "to repeat" cards, and check your <a href="../progress.html">progress page</a> for topics still amber or red.</div>

<section class="quiz" id="quiz"><h2>Mixed quiz: week 1</h2>
<p style="font-size:.95rem;color:var(--ink-soft)">The subject appears after you answer. First decide: which subject, which method?</p>{qhtml}
  <div class="score" id="score">Score: 0 / {len(Q)} answered 0</div>
</section>
'''
html=page("Weekly review: week 1 (Sun 15 Nov 2026)","../index.html","Weekly review: week 1","Sunday 15 November 2026. One hour (the rest of today is Biology B1.1 and planning next week): pull the week out of memory, test yourself on everything mixed together, write three exam answers, then turn your mistakes into rules.",body,quiz_js('ib-quiz-review-2026-11-08'),crumb_label="All days")
assert '—' not in html
open(out+'/review/2026-11-08-week-1.html','w').write(html)
print(len(Q),"questions,",len(W),"written items,",T_W,"written marks, blocks",BLOCKS)
