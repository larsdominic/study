# German track for Jamila (not an IB subject): her route to a German-taught degree in Germany from autumn 2028.
# Run from the repo root: python3 tools/german.py tools .   ->  german.html
# localStorage: 'ib-german-level' (level self-check ticks), 'ib-german-days' (daily sessions 9 Nov to 4 Dec 2026),
#               'ib-german-weeks' (weekly path, Dec 2026 to Mar 2027); each = {box id: date ticked}.
# Sources (all fetched 8 Nov 2026):
#  - DW Learn German, Nicos Weg A1 course page https://learngerman.dw.com/en/nicos-weg/c-36519789 (76 lessons + Final Test A1,
#    lesson titles, chapters and topics copied from it; lessons and exercises open without logging in, checked in a browser;
#    exercise counts for lessons 1 to 10 read from the first exercise page, "1 / N"); A2 c-36519797; B1 (German only) /de/ c-36519718;
#    DW help page (certificate needs login, not official; from B1 the courses are in German only).
#  - Goethe-Institut Glasgow FAQ (hours per level), Goethe-Institut Germany course page (intensive course = 75 units of 45 min),
#    Goethe-Institut Singapore (courses from 16, TestDaF offered), Goethe "Deutsch für dich" (free, login removed).
#  - DAAD "The German language", TestDaF Institute (TDN 4 in all parts, RO-DT section 4(5)), uni-assist language certificates,
#    TUM language certificates, Goethe University Frankfurt, TU Braunschweig, Europa-Universität Viadrina (Goethe C1 not enough).
#  - KMK agreement on the IB Diploma (10.03.1986 as amended 15.06.2023, Anlage 1 as of 26.03.2026, Anlage 2 as of 19.11.2024).
#  - CEFR self-assessment grid (Council of Europe) as published by Europass.
# Every number on the page is computed below.
import sys, datetime, math, urllib.parse
sys.path.insert(0, sys.argv[1]); from common import *
out = sys.argv[2]
D = datetime.date

DW = 'https://learngerman.dw.com'
A1_COURSE = DW + '/en/nicos-weg/c-36519789'
A2_COURSE = DW + '/en/nicos-weg/c-36519797'
B1_COURSE = DW + '/de/nicos-weg/c-36519718'
A1_TEST = DW + '/en/final-test-a1/l-44875550'
KMK_IB = ('https://www.kmk.org/zab/fileadmin/Dateien/pdf/ZAB/Hochschulzugang_Beschluesse_der_KMK/aktuell/'
          '283_Vereinb_Anerkenn_Int_Baccalaureate_Diploma-2023-06-15_Liste1__2026-03-26_Liste2-2024-11-19.pdf')
SRC = dict(
    daad='https://www.daad.de/en/studying-in-germany/living-in-germany/german-language/',
    testdaf='https://www.testdaf.de/de/hochschulen/der-testdaf-und-hochschulen/nachweis-der-deutschkenntnisse-fuer-das-studium/',
    uniassist='https://www.uni-assist.de/en/how-to-apply/plan-your-application/language-certificates/',
    tum='https://www.tum.de/en/studies/application/application-info-portal/admission-requirements/language-certificates',
    ffm='https://www.uni-frankfurt.de/124980722/German_Language_Requirements?locale=en',
    tubs='https://www.tu-braunschweig.de/international-students/application',
    viadrina='https://www.europa-uni.de/de/studium/studieneinstieg/internationale-studieninteressierte/sprachnachweise/index.html',
    goethe_hours='https://www.goethe.de/ins/gb/de/sta/gla/kur/faq.html',
    goethe_de='https://www.goethe.de/ins/de/en/uun/dln.html',
    goethe_sg='https://www.goethe.de/ins/sg/en/kur/kur.html',
    goethe_sg_testdaf='https://www.goethe.de/ins/sg/en/kur/prf/testdaf.html',
    dfd='https://www.goethe.de/prj/dfd/en/home.cfm',
    goethe_free='https://www.goethe.de/de/spr/ueb.html',
    lgn='https://learngerman.dw.com/de/langsam-gesprochene-nachrichten/s-60040332',
    dwexam='https://learngerman.dw.com/en/deine-deutschpr%C3%BCfung/s-68305661',
    dwhelp='https://learngerman.dw.com/en/help',
    europass='https://europass.europa.eu/en/common-european-framework-reference-language-skills',
)

# Nicos Weg A1, in course order: (chapter, lesson title, path, topics) from the DW course page
A1 = [
  ('Welcome', 'Hallo!', '/en/hallo/l-37250531', 'Greetings · Informal and formal'),
  ('Welcome', 'Kein Problem!', '/en/kein-problem/l-37251054', 'Basic words in German'),
  ('Welcome', 'Tschüss!', '/en/tschüss/l-37251033', 'Saying goodbye · Informal and formal'),
  ('Welcome', 'Von A bis Z', '/en/von-a-bis-z/l-37256418', 'Spelling'),
  ('1 Meeting people', 'Ich heiße Emma', '/en/ich-heiße-emma/l-37262882', 'Introducing yourself · Personal pronouns: ich, du'),
  ('1 Meeting people', 'Das ist Nico', '/en/das-ist-nico/l-37262923', 'Introducing others'),
  ('1 Meeting people', 'Woher kommst du?', '/en/woher-kommst-du/l-37263828', 'Name and background · Conjugation: present tense'),
  ('1 Meeting people', 'Nico hat ein Problem', '/en/nico-hat-ein-problem/l-37265543', 'Finding out about other people · Personal pronouns: er, sie'),
  ('2 Contact details', 'Zahlen von 1 bis 100', '/en/zahlen-von-1-bis-100/l-37265621', 'Numbers from 1 to 100 · Numbers from 11 to 19'),
  ('2 Contact details', 'Wichtige Nummern', '/en/wichtige-nummern/l-37269501', 'Important numbers'),
  ('2 Contact details', 'Adressen', '/en/adressen/l-37269671', 'Providing personal information · W-questions'),
  ('2 Contact details', 'Auf dem Amt', '/en/auf-dem-amt/l-37269629', 'Formal address · Numbers over 100'),
  ('3 In company', 'Was machst du hier?', '/en/was-machst-du-hier/l-37278679', 'Social situations'),
  ('3 In company', 'Was trinkst du?', '/en/was-trinkst-du/l-37279418', 'Offering drinks · Nouns: gender'),
  ('3 In company', 'Eine Pizza bitte!', '/en/eine-pizza-bitte/l-37279261', 'Placing an order · Vowel change: e to i'),
  ('3 In company', 'Zahlen bitte!', '/en/zahlen-bitte/l-37280348', 'Paying the bill'),
  ('4 Around the world', 'Ich war schon in Berlin', '/en/ich-war-schon-in-berlin/l-37325550', 'Sightseeing attractions · Simple past: sein'),
  ('4 Around the world', 'Wo liegt das?', '/en/wo-liegt-das/l-37337877', 'Geographic info · Questions and statements'),
  ('4 Around the world', 'In Europa', '/en/in-europa/l-37328492', 'Speaking about countries · Indefinite pronouns: man'),
  ('4 Around the world', 'Andere Länder', '/en/andere-länder/l-37337244', 'Languages · Conjugation: sprechen'),
  ('5 Things', 'Was ist das?', '/en/was-ist-das/l-37368285', 'Naming objects · Articles: definite'),
  ('5 Things', 'Wem gehört das?', '/en/wem-gehört-das/l-37372077', 'Asking about objects · Articles: indefinite'),
  ('5 Things', 'Ich habe kein …', '/en/ich-habe-kein/l-37382992', 'What you (do not) have · Sentence construction: subject'),
  ('5 Things', 'Das Auto ist rot', '/en/das-auto-ist-rot/l-37401537', 'Naming objects · Adjectives following "sein"'),
  ('6 Living', 'So wohne ich', '/en/so-wohne-ich/l-37425145', 'Living arrangements · Articles'),
  ('6 Living', 'Meine Wohnung', '/en/meine-wohnung/l-37425763', 'The rooms in an apartment · Negatives: nicht'),
  ('6 Living', 'Sofa, Sessel und Tisch', '/en/sofa-sessel-und-tisch/l-37438475', 'Describing interiors · zu + adjective'),
  ('6 Living', 'Unser Haus', '/en/unser-haus/l-37439097', 'Saying what is whose · Possessive determiners'),
  ('7 Days and times', 'Emmas Tag', '/en/emmas-tag/l-37442425', 'Talking about the day · Time: 12-hour clock'),
  ('7 Days and times', 'Tageszeiten', '/en/tageszeiten/l-37445884', 'Describing the day · Separable verbs'),
  ('7 Days and times', 'Am Sonntag koche ich', '/en/am-sonntag-koche-ich/l-37452061', 'Free time activities · Prepositions of time: an'),
  ('7 Days and times', 'Emmas Wochenende', '/en/emmas-wochenende/l-37452629', 'The weekend · Adverbs: sequence'),
  ('8 Appointments', 'Wie spät ist es?', '/en/wie-spät-ist-es/l-37453621', 'Understanding time and date · Time specification: 24-hour clock'),
  ('8 Appointments', 'Hast du morgen Zeit?', '/en/hast-du-morgen-zeit/l-37461035', 'Planning dates · Ordinal numbers'),
  ('8 Appointments', 'Wann spielen wir?', '/en/wann-spielen-wir/l-37468614', 'Making arrangements · Conjugation: können'),
  ('8 Appointments', 'Zu spät!?', '/en/zu-spät/l-37460778', 'Delays · Simple past: haben'),
  ('9 Working life', 'Ich bin Lehrerin', '/en/ich-bin-lehrerin/l-37469204', 'Talking about professions · Word formation: professions'),
  ('9 Working life', 'Mein Beruf', '/en/mein-beruf/l-37475138', 'Describing activities · Modal verbs'),
  ('9 Working life', 'Wo ist der Aufzug?', '/en/wo-ist-der-aufzug/l-37476734', 'Finding your way around a building · The dative'),
  ('9 Working life', 'Traumberufe', '/en/traumberufe/l-37477568', 'Career hopes · Modal verbs: wollen'),
  ('10 Orientation', 'Wo ist der Bahnhof?', '/en/wo-ist-der-bahnhof/l-37594551', 'Living and working · Prepositions: bei, von'),
  ('10 Orientation', 'An der Ampel links', '/en/an-der-ampel-links/l-37595076', 'Giving directions · Prepositions of place'),
  ('10 Orientation', 'Mit Bus und Bahn', '/en/mit-bus-und-bahn/l-37595395', 'Commuting to work · Prepositions: mit'),
  ('10 Orientation', 'Im Büro', '/en/im-büro/l-37595501', 'Objects in the office · Two-case prepositions'),
  ('11 Eating and leisure', 'Lebensmittel', '/en/lebensmittel/l-37597045', 'Talking about food · Negation: nicht/kein'),
  ('11 Eating and leisure', 'Ich mag (nicht)!', '/en/ich-mag-nicht/l-37599970', 'Eating preferences · Comparative'),
  ('11 Eating and leisure', 'Haushaltsarbeit', '/en/haushaltsarbeit/l-37631238', 'Preferences at home · Comparison: wie/als'),
  ('11 Eating and leisure', 'Was macht dir Spaß?', '/en/was-macht-dir-spaß/l-37630630', 'Leisure activities · gehen + infinitive'),
  ('12 Food', 'Mengen und Preise', '/en/mengen-und-preise/l-37628421', 'Buying groceries · Prepositions: in, auf'),
  ('12 Food', 'Was darf es sein?', '/en/was-darf-es-sein/l-37635620', 'Shopping conversations'),
  ('12 Food', 'Sonst noch etwas?', '/en/sonst-noch-etwas/l-37646611', 'Shopping at the market · Question words: wie viel'),
  ('12 Food', 'Wie viel Mehl?', '/en/wie-viel-mehl/l-37647289', 'Following a recipe · Instructions'),
  ('13 Weather and holiday', 'Wie war dein Urlaub?', '/en/wie-war-dein-urlaub/l-37648534', 'Talking about holidays · Present perfect with "haben"'),
  ('13 Weather and holiday', 'Jahreszeiten', '/en/jahreszeiten/l-37651758', 'Comparing the seasons · Comparison'),
  ('13 Weather and holiday', 'Der Ausflug', '/en/der-ausflug/l-37651657', 'Talking about the past · Present perfect with "sein"'),
  ('13 Weather and holiday', 'Wie wird das Wetter?', '/en/wie-wird-das-wetter/l-37653197', 'Talking about the weather · Pronouns: es'),
  ('14 Clothing', 'Das ist jetzt modern', '/en/das-ist-jetzt-modern/l-37655848', 'Talking about clothing · Adjective declension'),
  ('14 Clothing', 'Mein Lieblingspulli', '/en/mein-lieblingspulli/l-37656274', 'Describing clothing · Question words: welch-'),
  ('14 Clothing', 'Das passt gut!', '/en/das-passt-gut/l-37661740', 'Shopping for clothes · Verbs with a dative object'),
  ('14 Clothing', 'Schick!', '/en/schick/l-37661765', 'Casual wear'),
  ('15 Family', 'Meine Familie', '/en/meine-familie/l-37661741', 'Talking about family · Adjective declension'),
  ('15 Family', 'Meine Eltern', '/en/meine-eltern/l-37664246', 'Introducing parents · Personal pronouns: accusative'),
  ('15 Family', 'Meine Tante', '/en/meine-tante/l-37664498', 'Career choices · The possessive determiner'),
  ('15 Family', 'Mein Bruder', '/en/mein-bruder/l-37664164', 'Talking about siblings · Modal verbs: sollen'),
  ('16 Sports and exercise', 'Von Kopf bis Fuß', '/en/von-kopf-bis-fuß/l-37664951', 'Sports · Comparison'),
  ('16 Sports and exercise', 'Bist du fit?', '/en/bist-du-fit/l-37668333', 'Sports and training · Time specification: Wann ...?'),
  ('16 Sports and exercise', 'Fitness', '/en/fitness/l-37668815', 'Fitness tips · Comparison'),
  ('16 Sports and exercise', 'Ist das gesund?', '/en/ist-das-gesund/l-37670365', 'Talking about nutrition · Imperative: informal'),
  ('17 Health', 'Geht es dir gut?', '/en/geht-es-dir-gut/l-37778457', 'Talking about illnesses · Müssen or sollen?'),
  ('17 Health', 'Beim Arzt', '/en/beim-arzt/l-37778169', "Checking in at the doctor's · Modal verbs: dürfen"),
  ('17 Health', 'Gute Besserung!', '/en/gute-besserung/l-37780308', 'Inquiring about patients · Present perfect'),
  ('17 Health', 'Nehmen Sie …', '/en/nehmen-sie/l-37782214', 'A visit to the doctor · Prepositions: vor, nach'),
  ('18 Home', 'Meine Heimat', '/en/meine-heimat/l-37776166', 'Talking about home · Adjective declension'),
  ('18 Home', 'Leben in Deutschland', '/en/leben-in-deutschland/l-37777069', 'To miss something · Personal pronouns: dative'),
  ('18 Home', 'Anders als zu Hause', '/en/anders-als-zu-hause/l-37779968', 'Comparisons'),
  ('18 Home', 'Ich träume von …', '/en/ich-träume-von/l-37783730', 'Hopes and dreams · Subjunctive: Wishes'),
]
assert len(A1) == 76
# number of exercise pages in lessons 1 to 10 (the "1 / N" counter on each lesson's first exercise, 8 Nov 2026)
EX = [12, 12, 12, 10, 9, 8, 12, 11, 14, 12]
NO_GRAMMAR = {2, 4, 6, 10}   # lessons 1 to 10 without a Grammar tab (they have a Vocabulary tab), checked 8 Nov 2026

def url(path): return DW + urllib.parse.quote(path, safe='/')
def lesson_link(i):  # i = 1-based lesson number
    ch, t, p, top = A1[i - 1]
    return f'<a href="{url(p)}">{t}</a>'
def fmt(d): return d.strftime('%a ') + str(d.day) + d.strftime(' %b')
def fmty(d): return str(d.day) + d.strftime(' %b %Y')

# ---------------------------------------------------------------- daily sessions, 9 Nov to 4 Dec 2026
START, END, REST = D(2026, 11, 9), D(2026, 12, 4), D(2026, 11, 29)
REVIEW = {D(2026, 11, 15), D(2026, 11, 22), D(2026, 11, 28), D(2026, 12, 3), D(2026, 12, 4)}
days = []
d, n = START, 0
while d <= END:
    if d == REST: days.append(('rest', d, None))
    elif d in REVIEW: days.append(('review', d, None))
    else:
        n += 1; days.append(('lesson', d, n))
    d += datetime.timedelta(days=1)
N_LESSON_DAYS = sum(1 for k, *_ in days if k == 'lesson')
N_REVIEW_DAYS = sum(1 for k, *_ in days if k == 'review')
N_DAYS_TICK = N_LESSON_DAYS + N_REVIEW_DAYS
N_CAL_DAYS = (END - START).days + 1
assert N_LESSON_DAYS == 20 and N_REVIEW_DAYS == 5
LESSONS_IN_DAILY = N_LESSON_DAYS // 2   # two short sessions per lesson
assert LESSONS_IN_DAILY == len(EX)

def day_row(kind, d, n):
    iso = d.isoformat()
    if kind == 'rest':
        return f'<li class="day rest"><span class="dd">{fmt(d)}</span><span class="dw"><b>Rest day.</b> No German today.</span></li>'
    if kind == 'review':
        what = ('<b>Review (15 min).</b> All due German flashcards, then replay one Nicos Weg video you have already done: '
                'once with subtitles, once without. Say three sentences about yourself out loud.')
        if d == END:
            what = ('<b>Review and level check (15 min).</b> Due flashcards, then redo the <a href="#check">level check</a> '
                    'at the top of this page and see what changed since 9 Nov.')
        return (f'<li class="day"><label class="ck"><input type="checkbox" data-store="days" data-k="{iso}"> '
                f'<span class="dd">{fmt(d)}</span></label><span class="dw">{what}</span></li>')
    li = (n + 1) // 2; part = 1 if n % 2 else 2
    N = EX[li - 1]; k = math.ceil(N / 2)
    if part == 1:
        task = f'watch the video, then exercises 1 to {k} (of {N})'
    else:
        task = f'exercises {k + 1} to {N}, then ' + ('look through the Vocabulary tab' if li in NO_GRAMMAR else 'read the Grammar tab')
    return (f'<li class="day"><label class="ck"><input type="checkbox" data-store="days" data-k="{iso}"> '
            f'<span class="dd">{fmt(d)}</span></label><span class="dw"><b>Session {n}:</b> lesson {li} {lesson_link(li)}, '
            f'part {part}: {task}.</span></li>')

daily_html = '<ol class="days">' + ''.join(day_row(*x) for x in days) + '</ol>'

# ---------------------------------------------------------------- weekly path from 5 Dec 2026 (weeks start on Monday)
W1 = D(2026, 12, 7)
PER_WEEK = 4
items = [('lesson', i) for i in range(LESSONS_IN_DAILY + 1, 77)] + [('test', None)]
weeks = [items[i:i + PER_WEEK] for i in range(0, len(items), PER_WEEK)]
N_WEEKS = len(weeks)
LAST_WEEK_END = W1 + datetime.timedelta(days=7 * N_WEEKS - 1)
assert LAST_WEEK_END.year == 2027 and LAST_WEEK_END.month in (3, 4)
HOLIDAY_WEEKS = {D(2026, 12, 21), D(2026, 12, 28)}

def week_card(w, its):
    a = W1 + datetime.timedelta(days=7 * (w - 1)); b = a + datetime.timedelta(days=6)
    lis = []
    for kind, i in its:
        if kind == 'test':
            lis.append(f'<li><a href="{A1_TEST}">Final Test A1</a> (check your knowledge of the whole A1 course)</li>')
        else:
            ch, t, p, top = A1[i - 1]
            lis.append(f'<li>Lesson {i}: {lesson_link(i)} <span class="tp">({top})</span></li>')
    chs = sorted({A1[i - 1][0] for kind, i in its if kind == 'lesson'}, key=lambda c: int(c.split()[0]))
    note = ''
    if a in HOLIDAY_WEEKS:
        note = '<p class="hol">Holiday week: if you travel, do at least 2 sessions and move the other lessons into next week.</p>'
    return (f'<div class="wk" id="w{w}"><label class="ck wh"><input type="checkbox" data-store="weeks" data-k="{a.isoformat()}"> '
            f'<b>Week {w}</b> <span class="dd">{fmt(a)} to {fmt(b)}</span></label>'
            f'<p class="chap">Chapter {" and ".join(chs)}</p><ol class="ls">{"".join(lis)}</ol>{note}</div>')

weeks_html = '<div class="wks">' + ''.join(week_card(w, its) for w, its in enumerate(weeks, 1)) + '</div>'

# ---------------------------------------------------------------- hours (Goethe-Institut guide figures vs this plan)
# Goethe-Institut Glasgow FAQ, total hours to reach each level (from zero; depends on the learner):
GOETHE = {'A1': (60, 150), 'A2': (150, 260), 'B1': (260, 490), 'B2': (450, 600), 'C1': (600, 750)}
WEEKLY = (3, 4)                       # hours a week in the weekly path
UNIT_MIN = 45                         # one Goethe teaching unit = 45 minutes
INTENSIVE_UNITS = 75                  # Goethe "Intensive German" in Germany: 75 units in 3 weeks
CONCISE_UNITS = 50                    # Goethe "Intensive German Concise": 50 units in 2 weeks
h_int = INTENSIVE_UNITS * UNIT_MIN / 60
h_con = CONCISE_UNITS * UNIT_MIN / 60
wk_2027 = (D(2027, 12, 31) - W1).days // 7          # full weeks from 7 Dec 2026 to end of 2027
wk_2028 = (D(2028, 4, 30) - D(2028, 1, 1)).days // 7  # Jan to Apr 2028 (IB final year, lighter: 2 to 3 h)
WEEKLY_2028 = (2, 3)
by_2027 = tuple(wk_2027 * h + h_int for h in WEEKLY)
by_apr28 = tuple(by_2027[i] + wk_2028 * WEEKLY_2028[i] + h_con for i in range(2))
gap = (GOETHE['C1'][0] - by_apr28[1], GOETHE['C1'][1] - by_apr28[0])
# after the IB exams: full-time intensive courses, June to August 2028 (12 weeks = 4 intensive courses of 3 weeks)
summer_courses = 12 // 3
h_summer28 = summer_courses * h_int
total_28 = (by_apr28[0] + h_summer28, by_apr28[1] + h_summer28)
h_daily = 25 * 15 / 60                 # the 25 daily sessions of 15 minutes, 9 Nov to 4 Dec 2026
if total_28[1] < GOETHE['C1'][0]:
    c1_verdict = f'still about {int(round(GOETHE["C1"][0] - total_28[1]))} to {int(round(GOETHE["C1"][0] - total_28[0]))} hours below the start of the C1 range'
elif total_28[0] < GOETHE['C1'][0]:
    c1_verdict = 'reaching the C1 range only at the top end of the plan'
else:
    c1_verdict = 'inside the C1 range'
R = lambda x: int(round(x))

# quarterly milestones after March 2027 (A2 and B1 courses have 76 lessons + a final test, like A1)
A2_START = LAST_WEEK_END + datetime.timedelta(days=1)
q2_weeks = (D(2027, 7, 1) - A2_START).days // 7   # full weeks from Mon 5 Apr to 30 Jun 2027
q2_lessons = q2_weeks * PER_WEEK

# ---------------------------------------------------------------- level self-check (CEFR self-assessment grid, Europass)
A1_CAN = [
    ('l1', 'Listening', 'I can recognise familiar words and very basic phrases concerning myself, my family and immediate concrete surroundings when people speak slowly and clearly.'),
    ('l2', 'Reading', 'I can understand familiar names, words and very simple sentences, for example on notices and posters or in catalogues.'),
    ('l3', 'Spoken interaction', "I can interact in a simple way provided the other person is prepared to repeat or rephrase things at a slower rate of speech and help me formulate what I'm trying to say."),
    ('l4', 'Spoken interaction', 'I can ask and answer simple questions in areas of immediate need or on very familiar topics.'),
    ('l5', 'Spoken production', 'I can use simple phrases and sentences to describe where I live and people I know.'),
    ('l6', 'Writing', 'I can write a short, simple postcard, for example sending holiday greetings.'),
    ('l7', 'Writing', 'I can fill in forms with personal details, for example entering my name, nationality and address on a hotel registration form.'),
]
A2_CAN = [
    ('m1', 'Listening', 'I can catch the main point in short, clear, simple messages and announcements.'),
    ('m2', 'Reading', 'I can read very short, simple texts.'),
    ('m3', 'Spoken interaction', "I can handle very short social exchanges, even though I can't usually understand enough to keep the conversation going myself."),
    ('m4', 'Writing', 'I can write short, simple notes and messages relating to matters in areas of immediate needs.'),
]
def can_list(lst, grp):
    return '<ul class="cans">' + ''.join(
        f'<li><label class="ck"><input type="checkbox" data-store="level" data-grp="{grp}" data-k="{k}"> '
        f'<span><span class="sk">{s}</span> {t}</span></label></li>' for k, s, t in lst) + '</ul>'

# ---------------------------------------------------------------- page
body = f'''
<div class="prog" id="progress" aria-live="polite">
  <h2>Your German progress</h2>
  <div class="pr"><span>Level check: A1 statements ticked</span><b id="pg-level">0 of {len(A1_CAN)}</b></div>
  <p class="small" id="pg-start"><b>Where to start:</b> do the <a href="#check">level check</a> first (5 minutes).</p>
  <div class="bar"><i id="bar-level"></i></div>
  <div class="pr"><span>Daily sessions (9 Nov to 4 Dec)</span><b id="pg-days">0 of {N_DAYS_TICK}</b></div>
  <div class="bar"><i id="bar-days"></i></div>
  <div class="pr"><span>Weeks done (Dec 2026 to Mar 2027)</span><b id="pg-weeks">0 of {N_WEEKS}</b></div>
  <div class="bar"><i id="bar-weeks"></i></div>
  <p class="small" id="savenote">Ticks are saved in this browser on this device.</p>
</div>

<nav class="jump" aria-label="On this page"><a href="#check">Level check</a><a href="#goal">Goal</a><a href="#now">Now to 4 Dec</a><a href="#weekly">From 5 Dec</a><a href="#later">Apr 2027 on</a><a href="#certs">Certificates</a><a href="#ib">IB and entry</a><a href="#free">Free resources</a></nav>

<section id="check">
<h2>1. Check your level (5 minutes)</h2>
<p>These are the official "I can" statements for level A1 from the Council of Europe's language scale (the CEFR, the European scale of language levels from A1, beginner, to C2, near native), as published by <a href="{SRC['europass']}">Europass</a>. Read each one and tick it only if it is true for you <b>in German</b> today.</p>
<p><b>Why tick them:</b> the result below tells you <b>where to start</b>. You had German lessons before, so you may not need to begin at lesson 1; or you may find that the basics need a fresh start. Redo the check every few weeks: it also shows you how far you have come.</p>
<p class="small">Quick test for the speaking line: say out loud now, in German, your name, where you live and who one person in your family is (for example: <i>Ich heiße …, ich wohne in Singapur, das ist meine Mutter, sie heißt …</i>).</p>
<h3>A1 (beginner)</h3>
{can_list(A1_CAN, "a1")}
<details class="more"><summary>Next level up: four A2 statements (optional)</summary>
{can_list(A2_CAN, "a2")}
</details>
<div class="verdict" id="verdict" aria-live="polite"><b>Where to start:</b> tick the statements that are true for you and your starting point appears here.</div>
</section>

<section id="goal">
<h2>2. The goal and the timeline</h2>
<p><b>Goal:</b> a degree taught in German at a German university, starting autumn 2028. For that you need a German certificate at about level C1 (see <a href="#certs">Certificates</a>). German is not one of your IB subjects, so this runs next to the IB, in small steady steps.</p>
<div class="tablewrap"><table>
<tr><th>When</th><th>Level (about)</th><th>How</th></tr>
<tr><td>Now (Nov 2026)</td><td>A1</td><td>15 minutes a day during the exam fortnight</td></tr>
<tr><td>End of Mar 2027</td><td>A1 complete</td><td>Weekly path: {WEEKLY[0]} to {WEEKLY[1]} hours a week, Nicos Weg A1 and its final test</td></tr>
<tr><td>Summer 2027</td><td>A2</td><td>Nicos Weg A2 plus a holiday intensive course</td></tr>
<tr><td>End of 2027</td><td>about B1</td><td>Nicos Weg B1 (in German only)</td></tr>
<tr><td>Summer 2028</td><td>about C1, certificate</td><td>B2 and C1 work, then a full-time course after the IB exams, then the test</td></tr>
</table></div>

<div class="honest">
<p><b>Being honest about the time.</b> The Goethe-Institut gives guide figures for the <i>total</i> time to reach each level from zero (<a href="{SRC['goethe_hours']}">Goethe-Institut Glasgow, FAQ</a>): B1 about {GOETHE['B1'][0]} to {GOETHE['B1'][1]} hours, C1 about {GOETHE['C1'][0]} to {GOETHE['C1'][1]} hours. It says the real time depends on the person, on other languages you already know (you have English and French, which helps) and on whether you live in Germany.</p>
<p>What this plan adds up to (computed, assumptions in brackets):</p>
<ul>
<li>By the end of 2027: about {R(by_2027[0])} to {R(by_2027[1])} hours ({wk_2027} weeks at {WEEKLY[0]} to {WEEKLY[1]} hours, plus one 3-week holiday intensive course in summer 2027 of {INTENSIVE_UNITS} lessons of {UNIT_MIN} minutes, about {R(h_int)} hours). That is around the start of the B1 range ({GOETHE['B1'][0]} hours), so "about B1" is realistic if the habit holds.</li>
<li>By the end of April 2028: about {R(by_apr28[0])} to {R(by_apr28[1])} hours (plus {wk_2028} weeks at {WEEKLY_2028[0]} to {WEEKLY_2028[1]} hours in the IB final year and a 2-week course in the December 2027 holiday, about {R(h_con)} hours).</li>
<li>That leaves about {R(gap[0])} to {R(gap[1])} hours short of the C1 range. A full-time course after the IB exams, June to August 2028 ({summer_courses} intensive courses of 3 weeks, about {R(h_summer28)} hours), brings the total to about {R(total_28[0])} to {R(total_28[1])} hours: {c1_verdict}. The German you learned before (and the {R(h_daily)} hours of daily sessions now) come on top.</li>
</ul>
<p><b>So:</b> C1 by summer 2028 is tight. It is possible if you learn faster than the average (English and French help) and keep the weekly habit every week, with holiday intensives (summer 2027 is the big one) and more hours whenever school allows. Keep a plan B in mind and discuss it with your parents: a German course in Germany that prepares for the university's own test (the DSH) before starting the degree (Goethe University Frankfurt, for example, asks for B1 to join its DSH course, <a href="{SRC['ffm']}">source</a>), or a degree taught in English.</p>
<p><b>Mind the dates.</b> Many universities want the certificate by the end of the application period, which for an October start is often 15 July (TU Braunschweig, <a href="{SRC['tubs']}">source</a>; also <a href="{SRC['tum']}">TUM</a>, <a href="{SRC['ffm']}">Frankfurt</a>). A test taken at the end of a June to August 2028 course is too late for those. Routes that fit: a test passed before the deadline, a university that takes your current German proof with the application and lets you pass its own DSH before the semester starts (Viadrina, <a href="{SRC['viadrina']}">source</a>), TU Braunschweig's rule for programmes without a selection limit (B2 course at application, certificate at enrolment), or starting a semester later.</p>
</div>
</section>

<section id="now">
<h2>3. Now to 4 Dec (exam fortnight): 15 minutes a day</h2>
<div class="recipe">
<p><b>Every day, 15 minutes, no more:</b></p>
<ol>
<li><b>5 to 8 min:</b> German flashcards on the <a href="flashcards.html">Flashcards page</a> (the German deck). Say each answer out loud before you turn the card.</li>
<li><b>7 to 10 min:</b> one short part of Deutsche Welle's free video course <a href="{A1_COURSE}">Nicos Weg A1</a>. Each lesson has a 1 to 2 minute video and about 8 to 16 short exercises, so each lesson is split into two days.</li>
</ol>
<p class="small">Free: lessons and exercises open without an account. Registering is optional; it only saves your progress across devices and unlocks DW's course certificate, which is not an official certificate (<a href="{SRC['dwhelp']}">DW help</a>).</p>
</div>
<p>{N_CAL_DAYS} days: {N_LESSON_DAYS} lesson sessions (lessons 1 to {LESSONS_IN_DAILY}), {N_REVIEW_DAYS} lighter review days on busy days, and a rest day on {fmt(REST)}. Tick each day when done. Missed a day? Just do the next one; do not double up.</p>
{daily_html}
</section>

<section id="weekly">
<h2>4. From 5 Dec: the weekly path</h2>
<p>After the exams the time goes up to about {WEEKLY[0]} to {WEEKLY[1]} hours a week: <b>{PER_WEEK} sessions of 45 to 60 minutes</b>, one Nicos Weg lesson per session. Rest on 5 and 6 Dec; week 1 starts on {fmt(W1)}.</p>
<div class="recipe">
<p><b>One session (45 to 60 min):</b></p>
<ol>
<li><b>5 to 10 min:</b> due German flashcards, then the lesson's Vocabulary tab on DW.</li>
<li><b>30 to 40 min:</b> the lesson: video once with subtitles and once without, all exercises, then the Grammar tab (if the lesson has one).</li>
<li><b>5 to 10 min:</b> use it. Write five sentences about your own life with the new words and grammar, then read them out loud. Once a week, record yourself for one minute and listen back.</li>
</ol>
</div>
<p>{N_WEEKS} weeks, {PER_WEEK} lessons each, from lesson {LESSONS_IN_DAILY + 1} to lesson 76 and the A1 final test (ends {fmt(LAST_WEEK_END)} 2027). Tick the week when all its sessions are done.</p>
{weeks_html}
</section>

<section id="later">
<h2>5. April 2027 to summer 2028: milestones</h2>
<div class="tablewrap"><table>
<tr><th>Quarter</th><th>Aim</th><th>Main resource</th></tr>
<tr><td>Apr to Jun 2027</td><td>A2: about {q2_lessons} of the 76 A2 lessons ({q2_weeks} weeks at {PER_WEEK} a week)</td><td><a href="{A2_COURSE}">Nicos Weg A2</a></td></tr>
<tr><td>Jul to Sep 2027</td><td>Finish A2 and its final test; holiday intensive course (2 to 3 weeks); start B1</td><td>Nicos Weg A2 and <a href="{B1_COURSE}">B1</a> (B1 is in German only), a course at the <a href="{SRC['goethe_sg']}">Goethe-Institut Singapore</a> (adult courses from age 16) or in Germany (<a href="{SRC['goethe_de']}">intensive courses</a>)</td></tr>
<tr><td>Oct to Dec 2027</td><td>About B1: most of Nicos Weg B1; a 2-week course in the December holiday</td><td>Nicos Weg B1, <a href="{SRC['dfd']}">Deutsch für dich</a> B1 exercises</td></tr>
<tr><td>Jan to Apr 2028</td><td>Towards B2 at {WEEKLY_2028[0]} to {WEEKLY_2028[1]} hours a week (IB final year). Choose programmes, check their language rule and deadline, book the test</td><td>DW <a href="{SRC['lgn']}">Langsam gesprochene Nachrichten</a>, TestDaF practice material (<a href="{SRC['goethe_sg_testdaf']}">Goethe-Institut Singapore</a>)</td></tr>
<tr><td>May 2028</td><td>IB exams: German pauses (flashcards only)</td><td></td></tr>
<tr><td>Jun to Aug 2028</td><td>Full-time intensive course (C1, test preparation), then the certificate test. Mind the deadlines (see the box in section 2)</td><td>Goethe-Institut intensive courses; TestDaF or telc C1 Hochschule, or the DSH in Germany</td></tr>
</table></div>
<!-- UNSURE: IB final exams assumed May 2028 (she is in Grade 11 now, diploma year 1); confirm with the school. -->
</section>

<section id="certs">
<h2>6. Certificates that German universities accept</h2>
<p>To study a programme taught in German, you prove your German with a certificate. These are the main ones. <b>Each university, and sometimes each programme, sets its own rule</b>, so always check the admission page of the programme you choose (<a href="{SRC['daad']}">DAAD</a>).</p>
<div class="tablewrap"><table>
<tr><th>Certificate</th><th>Result usually needed</th><th>Where you take it</th></tr>
<tr><td><b>TestDaF</b> (Test Deutsch als Fremdsprache)</td><td><b>TDN 4 in all four parts</b> (reading, listening, writing, speaking). This counts for unrestricted admission to all programmes (<a href="{SRC['testdaf']}">TestDaF Institute</a>, quoting the national framework rules RO-DT). Some programmes accept less in one part.</td><td>Test centres in about 100 countries (<a href="{SRC['daad']}">DAAD</a>); the <a href="{SRC['goethe_sg_testdaf']}">Goethe-Institut Singapore</a> offers it.</td></tr>
<tr><td><b>DSH</b> (the universities' own German test)</td><td><b>DSH-2</b> overall counts for all programmes (<a href="{SRC['tum']}">TUM</a>, <a href="{SRC['ffm']}">Goethe University Frankfurt</a>). Medicine and dentistry at Frankfurt need DSH-3.</td><td>In Germany, at universities (<a href="{SRC['daad']}">DAAD</a>).</td></tr>
<tr><td><b>telc Deutsch C1 Hochschule</b></td><td>Passed; "usually recognised" (<a href="{SRC['daad']}">DAAD</a>; accepted at <a href="{SRC['tum']}">TUM</a> and <a href="{SRC['tubs']}">TU Braunschweig</a>). Some ask for a grade: Frankfurt wants at least "befriedigend" (satisfactory) (<a href="{SRC['ffm']}">source</a>), Viadrina wants "gut" (good) (<a href="{SRC['viadrina']}">source</a>).</td><td>telc exam centres.</td></tr>
<tr><td><b>Goethe-Zertifikat C2</b></td><td>Passed; "usually recognised" (<a href="{SRC['daad']}">DAAD</a>, <a href="{SRC['tum']}">TUM</a>, <a href="{SRC['ffm']}">Frankfurt</a>).</td><td>Goethe-Institut, including Singapore.</td></tr>
<tr><td><b>Goethe-Zertifikat C1</b></td><td>Only "for some degree programmes" (<a href="{SRC['daad']}">DAAD</a>); Viadrina says C1 is not enough (<a href="{SRC['viadrina']}">source</a>). Do not plan on it without checking.</td><td>Goethe-Institut, including Singapore.</td></tr>
</table></div>
<ul class="small">
<li><b>Deadline:</b> some universities want the certificate by the end of the application period (<a href="{SRC['tum']}">TUM</a>, <a href="{SRC['ffm']}">Frankfurt</a>). TU Braunschweig, for programmes without a selection limit, accepts proof of a B2 course at application and the certificate at enrolment (<a href="{SRC['tubs']}">source</a>).</li>
<li>uni-assist (the service many universities use to check international applications) lists DSH, TestDaF, Goethe-Institut certificates and the school German diploma DSD as accepted by all universities, with levels that vary (<a href="{SRC['uniassist']}">uni-assist</a>).</li>
<li>Course attendance papers and DW's course certificate are not proof of German.</li>
</ul>
</section>

<section id="ib">
<div class="ibbox">
<h2>7. Your IB subjects and German university entry</h2>
<p class="small">Source: the official KMK agreement on recognising the IB Diploma (decision of 10.03.1986 as amended 15.06.2023; Anlage 1 as of 26.03.2026, Anlage 2 as of 19.11.2024), <a href="{KMK_IB}">KMK PDF</a>. KMK is the conference of German state education ministers.</p>
<ul>
<li><b>Your subjects meet the subject rules</b> (rule 1a and 1b): two languages (English A, French B), a science (Biology), Mathematics (Analysis and Approaches), a social science (Psychology, Business Management), and at least one of the Higher Level subjects is a language, maths or a science (English A HL, Biology HL). Every subject needs at least grade 4 (one grade 3 can be balanced by a 5 in another subject at the same or a higher level, with at least 24 points in total: rule 1d).</li>
<li><b>Maths is the catch</b> (footnote 3): with Mathematics AA at Standard Level you only get <i>subject-restricted</i> entry, to degrees outside mathematics, natural sciences and technology. So no maths, science or engineering degree. The exception is schools on the KMK's Anlage 1 or 2 lists; in Singapore only the German European School Singapore is listed. <b>With Mathematics AA at Higher Level you get general entry</b> to all subjects.</li>
<li><b>German proof</b> (rule 1e): German citizens who took the IB at a school abroad without German as a subject must prove enough German before starting a degree in Germany; the federal states set the details. Other applicants need a German certificate anyway (see <a href="#certs">Certificates</a>). That is what this page is for.</li>
</ul>
<p class="ask"><b>Question for the school:</b> you may want a science or engineering degree. Can you move to Mathematics AA HL, and by when? Without it, the IB alone does not open those degrees (the agreement's rule 2 allows an extra entrance exam, the Feststellungsprüfung, but that costs time).</p>
<!-- UNSURE: rule 1a asks that at least one language is a continued foreign language as Language A or Language B HL; English A is assumed to count. Confirm with the school or the ZAB if needed. -->
</div>
</section>

<section id="free">
<h2>8. Free resources</h2>
<ul class="res">
<li><a href="{A1_COURSE}"><b>DW Learn German: Nicos Weg</b></a>, a free video course: <a href="{A1_COURSE}">A1</a>, <a href="{A2_COURSE}">A2</a>, <a href="{B1_COURSE}">B1</a>. No login needed to watch and do the exercises; from B1 the course is in German only (<a href="{SRC['dwhelp']}">DW help</a>).</li>
<li><a href="{SRC['dfd']}"><b>Goethe-Institut: Deutsch für dich</b></a>: free grammar, vocabulary, reading and listening exercises for all levels. The login was switched off; the exercises stay free without it. More free Goethe material: <a href="{SRC['goethe_free']}">Kostenlos Deutsch üben</a> (page in German).</li>
<li><a href="{SRC['lgn']}"><b>DW: Langsam gesprochene Nachrichten</b></a> (slowly spoken news), Monday to Saturday, audio plus the full text to read along. DW labels it B2, so start it from about B1 (late 2027), with the text open.</li>
<li><a href="{SRC['dwexam']}"><b>DW: Deine Deutschprüfung</b></a>: what the official German tests look like, A1 to C2, with practice tasks for A1 to B1.</li>
</ul>
</section>

<details class="more" id="sources"><summary>Sources (all checked 8 Nov 2026)</summary>
<ul class="small">
<li>Course content and links: DW Nicos Weg <a href="{A1_COURSE}">A1</a>, <a href="{A2_COURSE}">A2</a>, <a href="{B1_COURSE}">B1</a>; <a href="{SRC['dwhelp']}">DW help</a>.</li>
<li>Level statements: CEFR self-assessment grid, <a href="{SRC['europass']}">Europass</a>.</li>
<li>Hours per level: <a href="{SRC['goethe_hours']}">Goethe-Institut Glasgow FAQ</a>; course sizes: <a href="{SRC['goethe_de']}">Goethe-Institut Germany</a>.</li>
<li>Certificates: <a href="{SRC['daad']}">DAAD</a>, <a href="{SRC['testdaf']}">TestDaF Institute</a>, <a href="{SRC['uniassist']}">uni-assist</a>, <a href="{SRC['tum']}">TUM</a>, <a href="{SRC['ffm']}">Goethe University Frankfurt</a>, <a href="{SRC['tubs']}">TU Braunschweig</a>, <a href="{SRC['viadrina']}">Viadrina</a>.</li>
<li>IB entry: <a href="{KMK_IB}">KMK agreement on the IB Diploma</a>.</li>
</ul>
</details>
'''

EXTRA = r'''
  .prog{background:var(--card);border:2px solid var(--indigo);border-radius:8px;padding:14px 16px 8px;margin:20px 0}
  .prog h2{margin:0 0 8px;font-size:1.25rem}
  .pr{display:flex;justify-content:space-between;gap:10px;font-size:.95rem;margin-top:6px}
  .bar{height:8px;background:#E8ECE9;border-radius:4px;overflow:hidden;margin:4px 0 2px}
  .bar i{display:block;height:100%;width:0;background:var(--green);transition:width .2s}
  .small{font-size:.92rem;color:var(--ink-soft)}
  .jump{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 0}
  .jump a{display:inline-flex;align-items:center;min-height:44px;padding:0 12px;border:1px solid var(--rule);border-radius:4px;background:var(--card);text-decoration:none;font-size:.95rem}
  section{margin-top:34px}
  .ck{display:flex;align-items:flex-start;gap:10px;min-height:44px;padding:8px 0;cursor:pointer}
  .ck input{width:20px;height:20px;margin:3px 0 0;flex:none;accent-color:var(--green)}
  ul.cans{list-style:none;padding:0;margin:6px 0}
  ul.cans li{border-bottom:1px solid var(--rule)}
  .sk{display:inline-block;font-weight:700;color:var(--indigo);margin-right:4px}
  .verdict{background:var(--indigo-soft);border-radius:8px;padding:10px 14px;margin-top:12px}
  .honest{background:var(--amber-soft);border-left:5px solid var(--amber);padding:12px 16px;margin:18px 0;border-radius:8px}
  .honest ul{padding-left:22px}
  .recipe{background:var(--card);border:1px solid var(--rule);border-left:5px solid var(--indigo);border-radius:8px;padding:12px 16px;margin:14px 0}
  .recipe ol{margin:4px 0 8px;padding-left:22px}
  ol.days{list-style:none;padding:0;margin:12px 0}
  ol.days li.day{display:grid;grid-template-columns:minmax(0,9.5em) minmax(0,1fr);gap:0 12px;align-items:start;border-bottom:1px solid var(--rule);padding:2px 0}
  ol.days li.day .dw{padding:10px 0 8px}
  ol.days li.rest{color:var(--ink-soft)}
  ol.days li.rest .dd{padding:10px 0 8px 30px}
  .dd{font-weight:700;white-space:nowrap}
  @media (max-width:600px){ol.days li.day{grid-template-columns:minmax(0,1fr)} ol.days li.day .dw{padding:0 0 10px 30px} ol.days li.rest .dd{padding-bottom:0}}
  .wks{display:grid;gap:10px;margin:14px 0}
  .wk{background:var(--card);border:1px solid var(--rule);border-radius:8px;padding:4px 16px 10px}
  .wk.done{border-color:var(--green);background:var(--green-soft)}
  .wk .wh{flex-wrap:wrap;gap:4px 10px;align-items:center}
  .wk .wh input{margin-top:0}
  .wk .chap{margin:0 0 4px;font-size:.9rem;color:var(--ink-soft)}
  .wk ol.ls{margin:0;padding-left:22px}
  .wk ol.ls li{margin:3px 0}
  .tp{color:var(--ink-soft);font-size:.9rem}
  .hol{margin:6px 0 0;font-size:.92rem;color:var(--amber-ink)}
  .ibbox{background:var(--card);border:1px solid var(--rule);border-top:6px solid var(--indigo);border-radius:8px;padding:6px 16px 10px}
  .ibbox h2{margin-top:10px}
  .ibbox ul{padding-left:22px}
  .ask{background:var(--amber-soft);border-radius:8px;padding:10px 14px}
  ul.res li{margin:8px 0}
  details.more{margin:14px 0}
  details.more > summary{font-weight:700;color:var(--indigo)}
'''

SCRIPT = r'''
(function(){
  var KEYS={level:'ib-german-level',days:'ib-german-days',weeks:'ib-german-weeks'};
  var ok=true; try{var t='__ib_t'; localStorage.setItem(t,'1'); localStorage.removeItem(t);}catch(e){ok=false;}
  function get(k){ try{ var v=JSON.parse(localStorage.getItem(k)||'null'); return v&&typeof v==='object'?v:{}; }catch(e){ return {}; } }
  function put(k,v){ try{ localStorage.setItem(k,JSON.stringify(v)); }catch(e){} }
  function today(){ var d=new Date(); return d.getFullYear()+'-'+('0'+(d.getMonth()+1)).slice(-2)+'-'+('0'+d.getDate()).slice(-2); }
  var boxes=[].slice.call(document.querySelectorAll('input[data-store]'));
  function count(sel){ var all=boxes.filter(function(b){return b.matches(sel);}); return [all.filter(function(b){return b.checked;}).length, all.length]; }
  function show(id,c){ var e=document.getElementById('pg-'+id); if(e) e.textContent=c[0]+' of '+c[1];
    var b=document.getElementById('bar-'+id); if(b) b.style.width=(c[1]?Math.round(100*c[0]/c[1]):0)+'%'; }
  function refresh(){
    var a1=count('[data-store=level][data-grp=a1]'), a2=count('[data-store=level][data-grp=a2]');
    show('level',a1); show('days',count('[data-store=days]')); show('weeks',count('[data-store=weeks]'));
    var v=document.getElementById('verdict'), st=document.getElementById('pg-start'), msg, short;
    if(!a1[0]&&!a2[0]){ msg='Tick the statements that are true for you and your starting point appears here.'; short='do the <a href="#check">level check</a> first (5 minutes).'; }
    else if(a1[0]<=4){ msg=a1[0]+' of '+a1[1]+' A1 statements: start at <a href="#now">session 1</a> (Nicos Weg lesson 1) and follow the daily sessions in order. That is exactly what they are made for.'; short='session 1, in order.'; }
    else if(a1[0]<a1[1]){ msg=a1[0]+' of '+a1[1]+' A1 statements: start at <a href="#now">session 1</a>, but move fast. If a session feels easy, do the next one the same day until the lessons feel new again.'; short='session 1, moving fast.'; }
    else if(a2[0]<3){ msg='All A1 statements: you have the basics. Try the free <a href="__A1TEST__">Nicos Weg A1 final test</a>. Passed: use the daily sessions until 4 Dec as quick review and start <a href="__A2__">Nicos Weg A2</a> in the weekly path from 5 Dec. Not passed: follow the daily sessions in order.'; short='take the A1 final test, then decide (see the level check).'; }
    else { msg='All A1 and '+a2[0]+' of '+a2[1]+' A2 statements: you are around A2. Take the free <a href="__A1TEST__">A1 final test</a> now. Passed: skip the A1 daily lessons and spend your 15 minutes on <a href="__A2__">Nicos Weg A2</a> from lesson 1; the weekly path from 5 Dec continues with A2.'; short='around A2: take the A1 final test, then Nicos Weg A2.'; }
    if(v) v.innerHTML='<b>Where to start:</b> '+msg;
    if(st) st.innerHTML='<b>Where to start:</b> '+short;
    boxes.forEach(function(b){ if(b.getAttribute('data-store')==='weeks'){ var w=b.closest('.wk'); if(w) w.classList.toggle('done',b.checked); } });
  }
  boxes.forEach(function(b){
    var k=KEYS[b.getAttribute('data-store')], id=b.getAttribute('data-k');
    b.checked=!!get(k)[id];
    b.addEventListener('change',function(){ var s=get(k); if(b.checked) s[id]=today(); else delete s[id]; put(k,s); refresh(); });
  });
  if(!ok){ var n=document.getElementById('savenote'); if(n) n.textContent='This browser is not saving ticks (private mode?). Your ticks will be lost when you close the page.'; }
  refresh();
})();
'''

SCRIPT = SCRIPT.replace('__A1TEST__', A1_TEST).replace('__A2__', A2_COURSE)
html = page('German: route to a German-taught degree', 'index.html', 'German: your route to a degree in Germany',
            'Not an IB subject: this is your own track to a German-taught degree from autumn 2028. '
            'Now: 15 minutes a day during the exams. From December: about 3 to 4 hours a week, step by step to a C1 certificate.',
            body, SCRIPT)
html = html.replace('</style>', EXTRA + '</style>', 1)
open(f'{out}/german.html', 'w', encoding='utf-8').write(html)
print('german.html', 'days', N_DAYS_TICK, 'weeks', N_WEEKS, 'hours', [R(x) for x in by_2027], [R(x) for x in by_apr28], [R(x) for x in gap], [R(x) for x in total_28], 'q2', q2_weeks, q2_lessons)
