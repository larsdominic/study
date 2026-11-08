"""Weekly review, week 2 (Sun 22 Nov 2026): one hour, cumulative and interleaved.

Usage (from anywhere): python3 tools/review2.py <tools dir> <repo root> [<sources.md path>]
Writes <repo root>/review/2026-11-22-week-2.html; with a third argument also writes the
question-to-guide-section list for the independent checker.
Modelled on review.py (week 1). Every fact comes from the study pages for 9 to 22 Nov;
every number is computed below (asserts) or in the comments next to it.
"""
import sys, math
sys.path.insert(0, sys.argv[1])
from common import *
from quizjs import quiz_js
out = sys.argv[2]
SRC_OUT = sys.argv[3] if len(sys.argv) > 3 else None

# ---- linked pages (paths relative to review/)
G = '../guides/'
P16 = G + '2026-11-16-psychology-hl-slt-memory-exam-technique.html'
M17 = G + '2026-11-10-maths-aa-sl-2.2-2.5.html'          # Maths functions, studied Tue 17 Nov
B18 = G + '2026-11-18-biology-hl-b1.2-c1.1.html'
N19 = G + '2026-11-19-business-sl-unit2-hrm.html'
E20 = G + '2026-11-20-english-a-hl-persepolis-water-cell.html'
K21 = '../practice/2026-11-21-mock-papers.html'
B22 = G + '2026-11-22-biology-hl-c1.2-cell-respiration.html'
P09 = G + '2026-11-09-psychology-hl-frame-research-methods.html'
M10 = G + '2026-11-04-maths-aa-sl-1.2-1.6.html'           # Maths sequences, studied Tue 10 Nov
B11 = G + '2026-11-05-biology-hl-a1.1-a1.2.html'
N12 = G + '2026-11-06-business-sl-1.1-1.6.html'
E13 = G + '2026-11-13-english-a-hl-paper1-satirical-cartoons.html'
P14 = G + '2026-11-14-psychology-hl-evaluating-research-conditioning.html'
B15 = G + '2026-11-15-biology-hl-b1.1-carbohydrates-lipids.html'

def fr(a, b):
    return f"<span class='frac'><span>{a}</span><span>{b}</span></span>"
SP = '&nbsp;'            # thousands separator
CM3S = 'cm<sup>3</sup> s<sup>−1</sup>'
MM3M = 'mm<sup>3</sup> min<sup>−1</sup>'

# ---- computed numbers (every number in the quiz)
rt = [300, 320, 340, 360, 380, 1000]
assert (rt[2] + rt[3]) / 2 == 350 and sum(rt) / 6 == 450
assert (40 - 1) + (25 - 1) == 63
assert 30 / 75 == 0.4 and 75 / 30 == 2.5 and 30 * 75 == 2250
assert 64 / 4 == 16 and 16 / 4 == 4
assert 1500 + 0.04 * 20000 == 2300 and 1500 + 0.4 * 20000 == 9500 and 1500 + 4 * 20000 == 81500
assert round(45 * 1.2, 6) == 54 and 45 / 1.2 == 37.5
V = math.pi * 0.5 ** 2 * 30
assert round(V, 1) == 23.6 and round(V / 5, 1) == 4.7
assert round(math.pi * 1.0 ** 2 * 30 / 5, 1) == 18.8 and round(math.pi * 0.5 ** 2 * 3 / 5, 2) == 0.47
S = lambda n: n * n + 3 * n
assert S(5) - S(4) == 12 and S(5) == 40 and S(4) == 28 and S(5) - S(1) == 36
assert sum(3 * r - 1 for r in range(5, 13)) == 196 and 12 - 5 + 1 == 8
assert sum(3 * r - 1 for r in range(6, 13)) == 182 and sum(3 * r - 1 for r in range(1, 13)) == 222
assert 7 / 2 * (2 * 14 + 6 * 3) == 161          # the "7 terms" slip
assert (100 - 2 * 22) / 2 == 28
f = lambda x: 2 * x - 1; g = lambda x: x * x
assert g(f(3)) == 25 and f(g(3)) == 17 and f(3) + g(3) == 14 and f(3) * g(3) == 45
assert 4 * 3 - 7 == 5 and (5 + 7) / 4 == 3

def rv(url, anchor, label):
    return f' <a href="{url}#{anchor}">Revisit: {label}</a>'

# ---- multiple-choice questions: (label, question, options, answer index, why, source for the checker)
# label = subject and day, shown only after answering. 23 from week 2, 8 spaced from week 1.
Q = [
("Psychology · Mon 16 Nov",
 "Amira is nervous about her driving test. Her cousin, who is the same age and was just as nervous, passed last month. Now Amira believes she can pass too. Which source of self-efficacy raised her belief?",
 ["Mastery experiences", "Vicarious experiences", "Social persuasion", "Emotional and physical states"], 1,
 "Seeing someone like you succeed is a vicarious experience. Mastery experiences are her own past successes; social persuasion is being told she can do it; emotional and physical states are her mood and body. Do not mix it up with vicarious reinforcement, which is watching a model being rewarded." + rv(P16, 'slt', '16 Nov, social learning theory'),
 "16 Nov guide #slt, 'Self-efficacy': four sources (LC09): mastery experiences, vicarious experiences (seeing someone like you succeed), social persuasion, emotional and physical states."),
("Maths · Tue 17 Nov",
 f"The largest possible domain of f(x) = {fr('1', 'x + 4')} is",
 ["x ≠ 4", "x ≠ −4", "x &gt; −4", "x ≥ −4"], 1,
 "You cannot divide by zero, and x + 4 = 0 when x = −4, so x ≠ −4. Every other number, above or below −4, is allowed. x ≠ 4 has the wrong sign; x &gt; −4 and x ≥ −4 throw away all the numbers below −4 (that is the kind of rule a square root gives, not a fraction)." + rv(M17, 's22', '17 Nov, SL 2.2 domain and range'),
 "17 Nov Maths guide (file 2026-11-10) #s22 'Domain and range': not allowed: dividing by zero, f(x) = 1/(x − 5) needs x ≠ 5."),
("Business · Thu 19 Nov",
 "A firm brings in new stock-control software. Several older warehouse staff say they are worried they will not cope with the computers. Which strategy tackles this cause most directly?",
 ["Coercion", "Facilitation and support", "Manipulation and co-option", "Negotiation and agreement"], 1,
 "The cause is fear of not coping (low tolerance of change), so training and time to adjust remove it, although that costs money. Coercion forces the change through and may make staff leave; manipulation risks trust; negotiation (for example a bonus) fits a group that will clearly lose something, not a worry about skills." + rv(N19, 's21', '19 Nov, 2.1 resistance to change'),
 "19 Nov guide #s21 'Why staff resist change': reasons incl. low tolerance of change (fear of not coping); strategy table: facilitation and support (training, time to adjust), best when staff fear not coping, drawback costly; coercion, manipulation, negotiation rows."),
("English · Fri 20 Nov",
 "A panel shows a tiny figure in a huge desert, seen from high above. Which shot type and angle?",
 ["A low-angle close-up", "A high-angle extreme long shot", "An eye-level medium shot", "A low-angle extreme long shot"], 1,
 "Tiny in a huge setting is an extreme long shot; looking down from above is a high angle. Shot type (how much we see) and angle (where we look from) are two separate choices. Together they usually make the figure look isolated and vulnerable." + rv(E20, 'shots', '20 Nov, shots and angles'),
 "20 Nov guide #shots: ELS = character tiny in a huge setting (scale, isolation); high angle = above looking down (small, vulnerable); 'a high-angle extreme long shot ... feels isolated and vulnerable'."),
("Biology · Wed 11 Nov (week 1)",
 "In a sample of double-stranded DNA, 22% of the bases are thymine. What percentage of the bases are cytosine?",
 ["22%", "28%", "56%", "78%"], 1,
 "T pairs with A, so A is also 22%, and A + T = 44%. The remaining 56% is shared equally by G and C: 56 ÷ 2 = 28% cytosine. 56% forgets to halve; 22% assumes all four bases are equal; 78% is 100 − 22." + rv(B11, 'a12', '11 Nov, A1.2 base pairing'),
 "11 Nov Biology guide (file 2026-11-05) #a12 A1.2.6: complementary pairing A with T, G with C; #a12hl A1.2.15 Chargaff: A ≈ T and G ≈ C."),
("Psychology · Mon 16 Nov",
 "Remembering the phone number 0 7 9 1 2 0 3 4 5 6 as 079, 120, 3456 makes it easier to hold in short-term memory. This is",
 ["chunking", "maintenance rehearsal", "displacement", "retrieval"], 0,
 "Grouping items into bigger units is chunking: 10 digits become 3 chunks, so short-term memory (7 ± 2 items, or about 4 chunks) can hold them. Maintenance rehearsal is repeating; displacement is new items pushing old ones out; retrieval is getting a memory back." + rv(P16, 'mem', '16 Nov, memory models'),
 "16 Nov guide #mem, multi-store model: STM capacity 7 ± 2 items (newer research about 4 chunks); chunking (MTV CNN ABC FOX); maintenance rehearsal; decay or displacement; retrieval in the banner text."),
("Maths · Tue 17 Nov",
 "f(x) = 2x − 1 and g(x) = x<sup>2</sup>. The value of (g ∘ f)(3) is",
 ["17", "25", "14", "45"], 1,
 "In (g ∘ f)(3), f acts first: f(3) = 5, then g(5) = 25. 17 is (f ∘ g)(3) = f(9), the wrong order; 14 adds f(3) + g(3); 45 multiplies them. A composite is neither a sum nor a product." + rv(M17, 's25', '17 Nov, SL 2.5 composite functions'),
 "17 Nov Maths guide #s25 'Composite functions': (f ∘ g)(x) = f(g(x)), the function next to x goes first; trap: wrong order."),
("Biology · Wed 18 Nov",
 "Catalase releases 30 cm<sup>3</sup> of oxygen in 75 s. The rate of reaction is",
 [f"0.4 {CM3S}", f"2.5 {CM3S}", f"2{SP}250 {CM3S}", "0.4 cm<sup>3</sup>"], 0,
 f"Rate = amount ÷ time = 30 ÷ 75 = 0.4, and the unit is amount per time: {CM3S}. 2.5 divides the time by the amount; 2{SP}250 multiplies; \"0.4 cm<sup>3</sup>\" has lost the per-second part of the unit, which often has its own mark." + rv(B18, 'c11', '18 Nov, C1.1.9 measuring rates'),
 "18 Nov guide #c11 C1.1.9: rate = amount of product ÷ time, unit e.g. cm3 s−1; worked example 24 cm3 in 40 s = 0.6 cm3 s−1; 'There is often a separate mark for the unit'."),
("Business · Thu 12 Nov (week 1)",
 "A coffee brand lets local owners open cafés under its name. Each owner pays a fee plus a share of sales. This method of growth is",
 ["franchising", "a joint venture", "a merger", "a takeover"], 0,
 "Franchisees buy the right to trade under the franchisor's brand for a fee plus royalties (a share of sales): growth paid for by the franchisees, but less control over quality. A joint venture sets up a new company owned by both firms; a merger combines two firms into one; a takeover gains control of another firm, even against its managers' wishes." + rv(N12, 's15', '12 Nov, 1.5 growth'),
 "12 Nov Business guide (file 2026-11-06) #s15 'Internal and external growth' table: franchising (fee plus royalties, a share of sales; less control over quality), merger, takeover; joint venture in the same table and its quiz."),
("Psychology · Sat 14 Nov (week 1)",
 "A reaction-time app always adds exactly 50 ms to every time it records. The app is",
 ["valid but not reliable", "reliable but not valid", "both reliable and valid", "neither reliable nor valid"], 1,
 "It makes the same error every time, so its results are consistent (reliable) but always wrong (not valid), like a bathroom scale that is always 2 kg too heavy. A valid measure must also be reliable, so \"valid but not reliable\" cannot happen." + rv(P14, 'relval', '14 Nov, reliability and validity'),
 "14 Nov guide #relval: reliability = consistency (glossary p67); 'Reliable but not valid: a scale that is always 2 kg too heavy'; 'A valid measure must also be reliable (slide 113)'."),
("Business · Thu 19 Nov",
 "A retailer has a chief executive, 4 directors, 16 area managers and 64 store managers. It removes all the area managers, so the store managers report straight to the directors. What is each director's span of control now?",
 ["4", "16", "20", "64"], 1,
 "The 64 store managers are shared between 4 directors: 64 ÷ 4 = 16. Span of control counts only direct reports. 4 was each director's span before (16 ÷ 4); 64 is all the store managers; 20 adds the old and new numbers. Wider spans and fewer levels are what delayering does." + rv(N19, 's22', '19 Nov, 2.2 structure'),
 "19 Nov guide #s22: span of control = number reporting directly to one manager; worked example 2 Bloom Books delayering (24 ÷ 3 = 8 after) and its Finish it (48 ÷ 4 = 12)."),
("Maths · Tue 10 Nov (week 1)",
 "S<sub>n</sub> = n<sup>2</sup> + 3n is the sum of the first n terms of a sequence. Find u<sub>5</sub>.",
 ["40", "12", "28", "36"], 1,
 "u<sub>5</sub> = S<sub>5</sub> − S<sub>4</sub> = 40 − 28 = 12. 40 is S<sub>5</sub>, the sum of five terms, not the fifth term; 28 is S<sub>4</sub>; 36 is S<sub>5</sub> − S<sub>1</sub>, which removes only the first term." + rv(M10, 's12', '10 Nov, SL 1.2 given S<sub>n</sub>, find u<sub>n</sub>'),
 "10 Nov Maths guide (file 2026-11-04) #s12 'Given Sn, find un': u1 = S1 and un = Sn − Sn−1 (Learn); example u6 = S6 − S5."),
("English · Fri 20 Nov",
 "A panel shows a smiling family on a beach. The caption reads: \"A week later, the war began.\" Which word-picture combination is this?",
 ["Duo-specific", "Picture-specific", "Interdependent", "Word-specific"], 2,
 "The picture alone is a happy holiday; the words alone give a date. Together they say something neither says alone: this happiness is about to end, and the reader knows it before the family does. Duo-specific would need words and picture to say the same thing; picture-specific would need the picture to tell it all." + rv(E20, 'words', '20 Nov, words and pictures'),
 "20 Nov guide #words: seven word-picture combinations table (interdependent: together they say something neither could say alone); worked example: father laughing + caption 'That was the last time I saw him laugh' = interdependent."),
("Biology · Wed 18 Nov",
 "A protein has two polypeptide chains, of 40 and 25 amino acids, joined to each other by disulfide bonds. How many peptide bonds does it contain?",
 ["65", "64", "63", "39"], 2,
 "Count each chain separately: 40 − 1 = 39 and 25 − 1 = 24, total 63. 64 treats the two chains as one long chain; 65 counts amino acids, not bonds; 39 counts only the longer chain. The chains are joined by disulfide bonds, not peptide bonds." + rv(B18, 'b12', '18 Nov, B1.2.2 peptide bonds'),
 "18 Nov guide #b12 B1.2.2: a chain of n amino acids has n − 1 peptide bonds; worked example insulin 21 and 30 → 20 + 29 = 49, 'insulin's two chains are joined by disulfide bonds instead'."),
("Psychology · Mon 16 Nov",
 "In a Paper 1 Section A 4-marker, a student explains the theory and then gives two examples, just in case. How are the examples marked?",
 ["Both are marked and the better one counts", "Only the first example is credited", "Two examples move the answer into the top band", "Each example earns 2 extra marks"], 1,
 "The specimen markscheme credits only the first example, so a second one wastes minutes you need for the essay. The top band needs one example that is \"relevant and explained\" (guide p45)." + rv(P16, 'technique', '16 Nov, the 4-marker'),
 "16 Nov guide #technique: exam trap (2) 'Only your first example is credited (specimen markscheme)'; markband 3-4 'The example is relevant and explained' (p45)."),
("Biology C1.2 · Sun 22 Nov (today)",
 "In human muscle cells without enough oxygen, glucose is converted to",
 ["lactate, with no carbon dioxide", "lactate and carbon dioxide", "ethanol and carbon dioxide", "carbon dioxide and water"], 0,
 "Anaerobic respiration in humans: glucose → lactate, with no carbon dioxide. Ethanol and carbon dioxide come from yeast; carbon dioxide and water are the products of aerobic respiration. If you have not done today's C1.2 block yet, this was a preview: no Error log row needed." + rv(B22, 'c12sl', '22 Nov, C1.2.5 aerobic and anaerobic'),
 "22 Nov guide #c12sl C1.2.5: glucose → lactate (anaerobic, human muscle); table: waste products lactate (no carbon dioxide); exam trap: CO2 comes from yeast (C1.2.10 ethanol + CO2)."),
("Maths · Tue 17 Nov",
 "The range of f(x) = 3 − x<sup>2</sup>, x ∈ ℝ, is",
 ["f(x) ≥ 3", "f(x) ≤ 3", "x ≤ 3", "f(x) ≥ 0"], 1,
 "x<sup>2</sup> is never negative, so 3 − x<sup>2</sup> is at most 3 (at x = 0) and goes down without limit: f(x) ≤ 3. \"x ≤ 3\" writes the range with x, which the mark scheme does not accept; f(x) ≥ 3 has the direction wrong; f(x) ≥ 0 is the range of a square root." + rv(M17, 's22', '17 Nov, SL 2.2 range'),
 "17 Nov Maths guide #s22: range written with f(x) or y; exam trap (1) range with x not accepted; self-check 2: f(x) = 5 − x²/3, x² ≥ 0 so largest value f(0), range f(x) ≤ 5/3."),
("Biology · Sun 15 Nov (week 1)",
 "A triglyceride forms from one glycerol and three fatty acids. Which bonds form, and what happens to water?",
 ["Three ester bonds; three water molecules are released", "Three glycosidic bonds; three water molecules are released", "Three ester bonds; one water molecule is released", "Three ester bonds; three water molecules are used up"], 0,
 "Each fatty acid joins glycerol by a condensation reaction that makes one ester bond and releases one water molecule: three of each. Glycosidic bonds join sugars; using water up is hydrolysis, the reverse." + rv(B15, 'b11c', '15 Nov, B1.1.9 triglycerides'),
 "15 Nov guide #b11c B1.1.9: 'Triglyceride: glycerol + three fatty acids: three condensations, three ester bonds, three waters released'; exam trap: ester bond, not glycosidic; hydrolysis in B1.1.2-3."),
("Business · Thu 19 Nov",
 "A research lab's manager sets the goal and the deadline, then lets her team of experienced scientists decide how to reach it. Her leadership style is",
 ["autocratic", "paternalistic", "laissez-faire", "situational"], 2,
 "Setting the goal and letting expert, self-motivated staff decide how is laissez-faire. It is not \"no leader\": she still sets the goal. Autocratic and paternalistic leaders decide alone; situational means switching between styles to fit the task." + rv(N19, 's23', '19 Nov, 2.3 leadership'),
 "19 Nov guide #s23 styles table: laissez-faire = leader sets the goal, staff decide how; fits expert, self-motivated staff; exam trap (2) 'Laissez-faire is not no leader'."),
("Psychology · Mon 16 Nov",
 f"Reaction times (ms) of six students: 300, 320, 340, 360, 380, 1{SP}000. The median is",
 ["340 ms", "350 ms", "360 ms", "450 ms"], 1,
 f"Six values, already in order, so the median is the mean of the 3rd and 4th: (340 + 360) ÷ 2 = 350 ms. 340 or 360 takes only one of the middle two; 450 ms is the mean (2{SP}700 ÷ 6), pulled up by the outlier of 1{SP}000 ms, which is why the median is the better average here." + rv(P16, 'data', '16 Nov, HL averages'),
 "16 Nov guide #data: median 'With an even number of values, the mean of the middle two'; worked example 5: outlier pulls the mean, median the better measure."),
("Biology · Sat 21 Nov mock",
 "A Biology paper has 45 marks and no time printed. Using your mock page's pace of 1.2 minutes a mark, how long should you allow?",
 ["37.5 minutes", "45 minutes", "54 minutes", "60 minutes"], 2,
 "45 × 1.2 = 54 minutes. 37.5 divides by 1.2 instead of multiplying; 45 minutes is one minute a mark and leaves no time to check. Set a timer and move on when one question goes over its share." + rv(K21, 'bio-combined', '21 Nov, mock timing'),
 "21 Nov mock page #bio-combined: 'No time is printed, so 1.2 minutes a mark: 30 marks = 36 minutes.'"),
("English · Fri 13 Nov (week 1)",
 "A cartoon furiously attacks a company whose factory poisoned a river, drawing its boss as a vulture over dead fish. Its angry, harsh tone makes it",
 ["Horatian satire", "Juvenalian satire", "a comic strip", "a stereotype"], 1,
 "Juvenalian satire is harsh and angry and attacks serious harm; Horatian satire is gentle and amused. A comic strip mainly amuses. The vulture is a symbol (an animal standing for an idea), not a stereotype of a group." + rv(E13, 'satire', '13 Nov, satire'),
 "13 Nov English guide #satire: Horatian (gentle, amused) vs Juvenalian (harsh, angry; attacks serious harm: war, corruption); self-check 'oil spill' = Juvenalian; comic strip mainly amuses; #visual: symbolism = object or animal standing for an idea; stereotype = oversimplified picture of a group."),
("Biology · Wed 18 Nov",
 "Which of the bonds that hold a protein's tertiary structure is covalent?",
 ["Hydrogen bonds between polar R-groups", "Ionic bonds between charged R-groups", "Disulfide bonds between two cysteines", "Hydrophobic interactions between non-polar R-groups"], 2,
 "The disulfide bond (−S−S−) between the sulfur atoms of two cysteines is covalent, the strongest of the four. The other three are weaker, which is why heat and pH can break them and denature the protein." + rv(B18, 'b12hl', '18 Nov, B1.2.9 tertiary structure'),
 "18 Nov guide #b12hl B1.2.9 table: hydrogen bonds (polar R-groups), ionic bonds (charged), disulfide bonds (covalent, the strongest; two cysteines), hydrophobic interactions (non-polar); B1.2.5: heat/pH break bonds between R-groups."),
("Maths · Tue 17 Nov",
 "f(x) = 4x − 7. f<sup>−1</sup>(x) is",
 [fr('x + 7', '4'), fr('x − 7', '4'), "4x + 7", fr('1', '4x − 7')], 0,
 f"Swap: x = 4y − 7, so 4y = x + 7 and y = {fr('x + 7', '4')}. Check: f(3) = 5 and f<sup>−1</sup>(5) = 12 ÷ 4 = 3. {fr('x − 7', '4')} undoes the multiplying but not the subtracting; 4x + 7 undoes only the subtracting; {fr('1', '4x − 7')} is the reciprocal: f<sup>−1</sup> never means 1 over f." + rv(M17, 's25', '17 Nov, SL 2.5 finding the inverse'),
 "17 Nov Maths guide #s25 'Finding f−1(x) in four steps' (write y = f(x), swap, rearrange, state domain); trap (5) f−1(x) is not 1/f(x)."),
("Psychology · Mon 9 Nov (week 1)",
 "A study compares revising with flashcards and rereading. The flashcard group revises in a quiet library, the rereading group in a noisy canteen. The flashcard group scores higher. The noise is",
 ["a control variable", "a confounding variable", "the dependent variable", "the independent variable"], 1,
 "The noise was not controlled and differs between the conditions, so it could explain the result instead of the revision method: a confounding variable. A control variable is kept the same in every condition; the IV is the revision method and the DV is the test score." + rv(P09, 'exp', '9 Nov, confounding variables'),
 "9 Nov Psychology guide #exp 'Controls and confounding variables': control variable kept the same in every condition; confounding variable = extraneous variable not controlled and differing between conditions (RM01 slide 19); worked example 7 time of day."),
("Business · Thu 19 Nov",
 "Which is a hygiene factor in Herzberg's motivation-hygiene theory?",
 ["Recognition", "Responsibility", "Working conditions", "Promotion"], 2,
 "Hygiene factors are around the job (pay, conditions, security, supervision): poor ones cause dissatisfaction, good ones only remove it. Recognition, responsibility and promotion are motivators, in the job itself." + rv(N19, 's24', '19 Nov, 2.4 Herzberg'),
 "19 Nov guide #s24 'Herzberg: motivation-hygiene theory': hygiene factors (pay, conditions, security, supervision, policy, colleagues); motivators (achievement, recognition, the work itself, responsibility, promotion, growth)."),
("Biology C1.2 · Sun 22 Nov (today)",
 "A respirometer's capillary tube has an internal diameter of 1.0 mm. The coloured fluid moves 3.0 cm in 5 minutes. The rate of oxygen uptake is about",
 [f"0.47 {MM3M}", f"4.7 {MM3M}", f"18.8 {MM3M}", f"23.6 {MM3M}"], 1,
 f"r = 1.0 ÷ 2 = 0.5 mm and d = 3.0 cm = 30 mm, so volume = π × 0.5<sup>2</sup> × 30 = 23.6 mm<sup>3</sup>, and rate = 23.6 ÷ 5 = 4.7 {MM3M}. 18.8 uses the diameter as the radius; 0.47 leaves the distance in cm; 23.6 is the volume, not yet divided by the time. A calculator is fine here. A preview if you have not done today's Biology yet." + rv(B22, 'rate', '22 Nov, C1.2.6 respirometer'),
 "22 Nov guide #rate C1.2.6: volume of oxygen = π r² d, rate = volume ÷ time (mm3 min−1); worked example halves the diameter, converts cm to mm; 'Diameter instead of radius; cm mixed with mm' traps."),
("Maths · Tue 10 Nov (week 1)",
 "<span class='nw'>Σ from r = 5 to 12</span> of (3r − 1) equals",
 ["161", "182", "196", "222"], 2,
 f"Number of terms: 12 − 5 + 1 = 8. First term 3 × 5 − 1 = 14, last term 3 × 12 − 1 = 35, so the sum is {fr('8', '2')}(14 + 35) = 4 × 49 = 196. 161 uses only 7 terms (12 − 5, forgetting the + 1); 182 starts at r = 6; 222 starts at r = 1." + rv(M10, 's12', '10 Nov, sigma notation'),
 "10 Nov Maths guide #s12 'Sigma notation': number of terms = top − bottom + 1 (Learn); Sn = n/2(u1 + un) in booklet; trap (4) sigma terms."),
("English · Fri 20 Nov",
 "Panel 1: a girl packs a suitcase in her bedroom at night. Panel 2: the same girl, years older, walks out of an airport in another country. Which panel transition is this?",
 ["Moment-to-moment", "Action-to-action", "Scene-to-scene", "Aspect-to-aspect"], 2,
 "A jump across a lot of time and space is scene-to-scene: the reader fills a big gap (closure). Action-to-action shows one subject doing one thing after another; moment-to-moment shows almost no change; aspect-to-aspect shows different parts of one place or mood." + rv(E20, 'pace', '20 Nov, panels and closure'),
 "20 Nov guide #pace: six panel transitions table (scene-to-scene: a jump across a lot of time or space; the reader fills a big gap); closure definition."),
("Biology · Wed 18 Nov",
 "An inhibitor lowers the rate of an enzyme reaction, but adding much more substrate brings the rate back close to normal. The inhibitor is most likely",
 ["competitive, binding reversibly to the active site", "non-competitive, binding to an allosteric site", "mechanism-based, binding permanently to the active site", "denaturing the enzyme"], 0,
 "Only competitive inhibition depends on substrate concentration: substrate and inhibitor compete for the active site, so lots of substrate wins most collisions. With a non-competitive or mechanism-based inhibitor, or a denatured enzyme, more substrate does not help." + rv(B18, 'c11hl', '18 Nov, C1.1 inhibitors (HL)'),
 "18 Nov guide #c11hl C1.1.14-17 table: more substrate overcomes competitive, does not help non-competitive or mechanism-based; 'Only competitive inhibition depends on substrate concentration'; C1.1.7 denaturation."),
("Business · Thu 19 Nov",
 f"Lena earns a basic salary of $1{SP}500 a month plus 4% commission on her sales. This month she sold $20{SP}000. Her total pay is",
 ["$800", f"$2{SP}300", f"$9{SP}500", f"$81{SP}500"], 1,
 f"4% = 0.04, and 0.04 × 20{SP}000 = $800 commission, plus the $1{SP}500 basic: $2{SP}300. $800 forgets the basic salary; $9{SP}500 uses 0.4 (that is 40%); $81{SP}500 multiplies by 4 instead of 0.04." + rv(N19, 's24', '19 Nov, 2.4 financial rewards'),
 "19 Nov guide #s24 financial rewards table (commission = a percentage of sales); worked example 1 (5% as 0.05); self-check 3: $1 800 + 3% of $25 000 = $2 550."),
]
N_W2 = sum(1 for q in Q if 'week 1' not in q[0]); N_W1 = len(Q) - N_W2
assert (N_W2, N_W1) == (23, 8), (N_W2, N_W1)
assert all(0 <= a < len(o) for _, _, o, a, _, _ in Q)
assert all(len(set(o)) == len(o) for _, _, o, _, _, _ in Q)      # exactly one button can be right
labels = [q[0].split(' ')[0] for q in Q]
assert all(labels[i] != labels[i + 1] for i in range(len(labels) - 1)), labels   # interleaved: no subject twice in a row

qhtml = ''
for i, (s, q, opts, a, why, _src) in enumerate(Q, 1):
    b = ''.join(f'\n    <button>{o}</button>' for o in opts)
    qhtml += f'\n  <div class="q" data-a="{a}"><p><span class="subj">{s}</span>{i}. {q}</p>{b}\n    <div class="why">{why}</div></div>\n'

# ---- three written items (self-marked; not part of the saved quiz score)
W = [('psy', 'Psychology', 4, 'Paper 1 Section A style',
 '<p><b>Describe the multi-store model of memory with reference to one example.</b> [4]</p><p class="hint">Use a different example from the 16 Nov worked example (Peterson and Peterson): try the serial position effect.</p>',
 f'''<p><b>Model answer</b> (written for this site, not an official IB answer):</p>
<p><b>Point.</b> The multi-store model (Atkinson and Shiffrin, 1968) describes memory as three separate stores: sensory memory, short-term memory (STM) and long-term memory (LTM). Information flows one way: attention moves it from sensory memory into STM, which holds about 7 ± 2 items for about 15 to 30 seconds without rehearsal, and rehearsal moves it into LTM, which has no known limit.</p>
<p><b>Evidence.</b> The serial position effect (Glanzer and Cunitz, 1966): when people hear a list of words and recall it straight away, they remember the first words and the last words better than the words in the middle.</p>
<p><b>Explain.</b> The first words had the most time to be rehearsed, so they were passed on to LTM. The last words are still in STM at the moment of recall. The middle words were rehearsed little and were pushed out of STM by newer words (displacement). Two separate effects fit two separate stores, which is what the model describes.</p>
<p><b>Link.</b> So the model explains why forgetting depends on whether information was rehearsed into LTM.</p>
<p><b>Check it against the official markband</b> (Paper 1 Section A, IB Psychology guide p45):</p>
<ul><li>1 to 2 marks: "The response demonstrates limited knowledge relevant to the question." "The example is relevant but is not explained."</li>
<li>3 to 4 marks: "The response demonstrates detailed knowledge relevant to the question." "The example is relevant and explained."</li></ul>
<p><b>Tick list:</b> three stores named? attention and rehearsal as the routes between them? at least one capacity or duration? <b>one</b> example (only the first counts)? each part of the example matched to a part of the model (first words: LTM; last words: STM)? a link sentence, and no evaluation? All six: 3 to 4 band. Example named but not explained: 1 to 2. See the <a href="{P16}#mem">16 Nov memory section</a>.</p>'''),
('bus', 'Business', 4, 'Paper 1 style, short case',
 '''<p><i>PetPal sells pet food and accessories from 3 shops. Its 15 sales staff earn a fixed salary. Sales have not grown for a year, so the owner plans to pay a lower basic salary plus 5% commission on what each person sells.</i></p>
<p><b>Explain one advantage and one disadvantage for PetPal of paying its sales staff commission.</b> [4]</p>''',
 f'''<p><b>Model answer</b> (written for this site, not an official IB answer):</p>
<p><b>Advantage.</b> Commission links pay to sales, so each of the 15 staff now has a reason to sell more, for example suggesting a lead or a bed to a customer who came in for food. This could end PetPal's year of flat sales, and PetPal's pay bill only rises when sales rise.</p>
<p><b>Disadvantage.</b> Pay now falls when sales fall. In quiet months staff earn less and may feel insecure (security is a hygiene factor in Herzberg's theory), so some may leave and PetPal must recruit and train new staff. Staff in the same shop may also compete for customers, which can harm teamwork.</p>
<p><b>How to mark it</b> (the 2 + 2 pattern from your <a href="{N19}#s23">19 Nov Business guide</a>: each a point plus why, tied to the case; not an official mark scheme): advantage identified (1) and explained with PetPal's case (1); disadvantage identified (1) and explained with PetPal's case (1). No case facts (15 staff, 3 shops, flat sales, pet products): only the first mark of each pair. Describing piece rate or a pay rise instead of commission: 0 for that half.</p>'''),
('bio', 'Biology', 3, 'short written answer',
 '<p><b>Explain how the structure of the active site makes an enzyme specific, and why a denatured enzyme no longer works.</b> [3]</p>',
 f'''<p><b>Mark points</b> (written for this site in the style of your class mark schemes, one mark per point, max 3; not an official IB mark scheme. The official guide asks you to "explain these relationships" for C1.1.7):</p>
<ul><li>the active site's shape and chemical properties match (are complementary to) one substrate;</li>
<li>so only that substrate binds / forms an enzyme-substrate complex;</li>
<li>high temperature or extreme pH breaks the bonds that hold the enzyme's 3D shape (hydrogen and ionic bonds between R-groups);</li>
<li>so the active site changes shape and the substrate no longer fits / no enzyme-substrate complexes form;</li></ul>
<p>No mark for "peptide bonds break" or "the enzyme is killed". See C1.1.7 and B1.2.5 in your <a href="{B18}#c11">18 Nov Biology guide</a> if you missed one.</p>''')]
T_W = sum(w[2] for w in W); assert T_W == 11
whtml = ''
for k, subj, mx, kind, qtext, model in W:
    whtml += f'''
<div class="written card" id="w-{k}" data-k="w2-{k}" data-max="{mx}"><p class="wh"><span class="wsubj">{subj}</span> {kind}, {mx} marks</p>
{qtext}
<details><summary>Show model answer (only after you have written yours on paper)</summary>{model}</details></div>'''

# ---- timings: one hour; the 3-minute break sits between blocks 2 and 3
BD, BD_CHECK = 5, 2
QZ = 21
BRK = 3
W_WRITE, W_MARK = 12, 3
EL = 4
PLAN = 10
BLOCKS = [BD + BD_CHECK, QZ, BRK, W_WRITE + W_MARK, EL, PLAN]
assert sum(BLOCKS) == 60, BLOCKS
assert W_WRITE == 5 + 4 + 3          # Psychology 5, Business 4, Biology 3 minutes

DAYS = [('Psychology, Mon 16 Nov', P16, 'the 4-marker (PEEL and the markband), social learning theory, the multi-store model and levels of processing, HL averages'),
        ('Maths, Tue 17 Nov', M17, 'functions 2.2 to 2.5: domain and range, graphs, key features, composite and inverse functions'),
        ('Biology, Wed 18 Nov', B18, 'B1.2 proteins and C1.1 enzymes'),
        ('Business, Thu 19 Nov', N19, 'Unit 2, 2.1 to 2.4: HR planning and change, structure, leadership, motivation'),
        ('English, Fri 20 Nov', E20, 'Persepolis, "The Water Cell": shots and angles, panels and closure, words and pictures, the analysis chain'),
        ('Mock papers, Sat 21 Nov', K21, 'not "I can" lines: write the three things you would do differently next time')]
glist = ''.join(f'<li><b>{d}</b>: {t} (<a href="{u}">{"page" if "practice" in u else "guide"}</a>)</li>' for d, u, t in DAYS)

EXTRA_CSS = '''<style>
.quiz .q:not(.done) .subj{display:none}
.written .wh{font-weight:700;margin-bottom:6px}
.written .wsubj{display:inline-block;font-size:.75rem;font-weight:700;color:var(--indigo);background:var(--indigo-soft);padding:1px 7px;border-radius:3px}
.written details{background:#F7F8F6;border:1px solid var(--rule);padding:8px 12px;margin:10px 0}
.written summary{cursor:pointer;font-weight:600}
.written ul{padding-left:22px}
.written .hint{font-size:.92rem;color:var(--ink-soft)}
.stuck{background:var(--amber-soft);border-left:5px solid var(--amber);padding:10px 16px;margin:14px 0}
.star{color:var(--amber);font-weight:700}
.brk{text-align:center;font-weight:700;color:var(--green);background:var(--green-soft);padding:10px;margin:16px 0}
.goals{background:var(--green-soft);border-left:5px solid var(--green);padding:12px 16px;margin:24px 0 12px}
.goals ol{margin:6px 0 0;padding-left:22px}
.checked{font-size:.92rem;color:var(--ink-soft)}
</style>'''

body = f'''{EXTRA_CSS}
<div class="goals"><b>Today you will be able to</b><ol>
<li>pull week 2 out of memory and see which lines are still weak;</li>
<li>answer mixed questions from both weeks, choosing the method without being told the subject;</li>
<li>write and mark three exam answers, then turn your lost marks into a revision list for the exam fortnight.</li></ol></div>
<div id="warmup"></div>
<p class="checked">Checked against: your study pages for 9 to 22 November, which were checked against the official IB guides (Psychology, Maths, Business, Biology, Language and Literature) and your class mark schemes. The Psychology markband wording is quoted from the official guide; the Business and Biology mark points are written for this site, not taken from an official IB mark scheme.</p>
<div class="card"><b>How the hour goes:</b> {BLOCKS[0]} min brain dump, {QZ} min mixed quiz, a {BRK}-minute break, {BLOCKS[3]} min on three written questions, {EL} min Error log, {PLAN} min planning the exam fortnight. That is {sum(BLOCKS)} minutes. The planning hour later today finishes the plan.<br>
<span class="star">★</span> steps are extras. <b>Short on time: skip ★ steps, still do the quiz.</b></div>
<div class="stuck"><b>Stuck?</b> Look at the worked example in that day's guide (every quiz answer links to its section), then redo that section's self-check. Still stuck after 10 minutes? Log it as "ask teacher" in the Error log and move on.</div>

<div class="step"><div class="bh"><b>Block 1 · {BLOCKS[0]} min</b><span>Brain dump on a blank page</span></div><ol>
<li><b>{BD} min, no notes, page scrolled away.</b> Write the six headings below on a blank sheet. Under each, write every "I can" line you remember from that day, in your own words. Key words are enough.<ul>{glist}</ul></li>
<li><b>{BD_CHECK} min, check.</b> Open each guide and compare with its "I can" boxes. Tick what you had; add what you missed in a different colour. The missed lines are your weak spots for the quiz.</li>
<li><span class="star">★ If time:</span> add one example under each line you missed.</li></ol></div>

<div class="step"><div class="bh"><b>Block 2 · {QZ} min</b><span>Mixed quiz, both weeks (below)</span></div><ol>
<li>{len(Q)} questions: {N_W2} from this week and {N_W1} from week 1, mixed together. <b>The subject label is hidden until you answer.</b> Before you click, write in the margin which subject and which rule or method it needs (for example "Maths: inverse, swap x and y"). Spotting the method is what the exams test; mixing trains it.</li>
<li>Work each one on paper first, then click. Every answer explains the trap and links to the guide section. Maths without a calculator; Biology calculations may use one.</li>
<li>Two questions are on today's Biology (C1.2 cell respiration). If you have not done today's Biology block yet, reason them out: they are a preview and need no Error log row.</li>
<li><span class="star">★ If time:</span> any you got right by guessing count as wrong for the Error log.</li></ol></div>

<p class="brk">{BRK}-minute break: stand up, drink water, look out of a window. No phone.</p>

<div class="step"><div class="bh"><b>Block 3 · {BLOCKS[3]} min</b><span>Three written exam questions ({T_W} marks)</span></div><ol>
<li><b>{W_WRITE} min:</b> write all three on paper, page scrolled away: about 5 min for the Psychology one, 4 for Business, 3 for Biology.</li>
<li><b>{W_MARK} min:</b> open each "Show model answer", mark yours with the tick list or mark points, and choose your mark in the "My mark" menu under the question. It saves on this device.</li>
<li><span class="star">★ If time:</span> underline in your answer the words that earned each mark.</li></ol></div>
<section id="written"><h2>Written questions</h2>
{whtml}
</section>

<div class="step"><div class="bh"><b>Block 4 · {EL} min</b><span>Error log</span></div><ol>
<li>Open the <a href="{SHEET}">study sheet</a>, Error log tab. Write one row for every mark you lost today (quiz and written), with its type: <b>did not know</b>, <b>wrong method</b>, <b>slip</b>, <b>time</b> or <b>ask teacher</b>, and the rule that fixes it (for example "wrong method: in g ∘ f, f goes first").</li>
<li><b>Fix-it</b> (first 5 minutes of today's planning hour): take one written answer where you lost marks and rewrite it to full marks, using the tick list but your own words. Then close the page, redo that section's self-check from memory and write the rule.</li>
<li><span class="star">★ If time:</span> mark each new row with the week it came from, so repeats from week 1 stand out.</li></ol></div>

<div class="step" id="plan-exams"><div class="bh"><b>Block 5 · {PLAN} min</b><span>Plan the exam fortnight (23 Nov to 4 Dec)</span></div><ol>
<li><b>3 min.</b> On a sheet, make a table with one row per subject (Psychology, Maths, Biology, Business, English, French) and four columns: exam date, paper and topics, my top three Error log rules, my revision day. Fill in what you already know.</li>
<li><b>Tomorrow, ask each teacher for the exam date and the topics</b> (and which paper or question types). Write the six questions now, so you only have to ask: "When is our exam, and which topics and papers does it cover?"</li>
<li><b>4 min.</b> Read the whole Error log in the <a href="{SHEET}">study sheet</a>. For each subject, pick the three rows that came up most or cost the most marks and copy their rules into your table.</li>
<li><b>3 min.</b> In the study sheet's Daily plan tab, every weekday from 23 Nov already has one subject's revision. Write each subject's three rules into the Notes column of its revision day. If a date you learn tomorrow comes before that subject's revision day, swap the days so you revise first.</li>
<li><span class="star">★ If time:</span> put every exam date into your phone calendar with a reminder the day before.</li></ol></div>
<div class="card"><b>Later today</b>, in the planning hour: the Fix-it rewrite first, then finish the table, log CAS. Also useful: the <a href="../flashcards.html">flashcards</a> ("to repeat" cards), your <a href="../progress.html">progress page</a> (topics still amber or red), and the exam technique pages for <a href="../exam-psychology-hl.html">Psychology</a>, <a href="../exam-maths-aa-sl.html">Maths</a>, <a href="../exam-business-management-sl.html">Business</a> and <a href="../exam.html">all subjects</a>.</div>

<section class="quiz" id="quiz"><h2>Mixed quiz: weeks 1 and 2</h2>
<p style="font-size:.95rem;color:var(--ink-soft)">The subject appears after you answer. First decide: which subject, which method?</p>{qhtml}
  <div class="score" id="score">Score: 0 / {len(Q)} answered 0</div>
</section>
'''
html = page("Weekly review: week 2 (Sun 22 Nov 2026)", "../index.html", "Weekly review: week 2",
            "Sunday 22 November 2026. One hour (the rest of today is Biology C1.2 and planning the exam fortnight): pull week 2 out of memory, test yourself on both weeks mixed together, write three exam answers, then turn your mistakes into a revision plan.",
            body, quiz_js('ib-quiz-review-2026-11-22'), crumb_label="All days")
assert '—' not in html
open(out + '/review/2026-11-22-week-2.html', 'w').write(html)
print(len(Q), "questions (", N_W2, "week 2,", N_W1, "week 1 ),", len(W), "written items,", T_W, "written marks, blocks", BLOCKS)

if SRC_OUT:
    import re
    unfrac = lambda s: re.sub(r"<span class='frac'><span>(.*?)</span><span>(.*?)</span></span>", r'(\1)/(\2)', s)
    strip = lambda s: re.sub(r'<[^>]+>', '', unfrac(s)).replace('&nbsp;', ' ').replace('&gt;', '>')
    lines = ['# Week 2 review (Sun 22 Nov 2026): question sources', '',
             'Page: `~/ClaudeMe/study/review/2026-11-22-week-2.html` (generator `tools/review2.py`), quiz key `ib-quiz-review-2026-11-22`.',
             'Every question is new (not copied from a guide quiz); facts come only from the guide section named. Guide paths are under `~/ClaudeMe/study/`.', '',
             '## Multiple choice (correct option in brackets)', '']
    for i, (s, q, opts, a, why, src) in enumerate(Q, 1):
        lines.append(f'{i}. **{s}**: {strip(q)} [{strip(opts[a])}]  ')
        lines.append(f'   Source: {src}')
    lines += ['', '## Written items', '',
              f'- Psychology 4-marker (Paper 1 A), multi-store model with the serial position effect: `{P16[3:]}` #mem (multi-store model table, rehearsal, displacement, "Evidence (LC13) ... serial position effect (Glanzer and Cunitz, 1966)"); markband quoted from #technique (official guide p45); "only the first example is credited".',
              f'- Business 4-marker (mini case PetPal, commission): `{N19[3:]}` #s24 financial rewards table (commission: a percentage of sales; pay falls when sales fall), Herzberg hygiene factors incl. security; 2 + 2 marking pattern from #s23 worked example ("Marks: 2 + 2, each a point plus why, tied to the case").',
              f'- Biology 3-marker (active site, specificity, denaturation): `{B18[3:]}` #c11 C1.1.4, C1.1.5, C1.1.7 (complementary shape and chemical properties, enzyme-substrate complex, denaturation changes the active site) and #b12 B1.2.5 (heat/pH break bonds between R-groups, not peptide bonds; "denatured", never "killed"). Official guide C1.1.7: "Students should be able to explain these relationships." (refs/biology-guide.txt line 3457).',
              '', '## Numbers', '', 'All computed by asserts at the top of `tools/review2.py` (median 350, peptide bonds 63, rate 0.4, span 16, pay 2 300, 54 min, respirometer 23.6 mm3 and 4.7 mm3/min, u5 = 12, sigma 196 with 8 terms, cytosine 28%, (g o f)(3) = 25, inverse check f(3) = 5).', '']
    open(SRC_OUT, 'w').write('\n'.join(lines))
    print('sources written to', SRC_OUT)
