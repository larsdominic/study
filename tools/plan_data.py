# Jamila IB catch-up plan, Mon 9 Nov to Fri 4 Dec 2026 (clean slate from 9 Nov, Lars 8 Nov).
# Single source for: the new study sheet (Daily plan tab), the site's tools/plan.json + landing LINKS, the plan doc.
# Links: ("d", drive_id, label) for Drive files, ("u", url, label) for checked free web resources.
D = lambda i, l: ("d", i, l)
U = lambda u, l: ("u", u, l)
B1 = "Class follow-up (homework, notes, questions)"
SITE = "https://larsdominic.github.io/study/"

# ---- frequently used files (new IDs after the 8 Nov re-upload) ----
P_GUIDE = D("1Khqsn6PrxoS5UXAEKBpu5G_XG5Viyvtq", "Psychology subject guide")
P_SPEC = D("1KoOk8IT670o-bbr1HKc-Nw2Kub_Gf1Mr", "Psychology specimen papers")
P_GLO = D("1pjh95S1mQYIxbI25HhP19Ozc3JBE7A1N", "Psychology glossary")
M_SEQ_Q = D("1HUMbO0pFdie-qUVSvB5vzkLBLLErWCnL", "Sequences questions")
M_SEQ_MS = D("13_E6OeummnBtiEB9_BRN9tZCKe2HhilT", "Sequences mark scheme")
M_PROOF = D("1e3vUzjc8okb6yeCJ5ivd9HlTg4M_WbJ7", "Proof questions")
M_FB = D("19EX75prXgep28AagsDaWsr3eM6O8rVDV", "Formula booklet")
M_FN_Q = D("19sUU39ZRrlpkzKm-X7eaQcAT9Hjs9I0F", "Functions toolkit questions")
M_FN_S = D("1FAgeuAIx3kqqFpTTW6A3A-iArnzCoDKN", "Functions toolkit with solutions")
M_GDC = D("1GuVaS8OSu_0PNWIqlOIego3OE-LbtTtc", "GDC guide")
M_QUAD = D("1kAuZnYoA_0MO217OygT4zNmOJDWC5HJL", "Quadratics worksheet")
M_IA_A = D("1RoBiMtL5XS2KliU-GQynzZcQILzvaWui", "Maths IA Form A")
M_IA_S = D("17bWOHVKnzm-j0yzDJgxJzwzMfUmSkhvQ", "Maths IA slides")
BIO_DECK = D("1hDdIMtkgSsy9MQQIDUwo5JYk9morjjGK", "Biology Term 1 deck (link)")
BM_BOOK = D("1iruwf2Cjk2ngbd7GGVwk2wQq9XiTHvIk", "Hoang textbook")
BM_GUIDE = D("1KeX_WVc4uNQe-DdGS_7-1ITxBUqXveWD", "Business subject guide")
BM_STK_Q = D("18s5gxSC3ZwLebfmXzMPTYTVW9RaqV_WC", "Stakeholders questions")
BM_STK_MS = D("1hW8ntJdHx822fn6maOFfjKE4h2JRKDK8", "Stakeholders mark scheme")
BM_10 = D("1j1O-rA6lhi9CtxIdMGN93TBIW2IBGKd-", "10-marker format guide")
E_CART = D("1Sk7GD4FmWcB_crdej9xiSiWgg1iFySKR", "Satirical cartoons Paper 1 guide")
E_HORSEY = D("1mSfhzzcuxkvOuk33g9wqVY3xyNvbx7nP", "Horsey model answer")
E_BIG5 = D("1vXYq3D89JG8VLj2LIBcx1qnC-8RECXus", "The Big 5 slides")

DAYS = [
 # iso, day, date, week, hours, block1, subject, task, files (text), links, guide (site path or list of {url,label,quiz,review})
 dict(iso="2026-11-09", subject="Psychology (session 1)",
      task="New subject: the course map (approaches, concepts, contexts, the three HL papers and the IA), command terms, then research methods: variables, experiments, hypotheses, sampling. Follow the study guide block by block.",
      files="Psychology: subject guide, RM01 slides 1-59, RM02 and RM03 Giddens worksheets, concept sheets",
      links=[P_GUIDE, D("1cZcJIRkFGJhbWusL1hGaQZF7k2K-Wq3H","RM01 research methods slides"), D("1Aah8cvs6dwSuv8rOC00F6r5z8caaMmRG","RM02 experiments worksheet"), D("1s87lpvDXR_nv-OtaZaYoEbiBblXQFLsR","RM03 sampling worksheet"), D("1exoZh04Ac6Wym__lOYzQ8CuMHCfVtALC","Concept: Measurement"), D("1wiNZuZ7aX8NFteaqO9qwcsN9tfnMdpBL","Concept: Perspective"), P_GLO],
      guide=[dict(url="guides/2026-11-09-psychology-hl-frame-research-methods.html", label="Psychology HL: course map and research methods", quiz="ib-quiz-guide-2026-11-09")]),
 dict(iso="2026-11-10", subject="Maths",
      task="Sequences and series (official 1.2, 1.3, 1.4, 1.8) and proof (1.6) with the study guide; questions from the IB Questionbank pack, mark with the mark scheme; proof pack.",
      files="Maths AA SL: sequences pack + mark scheme, proof pack, formula booklet",
      links=[M_SEQ_Q, M_SEQ_MS, M_PROOF, M_FB],
      guide=[dict(url="guides/2026-11-04-maths-aa-sl-1.2-1.6.html", label="Maths AA SL 1.2 to 1.6 (sequences, series, proof)", quiz="ib-quiz-guide-2026-11-04")]),
 dict(iso="2026-11-11", subject="Biology",
      task="A1.1 Water and A1.2 Nucleic acids with the study guide and the summary notes; HL topical past papers, mark with the mark schemes.",
      files="Biology HL: A1.1 and A1.2 summary notes, HL topical papers + mark schemes, Term 1 deck",
      links=[D("1SaM0o8i5oZfHbB4oTpBY2s1OK4JIwlce","A1.1 summary notes"), D("10zk6yBpp_cXHh1hp9_11PcpETIgvIS6m","A1.2 summary notes"), D("110xkxMcBUsogPMOYuEjP8OokodQjw0iC","A1.1 HL questions"), D("1wlCYMEBgo2r6VEpaKs3xrcGwtUTckRkW","A1.1 HL mark scheme"), D("1sAe7m4WMX5Kb7nZt_fTYH9yD2rSS5zsp","A1.2 HL questions"), D("1A7Czi962qDxtXcddAV58Sg6DQNUbJBJX","A1.2 HL mark scheme"), BIO_DECK],
      guide=[dict(url="guides/2026-11-05-biology-hl-a1.1-a1.2.html", label="Biology HL A1.1 Water and A1.2 Nucleic acids", quiz="ib-quiz-guide-2026-11-05")]),
 dict(iso="2026-11-12", subject="Business + French (30 min)",
      task="Business Unit 1 (1.1 to 1.6) with the study guide and Hoang chapters 1.1 to 1.6; Priyanka Chopra case study against the mark scheme. French (30 min): cause and consequence grammar (17 and 18 Sep screenshots).",
      files="Business SL: textbook, Priyanka Chopra case + mark scheme, stakeholders questions; French B: grammar screenshots",
      links=[BM_BOOK, D("1PRR0uuj04ZK421Pa4LGzexhYnZw0yhbX","Priyanka Chopra case"), D("1Mcwj-VFwsFtFWXASfW1D3_E8xA2xAJKB","Priyanka Chopra mark scheme"), BM_STK_Q, BM_STK_MS, BM_10, D("17Gk45ODOkOje3MB4BlZiMXXpHlH-KGet","French: cause/consequence verbs"), D("17QY-rZlaM40MHvERe2ZjwL4seqQ-1rdd","French: verb exercise"), D("1d54TG2mwqwqvXnPtxVhKrcmIZHn5GuHo","French: connectors exercise")],
      guide=[dict(url="guides/2026-11-06-business-sl-1.1-1.6.html", label="Business Management SL Unit 1, 1.1 to 1.6", quiz="ib-quiz-guide-2026-11-06")]),
 dict(iso="2026-11-13", subject="English + French (30 min)",
      task="English Paper 1, satirical cartoons: Big 5 slides, revision guide steps 1 to 5, read the Horsey 20/20 model, then write one analytical paragraph. French (30 min): listening, the 'L'art, solution contre le stress ?' transcript (summarise in French, list 10 new words).",
      files="English (Lang & Lit): cartoons revision guide, Horsey model, Big 5 slides; French B: art and stress transcript",
      links=[E_BIG5, E_CART, E_HORSEY, D("1aNvK8Zyfvi0RpdAjAtMhlJbN064Dkn8W","French: art and stress transcript")],
      guide=[dict(url="guides/2026-11-13-english-a-hl-paper1-satirical-cartoons.html", label="English A HL Paper 1: satirical cartoons", quiz="ib-quiz-guide-2026-11-13")]),
 dict(iso="2026-11-14", subject="Timed practice + TOK + Psychology (session 2)",
      task="1 h: timed Maths set, sequences, no calculator (study site), then mark. 1 h TOK: exhibition prep (independent investigation task, May 2026 subject report pages, exhibition rubric). 2 h Psychology: evaluating research, then classical and operant conditioning. Take a 10-min break between the parts.",
      files="Maths: sequences pack + MS; TOK: exhibition task, subject report, rubric; Psychology: RM01 slides 60-148, RM04 task, LC01, LC02, LC03, LC06, LC07",
      links=[M_SEQ_Q, M_SEQ_MS, D("1k4p3RV7H_Qlt3tY9MRwgu9gJwx4R994Y","TOK exhibition task"), D("174JzLTpQ04ZtAsEBQeunwMmylTXKU5Jh","TOK subject report May 2026"), D("1ZVIRvkEVU_Gc0R5pVikFLhjWLaJoXixZ","TOK exhibition rubric"), D("1flZ_D46k42AkC-ctI-Syh2qtVWKygnG1","Psych RM04 evaluating research"), D("1lkfhHQ-iViZRwBVG8Nt9_yxnMVmHmsNu","Psych LC01 cognitive approach"), D("18G55fgHqH329URQeM2Ykm0o_JpWRWZsf","Psych LC02 classical conditioning"), D("1goFIwsIryUI9nB4CuG9HAXkTCPv5v-X0","Psych LC03 Skittles worksheet"), D("1DP96OHhubbSrZTsFbdy0U4VuoAbPIXqo","Psych LC06 operant conditioning"), D("1cZcJIRkFGJhbWusL1hGaQZF7k2K-Wq3H","Psych RM01 slides (60-148)"), D("1g3T5D0BLCgjobVuQfgqqGmJvEbqFsalW","Psych LC07 Dallery study"), D("1Aah8cvs6dwSuv8rOC00F6r5z8caaMmRG","Psych RM02 experiments worksheet")],
      guide=[dict(url="guides/2026-11-14-psychology-hl-evaluating-research-conditioning.html", label="Psychology HL: evaluating research and conditioning", quiz="ib-quiz-guide-2026-11-14"), dict(url="practice/2026-11-07-timed-maths-sequences.html", label="Timed set: Maths sequences (no calculator)", quiz="ib-timed-2026-11-07")]),
 dict(iso="2026-11-15", subject="Week review + Biology B1.1 + plan + CAS",
      task="1 h: week 1 review page (Error log top 3, mixed quiz, flashcards). 2 h Biology: B1.1 Carbohydrates and lipids from the summary notes and the Term 1 deck (slides 241-362); HL topical pack, skip Q1 (it is in the 21 Nov mock), mark with the mark scheme. 1 h: plan next week, log CAS. Take a 10-min break between the parts.",
      files="Biology HL: B1.1 summary notes, B1.1 HL topical questions + mark scheme, Term 1 deck",
      links=[D("1Kcwxqupd_m7EiVX29SDDbC3PBc5ufknX","B1.1 summary notes"), D("16BAwh43g-yPtpnlj6EFXTgi89E5Y7KeT","B1.1 HL questions"), D("1ZSJTC85Bs07He9mWFmCMACGV01loodJl","B1.1 HL mark scheme"), BIO_DECK],
      guide=[dict(url="guides/2026-11-15-biology-hl-b1.1-carbohydrates-lipids.html", label="Biology HL B1.1 Carbohydrates and lipids", quiz="ib-quiz-guide-2026-11-15"), dict(url="review/2026-11-08-week-1.html", label="Week 1 review", quiz="ib-quiz-review-2026-11-08")]),
 dict(iso="2026-11-16", subject="Psychology (session 3)",
      task="Exam technique (classical conditioning 4-marker, timed 10 min), social learning theory (slides, key terms, mindmap, then the quiz 4-marker on aggression marked against the exemplar), memory: multi-store model and levels of processing, HL start: levels of measurement and averages.",
      files="Psychology: EX01, LC09-LC11, EX03 mark scheme, LC13, LC14, HL01, specimen paper",
      links=[D("1PRhaPPsIOqIk3SR-hFoj-ihbJioLIbcv","EX01 Paper 1 practice"), D("1uFDHyaGy0dTjFsQOHTMkk06TWdiFrdgD","LC09 social learning theory"), D("1JUhZK_tTTblZ0womqTrPS9RU19fci850","LC10 SLT key terms"), D("1BK35SHCOZ60enGlCcuTp4Ce4PyoFfHRb","LC11 SCT mindmap"), D("1XdzFHCKtH4ON-6unUNZ2lNobc45Szg3A","EX03 quiz mark scheme"), D("1em1IyD-CEsjzBsy13z6RBcjn_h4wzOt_","LC13 memory models"), D("1k8Zn60K1jfXQIEJIRxgeXYkuNbfThLil","LC14 cognitive models worksheet"), D("1WASZdO0iLXxNuY7JfEdTtwbAoYVITuWv","HL01 central tendency"), P_SPEC],
      guide=[dict(url="guides/2026-11-16-psychology-hl-slt-memory-exam-technique.html", label="Psychology HL: social learning theory, memory, exam technique", quiz="ib-quiz-guide-2026-11-16")]),
 dict(iso="2026-11-17", subject="Maths",
      task="Functions 2.2 to 2.5 (domain and range, graphs, composite and inverse functions) with the study guide; functions toolkit pack, check against the solutions version; GDC guide for graphs and intersections.",
      files="Maths AA SL: functions toolkit questions + solutions, GDC guide, formula booklet",
      links=[M_FN_Q, M_FN_S, M_GDC, M_FB],
      guide=[dict(url="guides/2026-11-10-maths-aa-sl-2.2-2.5.html", label="Maths AA SL 2.2 to 2.5 (functions)", quiz="ib-quiz-guide-2026-11-10")]),
 dict(iso="2026-11-18", subject="Biology",
      task="B1.2 Proteins (no notes file in the Drive: use the Term 1 deck and the HL pack mark scheme's tips) and C1.1 Enzymes and metabolism (summary notes). HL topical packs, about 15 marks each, skip B1.2 Q1 and C1.1 Q1-2 (they are in the 21 Nov mock); mark with the mark schemes.",
      files="Biology HL: B1.2 and C1.1 HL topical questions + mark schemes, C1.1 summary notes, Term 1 deck",
      links=[D("1akQqhFxyv-Br_QT6gVbuRUOk0fDtkE5Y","B1.2 HL questions"), D("1neUWjQfWI5VM8Pr1II-OXGtiEmgZiC78","B1.2 HL mark scheme"), D("1meJNCi9WbEl-xS0APA0aHqWE1rnbOyds","C1.1 summary notes"), D("13qg60J1odzTkDIDiyujJlONsVCyt-eem","C1.1 HL questions"), D("1DgkqjNngIKSiV6Lityt-hnozdafoZeCz","C1.1 HL mark scheme"), BIO_DECK],
      guide=[dict(url="guides/2026-11-18-biology-hl-b1.2-c1.1.html", label="Biology HL B1.2 Proteins and C1.1 Enzymes", quiz="ib-quiz-guide-2026-11-18")]),
 dict(iso="2026-11-19", subject="Business + French (30 min)",
      task="Business Unit 2 HRM 2.1 to 2.4 (HR planning, organisational structure, leadership and management, motivation) from Hoang Unit 2 and the free IB teacher pages for 2.1, 2.2, 2.3 and 2.4 (the class slides are missing); the tutor2u pages are extras. Notes: learn the 5 IB leadership styles (autocratic, paternalistic, democratic, laissez-faire, situational) from the 2.3 page; Herzberg's two-factor theory is what the IB calls motivation-hygiene theory; matrix structure is SL; skip the HL parts (shamrock and project-based structures, McClelland, Deci and Ryan, equity and expectancy theory, labour turnover, appraisal, recruitment, job descriptions) and ignore Pink (old syllabus). Then the NorthStar Dairies 10-marker (stakeholders Q2), timed 20 min, mark with the mark scheme. French (30 min): start the screen-time writing task (plan + first 150 words).",
      files="Business SL: Hoang textbook Unit 2, stakeholders questions + mark scheme, 10-marker guide, tutor2u pages; French B: writing task (25 Sep)",
      links=[BM_BOOK, U("https://sites.google.com/view/ibbusinessandmanagement/unit-2-human-resources/2-1-introduction-to-human-resource-management","IB page: 2.1 intro to HRM"), U("https://sites.google.com/view/ibbusinessandmanagement/unit-2-human-resources/2-2-organizational-structure","IB page: 2.2 structure"), U("https://sites.google.com/view/ibbusinessandmanagement/unit-2-human-resources/2-3-leadership-and-management","IB page: 2.3 leadership"), U("https://sites.google.com/view/ibbusinessandmanagement/unit-2-human-resources/2-4-motivation-and-demotivation","IB page: 2.4 motivation"), U("https://www.tutor2u.net/business/reference/workforce-planning","tutor2u: workforce planning"), U("https://www.tutor2u.net/business/reference/span-of-control","tutor2u: span of control"), U("https://www.tutor2u.net/business/reference/leadership-styles","tutor2u: leadership styles"), U("https://www.tutor2u.net/business/reference/motivation-theories-explained","tutor2u: motivation theories"), U("https://www.tutor2u.net/business/reference/motivation-herzberg-two-factor-theory","tutor2u: Herzberg"), BM_STK_Q, BM_STK_MS, BM_10, D("1Hqi6Qh2X_FeRENOisYlvq6koDnDQH9QY","French: writing task")],
      guide=[dict(url="guides/2026-11-19-business-sl-unit2-hrm.html", label="Business Management SL Unit 2 HRM", quiz="ib-quiz-guide-2026-11-19")]),
 dict(iso="2026-11-20", subject="English + French (30 min)",
      task="English, Persepolis: recap the film codes and comics terms, answer 'The Water Cell' Parts 1 and 2 and mark them with the answer sheet, then write the Part 4 Paper 1 paragraph and compare with the model. French (30 min): finish the screen-time text (250 to 400 words).",
      files="English (Lang & Lit): Water Cell answer sheet, film codes worksheet, Persepolis LitChart, Bicycle and Water Cell notes; French B: writing task",
      links=[D("1J_dJFwabatvDaJTrPJ1LpiSug5BZoQGP","Water Cell questions + answers"), D("1H51Jgsj4O8ylb7bb9CxFMS-0nEOuS1zW","Film codes worksheet"), D("1BrxGopIN15j-7jwiJdcnQxxkUOFPKuHW","Bicycle and Water Cell notes"), D("1l84bHxigAm2MQERz1D_BAFqhtRx-OK85","Persepolis LitChart"), D("1Hqi6Qh2X_FeRENOisYlvq6koDnDQH9QY","French: writing task")],
      guide=[dict(url="guides/2026-11-20-english-a-hl-persepolis-water-cell.html", label="English A HL: Persepolis, The Water Cell", quiz="ib-quiz-guide-2026-11-20")]),
 dict(iso="2026-11-21", subject="Mock papers + Psychology (session 4)",
      task="Timed, no notes, follow the study-site page: Biology Grade 11 combined paper HL plus a mock selection, one English Paper 1 cartoon analysis, then Psychology session 4 (Paper 1 A and B block, research methods set, HL Paper 3 Q1-2). Mark everything with the mark schemes and markbands; log mistakes. Breaks are planned on the page.",
      files="Biology HL: combined paper HL, mock paper + mark scheme; English: cartoons guide, Horsey model; Psychology: EX01, RM04, specimen papers",
      links=[D("1-fhyVSaXdMn9DuMLD5SWpO5TV37zB8eW","Bio combined paper HL"), D("1S-X8BUmQiUTuiLWlr382zDg1dFsjcyLW","Bio mock questions"), D("1bS3dMIiu8HZOnYBdk5U3FvWgjHS5gJLe","Bio mock mark scheme"), E_CART, E_HORSEY, D("1PRhaPPsIOqIk3SR-hFoj-ihbJioLIbcv","Psych EX01"), D("1flZ_D46k42AkC-ctI-Syh2qtVWKygnG1","Psych RM04"), D("1upA3pwuiQj7stqZapW62OuZ9wedazOW-","Psych RM06 practical template"), P_SPEC, P_GUIDE, D("1yjhzAAk0bqPrv-wCYw5DxB8uQP89z_Hp","Bio combined paper SL (extra)")],
      guide=[dict(url="practice/2026-11-21-mock-papers.html", label="Mock papers: Biology, English, Psychology", quiz="ib-timed-2026-11-21")]),
 dict(iso="2026-11-22", subject="Week review + Biology C1.2 + exam plan",
      task="1 h: Error log review (all subjects), build the exam-fortnight revision list. 2 h Biology: C1.2 Cell respiration from the summary notes; HL topical pack about 15 marks incl. one respirometer question, mark with the mark scheme. 1 h: plan the exam fortnight, log CAS.",
      files="Biology HL: C1.2 summary notes, C1.2 HL topical questions + mark scheme",
      links=[D("139mP607DbLhM4Dg7YFm-uVQoN07iMOW-","C1.2 summary notes"), D("1q0i1Ut8OaAjMKTUtHKpRWdlrrg4KF_jG","C1.2 HL questions"), D("1rcsdV7q0tDQtubaS1suHzUE-AnrDMKx6","C1.2 HL mark scheme")],
      guide=[dict(url="review/2026-11-22-week-2.html", label="Week 2 review", quiz="ib-quiz-review-2026-11-22"), dict(url="guides/2026-11-22-biology-hl-c1.2-cell-respiration.html", label="Biology HL C1.2 Cell respiration", quiz="ib-quiz-guide-2026-11-22")]),
 # ---------------- exam window: revision, redo Error log mistakes; review the guides ----------------
 dict(iso="2026-11-23", subject="Psychology (revision)",
      task="Revision, from memory first: 5-min brain dump of everything you know; then the shuffled re-take of the 9, 14 and 16 Nov guide quizzes; redo the 6 Oct quiz short answers from the mark scheme (answers covered); Fix-it: rewrite your weakest 21 Nov answer to the top markband. Last 15 min: due flashcards from other subjects.",
      files="Psychology: EX03 quiz mark scheme, glossary, Error log",
      links=[D("1XdzFHCKtH4ON-6unUNZ2lNobc45Szg3A","EX03 quiz mark scheme"), P_GLO],
      guide=[dict(url="guides/2026-11-09-psychology-hl-frame-research-methods.html", label="Psychology: course map and research methods", quiz="ib-quiz-guide-2026-11-09", review=True), dict(url="guides/2026-11-14-psychology-hl-evaluating-research-conditioning.html", label="Psychology HL: evaluating research and conditioning", quiz="ib-quiz-guide-2026-11-14", review=True), dict(url="guides/2026-11-16-psychology-hl-slt-memory-exam-technique.html", label="Psychology HL: social learning theory, memory, exam technique", quiz="ib-quiz-guide-2026-11-16", review=True)]),
 dict(iso="2026-11-24", subject="Maths",
      task="Revision, from memory first: 5-min brain dump; Error log lines; shuffled re-take of both Maths guide quizzes; a timed set of 5 questions from the sequences and functions packs, marked with the mark schemes; Fix-it rewrites. Quadratics (official 2.6-2.7) only if the teacher confirms it is on the Maths exam: then the worksheet with the GDC guide. Last 15 min: due flashcards from other subjects.",
      files="Maths AA SL: quadratics worksheet, GDC guide, formula booklet, Error log",
      links=[M_QUAD, M_GDC, M_FB, M_SEQ_MS, M_FN_S],
      guide=[dict(url="guides/2026-11-04-maths-aa-sl-1.2-1.6.html", label="Maths 1.2 to 1.6", quiz="ib-quiz-guide-2026-11-04", review=True), dict(url="guides/2026-11-10-maths-aa-sl-2.2-2.5.html", label="Maths 2.2 to 2.5", quiz="ib-quiz-guide-2026-11-10", review=True)]),
 dict(iso="2026-11-25", subject="Biology",
      task="Revision A1.1, A1.2, B1.1, from memory first: 5-min brain dump; Error log lines; timed InThinking topic tests A1.2 and B1.1, marked with their mark schemes; A1.1 test if time; Fix-it rewrites. Last 15 min: due flashcards from other subjects.",
      files="Biology HL: InThinking topic tests A1.1, A1.2, B1.1 + mark schemes, summary notes",
      links=[D("1SHxFDU3WZIAcz3xGE022MSugMfQo26Jc","A1.2 topic test"), D("1y9aE0VEiPYHblwoLX-LtyYGW2McyzO1K","A1.2 test mark scheme"), D("1hq33th0_apNZ4jkbGqSSmGNzoWwKyi6T","B1.1 topic test"), D("1dl4R7i9JspYqViCskiHNp1ssX3XojFFX","B1.1 test mark scheme"), D("15-g45sYFJCjY9voplAebcHUGJhDj1XMk","A1.1 topic test"), D("1QZwF3gD2hqGgwd6PL4Ilguhie1XfmA1m","A1.1 test mark scheme")],
      guide=[dict(url="practice/2026-11-25-biology-revision-a1-b1.1.html", label="Timed revision: Biology A1.1, A1.2, B1.1", quiz="ib-timed-2026-11-25"), dict(url="guides/2026-11-05-biology-hl-a1.1-a1.2.html", label="Biology A1.1 and A1.2", quiz="ib-quiz-guide-2026-11-05", review=True), dict(url="guides/2026-11-15-biology-hl-b1.1-carbohydrates-lipids.html", label="Biology HL B1.1 Carbohydrates and lipids", quiz="ib-quiz-guide-2026-11-15", review=True)]),
 dict(iso="2026-11-26", subject="Business + French (30 min)",
      task="Business revision, from memory first: 5-min brain dump of Units 1 and 2; shuffled re-take of both Business guide quizzes; one timed 10-marker with the mark scheme; Fix-it rewrite. The toolkit (SWOT, STEEPLE, Ansoff) only if the teacher confirms it is on the exam: then the free pages linked (STEEPLE has 7 factors, Ethical included; PESTLE sites leave Ethical out) and the McDonald's CosMc's Ansoff question. French (30 min): photo analysis phrase bank, describe one photo out loud for 3 minutes.",
      files="Business SL: Ansoff exam question (mark scheme inside), 10-marker guide, toolkit pages; French B: phrase bank (2 Sep)",
      links=[D("1lqBHPjTZcvGgY-2_yxOAl283Jraedh8q","Ansoff McDonald's question"), BM_10, U("https://www.tutor2u.net/business/reference/swot-analysis","tutor2u: SWOT"), U("https://www.tutor2u.net/business/reference/ansoffs-matrix","tutor2u: Ansoff"), U("https://sites.google.com/view/ibbam/business-management-toolkit/steeple-analysis","Toolkit: STEEPLE"), BM_GUIDE, D("1OBmRitJaciZS1NDYQwHxde3KnIb0T2fv","French: photo phrase bank")],
      guide=[dict(url="guides/2026-11-06-business-sl-1.1-1.6.html", label="Business Unit 1", quiz="ib-quiz-guide-2026-11-06", review=True), dict(url="guides/2026-11-19-business-sl-unit2-hrm.html", label="Business Management SL Unit 2 HRM", quiz="ib-quiz-guide-2026-11-19", review=True)]),
 dict(iso="2026-11-27", subject="English + French (30 min)",
      task="English revision, from memory first: 5-min brain dump of the cartoon analysis chain and the Persepolis visual terms; Error log; a second timed cartoon analysis paragraph, self-marked with the criteria checklist; Fix-it rewrite. French (30 min): your corrected writing task, then the 9 cause connectors from the flashcards.",
      files="English (Lang & Lit): cartoons guide, graphic novels session slides; French B: grammar screenshots",
      links=[E_CART, D("193O2yAwIEA-yMGF_1PGG4I9UEHl8RKy_","Graphic novels session 3"), D("1dPY1MSzxeClWZnuqlcg-Gkfs2izvvreb","Graphic novels session 4"), D("1VeAjxEUlIENsgDKDWh6zrRjKCgSEZrwn","Graphic novels session 5"), D("11InV6-AedsZkNS5C9f5XOfr7z_yavt-u","Graphic novels session 7"), D("1d54TG2mwqwqvXnPtxVhKrcmIZHn5GuHo","French: connectors")],
      guide=[dict(url="guides/2026-11-27-english-a-hl-revision-1.html", label="English revision 1: timed cartoon analysis", quiz="ib-quiz-guide-2026-11-27")]),
 dict(iso="2026-11-28", subject="Light revision + Maths IA Form A",
      task="Maths IA Form A (due Mon 30 Nov, 4 pm: confirm the date with the teacher), using the IA slides. Then light mixed revision: re-do the timed Maths set and the week 1 review quiz. Rest afterwards.",
      files="Maths AA SL: IA Form A, IA slides",
      links=[M_IA_A, M_IA_S],
      guide=[dict(url="practice/2026-11-07-timed-maths-sequences.html", label="Timed set: Maths sequences", quiz="ib-timed-2026-11-07", review=True), dict(url="review/2026-11-08-week-1.html", label="Week 1 mixed quiz", quiz="ib-quiz-review-2026-11-08", review=True), dict(url="review/2026-11-22-week-2.html", label="Week 2 mixed quiz", quiz="ib-quiz-review-2026-11-22", review=True)]),
 dict(iso="2026-11-29", subject="Rest + plan the exam week",
      task="Rest. Plan the last exam week, check exam dates, sleep.",
      files="", links=[]),
 dict(iso="2026-11-30", subject="Psychology (revision)",
      task="HL data block: the Bandura vs Charlton homework, the 'space between data and conclusion' handout (Paper 3-style limitation in 3 sentences), the levels of processing answer key Q10-13 as prompts; then a 15-minute command-term and concept drill. (Maths IA Form A due 4 pm today.)",
      files="Psychology: HL02 homework, HL05 handout, RM05 answer key, HL03 source cards",
      links=[D("1EUXpuau1dt9DGImsFaEmUkzm4uhYAqEk","HL02 Bandura vs Charlton"), D("1wFfgZKnqZpR8MwI3vLZwZpaBLI8BnbeW","HL05 data and conclusion"), D("154Sv75_2rUuphHDny_SyP0Fx0WaqWniH","RM05 answer key"), D("16iMT1Pt_X1Z4pTY4TeuD83WpOOQdtIw1","HL03 Clancy source cards"), D("1u4egvuCi6IjpuM18g9lU3_MUMjvHOehc","HL04 Clancy debate rules"), P_GLO, P_SPEC],
      guide=[dict(url="guides/2026-11-30-psychology-hl-data-analysis.html", label="Psychology HL: data analysis and interpretation (Paper 3)", quiz="ib-quiz-guide-2026-11-30")]),
 dict(iso="2026-12-01", subject="Maths",
      task="Revision, from memory first: 5-min brain dump; Error log; redo the worst 5 questions of the sequences and functions packs under time; formula booklet fluency; Fix-it rewrites. Last 15 min: due flashcards from other subjects.",
      files="Maths AA SL: sequences + functions packs with mark schemes, formula booklet",
      links=[M_SEQ_Q, M_SEQ_MS, M_FN_Q, M_FN_S, M_FB],
      guide=[dict(url="guides/2026-11-04-maths-aa-sl-1.2-1.6.html", label="Maths 1.2 to 1.6", quiz="ib-quiz-guide-2026-11-04", review=True), dict(url="guides/2026-11-10-maths-aa-sl-2.2-2.5.html", label="Maths 2.2 to 2.5", quiz="ib-quiz-guide-2026-11-10", review=True)]),
 dict(iso="2026-12-02", subject="Biology",
      task="Revision B1.2, C1.1, C1.2 and the 21 Nov mock mistakes, from memory first: 5-min brain dump; timed InThinking topic tests C1.1 and C1.2, marked with their mark schemes; B1.2 test if time; Fix-it rewrites. Last 15 min: due flashcards from other subjects.",
      files="Biology HL: InThinking topic tests B1.2, C1.1, C1.2 + mark schemes",
      links=[D("1bWufdbYTQQuz1TxMx_4ZDPoS8SWV8gBd","C1.1 topic test"), D("1jPTfhkPdN4UAKgRoZBFwzm_Iq45IXlVJ","C1.1 test mark scheme"), D("1x9ETyIewHLbTA4iHBd_XJ1l8e2W5Qlwu","C1.2 topic test"), D("1HSNmbJniMdlr895yTTlfaUWYztFz7Ut5","C1.2 test mark scheme"), D("1Q6UY3cWhUJRK8voRZ6PNc9m7G3AMQI-S","B1.2 topic test"), D("1qDi7Bj8WtQTwJlpO_qKHVGDQTVy5yxDs","B1.2 test mark scheme")],
      guide=[dict(url="practice/2026-12-02-biology-revision-b1.2-c1.2.html", label="Timed revision: Biology B1.2, C1.1, C1.2", quiz="ib-timed-2026-12-02"), dict(url="guides/2026-11-18-biology-hl-b1.2-c1.1.html", label="Biology HL B1.2 Proteins and C1.1 Enzymes", quiz="ib-quiz-guide-2026-11-18", review=True), dict(url="guides/2026-11-22-biology-hl-c1.2-cell-respiration.html", label="Biology HL C1.2 Cell respiration", quiz="ib-quiz-guide-2026-11-22", review=True)]),
 dict(iso="2026-12-03", subject="Business + French (30 min)",
      task="Business, from memory first: 5-min brain dump; Error log; rehearse the Paper 1 answer structure (define, apply, analyse, evaluate) on the stakeholders Q1 again, timed 20 min; Fix-it rewrite. French daily habit: 10 min flashcards + say 3 sentences out loud.",
      files="Business SL: stakeholders questions + mark scheme, 10-marker guide",
      links=[BM_STK_Q, BM_STK_MS, BM_10],
      guide=[dict(url="guides/2026-11-06-business-sl-1.1-1.6.html", label="Business Unit 1", quiz="ib-quiz-guide-2026-11-06", review=True), dict(url="guides/2026-11-19-business-sl-unit2-hrm.html", label="Business Management SL Unit 2 HRM", quiz="ib-quiz-guide-2026-11-19", review=True)]),
 dict(iso="2026-12-04", subject="English + French (30 min)",
      task="English, from memory first: 5-min brain dump; then compare your two cartoon paragraphs with the Horsey model and list your three habits that lose marks; one last timed paragraph. French daily habit: 10 min flashcards + say 3 sentences out loud. End of the plan.",
      files="English (Lang & Lit): cartoons guide, Horsey model",
      links=[E_CART, E_HORSEY],
      guide=[dict(url="guides/2026-12-04-english-a-hl-revision-2.html", label="English revision 2: unseen infographic and your habits", quiz="ib-quiz-guide-2026-12-04")]),
]
GERMAN = " German (extra 15 min): flashcards, then today's short lesson on the German page."
import datetime
for d in DAYS:
    if "Rest" not in d["subject"] and "German (extra 15 min)" not in d["task"]:
        d["task"] = d["task"] + GERMAN
    dt = datetime.date.fromisoformat(d["iso"])
    d["day"] = dt.strftime("%a"); d["date"] = f"{dt.day} {dt.strftime('%b')}"
    d["week"] = "Week 1" if dt <= datetime.date(2026,11,15) else ("Week 2" if dt <= datetime.date(2026,11,22) else "Exam window")
    d["hours"] = 4 if dt.weekday() >= 5 else 3
    d["block1"] = "" if dt.weekday() >= 5 else B1
    d.setdefault("guide", [])
