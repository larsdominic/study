import sys, json, html, re; sys.path.insert(0,sys.argv[1]); from common import *
out=sys.argv[2]
M='guides/2026-11-04-maths-aa-sl-1.2-1.6.html'
# (id, subject, topic, link, front, back)  -- add cards for every new guide here
cards=[
("m01","Maths","SL 1.2",M+"#s12","How do you test whether a sequence is arithmetic?","Check the differences are equal: u<sub>2</sub> − u<sub>1</sub> = u<sub>3</sub> − u<sub>2</sub>. That constant is d."),
("m02","Maths","SL 1.2",M+"#s12","n<sup>th</sup> term of an arithmetic sequence","u<sub>n</sub> = u<sub>1</sub> + (n − 1)d (in the formula booklet). n − 1 steps, not n."),
("m03","Maths","SL 1.2",M+"#s12","Sum of the first n terms of an arithmetic sequence (two forms)","S<sub>n</sub> = n/2 (2u<sub>1</sub> + (n − 1)d) = n/2 (u<sub>1</sub> + u<sub>n</sub>) (both in the booklet)."),
("m04","Maths","SL 1.2",M+"#s12","How many terms in a sigma sum from r = a to r = b?","b − a + 1. From r = 3 to r = 12 is 10 terms, not 9."),
("m05","Maths","SL 1.2",M+"#s12","You are given S<sub>n</sub>. How do you find u<sub>n</sub> and u<sub>1</sub>?","u<sub>n</sub> = S<sub>n</sub> − S<sub>n−1</sub>, and u<sub>1</sub> = S<sub>1</sub>."),
("m06","Maths","SL 1.2",M+"#s12","Simple interest: arithmetic or geometric?","Arithmetic: the same amount is added every year (for example 5000 + 189n)."),
("m07","Maths","SL 1.2",M+"#s12","Data is nearly but not exactly arithmetic. How do you model it?","Approximate d by the average step: (last − first) ÷ (number of gaps). Predictions far outside the data are less reliable."),
("m08","Maths","SL 1.3",M+"#s13","How do you test whether a sequence is geometric?","Check the ratios are equal: u<sub>2</sub>/u<sub>1</sub> = u<sub>3</sub>/u<sub>2</sub>. That constant is r."),
("m09","Maths","SL 1.3",M+"#s13","n<sup>th</sup> term of a geometric sequence","u<sub>n</sub> = u<sub>1</sub>r<sup>n−1</sup> (in the booklet)."),
("m10","Maths","SL 1.3",M+"#s13","Sum of the first n terms of a geometric sequence","S<sub>n</sub> = u<sub>1</sub>(r<sup>n</sup> − 1)/(r − 1) = u<sub>1</sub>(1 − r<sup>n</sup>)/(1 − r), r ≠ 1 (in the booklet)."),
("m11","Maths","SL 1.3",M+"#s13","Two terms of a geometric sequence are given. Fastest way to find r?","Divide them: u<sub>5</sub>/u<sub>2</sub> = r<sup>3</sup>. Remember r<sup>2</sup> = 3 gives r = ±√3."),
("m12","Maths","SL 1.3",M+"#s13","Grows by 2.5% a year. Multiplier? After n years or in year n?","× 1.025. After n years: × 1.025<sup>n</sup>. In year n when year 1 is the start: × 1.025<sup>n−1</sup>."),
("m13","Maths","SL 1.8",M+"#s18","Sum to infinity and its condition","S<sub>∞</sub> = u<sub>1</sub>/(1 − r), only if |r| &lt; 1 (in the booklet). Always write the check."),
("m14","Maths","SL 1.8",M+"#s18","First term of the sum from r = 1 of 5(1/4)<sup>r</sup>?","Put r = 1: 5 × 1/4 = 5/4, not 5."),
("m15","Maths","SL 1.8",M+"#s18","Ball dropped from h, each bounce reaches r of the last. Total distance?","h + 2 × hr/(1 − r). The first drop counts once, every later height twice."),
("m16","Maths","SL 1.4",M+"#s14","Compound interest formula","FV = PV × (1 + r/(100k))<sup>kn</sup> (in the booklet). k = 1 yearly, 2 half-yearly, 4 quarterly, 12 monthly."),
("m17","Maths","SL 1.4",M+"#s14","Depreciation by r% a year for n years","Value = original × (1 − r/100)<sup>n</sup>."),
("m18","Maths","SL 1.4",M+"#s14","Real value of an investment with inflation i% a year","Divide the nominal value by (1 + i/100)<sup>n</sup>. Quick method: use the rate r − i."),
("m19","Maths","SL 1.4",M+"#s14","GDC financial app: the sign rule","PV and FV must have opposite signs (money paid in is negative)."),
("m20","Maths","SL 1.6",M+"#s16","= or ≡ ?","= is true for some values (x + 2 = 5). ≡ is true for every value (an identity)."),
("m21","Maths","SL 1.6",M+"#s16","How to lay out an LHS to RHS proof","Start from one side only, change it step by step, reach the other side, write \"= RHS\" and a concluding sentence."),
("m22","Maths","SL 1.6",M+"#s16","Algebraic form of an even and of an odd integer","Even 2k, odd 2k + 1. Two different odd numbers: 2a + 1 and 2b + 1."),
("m23","Maths","Exam","exam-maths-aa-sl.html","Command term \"Write down\"","Obtain the answer, usually by extracting information. Little or no calculation; working does not need to be shown."),
("m24","Maths","Exam","exam-maths-aa-sl.html","Command term \"Hence\"","Use the preceding work to obtain the required result. Another method scores nothing."),
("m25","Maths","Exam","exam-maths-aa-sl.html","Paper 1 and Paper 2: calculator?","Paper 1: no calculator. Paper 2: GDC required. Both 90 minutes, 80 marks."),
("n01","Business","1.1","guides/2026-11-06-business-sl-1.1-1.6.html#s11","Name the four sectors of the economy with one example each","Primary: takes natural resources (farm, mine). Secondary: manufacturing and construction (factory). Tertiary: services to people (shop, bank). Quaternary: knowledge and information (software, research)."),
("n02","Business","1.1","guides/2026-11-06-business-sl-1.1-1.6.html#s11","Added value","Selling price minus the cost of bought-in materials and services. Wages, rent and profit come out of it, so it is <b>not</b> profit."),
("n03","Business","1.1","guides/2026-11-06-business-sl-1.1-1.6.html#s11","Entrepreneur vs intrapreneur","Entrepreneur: spots an opportunity, organises the resources and takes the risk of starting a business. Intrapreneur: an employee who acts entrepreneurially inside an existing organisation, using its resources."),
("n04","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","Limited vs unlimited liability","Unlimited: the owner is personally liable for all business debts (sole traders, most partners). Limited: shareholders can lose at most what they invested."),
("n05","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","Privately held vs publicly held company","Both have limited liability and are in the private sector. Privately held: shares sold privately, with the other owners agreeing. Publicly held: shares sold to the general public on a stock exchange."),
("n06","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","Cooperative: main features","Owned and run by its members (workers, customers or producers), usually one member one vote; profits shared among members or reinvested. A for-profit social enterprise."),
("n07","Business","1.2","guides/2026-11-06-business-sl-1.1-1.6.html#s12","NGO","Non-governmental organisation: a non-profit social enterprise, independent of government, run for a cause; funded by donations, grants and fundraising; any surplus goes to the cause."),
("n08","Business","1.3","guides/2026-11-06-business-sl-1.1-1.6.html#s13","Vision statement vs mission statement","Vision: the long-term ideal future the organisation wants to reach. Mission: its purpose now, what it does, for whom and what it values."),
("n09","Business","1.3","guides/2026-11-06-business-sl-1.1-1.6.html#s13","Strategic vs tactical objectives","Strategic: long term, whole organisation, set by senior managers. Tactical: shorter term, one department or area, helps achieve a strategic objective."),
("n10","Business","1.3","guides/2026-11-06-business-sl-1.1-1.6.html#s13","Corporate social responsibility (CSR)","Acting in the interests of society and the environment <b>beyond</b> what the law requires, and taking responsibility for the effects of the business."),
("n11","Business","1.4","guides/2026-11-06-business-sl-1.1-1.6.html#s14","Internal vs external stakeholders","Internal: employees, managers and directors, shareholders. External: customers, suppliers, lenders, government, local community, pressure groups, competitors."),
("n12","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Average cost formula (is it on the formula sheet?)","Average cost = total cost &divide; output. Not on the formula sheet: learn it."),
("n13","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Six internal economies of scale","Purchasing (bulk buying), technical, financial, marketing, managerial, risk-bearing."),
("n14","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","External economies of scale vs external growth","External economies: lower average costs because the whole industry or area grows. External growth: growing by joining with or working through other firms (M&amp;As, takeovers, joint ventures, alliances, franchising)."),
("n15","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Joint venture vs strategic alliance","Joint venture: firms create a new, separate business they own together. Strategic alliance: firms cooperate but stay independent, and no new business is created."),
("n16","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Merger vs acquisition vs takeover","Merger: two firms agree to combine into one. Acquisition: one firm buys a controlling interest in another, with its agreement. Takeover: a hostile acquisition, against the wishes of the target managers."),
("n17","Business","1.5","guides/2026-11-06-business-sl-1.1-1.6.html#s15","Franchising: who pays whom?","The franchisee pays the franchisor an initial fee plus royalties (a share of sales) for the right to use its brand and system."),
("n18","Business","1.6","guides/2026-11-06-business-sl-1.1-1.6.html#s16","MNC, home country and host country","MNC: a company with its head office in one country that produces in more than one country. Home country: where the head office is. Host country: any other country where it operates."),
("m26","Maths","SL 2.2","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s22","Largest possible domain: the two things you must avoid at SL","Dividing by zero and the square root of a negative number. Example: √(2 − x) needs x ≤ 2."),
("m27","Maths","SL 2.2","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s22","Domain and range: which letter do you write them in?","Domain in x (x ≤ 2). Range in f(x) or y (f(x) ≥ 0). A range written with x loses the mark."),
("m28","Maths","SL 2.2","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s22","Solving f(x) = 10 is the same as finding ...","f<sup>−1</sup>(10): the input that f sends to 10."),
("m29","Maths","SL 2.2","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s22","How do you get the graph of f<sup>−1</sup> from the graph of f?","Reflect it in the line y = x: each point (a, b) on f becomes (b, a) on f<sup>−1</sup>."),
("m30","Maths","SL 2.2","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s22","When does a function have an inverse function?","Only when it is one-to-one: each output comes from exactly one input. A horizontal line crosses its graph at most once."),
("m31","Maths","SL 2.2","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s22","Domain and range of f<sup>−1</sup>","Domain of f<sup>−1</sup> = range of f. Range of f<sup>−1</sup> = domain of f."),
("m32","Maths","SL 2.2","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s22","Interval notation for x ≥ 1 and for 2 &lt; x &lt; 5","[1, ∞[ and ]2, 5[. A bracket turned outwards means that end is not included."),
("m33","Maths","SL 2.3","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s23","Command terms: draw or sketch?","Draw: accurate, to scale, points plotted, ruler for straight lines. Sketch: general shape with the relevant features labelled."),
("m34","Maths","SL 2.3","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s23","What must every sketch of a graph show?","Labelled axes, intercepts, turning points, asymptotes (dashed, with equations), end points of a restricted domain, and the right shape at both ends."),
("m35","Maths","SL 2.4","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s24","Zeros, roots, x-intercepts: what are they?","Three names for the same x-values, where f(x) = 0. As points they are (x, 0)."),
("m36","Maths","SL 2.4","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s24","Axis of symmetry and vertex of y = ax<sup>2</sup> + bx + c","x = −b/(2a) (in the booklet). Put that x back in to get the y-coordinate of the vertex, which is the max or min value."),
("m37","Maths","SL 2.4","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s24","Asymptotes of y = 1 + 3/(x − 2)","Vertical x = 2 (the denominator is zero). Horizontal y = 1 (the fraction tends to 0). Always write them as equations."),
("m38","Maths","SL 2.4","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s24","Points of intersection of y = f(x) and y = g(x)","Solve f(x) = g(x) for x, then find each y. On the GDC: graph both and use intersect. Give points, not just x-values."),
("m39","Maths","SL 2.5","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s25","(f ∘ g)(x) means ...","f(g(x)): g acts first, then f. Usually (f ∘ g)(x) ≠ (g ∘ f)(x)."),
("m40","Maths","SL 2.5","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s25","Identity property of an inverse","(f ∘ f<sup>−1</sup>)(x) = (f<sup>−1</sup> ∘ f)(x) = x. It is also the quickest check of an inverse."),
("m41","Maths","SL 2.5","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s25","Four steps to find f<sup>−1</sup>(x)","Write y = f(x), swap x and y, make y the subject, write f<sup>−1</sup>(x) = ... and state its domain (the range of f)."),
("m42","Maths","SL 2.5","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s25","Is f<sup>−1</sup>(x) the same as 1/f(x)?","No. f<sup>−1</sup> undoes f. For f(x) = 2x + 1, f<sup>−1</sup>(x) = (x − 1)/2, but 1/f(x) = 1/(2x + 1)."),
("m43","Maths","SL 2.5","guides/2026-11-10-maths-aa-sl-2.2-2.5.html#s25","Inverse of f(x) = (x − 1)<sup>2</sup> + 3, x ≥ 1: plus or minus root?","Plus: f<sup>−1</sup>(x) = 1 + √(x − 3), x ≥ 3, because the range of f<sup>−1</sup> must be the domain of f (y ≥ 1)."),
("b01","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a11","What is a hydrogen bond in water?","The attraction between a δ+ hydrogen of one water molecule and the δ− oxygen of a neighbouring molecule. It is between molecules; the O-H bonds inside a molecule are polar covalent."),
("b02","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a11","Why is a water molecule polar?","Oxygen is more electronegative than hydrogen, so it pulls the shared electrons towards itself (O δ−, H δ+), and the bent shape (about 104.5°) stops the charges cancelling."),
("b03","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a11","Cohesion vs adhesion","Cohesion: water sticking to water (hydrogen bonds between water molecules). Adhesion: water sticking to other polar or charged materials such as cellulose, xylem walls, glass, soil."),
("b04","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a11","Two consequences of cohesion for organisms","Water is pulled up the xylem under tension as an unbroken column; surface tension lets small animals such as pond skaters stand on water."),
("b05","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a11","Which property forms a meniscus and drives capillary action in cell walls and soil?","Adhesion (to polar surfaces), with cohesion pulling the following molecules along. Not cohesion or surface tension alone."),
("b06","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a115","Hydrophilic, hydrophobic, amphipathic: meanings and one example each","Hydrophilic: attracted to water (glucose, salts). Hydrophobic: non-polar, not attracted (fats, oils). Amphipathic: both parts in one molecule (phospholipids)."),
("b07","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a115","How are glucose, oxygen and cholesterol carried in blood?","Glucose: dissolved in plasma. Oxygen: a little dissolved, nearly all bound to haemoglobin. Cholesterol (and fats): inside lipoproteins."),
("b08","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a115","Four physical properties of water vs air that matter to aquatic animals","Buoyancy (much more support), viscosity (more drag, so streamlining), thermal conductivity (heat lost about 24 times faster, so blubber), specific heat capacity (stable water temperature)."),
("b09","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a115","Sweating cools you because of which property of water?","High latent heat of vaporisation: evaporating water must break hydrogen bonds, which takes a lot of heat from the body. Not specific heat capacity."),
("b10","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a115","(HL) Where did Earth's water probably come from, and why did Earth keep it?","Mainly from asteroids (extraplanetary origin). Kept because Earth's gravity holds the atmosphere and its distance from the Sun keeps temperatures between 0 and 100 °C, so water stays liquid."),
("b11","Biology","A1.1","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a115","(HL) What is the Goldilocks zone?","The range of distances from a star where a planet's surface is neither too hot nor too cold, so liquid water can exist. The search for life elsewhere starts with water."),
("b12","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12","The three parts of a nucleotide and their drawing shapes","Phosphate (circle), pentose sugar (pentagon: deoxyribose in DNA, ribose in RNA), nitrogenous base (rectangle). Base on carbon 1′, phosphate on carbon 5′."),
("b13","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12","Bases in DNA and in RNA","DNA: adenine, cytosine, guanine, thymine. RNA: adenine, cytosine, guanine, uracil (uracil replaces thymine)."),
("b14","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12","Complementary base pairing in DNA","Adenine with thymine, guanine with cytosine, held by hydrogen bonds (A-T two, G-C three)."),
("b15","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12","Three structural differences between DNA and RNA","DNA: two strands (double helix), deoxyribose, thymine. RNA: one strand, ribose, uracil."),
("b16","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12","What forms the backbone of a DNA or RNA strand?","Alternating sugar and phosphate groups joined by covalent bonds (phosphate to carbon 3′ of the next sugar), made by condensation reactions."),
("b17","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12","How many base sequences are possible with n bases? Why are codons triplets?","4<sup>n</sup>. Pairs give only 16 codes, fewer than 20 amino acids; triplets give 64."),
("b18","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12","Why is the universal genetic code evidence for common ancestry?","Which triplet codes for which amino acid is arbitrary, yet almost all organisms share the same code, so it was most likely inherited from one common ancestor."),
("b19","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12hl","(HL) What is at the 5′ end and at the 3′ end of a strand? Which end grows?","5′ end: phosphate on carbon 5′. 3′ end: sugar with a free -OH on carbon 3′. New nucleotides are added only to the 3′ end, so strands grow 5′ to 3′."),
("b20","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12hl","(HL) Purines and pyrimidines, and why each pair needs one of each","Purines (two rings): adenine, guanine. Pyrimidines (one ring): cytosine, thymine, uracil. Purine plus pyrimidine keeps the helix the same width everywhere, so it is stable."),
("b21","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12hl","(HL) Structure of a nucleosome","DNA wound about twice round a core of eight histone proteins (two each of four types), held by an H1 histone, with linker DNA to the next nucleosome. Prokaryotes have none."),
("b22","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12hl","(HL) Hershey-Chase: labels and results","<sup>35</sup>S labels protein and ended in the supernatant (stayed outside). <sup>32</sup>P labels DNA and ended in the pellet (entered the bacteria). So DNA is the genetic material."),
("b23","Biology","A1.2","guides/2026-11-05-biology-hl-a1.1-a1.2.html#a12hl","(HL) What did Chargaff find, and what did it falsify?","A ≈ T and G ≈ C, but the proportions differ between species and are not 25% each. This falsified the tetranucleotide hypothesis (four bases in equal, repeating amounts)."),
("p01", "Psychology", "Frame", "guides/2026-11-09-psychology-hl-frame-research-methods.html#frame", "Psychology (class definition)", "The scientific study of behaviour and mental processes."),
("p02", "Psychology", "Frame", "guides/2026-11-09-psychology-hl-frame-research-methods.html#frame", "The six concepts", "Bias, causality, change, measurement, perspective, responsibility."),
("p03", "Psychology", "Frame", "guides/2026-11-09-psychology-hl-frame-research-methods.html#frame", "The four content areas", "Biological, cognitive and sociocultural approaches, plus research methodology."),
("p04", "Psychology", "Frame", "guides/2026-11-09-psychology-hl-frame-research-methods.html#frame", "The four contexts", "Health and well-being; human development; human relationships; learning and cognition."),
("p05", "Psychology", "Frame", "guides/2026-11-09-psychology-hl-frame-research-methods.html#frame", "The two HL extensions", "The role of culture, motivation and technology in shaping human behaviour; data analysis and interpretation."),
("p06", "Psychology", "Frame", "guides/2026-11-09-psychology-hl-frame-research-methods.html#frame", "HL papers: time, marks, weight", "P1 1 h 30, 35 marks, 25%. P2 1 h 30, 35 marks, 25%. P3 1 h 45, 30 marks, 30%."),
("p07", "Psychology", "Frame", "guides/2026-11-09-psychology-hl-frame-research-methods.html#frame", "The IA (HL)", "Research proposal: design a study but do not carry it out. 24 marks, 20%, max 2 200 words."),
("p08", "Psychology", "Command terms", "guides/2026-11-09-psychology-hl-frame-research-methods.html#cmd", "Describe", "Give a detailed account."),
("p09", "Psychology", "Command terms", "guides/2026-11-09-psychology-hl-frame-research-methods.html#cmd", "Explain", "Give a detailed account including reasons or causes."),
("p10", "Psychology", "Command terms", "guides/2026-11-09-psychology-hl-frame-research-methods.html#cmd", "Evaluate", "Make an appraisal by weighing up the strengths and limitations."),
("p11", "Psychology", "Command terms", "guides/2026-11-09-psychology-hl-frame-research-methods.html#cmd", "Discuss", "Offer a considered and balanced review that includes a range of arguments, factors or hypotheses. Opinions or conclusions should be presented clearly and supported by appropriate evidence."),
("p12", "Psychology", "Command terms", "guides/2026-11-09-psychology-hl-frame-research-methods.html#cmd", "Compare and contrast", "Give an account of similarities and differences between two (or more) items or situations, referring to both (all) of them throughout."),
("p13", "Psychology", "Concepts", "guides/2026-11-09-psychology-hl-frame-research-methods.html#concepts", "Bias (opening statement)", "A bias is a limitation in objective thinking; it is a tendency to perceive information through a cognitive filter of experience and preference."),
("p14", "Psychology", "Concepts", "guides/2026-11-09-psychology-hl-frame-research-methods.html#concepts", "Causality (opening statement)", "Psychologists investigate the relationship between variables with the goal of determining cause-and-effect relationships."),
("p15", "Psychology", "Concepts", "guides/2026-11-09-psychology-hl-frame-research-methods.html#concepts", "Change (opening statement)", "A key focus of psychological research is how to apply theory and psychological findings with the goal of changing individual behaviours."),
("p16", "Psychology", "Concepts", "guides/2026-11-09-psychology-hl-frame-research-methods.html#concepts", "Measurement (opening statement)", "A fundamental challenge for psychologists is that human behaviour is difficult to observe and objectively measure."),
("p17", "Psychology", "Concepts", "guides/2026-11-09-psychology-hl-frame-research-methods.html#concepts", "Perspective (opening statement)", "No single perspective explains behaviour sufficiently on its own; each provides a means by which to interpret and examine behaviour."),
("p18", "Psychology", "Concepts", "guides/2026-11-09-psychology-hl-frame-research-methods.html#concepts", "Responsibility (opening statement)", "Psychologists rely on humans as participants in their research; the relationship between researchers and participants is based on the premise of treating each other with respect."),
("p19", "Psychology", "RM", "guides/2026-11-09-psychology-hl-frame-research-methods.html#vars", "Operationalisation (guide glossary)", "Stating exactly how a variable will be manipulated or measured in experimental research."),
("p20", "Psychology", "RM", "guides/2026-11-09-psychology-hl-frame-research-methods.html#vars", "IV and DV", "IV: what the researcher changes (at least two conditions). DV: what the researcher measures."),
("p21", "Psychology", "RM", "guides/2026-11-09-psychology-hl-frame-research-methods.html#exp", "True experiment (guide glossary)", "A controlled experiment where researchers manipulate an independent variable to observe its impact on a dependent variable, using random allocation of participants to conditions to ensure causation."),
("p22", "Psychology", "RM", "guides/2026-11-09-psychology-hl-frame-research-methods.html#exp", "True vs quasi-experiment: the key difference", "Random allocation. In a quasi-experiment the groups already exist (age, gender, diagnosis), so it cannot establish cause and effect."),
("p23", "Psychology", "RM", "guides/2026-11-09-psychology-hl-frame-research-methods.html#exp", "Extraneous vs confounding variable", "Extraneous: anything other than the IV that could affect the DV. Confounding: an extraneous variable not controlled that differs between conditions."),
("p24", "Psychology", "Sampling", "guides/2026-11-09-psychology-hl-frame-research-methods.html#samp", "The five sampling techniques in the guide", "Self-selected, opportunity, stratified, random, snowball."),
("p25", "Psychology", "Sampling", "guides/2026-11-09-psychology-hl-frame-research-methods.html#samp", "Random sampling vs random allocation", "Random sampling: every member of the population has an equal chance of being in the study. Random allocation: chance decides each participant's condition."),
]
for c in cards: assert "—" not in c[4]+c[5]
data=[dict(id=a,s=b,t=t,l=l,f=f,b=bk) for a,b,t,l,f,bk in cards]
# Anki import file: front<TAB>back<TAB>tags
with open(out+'/flashcards-anki.txt','w') as fh:
    fh.write("#separator:tab\n#html:true\n#tags column:3\n")
    for a,s,t,l,f,bk in cards:
        fh.write(f"{f}\t{bk}\tIB::{s} {t.replace(' ','_')}\n")
body='''
<div class="card" style="margin-top:24px">
  <p style="margin:0 0 8px"><b>How to use:</b> read the question, answer it out loud or on paper, then press <b>Show answer</b>. Press <b>Again</b> if you were wrong or slow, <b>Got it</b> if you knew it. "Again" cards come back first next time. Your progress is saved on this device.</p>
  <div id="filters" style="display:flex;flex-wrap:wrap;gap:6px"></div>
</div>
<div id="stats" style="font-size:.92rem;color:var(--ink-soft);margin:8px 2px"></div>
<div class="card" id="box" style="min-height:220px">
  <div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;font-size:.85rem;color:var(--ink-soft)"><span id="meta"></span><a id="src" href="#">open the section</a></div>
  <p id="front" style="font-size:1.25rem;font-weight:600;margin:14px 0"></p>
  <div id="back" style="display:none;border-top:1px solid var(--rule);padding-top:12px;font-size:1.08rem"></div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:16px">
    <button id="show" class="fb">Show answer</button>
    <button id="again" class="fb" style="display:none;background:var(--red-soft);border-color:var(--red)">Again</button>
    <button id="got" class="fb" style="display:none;background:var(--green-soft);border-color:var(--green)">Got it</button>
  </div>
</div>
<p style="font-size:.92rem;color:var(--ink-soft)">Prefer Anki? Download <a href="flashcards-anki.txt" download>flashcards-anki.txt</a> and use File, Import in Anki. <button id="reset" class="fb" style="font-size:.85rem;padding:3px 10px;margin-left:6px">Reset progress</button></p>
<style>.fb{font:inherit;padding:8px 16px;border-radius:6px;border:1px solid var(--rule);background:#F3F5F2;color:var(--ink);cursor:pointer}.fb.on{background:var(--indigo);color:#fff;border-color:var(--indigo)}</style>
'''
script='''
var CARDS=__DATA__;
var KEY='ib-flash-v1', st={}; try{st=JSON.parse(localStorage.getItem(KEY)||'{}');}catch(e){}
var subj='All', cur=null, queue=[];
function save(){try{localStorage.setItem(KEY,JSON.stringify(st));}catch(e){}}
function box(c){return (st[c.id]&&st[c.id].b)||0;}
function pool(){return CARDS.filter(function(c){return subj==='All'||c.s===subj;});}
function build(){var p=pool();
  // never-seen and "again" cards first, then by box, keep list order inside a box
  queue=p.slice().sort(function(a,b){var sa=st[a.id]?1:0, sb=st[b.id]?1:0; var ka=st[a.id]?box(a)+1:0, kb=st[b.id]?box(b)+1:0; return ka-kb;});
}
function stats(){var p=pool(),again=0,learning=0,known=0,fresh=0;p.forEach(function(c){if(!st[c.id])fresh++;else if(box(c)===0)again++;else if(box(c)<3)learning++;else known++;});
  document.getElementById('stats').textContent=p.length+' cards: '+fresh+' new, '+again+' to repeat, '+learning+' learning, '+known+' known (3 correct in a row)';}
function next(){if(!queue.length)build(); cur=queue.shift();
  document.getElementById('meta').textContent=cur.s+' · '+cur.t;
  var a=document.getElementById('src'); a.href=cur.l;
  document.getElementById('front').innerHTML=cur.f; var bk=document.getElementById('back'); bk.innerHTML=cur.b; bk.style.display='none';
  document.getElementById('show').style.display=''; document.getElementById('again').style.display='none'; document.getElementById('got').style.display='none'; stats();}
document.getElementById('show').onclick=function(){document.getElementById('back').style.display='block';this.style.display='none';document.getElementById('again').style.display='';document.getElementById('got').style.display='';};
document.getElementById('again').onclick=function(){st[cur.id]={b:0,d:Date.now()};save();queue.splice(Math.min(3,queue.length),0,cur);next();};
document.getElementById('got').onclick=function(){var b=box(cur);st[cur.id]={b:Math.min(3,(st[cur.id]?b:0)+1),d:Date.now()};save();next();};
document.getElementById('reset').onclick=function(){if(confirm('Forget all flashcard progress on this device?')){st={};save();build();next();}};
var subs=['All'];CARDS.forEach(function(c){if(subs.indexOf(c.s)<0)subs.push(c.s);});
var fl=document.getElementById('filters');subs.forEach(function(s){var b=document.createElement('button');b.className='fb'+(s===subj?' on':'');b.textContent=s;b.onclick=function(){subj=s;[].forEach.call(fl.children,function(x){x.classList.toggle('on',x===b);});build();next();};fl.appendChild(b);});
build();next();
'''.replace('__DATA__',json.dumps(data,ensure_ascii=False))
open(out+'/flashcards.html','w').write(page("Flashcards: IB study","index.html","Flashcards","The things to learn by heart from each study guide: formulas, definitions and exam rules. Five to ten minutes a day beats an hour once a week.",body,script))
print(len(cards),"cards")
