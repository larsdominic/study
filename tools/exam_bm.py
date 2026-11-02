# Exam technique: Business Management SL. Source: IB Business management guide (first assessment 2024, updated July 2024), Drive 1DO0yC9MM9GSi3ecg6vMTTV17vDLaAqEv
import sys; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
TERMS=[("Analyse","AO2","Break down in order to bring out the essential elements or structure."),
("Annotate","AO4","Add brief notes to a diagram or graph."),
("Apply","AO2","Use an idea, equation, principle, theory or law in relation to a given problem or issue."),
("Calculate","AO4","Obtain a numerical answer showing the relevant stages in the working."),
("Comment","AO2","Give a judgment based on a given statement or result of a calculation."),
("Compare","AO3","Give an account of the similarities between two (or more) items or situations, referring to both (all) of them throughout."),
("Compare and contrast","AO3","Give an account of similarities and differences between two (or more) items or situations, referring to both (all) of them throughout."),
("Complete","AO4","Add missing information/data."),
("Construct","AO4","Display information in a diagrammatic or logical form."),
("Contrast","AO3","Give an account of the differences between two (or more) items or situations, referring to both (all) of them throughout."),
("Define","AO1","Give the precise meaning of a word, phrase, concept or physical quantity."),
("Demonstrate","AO2","Make clear by reasoning or evidence, illustrating with examples or practical application."),
("Describe","AO1","Give a detailed account."),
("Determine","AO4","Obtain the only possible answer."),
("Discuss","AO3","Offer a considered and balanced review that includes a range of arguments, factors or hypotheses. Opinions or conclusions should be presented clearly and supported by appropriate evidence."),
("Distinguish","AO2","Make clear the differences between two or more concepts or items."),
("Draw","AO4","Represent by means of a labelled, accurate diagram or graph, using a pencil. A ruler (straight edge) should be used for straight lines. Diagrams should be drawn to scale. Graphs should have points correctly plotted (if appropriate) and joined in a straight line or smooth curve."),
("Evaluate","AO3","Make an appraisal by weighing up the strengths and limitations."),
("Examine","AO3","Consider an argument or concept in a way that uncovers the assumptions and interrelationships of the issue."),
("Explain","AO2","Give a detailed account including reasons or causes."),
("Identify","AO1","Provide an answer from a number of possibilities."),
("Justify","AO3","Give valid reasons or evidence to support an answer or conclusion."),
("Label","AO4","Add labels to a diagram."),
("List","AO1","Give a sequence of brief answers with no explanation."),
("Outline","AO1","Give a brief account or summary."),
("Plot","AO4","Mark the position of points on a diagram."),
("Prepare","AO4","Put given data or information from a stimulus/source into a suitable format."),
("Recommend","AO3","Present an advisable course of action with appropriate supporting evidence/reason in relation to a given situation, problem or issue."),
("State","AO1","Give a specific name, value or other brief answer without explanation or calculation."),
("Suggest","AO2","Propose a solution, hypothesis or other possible answer."),
("To what extent","AO3","Consider the merits or otherwise of an argument or concept. Opinions and conclusions should be presented clearly and supported with appropriate evidence and sound argument.")]
BANDS=[("0","The work does not reach a standard described by the descriptor."),
("1 to 2","Little understanding of the demands of the question. Little use of business management tools and theories; any tools and theories that are used are irrelevant or used inaccurately. Little or no reference to the stimulus material. No arguments are made."),
("3 to 4","Some understanding of the demands of the question. Some use of business management tools and theories, but these are mostly lacking in accuracy and relevance. Superficial use of information from the stimulus material, often not going beyond the name of the person(s) or name of the organization. Any arguments made are mostly unsubstantiated."),
("5 to 6","The response indicates an understanding of the demands of the question, but these demands are only partially addressed. Some relevant and accurate use of business management tools and theories. Some relevant use of information from the stimulus material that goes beyond the name of the person(s) or name of the organization but does not effectively support the argument. Arguments are substantiated but are mostly one-sided."),
("7 to 8","Mostly addresses the demands of the question. Mostly relevant and accurate use of business management tools and theories. Information from the stimulus material is generally used to support the argument, although there is some lack of clarity or relevance in some places. Arguments are substantiated and have some balance."),
("9 to 10","Clear focus on addressing the demands of the question. Relevant and accurate use of business management tools and theories. Relevant information from the stimulus material is integrated effectively to support the argument. Arguments are substantiated and balanced, with an explanation of the limitations of the case study or stimulus material.")]
tt=''.join(f'<tr><td><b>{a}</b></td><td style="text-align:center">{l}</td><td>{d}</td></tr>' for a,l,d in TERMS)
bt=''.join(f'<tr><td style="white-space:nowrap"><b>{m}</b></td><td>{d}</td></tr>' for m,d in BANDS)
body=f'''
<h2 style="margin-top:28px">The SL papers</h2>
<div class="tablewrap"><table>
<tr><th></th><th>Paper 1</th><th>Paper 2</th></tr>
<tr><td>Time and weight</td><td>1 hour 30 minutes, 35%, 30 marks</td><td>1 hour 30 minutes, 35%, 40 marks</td></tr>
<tr><td>Based on</td><td>An unseen case study (about 800 to 1,000 words). Three months before the exam the IB releases a statement: a few context topics to research (about five hours) and roughly the first 200 words of the case. Mostly qualitative, maybe minor calculations.</td><td>Unseen stimulus material with a <b>quantitative</b> focus (charts, infographics, text), given in parts: read each part, answer its question, then read the next.</td></tr>
<tr><td>Section A</td><td>All structured questions on the case study (20 marks)</td><td>All structured questions (20 marks)</td></tr>
<tr><td>Section B</td><td>Choose <b>one of two</b> extended response questions (10 marks)</td><td>Choose <b>one of two</b> questions: structured parts (10 marks) plus an extended response (10 marks). One option may be about a social enterprise.</td></tr>
</table></div>
<p>The other 30% is the internal assessment: a business research project on a real business issue, using a conceptual lens, at most 1,800 words (25 marks). Every paper starts with five minutes of reading time. A four-function calculator is enough for every calculation, and graphic calculators are allowed. You get a formula sheet in the exam.</p>

<h2>Habits that win marks</h2>
<div class="card"><ol style="margin:0;padding-left:22px">
<li><b>Use the case, do not just name it.</b> The markbands punish answers that only mention the company or person's name. Pull specific facts and figures from the case into every point and explain how they support your argument.</li>
<li><b>Balance and limitations for the top band.</b> A 9 to 10 answer needs arguments for and against, a clear judgement, and a sentence on the limitations of the case or stimulus (missing data, one source, a short time period).</li>
<li><b>Use the toolkit.</b> SL tools: SWOT, Ansoff matrix, STEEPLE, BCG matrix, business plan, decision trees, descriptive statistics, circular business models. Name the tool, apply it to the case, then draw a conclusion from it.</li>
<li><b>Define precisely.</b> The guide expects you to define, use and apply business terms correctly. Lead with a precise definition when the command term is "Define", and use the exact term elsewhere.</li>
<li><b>Prepare the pre-release.</b> Research the context topics in the statement for about five hours, and read the first 200 words of the case carefully: they tell you the business and its situation.</li>
<li><b>Calculations: show the working</b> ("Calculate" asks for the relevant stages) and give units: %, $, times.</li>
<li><b>Choose Section B quickly.</b> Read both options for a minute and pick the one where you can bring in a tool and real evidence from the case.</li>
<li><b>Time.</b> Paper 1 is 30 marks in 90 minutes (3 minutes per mark, so about 30 minutes for the 10-mark question). Paper 2 is 40 marks in 90 minutes (just over 2 minutes per mark).</li>
</ol></div>

<h2>How the 10-mark questions are marked</h2>
<p>Section B extended responses (both papers) are marked with these markbands, best fit. Section A questions use a question-specific markscheme instead.</p>
<div class="tablewrap"><table><tr><th>Marks</th><th>What the answer shows (official markband)</th></tr>{bt}</table></div>

<h2>Formulas you are given</h2>
<p>These are on the formula sheet in the exam, so learn how to use them, not the formulas themselves.</p>
<div class="card"><ul style="margin:0;padding-left:20px">
<li>Gross profit margin = gross profit ÷ sales revenue × 100%</li>
<li>Profit margin = profit before interest and tax ÷ sales revenue × 100%</li>
<li>ROCE = profit before interest and tax ÷ capital employed × 100%, where capital employed = non-current liabilities + equity</li>
<li>Current ratio = current assets ÷ current liabilities</li>
<li>Acid test (quick) ratio = (current assets − stock) ÷ current liabilities</li>
<li>Average rate of return = ((total returns − capital cost) ÷ years of use) ÷ capital cost × 100%</li>
</ul></div>

<h2>Command terms</h2>
<p>The level is the assessment objective: AO1 knowledge (short), AO2 application and analysis, AO3 synthesis and evaluation (judgements with evidence), AO4 skills such as calculating and drawing. A question can never use a harder command term than its syllabus topic allows, so "evaluate" only appears where the syllabus says AO3.</p>
<div class="tablewrap"><table><tr><th>Command term</th><th>Level</th><th>What the IB means (official definition)</th></tr>{tt}</table></div>
<p style="font-size:.9rem;color:var(--ink-soft)">Source: the IB Business management guide, first assessment 2024 (updated July 2024), <a href="{DRIVE('1DO0yC9MM9GSi3ecg6vMTTV17vDLaAqEv')}">in your folder</a>: assessment outline, markbands, formulae appendix and glossary of command terms.</p>
'''
open(out+'/exam-business-management-sl.html','w').write(page("Exam technique: Business Management SL","exam.html","Exam technique: Business Management SL","How the two SL papers work, how the 10-mark answers are marked, and what every command word asks for.",body,crumb_label="Exam technique: all subjects"))
print("bm ok")
