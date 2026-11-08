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

ANNO_CSS = r'''<style>
.anno{background:var(--card);border:1px solid var(--rule);padding:12px 16px;margin:12px 0 22px}
.anno .qq{font-weight:700;margin-bottom:8px}
.anno .row{display:grid;grid-template-columns:3fr 2fr;gap:4px 14px;border-top:1px solid var(--rule);padding:8px 0}
.anno .s{margin:0}
.anno .a{margin:0;font-size:.9rem;color:var(--green);background:var(--green-soft);padding:4px 8px;border-left:4px solid var(--green)}
.anno .verdict{border-top:2px solid var(--ink);padding-top:8px;margin:4px 0 0}
.mlabel{display:inline-block;background:var(--amber-soft);border-left:5px solid var(--amber);padding:6px 12px;font-size:.92rem}
@media (max-width:600px){.anno .row{grid-template-columns:1fr}}
</style>
'''
def anno(q, rows, verdict):
    r = ''.join(f'<div class="row"><p class="s">{t}</p><p class="a">{a}</p></div>' for t, a in rows)
    return f'<div class="anno"><p class="qq">{q}</p>{r}<p class="verdict">{verdict}</p></div>'
# Markband wording: psych-assessment.json and psychology-audit.md 1.9 (guide p45-46). Section A content: classical conditioning
# (cognitive approach, Table 3.2 p25). Section B context: health and well-being, area "social learning and health" (p28-30).
anno_a = anno('Paper 1 Section A style: "Explain classical conditioning with reference to one example." [4]', [
 ('Classical conditioning is learning by association: a neutral stimulus that is repeatedly paired with an unconditioned stimulus comes to produce a similar response on its own.',
  'Knowledge: an accurate definition of the process.'),
 ('The unconditioned stimulus (UCS) triggers an unconditioned response (UCR) without any learning; after the pairings the neutral stimulus has become a conditioned stimulus (CS), and the response it now triggers is a conditioned response (CR).',
  'Knowledge: all five terms used correctly. This is what moves the answer from "limited knowledge" (1 to 2) to "detailed knowledge" (3 to 4).'),
 ('For example, a child has a painful filling at the dentist (UCS), which makes her afraid (UCR); each time, she also hears the sound of the drill (neutral stimulus).',
  'Example: relevant. A made-up (hypothetical) example is fine: details of research studies are not assessed in Section A.'),
 ('Because the drill sound has been paired with pain several times, it becomes a CS: later the sound alone, even from another room, makes her anxious (CR).',
  'Example explained: each part of the example is linked to a term. Without this sentence the example would be "relevant but is not explained", which caps the answer at 2.'),
 ('So a fear can be learned through association with something that never caused harm itself.',
  'Links the process to its role in behaviour, the wording of the syllabus point.')],
 '<b>Band:</b> detailed knowledge and an example that is relevant and explained, so the 3 to 4 band; 4 marks. About 130 words: one example only, fully developed.')
anno_b = anno('Paper 1 Section B style, health and well-being: "A secondary school wants its students to eat more vegetables at lunch. Explain how social learning theory could be used to achieve this goal." [6]', [
 ('Social learning theory (Bandura) says people learn behaviours by observing models and imitating them, especially when they see the model being rewarded (vicarious reinforcement).',
  'Knowledge: accurate statement of the theory with a key term.'),
 ('Whether a behaviour is imitated depends on four processes: attention, retention, reproduction and motivation.',
  'Knowledge: detailed. Together with the first sentence this is "accurate and detailed" (5 to 6), not just "some detail" (3 to 4).'),
 ('The school could choose models the students pay attention to and identify with, such as popular older students or sports captains, and ask them to eat vegetables where everyone can see them in the canteen.',
  'Application: attention, applied to this school and this canteen.'),
 ('Short videos of the same models enjoying vegetable dishes, shown at lunchtime every day, would help students remember the behaviour (retention).',
  'Application: retention, still tied to the scenario.'),
 ('Vegetables should be easy to pick up at the counter the models use, so that the behaviour is simple to copy (reproduction).',
  'Application: reproduction. Covering the processes one by one, each in the scenario, is what makes it "well developed".'),
 ('Students should also see the models being praised by teachers, so vicarious reinforcement raises their motivation to imitate them.',
  'Application: motivation through vicarious reinforcement, linked back to the theory.'),
 ('Because the behaviour is noticed, remembered, easy to copy and seen to be rewarded, more students are likely to choose vegetables themselves.',
  'Final link back to the goal in the question.')],
 '<b>Band:</b> knowledge accurate and detailed, application well developed throughout, so the 5 to 6 band; 6 marks. An answer that described the theory well but said only "use role models" would be "partially developed" (3 to 4).')
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

<h2 id="annotated">Two annotated model answers</h2>
<p class="mlabel">Models written for this site, not official IB answers. The green notes say which part of the official markband (guide p45 to 46) each sentence helps to earn.</p>
{ANNO_CSS}
{anno_a}{anno_b}
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
<li><b>Time.</b> Paper 1 and Paper 2: 35 marks in 90 minutes, about 2.5 minutes a mark, so about 38 to 40 minutes for the 15-mark question. Paper 3: 30 marks in 105 minutes, 3.5 minutes a mark.</li>
</ol></div>

<h2>Command terms</h2>
<p>AO1 terms ask for knowledge (shorter answers), AO2 for application and AO3 for evaluation (longer, with arguments on both sides).</p>
<div class="tablewrap"><table><tr><th>Command term</th><th>AO</th><th>What the IB means (official definition)</th></tr>{tr}</table></div>
<p>Practise on the official <a href="{SPEC}">specimen papers 1, 2 and 3 with mark schemes</a>, in your folder.</p>
<p style="font-size:.9rem;color:var(--ink-soft)">Source: the assessment outline (p42 to 52), markbands and glossary of command terms (p60 to 61) in the IB Psychology guide, first assessment 2027 (<a href="{GUIDE}">in your folder</a>), and the specimen mark schemes. Timings per mark are simple division, not IB rules.</p>
'''
open(out+'/exam-psychology-hl.html','w').write(page("Exam technique: Psychology HL","exam.html","Exam technique: Psychology HL","How the three HL papers and the internal assessment work, the habits that win marks, and what every command word asks for.",body,crumb_label="Exam technique"))
print("exam psychology ok")
