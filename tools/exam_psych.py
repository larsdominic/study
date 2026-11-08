# Exam technique page for Psychology HL. Every fact comes from the official IB Psychology guide
# (first assessment 2027, Drive 1Khqsn6PrxoS5UXAEKBpu5G_XG5Viyvtq) as extracted in
# ~/ClaudeMe/ib-notes/research/psych-assessment.json and psychology-audit.md (page numbers below),
# and from the official specimen papers (Drive 1KoOk8IT670o-bbr1HKc-Nw2Kub_Gf1Mr).
import sys, json; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
GUIDE=DRIVE('1Khqsn6PrxoS5UXAEKBpu5G_XG5Viyvtq'); SPEC=DRIVE('1KoOk8IT670o-bbr1HKc-Nw2Kub_Gf1Mr')
TERMS=[("AO1","Describe","Give a detailed account."),
("AO1","State","Give a specific name, value or other brief answer without explanation or calculation."),
("AO2","Analyse","Break down in order to bring out the essential elements or structure."),
("AO2","Apply","Use an idea, equation, principle, theory or law in relation to a given problem or issue."),
("AO2","Comment","Give a judgement based on a given statement or result of a calculation."),
("AO2","Design","Produce a plan, simulation or model."),
("AO2","Explain","Give a detailed account including reasons or causes."),
("AO2","Interpret","Use knowledge and understanding to recognize trends and draw conclusions from given information."),
("AO2","Predict","Give an expected result."),
("AO2","Suggest","Propose a solution, hypothesis or other possible answer."),
("AO3","Compare and contrast","Give an account of similarities and differences between two (or more) items or situations, referring to both (all) of them throughout."),
("AO3","Discuss","Offer a considered and balanced review that includes a range of arguments, factors or hypotheses. Opinions or conclusions should be presented clearly and supported by appropriate evidence."),
("AO3","Evaluate","Make an appraisal by weighing up the strengths and limitations."),
("AO3","Examine","Consider an argument or concept in a way that uncovers the assumptions and interrelationships of the issue."),
("AO3","To what extent","Consider the merits or otherwise of an argument or concept. Opinions and conclusions should be presented clearly and supported with appropriate evidence and sound argument.")]
tr=''.join(f'<tr><td><b>{t}</b></td><td style="text-align:center">{ao}</td><td>{d}</td></tr>' for ao,t,d in TERMS)
body=f'''
<h2 style="margin-top:28px">The HL assessment at a glance</h2>
<div class="tablewrap"><table>
<tr><th></th><th>Time</th><th>Marks</th><th>Share of the grade (HL)</th></tr>
<tr><td><b>Paper 1</b>: concepts, content and contexts together</td><td>1 h 30</td><td>35</td><td>25%</td></tr>
<tr><td><b>Paper 2</b>: applying concepts and content to research</td><td>1 h 30</td><td>35</td><td>25%</td></tr>
<tr><td><b>Paper 3</b> (HL only): data analysis and interpretation</td><td>1 h 45</td><td>30</td><td>30%</td></tr>
<tr><td><b>Internal assessment</b>: a research proposal</td><td>about 20 h of class time</td><td>24</td><td>20%</td></tr>
</table></div>
<p>All three papers are written answers: there is no multiple choice in Psychology. At SL there is no Paper 3 and the weights are 35%, 35% and 30%.</p>

<h2>Paper 1, section by section</h2>
<div class="tablewrap"><table>
<tr><th>Section</th><th>What you do</th><th>Marks</th><th>What gets the top band</th></tr>
<tr><td>A</td><td>Two short answers, each from a different approach (biological, cognitive, sociocultural): describe or explain an idea and give an example</td><td>4 + 4</td><td>Detailed knowledge, and an example that is relevant <b>and explained</b></td></tr>
<tr><td>B</td><td>Two short answers that apply what you know to a new situation printed in the question, each from one context</td><td>6 + 6</td><td>Accurate, detailed knowledge and an application that is "well developed": keep linking back to the situation</td></tr>
<tr><td>C</td><td>One essay from a choice of two, built on one of the six concepts</td><td>15</td><td>Critical analysis, clear links between the topic and the concept, a conclusion that follows from your arguments, accurate terms</td></tr>
</table></div>

<h2>Paper 2, section by section</h2>
<div class="tablewrap"><table>
<tr><th>Section</th><th>What you do</th><th>Marks</th></tr>
<tr><td>A, Q1</td><td>Describe one of <b>your own class practicals</b>: method, aim, procedure</td><td>4</td></tr>
<tr><td>A, Q2</td><td>Explain a concept (for example bias) in relation to that practical</td><td>4</td></tr>
<tr><td>A, Q3</td><td>Compare and contrast its method with another method</td><td>6</td></tr>
<tr><td>A, Q4</td><td>Design a study on the same topic with a different method</td><td>6</td></tr>
<tr><td>B</td><td>Discuss a new research study printed in the paper, using two or more of the concepts the question lists</td><td>15</td></tr>
</table></div>

<h2>Paper 3 (HL only), question by question</h2>
<p>Several sources (graphs, tables, short research summaries) about one HL extension (culture, motivation or technology) in one context.</p>
<div class="tablewrap"><table>
<tr><th>Q</th><th>What you do</th><th>Marks</th></tr>
<tr><td>1</td><td>Explain one issue that limits what a graph or source can tell you</td><td>3</td></tr>
<tr><td>2</td><td>Analyse the findings of one source and state a conclusion</td><td>6</td></tr>
<tr><td>3</td><td>Credibility, bias or transferability of a qualitative study</td><td>6</td></tr>
<tr><td>4</td><td>Use at least three sources plus your own knowledge to judge a claim</td><td>15</td></tr>
</table></div>

<h2>The internal assessment</h2>
<p>You <b>design</b> a study to investigate a group of people (the "population of interest") using an experiment, interviews, an observation or a survey, but you do <b>not</b> carry it out. Maximum 2,200 words; the examiner stops reading at the limit. Four criteria, 6 marks each: A Introduction, B Research methodology, C Data collection, D Discussion.</p>

<h2>Habits that win marks</h2>
<div class="card"><ol style="margin:0;padding-left:22px">
<li><b>Answer the command term.</b> "Describe" wants a detailed account; "explain" adds reasons or causes; "evaluate" weighs strengths <b>and</b> limitations. A description where the question says "evaluate" stays in the low bands.</li>
<li><b>Paper 1 Section A: explain your example.</b> The top band needs an example that is relevant and explained. A study name on its own is not enough. The guide says details of research studies are not assessed in Section A, so a clear real-life or made-up (hypothetical) example also works; the specimen mark scheme accepts hypothetical examples.</li>
<li><b>Only your first example counts.</b> The specimen mark schemes credit only the first chemical messenger, behaviour or example you write. Pick one and develop it.</li>
<li><b>Sections B and C: keep linking.</b> In B, refer back to the situation in the question in every paragraph. In C, tie every point to the named concept and finish with a conclusion that follows from what you argued.</li>
<li><b>Paper 2 Section A is about your own practical.</b> Answers that describe a method in general, not the practical you did, are capped in the low band (specimen mark scheme). After each class practical write a short note: aim, procedure, sampling technique, findings, ethical points.</li>
<li><b>Paper 2 Section B and Paper 3 Q4: use the numbers you need.</b> Paper 2 B wants two or more of the listed concepts; Paper 3 Q4 wants at least three sources. Fewer cannot reach the top band.</li>
<li><b>Learn the vocabulary exactly.</b> Many marks are for "accurate terminology". Use the glossary flashcards: operationalisation, random vs opportunity sampling, internal vs external validity, and so on.</li>
<li><b>Time.</b> Paper 1 and Paper 2: 35 marks in 90 minutes, about 2.5 minutes a mark, so about 37 minutes for the 15-mark question. Paper 3: 30 marks in 105 minutes, 3.5 minutes a mark.</li>
</ol></div>

<h2>Command terms</h2>
<p>AO1 terms ask for knowledge (shorter answers), AO2 for application and AO3 for evaluation (longer, with arguments on both sides).</p>
<div class="tablewrap"><table><tr><th>Command term</th><th>AO</th><th>What the IB means (official definition)</th></tr>{tr}</table></div>
<p>Practise on the official <a href="{SPEC}">specimen papers 1, 2 and 3 with mark schemes</a>, in your folder.</p>
<p style="font-size:.9rem;color:var(--ink-soft)">Source: the assessment outline (p42 to 52), markbands and glossary of command terms (p60 to 61) in the IB Psychology guide, first assessment 2027 (<a href="{GUIDE}">in your folder</a>), and the specimen mark schemes. Timings per mark are simple division, not IB rules.</p>
'''
open(out+'/exam-psychology-hl.html','w').write(page("Exam technique: Psychology HL","exam.html","Exam technique: Psychology HL","How the three HL papers and the internal assessment work, the habits that win marks, and what every command word asks for.",body,crumb_label="Exam technique"))
print("exam psychology ok")
