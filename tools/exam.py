import sys, os; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
BM_PAGE="exam-business-management-sl.html" if os.path.exists(os.path.join(sys.argv[1],"exam_bm.py")) else None
def terms_table(rows):
    tr=''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a,b in rows)
    return f'<div class="tablewrap"><table><tr><th>Command term</th><th>What the IB means (official definition)</th></tr>{tr}</table></div>'

M_TERMS=[("Calculate","Obtain a numerical answer showing the relevant stages in the working."),
("Comment","Give a judgment based on a given statement or result of a calculation."),
("Compare","Give an account of the similarities between two (or more) items or situations, referring to both (all) of them throughout."),
("Compare and contrast","Give an account of similarities and differences between two (or more) items or situations, referring to both (all) of them throughout."),
("Construct","Display information in a diagrammatic or logical form."),
("Contrast","Give an account of the differences between two (or more) items or situations, referring to both (all) of them throughout."),
("Deduce","Reach a conclusion from the information given."),
("Demonstrate","Make clear by reasoning or evidence, illustrating with examples or practical application."),
("Describe","Give a detailed account."),
("Determine","Obtain the only possible answer."),
("Differentiate","Obtain the derivative of a function."),
("Distinguish","Make clear the differences between two or more concepts or items."),
("Draw","Represent by means of a labelled, accurate diagram or graph, using a pencil. A ruler (straight edge) should be used for straight lines. Diagrams should be drawn to scale. Graphs should have points correctly plotted (if appropriate) and joined in a straight line or smooth curve."),
("Estimate","Obtain an approximate value."),
("Explain","Give a detailed account including reasons or causes."),
("Find","Obtain an answer showing relevant stages in the working."),
("Hence","Use the preceding work to obtain the required result."),
("Hence or otherwise","It is suggested that the preceding work is used, but other methods could also receive credit."),
("Identify","Provide an answer from a number of possibilities."),
("Integrate","Obtain the integral of a function."),
("Interpret","Use knowledge and understanding to recognize trends and draw conclusions from given information."),
("Investigate","Observe, study, or make a detailed and systematic examination, in order to establish facts and reach new conclusions."),
("Justify","Give valid reasons or evidence to support an answer or conclusion."),
("Label","Add labels to a diagram."),
("List","Give a sequence of brief answers with no explanation."),
("Plot","Mark the position of points on a diagram."),
("Predict","Give an expected result."),
("Prove","Use a sequence of logical steps to obtain the required result in a formal way."),
("Show","Give the steps in a calculation or derivation."),
("Show that","Obtain the required result (possibly using information given) without the formality of proof. “Show that” questions do not generally require the use of a calculator."),
("Sketch","Represent by means of a diagram or graph (labelled as appropriate). The sketch should give a general idea of the required shape or relationship, and should include relevant features."),
("Solve","Obtain the answer(s) using algebraic and/or numerical and/or graphical methods."),
("State","Give a specific name, value or other brief answer without explanation or calculation."),
("Suggest","Propose a solution, hypothesis or other possible answer."),
("Verify","Provide evidence that validates the result."),
("Write down","Obtain the answer(s), usually by extracting information. Little or no calculation is required. Working does not need to be shown.")]

maths_body=f'''
<h2 style="margin-top:28px">The two papers</h2>
<div class="tablewrap"><table>
<tr><th></th><th>Paper 1</th><th>Paper 2</th></tr>
<tr><td>Time</td><td>1 hour 30 minutes</td><td>1 hour 30 minutes</td></tr>
<tr><td>Calculator</td><td><b>None allowed</b></td><td><b>Graphic display calculator (GDC) required</b>, though not every question needs it</td></tr>
<tr><td>Marks</td><td>80 (40% of the grade)</td><td>80 (40% of the grade)</td></tr>
<tr><td>Layout</td><td>Section A: short questions, about 40 marks. Section B: a few long questions, about 40 marks. All compulsory.</td><td>Same layout as Paper 1</td></tr>
</table></div>
<p>The other 20% is the internal assessment, the mathematical exploration. Both papers give you a clean copy of the formula booklet. Neither paper is multiple choice.</p>

<h2>Habits that win marks</h2>
<div class="card"><ol style="margin:0;padding-left:22px">
<li><b>Always show working.</b> The IB guide says full marks are not necessarily awarded for a correct answer with no working. Most marks are for method.</li>
<li><b>Read the mark scheme letters.</b> M = method mark, A = accuracy (answer) mark, R = reasoning mark, AG = "answer given" (you must reach it, no extra mark for writing it). A mark in brackets, like (M1), can be implied by later correct work.</li>
<li><b>Accuracy.</b> Unless the question says otherwise, give answers exactly or to 3 significant figures. Keep full calculator values in the working and round only at the end. Money is usually to 2 decimal places or the nearest dollar: read the question.</li>
<li><b>Paper 1 answers stay exact.</b> Leave fractions, surds and π as they are (<span class="nw">√3</span>, <span class="nw">14/3</span>) unless asked to simplify further.</li>
<li><b>Proper notation, never calculator notation.</b> Write 5.2 × 10<sup>30</sup>, not 5.2E30 (the guide says calculator notation is not acceptable).</li>
<li><b>Time.</b> 80 marks in 90 minutes is just over a minute per mark. A 6-mark question should take about 6 to 7 minutes; if you are stuck, move on and come back.</li>
<li><b>"Show that" lines.</b> When a part says "show that … = 4", the answer is given: the marks are for the steps. If you cannot do it, still use the given result in the next part.</li>
<li><b>GDC in Paper 2.</b> Know the financial app (TVM: N, I%, PV, PMT, FV, P/Y, C/Y, with PV and FV of opposite sign), the equation solver, tables of values and finding intersections on a graph.</li>
</ol></div>

<h2>Command terms</h2>
<p>Every question starts with one of these words, and it tells you how much to write. The three that cause most lost marks: <b>"Write down"</b> (no working needed, so be quick), <b>"Show that"</b> (every step needed) and <b>"Hence"</b> (you must use the previous part, another method scores nothing).</p>
{terms_table(M_TERMS)}
<p>See also: <a href="given-maths-aa-sl.html">what the formula booklet gives vs what to learn</a>.</p>
<p style="font-size:.9rem;color:var(--ink-soft)">Source: the "Glossary of command terms" in the IB Mathematics: analysis and approaches guide (<a href="{DRIVE('19usrPWgR-_yAbEtM2QeF8vHtOR691ZXw')}">in your folder</a>). The formula booklet is <a href="{DRIVE('19EX75prXgep28AagsDaWsr3eM6O8rVDV')}">here</a>.</p>
'''
open(out+'/exam-maths-aa-sl.html','w').write(page("Exam technique: Maths AA SL","exam.html","Exam technique: Maths AA SL","How the two papers work, the habits that win marks, and what every command word asks for.",maths_body,crumb_label="Exam technique: all subjects"))


# ---------- hub: one card per subject; add new subjects here ----------
SUBJ=[("Maths AA SL","exam-maths-aa-sl.html","Paper 1 (no calculator) and Paper 2 (GDC), mark codes M1 A1 R1, all 36 command terms"),
      ("Business Management SL",BM_PAGE,"Papers, case study, markbands and command terms"),
      ("Psychology HL","exam-psychology-hl.html","Papers 1, 2 and 3, the research proposal (IA), markbands and all 15 command terms"),
      ("Biology HL",None,"Needs the official IB Biology guide (not in the folder yet: ask the school)"),
      ("English A HL",None,"Needs the official IB English A guide (not in the folder yet: ask the school)"),
      ("French B SL",None,"Needs the official IB Language B guide (not in the folder yet: ask the school)")]
cards=''
for name,link,desc in SUBJ:
    if link: cards+=f'<a class="sc" href="{link}"><b>{name}</b><span>{desc}</span></a>'
    else: cards+=f'<div class="sc off"><b>{name}</b><span class="soon">coming</span><span>{desc}</span></div>'
hub=f'''
<p style="margin-top:24px">Pick a subject. Each page covers how its exam papers work, the habits that win marks, and what every command word asks for, all taken from the official IB subject guide.</p>
<div class="grid">{cards}</div>
<style>.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin:16px 0}}
.sc{{display:block;background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);padding:12px 14px;text-decoration:none;color:var(--ink)}}
.sc b{{display:block;color:var(--indigo);font-size:1.1rem}} .sc span{{display:block;font-size:.9rem;color:var(--ink-soft);margin-top:2px}}
.sc.off{{border-left-color:#C3C9CD}} .sc.off b{{color:var(--ink-soft)}} .sc .soon{{display:inline-block;font-size:.75rem;font-weight:700;background:#EDF0EC;color:var(--grey);padding:1px 8px;border-radius:999px;margin:4px 0}}</style>
<h2>What you are given vs what you must learn</h2>
<p>Which formulas are printed in the exam (so you only need to use them) and which you must know by heart, topic by topic, each with an example.</p>
<div class="grid"><a class="sc" href="given-maths-aa-sl.html"><b>Maths AA SL</b><span>Formula booklet vs learn it, all five topics</span></a><a class="sc" href="given-business-management-sl.html"><b>Business Management SL</b><span>Formula sheet with worked examples, plus finance, break-even and toolkit to learn</span></a></div>
<p style="font-size:.92rem;color:var(--ink-soft)">Grey subjects get their page as soon as their official subject guide is in the IB folder.</p>
'''
open(out+'/exam.html','w').write(page("Exam technique: all subjects","index.html","Exam technique","Choose a subject.",hub))
print("exam ok")
