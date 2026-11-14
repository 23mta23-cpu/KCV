# Sales Recruiting Playbook

Nachschlagewerk für Bewerbungen im B2B-IT-Vertrieb im DACH-Raum. Es gilt für Lebenslauf,
Anschreiben, Bewerbungsmail, direkte Ansprache und Gesprächsvorbereitung.

Stand der Recherche: 14.11.2026. Alle Beispiele sind erfunden (Max Mustermann, Musterfirma).

## Inhalt

- 0. Geltung, Rangfolge, Lesehilfe
- 1. Human Writing: menschlicher Schreibstil und KI-Texte
- 2. Erfolgreiche Bewerbungen: Unterlagen, Anschreiben, Outreach
- 3. Entscheidungspsychologie im Recruiting
- 4. Perspektive Recruiter und HR
- 5. Perspektive Vertriebsleiter
- 6. Spezifika im IT-Vertrieb
- 7. Arbeitsweise: drei Brillen und Prüfliste vor jeder Abgabe
- 8. Mythen und Strittiges auf einen Blick

## 0. Geltung, Rangfolge, Lesehilfe

### Wofür das Playbook gilt

Für jede Aufgabe, bei der ein Text für eine Bewerbung entsteht oder geprüft wird: Lebenslauf,
Kurzprofil, Anschreiben, Bewerbungsmail, LinkedIn-Nachricht, Nachfass-Mail, Antwortgerüst für
das Gespräch.

### Rangfolge bei Widerspruch

1. Die fünf Regeln, die nie gebrochen werden
   (`paperclip/recruiting-agentur/package/agents/head-of-recruiting/AGENTS.md`): keine erfundenen
   Fakten, Jobtitel laut Arbeitsvertrag oder Zeugnis, Lücken nicht verstecken, persönliche Daten
   nur mit Freigabe, menschlicher Ton.
2. `CLAUDE.md`: keine Daten realer Personen in diesem Repository.
3. Dieses Playbook.
4. Die Handwerksregeln der Rollen Coach und CV & ATS. Sie bleiben gültig. Wo sie strenger sind
   als dieses Playbook, gilt die strengere Regel.

Zwei Folgen daraus, weil sie oft übersehen werden:

- Psychologische Hebel wirken nur mit wahren Angaben. Kein Hebel rechtfertigt eine Übertreibung,
  einen größeren Titel oder eine geschätzte Zahl.
- „Bewusste Imperfektion" heißt nicht, Fehler einzubauen. Die Regel des Coachs bleibt: keine
  absichtlichen Fehler. Siehe Abschnitt 1.

### Etiketten

Jede Aussage trägt eines von vier Etiketten.

| Etikett | Bedeutung |
|---|---|
| FAKT | Nachweisbar. Die Quelle ist genannt. |
| SCHLUSSFOLGERUNG | Logisch aus Fakten abgeleitet. Die Übertragung eines Laborbefunds auf Bewerbungstexte fällt fast immer hierunter. |
| ANNAHME | Plausible Praxisregel ohne harten Beleg. |
| SPEKULATION | Nicht ausreichend belegt. |

Bei Quellen steht dabei, ob es eine Primärquelle ist (Studie, Befragung mit Methodik, Gesetz,
Originalbuch, offizielle Dokumentation) oder eine Sekundärquelle (Blog, Ratgeber,
Anbieter-Marketing, das andere zitiert).

### Grenzen dieser Recherche

- Die Websuche liefert vor allem US-Quellen. Aussagen zum DACH-Raum sind dort markiert, wo sie
  aus deutschsprachigen Quellen stammen.
- Viel Vertriebswissen ist Anbieter-Marketing. Benchmarks von Softwareanbietern und Investoren
  sind als solche gekennzeichnet.
- Zahlen altern. Gehälter, Umfragewerte und Marktdaten vor der Verwendung neu prüfen.
- Vier oft zitierte Zahlen wurden zusätzlich einzeln nachgeprüft. Das Ergebnis steht in
  Abschnitt 8.

## 1. Human Writing: menschlicher Schreibstil und KI-Texte

Beleglage: Vollständig gelesen wurden die englische Wikipedia-Seite "Signs of AI writing" und die StepStone-Pressemitteilung von 2025. Alle anderen Zahlen stammen aus Zusammenfassungen der Websuche und sind so markiert. P = Primärquelle, S = Sekundärquelle. Quellennummern beziehen sich auf 1.G.

### 1.A Merkmale von KI-Texten

Vorab, FAKT: Die Wikipedia-Seite nennt ihre Merkmale nur Hinweise, nicht Beweise. Sie warnt, dass Menschen KI-Texte nach einer Studie von 2025 nicht besser als per Zufall erkennen. Mehrere Merkmale zusammen zählen mehr als eines allein. (Quelle 1, P für Wikipedia-Praxis, die Studien dahinter sind dort verlinkt.)

Wortschatz Englisch

1. Modewörter: delve, tapestry, intricate, pivotal, crucial, underscore, showcasing, meticulously, landscape, testament ("stands as a testament", "is a testament to"). FAKT. Kobak et al. fanden in 14 Mio. PubMed-Abstracts (2010 bis 2024) 2024 starken Mehrgebrauch, etwa "delves" mit Faktor 28; sie schätzen mindestens 10 % der 2024er Abstracts als LLM-bearbeitet (Untergrenze). Quelle 2, P. Wikipedia listet dieselben Wörter für GPT-4 (2023 bis Mitte 2024). Quelle 1, S zu den Studien.
2. Die Wortlisten altern. "delve" wurde laut Wikipedia 2025 stark seltener. FAKT, Quelle 1. SCHLUSSFOLGERUNG: Eine feste Verbotsliste veraltet; Muster zählen mehr als Einzelwörter.
3. Werbesprache und Bedeutungsaufblähung: "boasts", "vibrant", "rich", "groundbreaking", "plays a vital role", "reflects broader trends". FAKT, Quelle 1.
4. Kopula-Vermeidung: "serves as", "stands as" statt "is". FAKT, Quelle 1 (verweist auf Studien, bei GPT und Gemini beobachtet).

Wortschatz Deutsch

5. Eröffnungs- und Schlussfloskeln: "In der heutigen schnelllebigen Welt", "Zusammenfassend lässt sich sagen", "Es ist wichtig zu beachten", "eintauchen", "nahtlos", "ganzheitlich". ANNAHME. Diese konkreten Wendungen sind in keiner geprüften Quelle belegt. Die im Repo geprüften Wendungen stehen in `tools/cvkit/ki_check.py`. t3n nennt als Buzzwords "revolutionieren", "optimiert", "umfassend" und betont, Menschen nutzten sie auch. Quelle 3, S. Eine belastbare deutsche Wortliste im Stil von Kobak wurde nicht gefunden.
6. Fehlende Idiomatik: wenig Redensarten und Umgangssprache, Oberflächlichkeit. FAKT als Beobachtung von t3n und GameStar, Quelle 3 und 4, beide S, keine Messung.

Satzbau

7. Negativer Parallelismus: "nicht nur ..., sondern auch ...", "Es ist nicht X, sondern Y". Beispiel: "Das ist nicht nur ein Job, sondern eine Berufung." FAKT, Quelle 1.
8. Dreierketten ("schnell, flexibel und zuverlässig"). FAKT, Quelle 1 (Abschnitt "Rule of three").
9. Gedankenstriche: Wikipedia nennt Em-Dashes als Merkmal, meist mit Leerzeichen, aber nur in Kombination nutzbar; neuere Modelle unterdrücken sie, sodass die Lage sich ändert. t3n nennt sie für ChatGPT, Claude und Gemini. FAKT, Quelle 1 und 3. Im Deutschen ist der Halbgeviertstrich mit Leerzeichen als Gedankenstrich normales Schriftdeutsch, das Merkmal ist hier schwächer. SCHLUSSFOLGERUNG.
10. Rhetorische Frage mit Sofortantwort, Doppelpunkt-Pointen ("Das Ergebnis: ..."). ANNAHME. In der gelesenen Wikipedia-Liste ist dafür kein eigener Beleg geprüft.
11. Gleichförmige Satz- und Absatzlängen. t3n nennt es als Merkmal. S, Quelle 3. Belastbarkeit siehe B2.

Struktur

12. Fette Stichwort-Einstiege in Listen ("inline-header vertical lists"), viel Fettdruck, Emojis vor Überschriften, Title Case statt Satzschreibung, falsche Überschriftenebenen. FAKT, Quelle 1.
13. Zusammenfassende Schlusssätze je Abschnitt und "Ausblick/Herausforderungen"-Absätze am Ende. FAKT, Quelle 1 (Abschnitte "Section summaries", "Outline-like conclusions").

Inhalt

14. Vage Quellen ("Experten sagen"), übertriebene Bedeutung, Werbeton. FAKT, Quelle 1.
15. Behauptungen ohne Beleg, fehlende Ecken und Kanten, Absicherungsfloskeln, falsche Ausgewogenheit ("einerseits, andererseits"). SCHLUSSFOLGERUNG aus Punkt 14 und t3n (Oberflächlichkeit); als eigene Kategorie nicht gemessen belegt.
16. Technische Reste: "contentReference[oaicite", Parameter utm_source=chatgpt.com in Links, Chatbot-Anreden im Text. FAKT, Quelle 1. Für Bewerbungen relevant: Links im Lebenslauf bereinigen. ANNAHME.

### 1.B Merkmale menschlicher Texte

1. Perplexity und Burstiness: Perplexity misst, wie vorhersagbar ein Text für ein Sprachmodell ist; Burstiness, wie stark diese Werte im Dokument schwanken (grob: abwechselnd lange und kurze Sätze). Eingeführt von GPTZero (Edward Tian) 2023. FAKT, Quelle 5, P (Anbieter) bzw. S in Zusammenfassung.
2. Belastbarkeit: Nach der Zusammenfassung seiner eigenen Seite nutzt GPTZero seit Herbst 2023 nicht mehr nur diese beiden Werte, sondern ein Deep-Learning-Modell. Das ist nicht auf der Originalseite gegengeprüft. Liang et al. führen ihre Fehlalarme gegen Nichtmuttersprachler auf niedrige Perplexität zurück (Quelle 6, P). SCHLUSSFOLGERUNG: Kurze, einfache, korrekte Sätze lösen Alarme aus, ohne dass KI im Spiel ist. Burstiness taugt als Schreibhilfe (Rhythmus variieren), nicht als Beweis.
3. Rhythmus, Konkretes, präzise Verben, Subtext, eigene Meinung, ungewöhnliche Details. ANNAHME. Das ist Praxiswissen aus der Stillehre (siehe unten) und das Gegenstück zu A14 und A15; eine Studie, die diese Merkmale als Erkennungsmerkmal menschlicher Bewerbungen misst, wurde nicht gefunden.
4. Wikipedia nennt als menschliche Signale: Text vor dem 30.11.2022 entstanden (KI sicher ausgeschlossen), Fähigkeit, eigene Entscheidungen zu erklären, bestimmte Satzkonstruktionen, die Menschen häufiger nutzen. FAKT, Quelle 1. Übertragen auf Bewerbungen: Jede Aussage im Anschreiben muss im Gespräch erklärbar sein. SCHLUSSFOLGERUNG.
5. Bewusste Imperfektion: Es fand sich kein Beleg, dass absichtlich eingebaute Fehler Texte menschlicher wirken lassen oder Recruiter überzeugen. Wikipedia führt "perfekte Grammatik" ausdrücklich als ineffektiven Indikator, der sogar das Gegenteil anzeigen kann (viele Menschen schreiben sehr sauber). FAKT, Quelle 1. SCHLUSSFOLGERUNG: Fehler einbauen ist riskant und unbelegt. Persönliche Details und eigene Wortwahl wirken, nicht Tippfehler.

### 1.C KI-Detektoren und Datei-Spuren

1. OpenAI AI Classifier: seit 20.07.2023 abgeschaltet wegen niedriger Genauigkeit. Er erkannte nur 26 % KI-Texte als "wahrscheinlich KI" und stufte 9 % menschlicher Texte falsch ein. FAKT laut Berichten, die die OpenAI-Angabe wiedergeben (Quelle 7, S). Die Originalseite war nicht abrufbar.
2. Liang et al. 2023 (Stanford, Patterns): mehrere gängige Detektoren, 91 TOEFL-Aufsätze von Nichtmuttersprachlern; mittlere Fehlalarmquote 61,3 %, über die Hälfte als KI markiert; Texte von Muttersprachlern wurden korrekt erkannt. Durch Umformulieren mit "literarischer Sprache" sank die Erkennung nahe null. FAKT, Quelle 6 (P), Zahlen über Pressebericht bestätigt. Folge: Wer sauber, aber schlicht schreibt (viele Nichtmuttersprachler), wird eher zu Unrecht markiert. Relevant für DACH-Bewerber mit Deutsch als Zweitsprache. SCHLUSSFOLGERUNG.
3. Turnitin (2023, eigene Blogposts): Dokument-Fehlalarm unter 1 % bei Dokumenten mit mindestens 20 % KI-Anteil, auf Satzebene rund 4 %, mehr Fehler bei Mischtexten; Turnitin warnt, dass Werte sich ändern. FAKT als Herstellerangabe, Quelle 8 (P Hersteller, ohne Unabhängigkeit). Aktuelle Werte nicht geprüft.
4. GPTZero: wirkt am besten bei unbearbeitetem englischem KI-Text über etwa 250 Wörtern, schwächer bei gemischten und umformulierten Texten. S, Quelle 5, teils SEO-Seiten, Vorsicht.
5. Wikipedia rät, sich nicht allein auf Detektoren zu verlassen (GPTZero, Pangram): besser als Zufall, aber nicht triviale Fehlerquoten, anfällig für Paraphrasieren. FAKT, Quelle 1.
6. Für Bewerbungen: Die Recherche ergab keine belastbare Angabe, wie viele deutsche Recruiter Detektoren einsetzen. Entscheidend ist deshalb der menschliche Leser, und der liegt nach Quelle 1 selbst nicht zuverlässig richtig. SCHLUSSFOLGERUNG.
7. Content Credentials (C2PA): Manifeste können in Bildern, Video, Audio und PDF stehen und enthalten ein Feld digitalSourceType zur Kennzeichnung KI-erzeugter Inhalte. Fehlen sie, beweist das keine menschliche Herkunft; Metadaten lassen sich entfernen. FAKT, Quelle 9 (P, C2PA) und Zusammenfassungen. Prüfwerkzeug: c2patool. Eigene Messung an einer Datei (11/2026): Ein über ChatGPT erzeugtes PDF enthielt ein C2PA-Manifest. Es nannte ChatGPT als Ersteller und stufte den Inhalt als KI-erzeugt ein. Die Word-Datei aus demselben Vorgang enthielt keines. FAKT für diese eine Datei, nicht verallgemeinerbar. Prüfung: `grep -a -c -i c2pa datei.pdf` muss 0 ergeben.
8. PDF-Metadaten (Felder Producer, Creator, Author, Titel) können Werkzeug oder Pfad verraten. ANNAHME aus allgemeinem Wissen, nicht in der Recherche geprüft. Praxisregel: Vor dem Versand Metadaten ansehen und bereinigen.
9. Unsichtbare Unicode-Zeichen (Zero-Width-Zeichen, schmale geschützte Leerzeichen) als KI-Wasserzeichen: Dafür fand sich kein belastbarer Beleg. SPEKULATION. Technische Reste wie utm_source=chatgpt.com in Links sind dagegen belegt (A16).
10. Typografische Anführungszeichen: Wikipedia führt gerade Anführungszeichen als menschliches Gegenstück, krumme als KI-Hinweis (Quelle 1). Im Deutschen setzen Word und Mac typografische Zeichen („ “) automatisch. SCHLUSSFOLGERUNG: im Deutschen kaum aussagekräftig, ebenso der Halbgeviertstrich.

### 1.D Reaktion von Recruitern

Alle Angaben sind Umfragen von Anbietern mit Eigeninteresse. Vergleichbar sind sie kaum.

1. StepStone Österreich, Mai 2025 (P, Pressemitteilung gelesen): Befragt 23. bis 31. März 2025, 160 Recruiter und 700 Beschäftigte (repräsentativ für Österreich). 72 % der Recruiter loben das professionellere Erscheinungsbild von Unterlagen durch KI. 63 % sagen, Unterlagen seien weniger individuell angepasst, 68 % weniger authentisch, 73 % übertrieben dargestellt. 80 % bewerten eingehende Bewerbungen als höchstens mittelmäßig. 58 % der Befragten nutzen KI bei Jobsuche und Bewerbung. Quelle 10.
2. softgarden, Befragung Mai bis Juli 2025, fast 7.000 Bewerbende: 43,2 % nutzen KI für Anschreiben (2023: 12,7 %), 85,8 % davon ChatGPT. Recruiter laut Auswertung nicht per se negativ gegenüber KI-Bewerbungen. Zahlen über Suchzusammenfassung, Originalstudie nicht gelesen. S, Quelle 11. Keine Recruiter-Prozentzahl gefunden.
3. hokify, 2025, 1.600 Jobsuchende in DE und AT (S, Zusammenfassung): 43 % nutzen KI; mehr als zwei Drittel fürchten, dass Personaler KI-Bewerbungen sofort durchschauen. Das ist die Befürchtung der Bewerber, keine Recruiter-Aussage. Quelle 12.
4. Tellent/YouGov, 2026 (S): 73 % der Personaler sagen, KI erschwere die Vergleichbarkeit von Bewerbungen. Stichprobe nicht geprüft. Quelle 13.
5. Resume Genius, 2025, 1.000 US-Befragte (S): 74 % haben KI-Bewerbungen gesehen; 76 % sagen, es sei schwerer, Authentizität zu beurteilen. Quelle 14.
6. Resume Now, März 2025, 925 US-HR-Beschäftigte (S): 62 % lehnen KI-Unterlagen ohne Personalisierung oft ab. Quelle 14.
7. TopResume, Mai 2025, 600 US-Hiring-Manager (S): 19,6 % würden KI-Lebenslauf oder -Anschreiben ablehnen; 33,5 % erkennen ihn in unter 20 Sekunden. Quelle 15.
8. Robert Half, 2025, über 2.000 US-Hiring-Manager (S, Presseberichte): 67 % sagen, KI-Bewerbungen verlangsamen die Einstellung; 65 %, es sei schwerer, Fähigkeiten zu prüfen. Quelle 16.
9. CV Genius: 80 % negativ bei erkennbar KI-erzeugten Unterlagen. Weder Stichprobe noch Jahr in der Quelle genannt, nicht bis zur Primärquelle zurückverfolgt. Quelle 17 (S, nur zitieren mit diesem Vorbehalt).
10. Nicht gefunden: Bitkom, Indeed, Königsteiner, Canva/Sago-Zahlen zu diesem Thema.
11. SCHLUSSFOLGERUNG: Übereinstimmend wird nicht KI-Nutzung bestraft, sondern generische, unpersönliche, übertriebene Texte (StepStone, Resume Now).

### 1.E Dos und Don'ts für Bewerbungstexte

1. Do: Erste Fassung selbst schreiben oder KI-Entwurf komplett umschreiben. Don't: KI-Text unverändert senden (laut CVapp nur etwa 14 % überarbeiten, S, Quelle 18).
2. Do: Pro Behauptung eine belegbare Zahl oder ein konkretes Ergebnis (erfunden: "12 Neukunden in 9 Monaten"). Don't: "erfolgreich", "ganzheitlich", "nahtlos" ohne Beleg.
3. Do: Kurze Hauptsätze, Satzlängen mischen. Don't: gleich lange Absätze mit Schlusssatz.
4. Do: Verben statt Substantive ("ich verantwortete", nicht "in meiner Verantwortung lag"). Don't: Nominalketten.
5. Do: Eine eigene Meinung oder Einschätzung zur Stelle. Don't: "einerseits, andererseits".
6. Do: "nicht nur ... sondern auch", Dreierketten, Doppelpunkt-Pointen streichen oder sparsam setzen. Don't: Dreierkette in jedem Absatz.
7. Do: Gedankenstriche meiden, Kommas und Punkte nutzen (ANNAHME: Vorsichtsregel, weil viele Leser Gedankenstriche als KI-Hinweis lesen).
8. Do: Fett, Emojis, Title Case in Überschriften weglassen. Don't: Stichwortlisten mit fettem Einstieg im Anschreiben.
9. Do: Metadaten der PDF prüfen, Links ohne utm_source senden. Don't: absichtlich Tippfehler einbauen.
10. Do: Alles im Gespräch erklären können. Don't: Qualifikationen übertreiben (73 % der Recruiter beobachten das, Quelle 10).
11. Do: Nicht auf Detektoren verlassen, keine Detektor-Scores versprechen. Don't: nach Detektor-Ergebnis "humanisieren" mit Synonym-Tools.

### 1.F Strittiges und Mythen

1. "Burstiness und Perplexity erkennen KI sicher": nicht belegt, Anbieter selbst wich davon ab (B2). Mythos.
2. "Absichtliche Fehler machen menschlich": kein Beleg gefunden. Mythos bzw. SPEKULATION (B5).
3. "Perfekte Grammatik ist ein KI-Zeichen": von Wikipedia ausdrücklich verneint (B5).
4. "Em-Dash ist der sichere Tell": nur in Kombination, Modelle ändern sich, im Deutschen Normalschrift (A9, C10).
5. "Typografische Anführungszeichen verraten KI": im Deutschen schwach (C10).
6. "Unsichtbare Zeichen als Wasserzeichen in ChatGPT-Text": nicht belegt (C9).
7. "Fehlende C2PA-Daten beweisen menschliche Herkunft": falsch, Daten sind entfernbar (C7).
8. "Recruiter erkennen KI in Sekunden": nur Selbsteinschätzung in Umfragen (TopResume, CV Genius); Wikipedia zitiert eine Studie, wonach Menschen nicht besser als Zufall raten (Quelle 1).
9. "delve, nahtlos, eintauchen als Beweis": Wortlisten veralten, deutsche Liste unbelegt (A2, A5).
10. Oft zitierte Zahlen "80 % der Recruiter lehnen KI ab": nicht bis zur Primärquelle zurückverfolgt (D9). StepStones 80 % bezeichnet Bewerbungsqualität, nicht KI-Ablehnung.

### Stillehre gegen KI-Ton

1. Hamburger Verständlichkeitsmodell (Langer, Schulz von Thun, Tausch): Einfachheit, Gliederung/Ordnung, Kürze/Prägnanz, anregende Zusätze. FAKT, Quelle 19, S (Zusammenfassung). Die Primärquelle (Langer/Schulz von Thun/Tausch, "Sich verständlich ausdrücken") wurde nicht gelesen.
2. Wolf Schneider, "Deutsch für Profis": Verben vor Substantiven, kurze Hauptsätze, Adjektive streichen. Kapitelstruktur aus Leseprobe, Quelle 20, P (Verlagsleseprobe), Einzelregeln nur indirekt belegt. Ludwig Reiners nicht recherchiert. Die Regeln selbst: ANNAHME mit guter Praxistradition.

### 1.G Quellenliste

1. https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing : Merkmalskatalog, Gegenindikatoren, Detektor-Warnung; Rohtext gelesen. P als Wikipedia-Praxisseite (kein Studienersatz).
2. https://arxiv.org/abs/2406.07016 : Kobak et al., Excess Vocabulary in 14 Mio. PubMed-Abstracts. P.
3. https://t3n.de/news/ki-texte-erkennen-5-merkmale-chatgpt-1745388/ : deutsche Merkmale, Gedankenstriche, Floskeln. S.
4. https://www.gamestar.de/artikel/ki-texte-und-buecher-ekennen,3457410.html : deutsche Erkennungstipps. S.
5. https://gptzero.me/news/perplexity-and-burstiness-what-is-it/ : GPTZero-Erklärung der Begriffe. P (Anbieter), Aussage zur aktuellen Methode nur aus Suchzusammenfassung.
6. https://arxiv.org/abs/2304.02819 : Liang et al., Bias gegen Nichtmuttersprachler. P.
7. https://the-decoder.com/openai-discontinues-ai-text-detector-due-to-lack-of-accuracy/ : Abschaltung des AI Classifier, 26 %/9 %. S.
8. https://www.turnitin.ca/blog/understanding-the-false-positive-rate-for-sentences-of-our-ai-writing-detection-capability : Turnitin-Fehlalarmraten. P (Hersteller).
9. https://c2pa.org/wp-content/uploads/sites/33/2026/07/Use-of-Content-Credentials-to-Identify-Synthetic-and-Non-Synthetic-Content.pdf : C2PA zu Kennzeichnung synthetischer Inhalte. P, nur über Suchtreffer gesehen.
10. https://www.stepstone.at/Ueber-StepStone/pressebereich/studie-jede-zweite-bewerbung-mit-hilfe-von-ki-erstellt-recruiterinnen-fehlt-individualitat/ : StepStone-Studie 2025, 160 Recruiter. P (Pressemitteilung mit Methodik).
11. https://www.zfk.de/karriere/neue-softgarden-studie-die-ki-erobert-das-bewerbungsverfahren : softgarden-Studie, Bericht. S.
12. https://www.vienna.at/ki-nutzung-bei-bewerbungen-steigt-deutlich-an/10349336 : hokify-Zahlen. S.
13. https://tellent.com/hubfs/2607_Pressemitteilung_Studie_Tellent_YouGov.pdf : Tellent/YouGov 2026. P (Pressemitteilung), nicht gelesen.
14. https://www.resume-now.com/job-resources/careers/ai-applicant-report : Resume-Now-Bericht (Resume Genius nur über Suchzusammenfassung). S.
15. https://topresume.com/career-advice/ai-in-hiring-survey : TopResume-Umfrage Mai 2025. P (Anbieter-Umfrage).
16. https://www.peoplematters.in/news/ai-and-emerging-tech/67percent-of-hr-leaders-say-ai-generated-resumes-are-slowing-the-hiring-process-48742 : Robert-Half-Zahlen in Presse. S.
17. https://cvgenius.com/blog/career-advice/ai-for-job-application : CV-Genius-Zahl ohne Methodik. S.
18. https://www.computerwoche.de/article/2829440/ki-beschoenigt-lebenslaeufe.html : CVapp-Umfrage (2.800 Bewerbende). S.
19. https://school-scout.de/vorschau/84831/was-macht-einen-text-verstaendlich-sprach-und-stilebenen.pdf : Hamburger Modell, Zusammenfassung. S.
20. https://service.penguinrandomhouse.de/leseprobe/Deutsch-fuer-Profis/leseprobe_9783442161751.pdf : Leseprobe Schneider. P (Verlag), nur Suchtreffer.

## 2. Erfolgreiche Bewerbungen: Unterlagen, Anschreiben, Outreach

Beleglage: 14 Websuchen. Vollständig gelesen wurden die Greenhouse-Dokumentation, der LinkedIn-Beitrag zu InMails, der SHRM-Bericht, die StepStone-Seite und der Artikel der Personalwirtschaft. Alles andere ist Sekundärquelle. P = Primärquelle, S = Sekundärquelle.

### 2.A Was Spitzenbewerbungen auszeichnet

1. Zuschnitt auf die Stelle statt Serienbrief. Begründung: Recruiter erkennen Serienbriefe sofort, ein Serienbrief kann zum Ausschluss führen. ANNAHME (Praxisregel); gestützt durch Joblift-Befragung, nach der gut jeder Fünfte denselben Brief nur mit anderer Adresse und Ansprechperson nutzt (Joblift, 1.058 Bewerber, Jahr nicht geprüft; S über Suchtreffer). Quelle: https://t3n.de/news/?p=1190321 (S).
2. Belege statt Behauptungen. "Umsatz 1,2 Mio. EUR, 118 % der Quote" schlägt "erfolgreich im Vertrieb". SCHLUSSFOLGERUNG aus Ziel der Sichtung (Recruiter suchen Qualifikation; 57 % nennen sie als wichtigstes Kriterium, StepStone 2025, 700 Recruiter, P als Umfrage, über Ratgeberseite): https://www.stepstone.at/Karriere-Bewerbungstipps/die-3-haufigsten-bewerbungsmythen/
3. Klare Struktur, schnell erfassbar. Recruiter scannen nach Überschriften, Daten, Jobtiteln (StepStone-Eye-Tracking, laut Suchtreffer; Primärstudie nicht gelesen). FAKT mit Vorbehalt. Der Wert "43 Sekunden" auf iqb.de stammt aus einer Sekundärdarstellung, Methodik ungeprüft: https://iqb.de/karrieremagazin/bewerbung/darauf-achten-personaler-wirklich-der-lebenslauf/ (S).
4. Fehlerfreiheit. Rechtschreibfehler führen laut Befragungen häufig zur Absage (Zahlen siehe Abschnitt H). Quellen sind Karrierebibel/iqb, also S.
5. Roter Faden: Anzeige, Lebenslauf und Anschreiben erzählen dieselbe Geschichte. ANNAHME, kein Beleg gefunden.
6. Eigeninitiative: Anruf vorab, Ansprache der Fachabteilung, Empfehlung. Nur etwa jedes dritte der Top-500-Unternehmen spricht vor der Bewerbung mit Kandidaten; bei 45 % fehlt eine Telefonnummer der Personalabteilung (Untersuchung mit 1.728 Initiativbewerbungen, Jahr nicht geprüft; S über Suchtreffer). Eine belegte Erfolgsquote für den Anruf wurde nicht gefunden. Etikett: ANNAHME. Quelle: https://karrierebibel.de/anruf-vor-bewerbung/ (S).
7. Empfehlung erhöht die Chancen. Glassdoor-Auswertung: Annahmewahrscheinlichkeit steigt um knapp 7 % bei Empfehlung (Aussage über Annahme, nicht Einladung; Original nicht gelesen). Vendor-Daten (ERIN, 2024, über 1,1 Mio. Empfehlungen): etwa 1 von 10 Empfehlungen wird Einstellung. Das ist Anbieter-Marketing. Etikett: SCHLUSSFOLGERUNG, schwach belegt. Quelle: https://www.noon.ai/blog/articles/360-employee-referral-statistics-2026 (S).

### 2.B Einstiege

Tragen (alles ANNAHME, Praxisregeln; kein Test belegt eine Variante als überlegen):

- Bezug zu einem konkreten Anlass oder Problem der Firma: "Musterfirma baut den Vertrieb für Cloud-Security in der DACH-Region aus. Ich habe als Max Mustermann bei Musterdata in zwei Jahren 14 Neukunden in dieser Nische gewonnen."
- Ergebnis zuerst: "Im letzten Jahr habe ich 130 % meines Neukundenziels erreicht. Genau diese Neukundenarbeit beschreibt Ihre Anzeige."
- Nach Telefonat: "Danke für das Gespräch am Dienstag. Wie besprochen sende ich Ihnen meine Unterlagen für die Stelle Account Executive."
- Empfehlung: "Frau Beispiel aus Ihrem Team hat mir Ihre Stelle empfohlen, weil ich ähnliche Mittelstandskunden betreue."
- Quereinsteiger: "Als Servicetechniker habe ich 300 IT-Störungen pro Jahr gelöst. Jetzt will ich diese Kundennähe im Vertrieb nutzen."

Schaden:

- "Hiermit bewerbe ich mich auf die Stelle als ...": wiederholt nur die Betreffzeile.
- "Mit großem Interesse habe ich Ihre Anzeige gelesen": austauschbar, ohne Aussage.
- "Ich bin teamfähig, belastbar und motiviert": Behauptung ohne Beleg.
- LinkedIn: "Hallo, ich suche einen Job, haben Sie etwas?": kein Nutzen für den Empfänger.

Etikett für die Schadensliste: ANNAHME. Mehrere Ratgeber sagen dasselbe, eine Studie wurde nicht gefunden. Die StepStone-Aussage "kurz, konkret, stellenbezogen" gilt als Beleg für die Richtung: https://www.stepstone.at/Karriere-Bewerbungstipps/die-3-haufigsten-bewerbungsmythen/ (S).

### 2.C Nutzenargumentation und Belegführung

Formeln (alle drei sind Ordnungshilfen; ihre Wirkung ist nicht in Studien belegt, Etikett ANNAHME):

- Problem, Lösung, Ergebnis: Kundenproblem benennen, Maßnahme nennen, Ergebnis messen.
- CAR / PAR / STAR: Challenge (Situation), Action, Result.
- XYZ von Laszlo Bock (damals Google, SVP People Operations): "Accomplished X, as measured by Y, by doing Z". FAKT: Die Formel stammt aus Bocks LinkedIn-Beitrag "My Personal Formula for a Winning Resume" vom 29.09.2014; das Original wurde nicht gelesen, die Angabe stützt sich auf mehrere Sekundärtreffer (z. B. https://qz.com/201088/google-just-revealed-the-incredibly-simple-formula-for-killer-resumes, S). Bocks eigenes Beispiel handelt von einer Schulungsüberarbeitung mit 20 % mehr gemessener Kompetenz. Der Name "XYZ-Formel" ist ein späteres Etikett. Beispiel: "Neukundenumsatz um 25 % gesteigert (Y: 380.000 EUR Jahresumsatz), indem ich 40 Erstgespräche pro Monat über Telefon und LinkedIn geführt habe (Z)."

Arten von Belegen (SCHLUSSFOLGERUNG; im Vertrieb sind sie ohnehin Alltagswährung): Umsatz in EUR, Quotenerfüllung in %, Rang ("Platz 3 von 18"), Zeit ("Abschluss in 45 statt 70 Tagen"), Menge ("60 Kaltanrufe pro Woche"), Pipeline-Volumen, Kundengröße, Dauer von Kundenbeziehungen.

Wirkung von Zahlen: Studienlage. Eine unabhängige oder akademische Messung "Zahlen im Lebenslauf erhöhen die Einladungsquote um X %" wurde nicht gefunden. Genannte Werte (z. B. 41 % mehr Rückmeldungen bei fünf oder mehr Zahlen, Apollo Technical; 75 %, Jeff Su) stammen aus Anbieter-Blogs ohne veröffentlichte Methodik und sind Anbieter-Marketing: https://www.apollotechnical.com/?p=53500 (S). Eine kleine Blindauswahl mit 12 Hiring Managern (Blogbeitrag) fand drei Gewinner ohne Zahlen: SPEKULATION als Gegenbeleg. Fazit: Zahlen sind plausibel nützlich, der Effekt ist nicht beziffert.

Ohne große Zahlen (Berufs- und Quereinsteiger, ANNAHME): Umfang nennen (Anzahl Kunden, Anrufe, Tickets), Rang oder Lob (Bestnote, Auszeichnung), Zeitersparnis, Ergebnisse aus Praktika, Nebenjob, Studienprojekt (z. B. "Konzept für 3 Firmenkunden erstellt, 1 Folgeauftrag"). Ungefähre Zahlen nur, wenn der Kandidat sie selbst so nennt, und dann als "ca." kennzeichnen. Wer den Text schreibt, schätzt nie (Hausregel). Zahlen werden im Gespräch abgefragt.

### 2.D ATS: gesichertes Wissen, Systeme, Mythen

Funktionsweise. FAKT (P, Herstellerdoku): Greenhouse liest Lebensläufe ein und befüllt Profilfelder. Ein fehlgeschlagener Parse bedeutet unvollständige Felder, nicht Ablehnung. Greenhouse nennt als Ursachen: Datei über 2,5 MB, Bild-Dateien statt Text, Grafiken/Fotos/Wordart, Tabellen, Kopf- und Fußzeilen, Namen/Kontakt in Kopfzeile oder Textfeld, Spaltenlayout, fehlende Abschnitte, unvollständige Jobtitel (Beispiel dort "Sr." statt "Senior"). https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse (Stand März 2026).
FAKT (P, Herstellerdoku, nur dieses System): Greenhouse erlaubt Pdf und docx. Allgemeine Aussagen zu "PDF vs. DOCX" über alle Systeme sind widersprüchlich (Anbieterblogs, S). Etikett für die Empfehlung "Text-PDF oder DOCX, kein Scan": SCHLUSSFOLGERUNG.

Ranking, Knockout. Arbeitgeber können Automatikregeln setzen, typischerweise über Knockout-Fragen (z. B. Arbeitserlaubnis, Führerschein, Mindestsprachniveau). Das ist laut Sekundärquellen die Regel, nicht Schlüsselwort-Scores (https://scale.jobs/blog/greenhouse-ats-does-it-automatically-reject-your-resume, S, Anbieter). Harvard Business School und Accenture, "Hidden Workers", 2021: Befragung von über 8.000 Arbeitskräften und über 2.250 Führungskräften in USA, UK, Deutschland; Mehrheit der Arbeitgeber nutzt Filter und Rankings, Lücken im Lebenslauf filtern Bewerber teils aus (FAKT, P über Presseberichte; das Original-PDF wurde nur als Treffer gesehen): https://nahr.shrm.org/sites/default/files/hiddenworkers09032021.pdf

Mythos "75 % aller Lebensläufe werden vom ATS aussortiert". FAKT: Die Zahl lässt sich auf eine Pressemitteilung/Vertriebsaussage der Firma Preptel zurückführen (laut Suchtreffer 2012 oder 2013; die Firma verkaufte Lebenslauf-Optimierung). Eine Methodik oder Studie ist nicht veröffentlicht. Die Preptel-Quelle selbst wurde nicht gefunden; die Herkunft stützt sich auf Sekundärtexte: https://blog.theinterviewguys.com/?p=1967 (S). Behandle die Zahl als unbelegt. Die oft zitierten "92 % der Recruiter bestätigen: kein Auto-Reject" stammen von einer kleinen Stichprobe (23 von 25) auf einer Anbieterseite: unbrauchbar als Beleg.

Systeme im DACH-Raum. Personio (KMU bis Mittelstand), softgarden, rexx systems, d.vinci, SAP SuccessFactors, Workday, SmartRecruiters, Greenhouse, Lever, Recruitee, Teamtailor werden in Vergleichsseiten genannt. FAKT: Belastbare Marktanteile wurden nicht gefunden; Marktberichte (Straits Research) und Herstellerguides nennen keine. Zu Parsing-Qualität der einzelnen DACH-Systeme fanden sich keine unabhängigen Tests. Vergleichsseite (S): https://www.haufe.de/personal/hr-management/hr-software-die-besten-bewerbermanagement-systeme_80_471524.html

Praxisregeln (SCHLUSSFOLGERUNG aus Greenhouse-Doku plus ANNAHME für andere Systeme): einspaltig, Standardüberschriften (Berufserfahrung, Ausbildung, Kenntnisse), Kontaktdaten im Fließtext statt Kopfzeile, ausgeschriebene Jobtitel, Datumsformat einheitlich (MM/JJJJ), Text-PDF unter 2,5 MB, keine Skill-Balken. Schlüsselwörter: Begriffe der Anzeige wörtlich übernehmen, wo sie stimmen, plus gängiges Synonym einmal (z. B. "Key Account Management (KAM)"). Keyword-Stuffing wirkt bei menschlichen Lesern schädlich: ANNAHME.

### 2.E DACH-Normen und Stellenwert des Anschreibens

- Anschreiben: StepStone 2025 (700 Recruiter): 55 % der Unternehmen verlangen eins, nur 34 % der Recruiter halten es für entscheidend, 14 % der Bewerber brechen deshalb ab; Lebenslauf wird in 88 % verlangt; Qualifikationen entscheidend für 57 %. FAKT (Umfrage, über Ratgeber): https://www.stepstone.at/Karriere-Bewerbungstipps/die-3-haufigsten-bewerbungsmythen/
- Taledo-Analyse der 50 umsatzstärksten deutschen Arbeitgeber (IT-, Sales-, Marketing-Stellen, Jahr nicht ermittelt, Artikel zeigt Datum nur teilweise): Anschreiben bei 28 % Pflicht, 64 % optional, 2 % jobabhängig, 2 % ausdrücklich nicht erwünscht. FAKT (Analyse einer Plattform, über Fachmedium): https://personalwirtschaft.de/recruiting/artikel/nur-noch-rund-ein-viertel-der-unternehmen-verlangt-von-bewerbern-ein-anschreiben.html
- Robert Half (Deutschland, 500 Personalverantwortliche laut Suchtreffer, Jahr nicht geprüft): mehr als die Hälfte der Firmen könnte verzichten; 41 % schätzen es noch. S: https://www.roberthalf.com/ch/de/insights/bewerbungs-tipps/ist-ein-bewerbungsanschreiben-heute-ueberhaupt-noch-notwendig
- Firmen ohne Pflicht-Anschreiben: Deutsche Bahn (seit 2017 für Ausbildung, Praktikum, Werkstudenten, Trainees), Bosch (bei vielen IT-Stellen kein Anschreibenfeld), laut Sekundärtreffern, nicht auf Karriereseiten geprüft. S.
- Foto: AGG schreibt kein Foto vor, Arbeitgeber dürfen keines verlangen (SCHLUSSFOLGERUNG; Karrierebibel S). Üblich bleibt es: Befragungswerte schwanken stark (Karrierebibel 92 % "wünschen Foto" eigene Umfrage, Indeed 53 %, laut Skill-Sprinters nicht repräsentativ). Faustregel: Foto optional, Firmenkultur beachten (ANNAHME).
- Länge: eine bis zwei Seiten, tabellarisch, antichronologisch (umgekehrt chronologisch): ANNAHME, in allen Ratgebern gleich, keine Studie gefunden.
- Geburtsdatum, Familienstand, Unterschrift: nicht nötig; Geburtsdatum und Anschrift werden nach DSGVO/AGG-Logik meist weggelassen (ANNAHME). Unterschrift im Anschreiben als Scan optional.
- Kurzprofil: oben im Lebenslauf mit Rolle, Branche, stärkstem Beleg (ANNAHME). Ratgeber nennen 2 bis 3 Zeilen. Die Hausregel (CV & ATS) verlangt 3 bis 5 Sätze in Ich-Form und geht vor.
- Zeugnisse: als Anlage am Ende, die letzten relevanten; Ausnahme Quereinsteiger mit wenig Berufserfahrung dürfen Studien- und Schulzeugnisse beilegen (ANNAHME). Laut StepStone empfinden 62 % Referenzen als hilfreich, 24 % als entscheidend.
- Du oder Sie: im Anschreiben Sie; auf LinkedIn und bei Start-ups folgt man dem Ton des Gegenübers (ANNAHME).

### 2.F Bewerbungsmail, Dateien, Outreach, Nachfassen

- Betreff: "Bewerbung Account Executive (m/w/d), Ref. 4711, Max Mustermann" (Stelle, Referenznummer, Name). ANNAHME.
- Mailtext: 3 bis 5 Sätze mit Hook, Verweis auf Anlage, Erreichbarkeit; kein Wiederholen des Anschreibens. ANNAHME.
- Dateien: eine PDF "Bewerbung_Mustermann_Max.pdf" (Anschreiben, Lebenslauf, Zeugnisse); alternativ Lebenslauf und Zeugnisse getrennt. ComputerWoche empfiehlt eine PDF und rät zu höchstens 10 MB pro Mail (Ratschlag, keine Studie, S: https://www.computerwoche.de/a/6-tipps-fuer-jobsuchende,3552688). Für Portale gilt: Greenhouse parst nur bis 2,5 MB (FAKT, P), also Ziel unter 2 MB.
- LinkedIn-Länge. FAKT (Primärdaten des Herstellers, LinkedIn Talent Solutions, Zehnmillionen InMails von Recruitern an Kandidaten, April 2020 bis Februar 2021): Nachrichten unter 400 Zeichen erzielten 22 % mehr Antworten als der Durchschnitt; über 1.200 Zeichen 11 % weniger. https://business.linkedin.com/talent-solutions/blog/trends-and-research/2021/these-inmails-get-best-response-rates (P, aber Anbieterangabe) und https://www.shrm.org/resourcesandtools/hr-topics/talent-acquisition/pages/analysis-short-personalized-inmails-work-best-linkedin.aspx (S). Einschränkung: Daten gelten für Richtung Recruiter an Kandidat; auf Bewerber an Vertriebsleiter übertragbar nur per SCHLUSSFOLGERUNG. Absolute Antwortquoten fehlen.
- Gute Kurznachricht (ANNAHME, unter 400 Zeichen): "Guten Tag Herr Beispiel, Musterfirma sucht laut Ihrer Anzeige einen Account Executive für Security-Lösungen. Ich habe bei Musterdata 14 Neukunden im Mittelstand gewonnen (120 % Quote). Hätten Sie diese Woche 10 Minuten für ein Gespräch? Viele Grüße, Max Mustermann." Eine konkrete Frage, ein Beleg, ein Bezug.
- Nachfassen: Eine Studie zu Zeitpunkt und Häufigkeit wurde nicht gefunden. Praxisregel (ANNAHME): einmal nach etwa 5 bis 7 Werktagen mit neuem Mehrwert, ein zweites Mal höchstens nach weiteren 7 bis 10 Tagen, dann Schluss. Nennt die Anzeige einen Zeitrahmen, gilt der. Die Hausregel (Coach) setzt 5 Werktage bei Startups und Vermittlern und 10 bei Konzernen an.
- Eigeninitiative ohne offene Stelle: Kaltansprache an die Fachabteilung ist in Vertriebsteams üblich; Quote unbekannt (SPEKULATION über Wirkung).

### 2.G Dos und Don'ts

- Do: Anzeige in drei Anforderungen zerlegen und jede mit einem Beleg beantworten.
- Do: Ansprechperson namentlich prüfen, Firmenname dreimal kontrollieren.
- Do: Zahlen mit Bezugsgröße angeben (Quote, Zeitraum, Team).
- Do: einspaltigen Lebenslauf als Text-PDF unter 2 MB senden.
- Do: kurz telefonieren oder schreiben, wenn es einen konkreten Anlass gibt.
- Do: LinkedIn-Nachricht unter 400 Zeichen mit genau einer Frage.
- Don't: "hiermit bewerbe ich mich" oder "mit großem Interesse" als ersten Satz.
- Don't: Skill-Balken, Tabellen, Fotos in Kopfzeilen, Scan als PDF.
- Don't: Zahlen schönen oder erfinden.
- Don't: mehr als zwei Nachfassnachrichten.
- Don't: ein Anschreiben länger als eine Seite oder den Lebenslauf wiederholen.

### 2.H Strittiges und Mythen

- "75 % vom ATS aussortiert": unbelegt, siehe D.
- "Ohne Keywords keine Chance": Greenhouse nennt als Ablehnungsmechanismus Arbeitgeberregeln, nicht Keyword-Scores (S über Anbieter); für andere Systeme gibt es keine unabhängige Prüfung. SPEKULATION, ob einzelne ATS Scores sichtbar verwenden.
- Zweispaltig: Quellen widersprechen sich; Greenhouse listet Spalten als Parse-Risiko (FAKT, P). Sicherer ist einspaltig.
- PDF vs. DOCX: keine verlässliche systemübergreifende Aussage.
- Anschreiben tot? Nein: 34 % (StepStone) bis 41 % (Robert Half) halten es für wichtig; wo es optional ist, hilft ein kurzes, belegreiches Anschreiben. Wo es Pflicht ist, fehlt es nicht.
- Rechtschreibung: Quellen nennen 61 % (HR-Befragung laut iqb.de, Jahr und Herausgeber ungeprüft), ein Drittel "ein Fehler genügt", etwa 70 % "mehr als drei Fehler". Ein Prozentwert für "falscher Firmenname" oder "Serienbrief" wurde nicht gefunden; beide gelten laut Ratgebern als typische Absagegründe. Quelle: https://iqb.de/?p=14605 (S).
- Zahlen im Lebenslauf: Effekt plausibel, Größenordnung nicht belegt.
- Referral-Zahlen: stammen weitgehend von Anbietern; Werte von 10 % bis 50 % hängen von Firma und Programm ab.

### 2.I Quellenliste

- https://support.greenhouse.io/hc/en-us/articles/200989175-Unsuccessful-resume-parse : Herstellerdoku zu Parsing-Fehlern, Dateigröße 2,5 MB (primär)
- https://business.linkedin.com/talent-solutions/blog/trends-and-research/2021/these-inmails-get-best-response-rates : InMail-Länge und Antwortquote, LinkedIn-Daten (primär, Anbieter)
- https://www.shrm.org/resourcesandtools/hr-topics/talent-acquisition/pages/analysis-short-personalized-inmails-work-best-linkedin.aspx : SHRM-Bericht, Zeitraum 2020/21 (sekundär)
- https://www.stepstone.at/Karriere-Bewerbungstipps/die-3-haufigsten-bewerbungsmythen/ : StepStone-Umfrage 700 Recruiter, 2025 (primär über Ratgeber)
- https://personalwirtschaft.de/recruiting/artikel/nur-noch-rund-ein-viertel-der-unternehmen-verlangt-von-bewerbern-ein-anschreiben.html : Taledo-Auswertung Top-50-Arbeitgeber (sekundär)
- https://www.roberthalf.com/ch/de/insights/bewerbungs-tipps/ist-ein-bewerbungsanschreiben-heute-ueberhaupt-noch-notwendig : Robert Half zur Relevanz des Anschreibens (sekundär, ungeprüft)
- https://nahr.shrm.org/sites/default/files/hiddenworkers09032021.pdf : HBS/Accenture "Hidden Workers" 2021 (primär, nur Treffer gesehen)
- https://blog.theinterviewguys.com/?p=1967 : Herkunft des 75-Prozent-Mythos (sekundär)
- https://qz.com/201088/google-just-revealed-the-incredibly-simple-formula-for-killer-resumes : XYZ-Formel von Laszlo Bock (sekundär)
- https://www.apollotechnical.com/?p=53500 : Anbieterangabe 41 % mehr Rückmeldungen bei Zahlen (sekundär, Marketing)
- https://scale.jobs/blog/greenhouse-ats-does-it-automatically-reject-your-resume : Auto-Reject über Knockout-Regeln (sekundär, Anbieter)
- https://iqb.de/karrieremagazin/bewerbung/darauf-achten-personaler-wirklich-der-lebenslauf/ : Sichtungszeit Lebenslauf (sekundär)
- https://iqb.de/?p=14605 : Absagegründe, Rechtschreibung (sekundär)
- https://karrierebibel.de/anruf-vor-bewerbung/ : Anruf vor der Bewerbung (sekundär)
- https://www.noon.ai/blog/articles/360-employee-referral-statistics-2026 : Referral-Statistiken, Anbieter (sekundär)
- https://www.computerwoche.de/a/6-tipps-fuer-jobsuchende,3552688 : PDF und Dateigröße als Ratschlag (sekundär)
- https://www.haufe.de/personal/hr-management/hr-software-die-besten-bewerbermanagement-systeme_80_471524.html : ATS-Anbieter im DACH-Raum (sekundär)
- https://t3n.de/news/?p=1190321 : Serienbrief als Ausschlusskriterium (sekundär)

Nicht geklärt: Lebenslauf-Originalbeitrag von Bock, Preptel-Originalquelle, Jahre von Joblift, Taledo und Robert Half, Studien zu Nachfassen und Kaltansprache, DACH-Marktanteile der ATS.

## 3. Entscheidungspsychologie im Recruiting

Beleglage: Die Websuche lieferte meist nur Abstracts und Sekundärtexte, Volltexte wurden nicht gelesen. Steht bei einer Studie "URL nicht geprüft", ist sie aus dem Fachwissen zitiert. Die Übertragung von Laborbefunden auf Bewerbungstexte ist durchgehend SCHLUSSFOLGERUNG.

### 3.A Mechanismen

1. Halo- und Horn-Effekt. Ein einzelnes auffälliges Merkmal färbt das Gesamturteil positiv (Halo) oder negativ (Horn). Original: Thorndike 1920, Journal of Applied Psychology (URL nicht geprüft). Personalauswahl: Attraktivität und Sprachgewandtheit beeinflussen Interviewurteile, siehe Barrick et al. 2012 unter Nr. 2. Folge: Ein starker erster Satz, ein namhafter Arbeitgeber oder ein Tippfehler im Kopf des Anschreibens strahlt auf alles Weitere aus. Etikett: FAKT (Effekt), SCHLUSSFOLGERUNG (Textfolge). Quelle: keine geprüfte URL; sekundär nicht belegt.

2. Primacy, Anker, erster Eindruck. Frühe Information gewichtet stärker und wird zum Bezugspunkt. Befund: Barrick, Dustin, Giluk, Stewart, Shaffer, Swider 2012 (Journal of Occupational and Organizational Psychology): Der Eindruck aus dem Smalltalk hing stark mit späteren Bewertungen strukturierter Antworten zusammen, getrieben von Extraversion und Sprachfertigkeit, auch bei Kontrolle der Qualifikation. FAKT. Folge: Die erste Zeile des Lebenslaufs, der Einstieg des Anschreibens und die ersten Minuten im Gespräch sind überproportional wichtig. Primärquelle (Abstract): https://iro.uiowa.edu/esploro/outputs/journalArticle/Candidate-characteristics-driving-initial-impressions-during/9984380378602771

3. Bestätigungsfehler nach dem ersten Eindruck. Interviewer suchen Belege für den ersten Eindruck. Befund: Dougherty, Turban, Callender 1994 (Journal of Applied Psychology), Feldstudie, 79 Interviews: Erste Eindrücke hingen mit bestätigendem Interviewerverhalten zusammen. FAKT. Folge: Ein schwacher Anfang ist schwer zu korrigieren, ein guter Anfang wird gestützt. Primärquelle (Abstract): https://business.missouri.edu/departments-faculty/research-directory/confirming-first-impressions-employment-interview-field

4. Negativitätsverzerrung. Negative Information wiegt schwerer. Befund: Springbett 1958 beschrieb das Interview als "Suche nach negativer Information"; Hollman 1973 fand stärkeren Einfluss ungünstiger Information; ein Review (über Rowe 1989) berichtet, dass mehr als doppelt so viel positive wie negative Information nötig sei, um einen Ersteindruck zu drehen. Webster 1964 und Rowe 1989 im Original nicht geprüft. FAKT für die Richtung, die Größenangabe nur aus Sekundärquelle (ANNAHME). Folge: Ein Fehler (Lücke, Tippfehler, unklare Station) kostet mehr, als eine weitere Stärke bringt. Quellen: https://uh-ir.tdl.org/handle/10657/8755 (Abstract Hollman, primär), https://www.gwern.net/doc/psychology/cognitive-bias/2016-kausel.pdf (Review, sekundär).

5. Verlustaversion, Risikoscheu. Verluste wiegen etwa doppelt so schwer wie gleich große Gewinne. Original: Kahneman, Tversky 1979, Econometrica (URL nicht geprüft). Personalauswahl: kein eigener Beleg gefunden. Folge: Plausibel ist, dass Recruiter die Fehlbesetzung stärker fürchten als sie den Glückstreffer schätzen. SCHLUSSFOLGERUNG, im Kern SPEKULATION. Praktisch: Risiko senken (Referenzen, Belege, klare Verfügbarkeit) wirkt vermutlich mehr als Superlative.

6. Cognitive Ease, Verarbeitungsflüssigkeit. Leicht Lesbares wirkt wahrer, kompetenter. Oppenheimer 2006, Applied Cognitive Psychology: Unnötig komplexe Wörter senkten die wahrgenommene Intelligenz der Autoren, vermittelt über Flüssigkeit; getestet wurde unter anderem mit Bewerbungsessays für Graduiertenprogramme. FAKT (Abstract). Reber, Schwarz 1999, Consciousness and Cognition: besser sichtbare Sätze wurden eher für wahr gehalten; ein Review nennt nur d = 0,13. Eine Replikation von 2025 (Aktepe, Heck) fand keinen Effekt der Farbkontrast-Manipulation auf Wahrheitsurteile. Folge: kurze Sätze, bekannte Wörter, klare Gliederung. SCHLUSSFOLGERUNG. Quellen: https://zendy.io/title/10.1002/acp.1178 (Abstract, primär), https://thecrimson.com/article/2006/10/18/bigger-isnt-always-better-big-words (sekundär), https://openpolar.no/Record/ftciteseerx:oai:CiteSeerX.psu:10.1.1.472.2012 (Katalogeintrag Reber/Schwarz, primär), https://www.uni-marburg.de/@@multilingual-selector/78cea7189e874e8894b95dae9c9e1f55/en?set_language=en (Hinweis auf Replikationsarbeit, sekundär).

7. Konkretheit und präzise Zahlen. Hansen, Wänke 2010, Personality and Social Psychology Bulletin: Konkret formulierte Aussagen wirken wahrer (aus dem Gedächtnis zitiert, Suche fand das Paper nicht; URL nicht geprüft). Mason, Lee, Wiley, Ames 2013, Journal of Experimental Social Psychology: Präzise Erstangebote wirken als stärkere Anker, weil dem Anbieter mehr Wissen zugeschrieben wird. Spätere Arbeit: Bei Experten kann hohe Präzision nach hinten losgehen. FAKT für Verhandlungen, SCHLUSSFOLGERUNG für Bewerbungen. Folge: "37 Neukunden" statt "viele", "Quote 112 %" statt "über 100 %". Quelle: https://business.columbia.edu/press-release/cbs-press-releases/new-research-shows-asking-precise-not-round-number-during (Pressemitteilung, sekundär).

8. Cialdini-Prinzipien. Ähnlichkeit: Rivera 2012, American Sociological Review: In Eliteberatungen, Banken und Kanzleien bewerteten Entscheider Kandidaten stark nach kulturellem Match, also Ähnlichkeit in Freizeit, Stil, Erfahrungen; Interviewkorpus 120 Interviews, qualitativ, nicht auf IT-Vertrieb übertragbar belegt. FAKT (dort), SCHLUSSFOLGERUNG (Übertragung). Sympathie: Barrick 2012 (Nr. 2) stützt indirekt. Autorität und Social Proof: In der Personalauswahl über Signale (Arbeitgeber, Referenzen) plausibel, im Bewerbungskontext nicht belegt gefunden, ANNAHME. Reziprozität, Knappheit, Konsistenz: für Bewerbungen kein Beleg gefunden; Knappheit ("bin nur kurz verfügbar") ist riskant, SPEKULATION. Cialdini selbst (Influence, 1984) URL nicht geprüft. Quelle Rivera: https://www.kellogg.northwestern.edu/academics-research/research/detail/2012/hiring-as-cultural-matching-the-case-of-elite-professional/ (Zusammenfassung, sekundär).

9. Wärme und Kompetenz. Fiske, Cuddy, Glick 2007, Trends in Cognitive Sciences (URL nicht geprüft): Soziale Urteile laufen über Wärme (Absicht) und Kompetenz (Fähigkeit). Kein geprüfter Beleg aus der Personalauswahl. Folge: Der Text muss Können (Zahlen, Ergebnisse) und Zugewandtheit (Bezug zum Gegenüber, ruhiger Ton) zeigen. SCHLUSSFOLGERUNG.

10. Signaling. Spence 1973, Quarterly Journal of Economics (URL nicht geprüft): Kosten- bzw. aufwandsintensive Signale wie Abschlüsse, Zertifikate und namhafte Arbeitgeber zeigen unbeobachtbare Qualität. FAKT (Theorie). Folge: Prüfbare Signale an den Anfang, Zertifikat mit Jahr und Aussteller. Im Vertrieb sind Quotenbelege ein Signal. SCHLUSSFOLGERUNG.

11. Pratfall-Effekt und zweiseitige Argumentation. Aronson, Willerman, Floyd 1966, Psychonomic Science: Ein kompetenter Mensch wird nach einem kleinen Missgeschick sympathischer, ein durchschnittlicher weniger. Wikipedia verweist auf eine Replikation, die Qualität der Quellenangaben dort ist schwach. FAKT eingeschränkt. Folge: Eine kleine, ehrlich genannte Schwäche hilft nur, wenn die Kompetenz bereits belegt ist. SCHLUSSFOLGERUNG. Quelle: https://en.wikipedia.org/wiki/Pratfall_effect (sekundär).

12. Inokulation und Stealing Thunder. McGuire 1961 (Inokulation, URL nicht geprüft). Williams, Bourgeois, Croyle 1993, Law and Human Behavior: Wer belastende Information selbst zuerst nennt, mindert ihre Wirkung, vermittelt über Glaubwürdigkeit; zwei simulierte Gerichtsverfahren. FAKT (Abstract), Grenze: Bei geringer Verarbeitungstiefe half es weniger; Fennis, Stroebe 2013 fanden den Effekt nur bei Firmen mit schlechtem Ruf. Folge: Schwachpunkt früh, kurz, sachlich nennen. SCHLUSSFOLGERUNG. Quelle: https://ojp.gov/ncjrs/virtual-library/abstracts/effects-stealing-thunder-criminal-and-civil-trials (Abstract, primär/sekundär gemischt).

13. Framing, Kontrast, Peak-End, Mere-Exposure, Zeigarnik. Für Bewerbungstexte nicht belegt gefunden. Kontrast ist aus Interviewforschung bekannt (Vorgänger beeinflusst Bewertung), hier nicht geprüft. Nachfassen als Mere-Exposure: SPEKULATION. Nicht in Regeln als Wirkmechanismus aufnehmen.

14. Diskriminierung nach Name, Foto, Herkunft. Kaas, Manger 2012, German Economic Review: 528 Praktikumsanzeigen, deutscher Name brachte rund 14 % mehr Rückmeldungen, bei kleinen Firmen rund 24 %; bei Bewerbungen mit guter Referenz zur Persönlichkeit verschwand der Unterschied. Weichselbaumer 2016 (IZA DP 10217): Frauen mit türkischem Namen und Kopftuch erhielten nur 4,2 % Rückmeldungen. Koopmans, Veit, Yemane (WZB 2018, Ethnic and Racial Studies 2019): etwa 6.000 Stellen, 35 Gruppen; Diskriminierung stärker bei größerer Wertedistanz, eher "Geschmack" als Statistik. FAKT. Ableitung für Bewerber: Zusätzliche Information (Referenz, Zertifikat) verringerte die Lücke bei Kaas/Manger. SCHLUSSFOLGERUNG. Quellen: https://ideas.repec.org/a/bla/germec/v13y2012i1p1-20.html (Katalog, primär), https://newsroom.iza.org/en/archive/research/discrimination-against-female-migrants-wearing-a-headscarf (Pressetext, sekundär), https://econpapers.repec.org/RePEc:zbw:espost:205261 (Abstract, primär).

### 3.B Vertrauen und Kompetenz im Text

Alle Beispiele sind erfunden. Die Textmittel sind aus 3.A abgeleitet, also SCHLUSSFOLGERUNG.

- Spezifität. Vorher: "Ich habe erfolgreich viele Neukunden gewonnen." Nachher: "2024 habe ich bei der Beispiel GmbH 37 Neukunden im Mittelstand gewonnen, Jahresumsatz 1,2 Mio. Euro."
- Prüfbarkeit. Vorher: "Top-Performer im Team." Nachher: "Platz 3 von 14 im Vertrieb 2024; die Rangliste kann mein ehemaliger Vertriebsleiter bestätigen."
- Schlichte Sprache. Vorher: "Ich verfüge über eine ausgeprägte Expertise in der Akquisition komplexer Lösungsportfolios." Nachher: "Ich verkaufe erklärungsbedürftige Software an IT-Leiter."
- Eigener Anteil. Vorher: "Wir haben den Umsatz verdoppelt." Nachher: "Das Team hat den Umsatz verdoppelt. Mein Anteil: 4 der 9 Großabschlüsse, ich habe die Angebote geführt, der Technikpartner die Demos."
- Ruhiger Ton, keine Superlative. Vorher: "Ich bin der ideale Kandidat und der beste Vertriebler." Nachher: "Meine Stärke ist der Einstieg bei Fachbereichen; die Preisverhandlung lerne ich noch."
- Zahlen müssen stimmen und mit dem Lebenslauf und LinkedIn übereinstimmen (siehe E).

### 3.C Augenhöhe

- Bittsteller-Ton: Konjunktivketten ("würde mich sehr freuen, wenn Sie mir die Chance geben"), Dank im Voraus für "Ihre Zeit", Entschuldigungen für Lücken, "leider". Überheblichkeit: Superlative, Belehrung über das Unternehmen, Forderungen ("Ich erwarte ...").
- Gleichrangig: "Ich möchte prüfen, ob meine Erfahrung bei Ihrem Vertriebsziel hilft." "Ich schlage ein 20-minütiges Gespräch vor." "Ich melde mich am Donnerstag, falls Sie eine andere Form bevorzugen." ANNAHME (Praxisregel).
- Forschung: Stevens, Kristof 1995 (Journal of Applied Psychology), Feldstudie zu Selbstdarstellung im Interview; nur bibliografisch bestätigt, Inhalt nicht geprüft. Barrick, Shaffer, DeGrassi 2009 (Journal of Applied Psychology), Metaanalyse: Selbstdarstellung (Self-Promotion, Ingratiation) hängt stärker mit Interviewbewertungen (r = 0,47) als mit späterer Leistung (r = 0,15) zusammen, besonders im unstrukturierten Interview (Zahlen aus Sekundärquelle). FAKT mit Einschränkung. Levashina, Campion (u. a. 2007): Sie trennen ehrliches von täuschendem Impression Management; über 90 % der Studierenden berichteten, in früheren Interviews irgendeine Form genutzt zu haben; Beobachter erkennen den Unterschied schlecht. Überblick: Peck, Levashina zeigen positive Wirkung von IM auf Bewertungen, bei Täuschung gemischt. Folge: Ehrliche Selbstdarstellung (belegte Stärken hervorheben) ist üblich und wirksam; Täuschung ist der problematische Teil. Quellen: https://frontiersin.org/articles/10.3389/fpsyg.2017.00201/full (sekundär), https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5532427/ (Editorial, sekundär).

### 3.D Einwände vorwegnehmen

Muster: Fakt, Grund in einem Halbsatz, Beleg oder Nutzen, weiter. Keine Rechtfertigung, kein Entschuldigen. Forschungsstand: Stealing Thunder (A12) stützt das Selbstnennen; Laborbefund aus Gerichtssimulation, Übertragung SCHLUSSFOLGERUNG. Dass es im Vertrieb nutzt, ist ANNAHME.

- Lücke: "Von 03/2023 bis 08/2023 Auszeit wegen Pflege eines Angehörigen. Seit 09/2023 wieder im Vertrieb, 2024 Quote 104 %."
- Kurze Station: "Die Station dauerte 5 Monate, weil die Vertriebseinheit aufgelöst wurde. Ergebnis in der Zeit: 6 Abschlüsse."
- Fehlende Erfahrung: "Ich habe bisher keine Konzernkunden betreut. Ich habe 40 Mittelstandskunden mit vergleichbaren Entscheidungswegen."
- Branchenwechsel: "Ich komme aus dem Maschinenbau. Ich habe dort drei Jahre lang Software-Lizenzen als Zusatzprodukt verkauft und möchte das hauptberuflich tun."
- Später Start: "Mein frühester Start ist der 01.04. wegen 3 Monaten Kündigungsfrist. Einzelne Termine vorab sind möglich."
- Pratfall-Hinweis: Eine Schwäche nennen nur, wenn sie ohnehin sichtbar ist und die Kompetenz belegt ist. Nicht jede Schwäche anbieten.

### 3.E Grenzen, Ethik, Replikationslage

- Grenze: Wirkung bleibt ehrlich, wenn jede Aussage wahr und belegbar ist. Manipulation beginnt bei erfundenen Zahlen, vorgetäuschter Knappheit ("andere Angebote liegen vor", wenn nicht), erfundener Nähe oder Schmeichelei. Levashina/Campion ordnen Täuschung als eigene, schädliche Kategorie ein. SCHLUSSFOLGERUNG.
- Auffliegen: Eine Studie (Springer, 2017, Journal of Business and Psychology, "intentional resume deception") fand, dass Lebenslauf-Täuschung geringere Leistung und mehr abweichendes Arbeitsverhalten vorhersagt, über Interviewtäuschung hinaus. Das zeigt, warum Arbeitgeber das Thema ernst nehmen. Folgen bei Entdeckung (Kündigung, Anfechtung) sind arbeitsrechtlich plausibel, im DACH-Raum hier nicht geprüft: ANNAHME. Quelle: https://link.springer.com/journal/10869 (Zeitschrift; Artikel dort über die Suche, Abstract, primär).
- Replikation: (a) Fluenz und Wahrheitsurteile: Effekt klein (d = 0,13), neuere Replikation 2025 ohne Effekt, STARK UMSTRITTEN. (b) Oppenheimer 2006: nur Abstract geprüft, breite Replikation nicht gefunden; Richtung plausibel, Größe unklar. (c) Pratfall: Befund von 1966, eine Replikation laut Wikipedia, moderne systematische Replikation nicht gefunden; abhängig von Kompetenz. (d) Halo, Primacy, Negativität: im Interview solide belegt, Effektgrößen schwanken. (e) Anker mit präzisen Zahlen: bei Experten umgekehrt möglich. (f) Cialdini-Prinzipien: überwiegend Alltags- und Marketingbefunde, für Bewerbungen kaum geprüft. (g) Zeigarnik, Mere-Exposure, Peak-End: nicht belegt für Bewerbungen. (h) Verlustaversion: im Kern gut belegt, Reichweite bei Entscheidungen im Recruiting ungeprüft.

### 3.F Dos und Don'ts

- Do: Zahlen mit Jahr und Kontext nennen. Don't: "viele", "diverse", "erfolgreich".
- Do: Eigenen Anteil benennen. Don't: "wir" für Einzelleistungen.
- Do: Kurze Sätze, bekannte Wörter. Don't: Fremdwörter zur Wirkung.
- Do: Prüfbare Belege (Rangliste, Referenz). Don't: Angaben, die man nicht belegen kann.
- Do: Sichtbare Schwäche kurz und früh nennen. Don't: sich rechtfertigen oder entschuldigen.
- Do: Gleichrangig vorschlagen. Don't: bitten, fordern oder prahlen.
- Do: Fehlerfreier Text, vor allem am Anfang. Don't: Tippfehler im Kopf (Horn-Effekt).
- Do: Zahlen in allen Unterlagen angleichen. Don't: Abweichungen zwischen Lebenslauf und Profil.

### 3.G Quellenliste

- https://iro.uiowa.edu/esploro/outputs/journalArticle/Candidate-characteristics-driving-initial-impressions-during/9984380378602771 : Barrick et al. 2012, erster Eindruck und Bewertung, primär (Abstract)
- https://business.missouri.edu/departments-faculty/research-directory/confirming-first-impressions-employment-interview-field : Dougherty, Turban, Callender 1994, Bestätigung, primär (Abstract)
- https://uh-ir.tdl.org/handle/10657/8755 : Hollman, negative vs. positive Information, primär (Abstract)
- https://www.gwern.net/doc/psychology/cognitive-bias/2016-kausel.pdf : Review zu Interviewerverzerrungen, sekundär
- https://zendy.io/title/10.1002/acp.1178 : Oppenheimer 2006, Abstract, primär
- https://thecrimson.com/article/2006/10/18/bigger-isnt-always-better-big-words : Pressebericht zu Oppenheimer, sekundär
- https://openpolar.no/Record/ftciteseerx:oai:CiteSeerX.psu:10.1.1.472.2012 : Reber, Schwarz 1999, Katalog, primär
- https://www.uni-marburg.de/@@multilingual-selector/78cea7189e874e8894b95dae9c9e1f55/en?set_language=en : Hinweis auf Replikationsarbeit Fluenz, sekundär
- https://business.columbia.edu/press-release/cbs-press-releases/new-research-shows-asking-precise-not-round-number-during : Mason et al. 2013, sekundär
- https://www.kellogg.northwestern.edu/academics-research/research/detail/2012/hiring-as-cultural-matching-the-case-of-elite-professional/ : Rivera 2012, Zusammenfassung, sekundär
- https://ojp.gov/ncjrs/virtual-library/abstracts/effects-stealing-thunder-criminal-and-civil-trials : Williams et al. 1993, Abstract
- https://en.wikipedia.org/wiki/Pratfall_effect : Pratfall-Überblick, sekundär
- https://frontiersin.org/articles/10.3389/fpsyg.2017.00201/full : Artikel mit Zitat der Metaanalyse Barrick et al. 2009, sekundär
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5532427/ : Editorial zu Impression Management und Faking, sekundär
- https://ideas.repec.org/a/bla/germec/v13y2012i1p1-20.html : Kaas, Manger 2012, Katalog, primär
- https://newsroom.iza.org/en/archive/research/discrimination-against-female-migrants-wearing-a-headscarf : Weichselbaumer 2016, Pressetext, sekundär
- https://econpapers.repec.org/RePEc:zbw:espost:205261 : Koopmans et al., Abstract, primär
- https://link.springer.com/journal/10869 : Journal of Business and Psychology, Artikel von 2017 zu Lebenslauf-Täuschung und Leistung, primär (Abstract)

Nicht geprüft (nur aus Fachwissen, keine URL): Thorndike 1920; Kahneman/Tversky 1979; Hansen/Wänke 2010; Fiske/Cuddy/Glick 2007; Spence 1973; Aronson et al. 1966 (Original); McGuire 1961; Cialdini; Schindler/Yalch; Webster 1964; Rowe 1989; Stevens/Kristof 1995 (Inhalt); Springbett 1958 (Original).

## 4. Perspektive Recruiter und HR

Beleglage: Websuche, Ergebnisse überwiegend als Zusammenfassungen. Das Original der TheLadders-Studie von 2018 ließ sich nicht abrufen, die Angaben dazu sind Sekundärangaben. P = Primärquelle, S = Sekundärquelle. Kurz genannte Quellen stehen mit voller Adresse in 4.K.

### 4.A Der erste Blick: was gemessen ist und was daraus folgt

1. Die Zahl "6 Sekunden" stammt aus einer Eye-Tracking-Studie von TheLadders (2012). Laut Sekundärberichten: 30 Recruiter, rund 10 Wochen, mittlere Erstentscheidung "passt / passt nicht" etwa 6 Sekunden. FAKT (als Angabe des Herausgebers), Stichprobe nur aus Sekundärquellen. Quellen: recruiter.com (S), theladders.com (S, Selbstdarstellung des Herausgebers).
2. Die Folgestudie von 2018 nennt etwa 7,4 Sekunden. Sie hatte zwei Teile: verdeckte Zeitmessung beim Sortieren und Eye-Tracking im Labor. Eine Stichprobengröße war in den gefundenen Sekundärquellen nicht ausgewiesen; Kritiker bemängeln fehlende Angaben zu Teilnehmerzahl und Erfahrung. FAKT (Kernzahl), Stichprobe unbelegt. Quellen: hrdive.com (S), ere.net (S, Kritik).
3. Gemessen wurde nur die erste Sichtung (Fit / kein Fit), nicht die gesamte Bewertung. Ein Bericht merkt an, die 6 Sekunden seien in der Rezession bei Bewerberüberfluss erhoben worden. SCHLUSSFOLGERUNG. Quelle: ere.net (S).
4. Blickschwerpunkte laut Sekundärangaben: Jobtitel und Zwischenüberschriften; Layouts mit klaren Abschnitts- und Stationsüberschriften schnitten besser ab, Fließtext ohne Struktur schlechter. Nach ungeprüfter Erinnerung an die Studie von 2012: Name, aktuelle Position und Firma, Zeiträume, vorige Position, Ausbildung bekamen den Großteil der Zeit. ANNAHME bis zum Abgleich mit dem Original. Quelle: hrdive.com (S).
5. Praktische Folge: Titel, Firma, Zeitraum und ein Ergebniszahl-Satz pro Station müssen ohne Lesen von Absätzen erfassbar sein; zwei Seiten sind bei Berufserfahrung zulässig, die zweite Seite wird laut Studie bei Interesse ähnlich lange gelesen. SCHLUSSFOLGERUNG. Quelle: hrdive.com (S).
6. Neuere Behauptung "11,2 Sekunden (2025)" ist nur in Blogs gefunden, Studie nicht verifiziert. SPEKULATION.
7. DACH-Gegenstück: Ein Artikel von iqb.de nennt "43 Sekunden für den ersten Eindruck". Die Primärquelle der Zahl wurde nicht ermittelt. Nicht zitieren, bevor sie geprüft ist. SPEKULATION. Quelle: iqb.de (S).
8. Für Bamberg (Recruiting Trends, Weitzel u. a.) ließ sich keine Kennzahl zur Lebenslauf-Sichtdauer finden. Die Studie liefert vor allem Daten zu Digitalisierung und Automatisierung des Recruitings (siehe H). FAKT (Lücke der Recherche).

### 4.B Ablauf der Vorauswahl und Kennzahlen

1. Typische Reihenfolge (Branchenpraxis): Eingang über Karriereseite, Jobbörse oder Netzwerk, Bewerbermanagementsystem (ATS) oder Mailpostfach, Erstsichtung durch HR-Recruiter gegen Muss-Kriterien der Stellenanzeige, Weitergabe der Auswahl an die Fachabteilung (im IT-Vertrieb Vertriebsleiter), dann Telefon-Screening, Gespräche. Externe Vermittler liefern parallel vorselektierte Profile. ANNAHME, keine DACH-Primärstudie dazu gefunden.
2. Knockout-Fragen (Arbeitserlaubnis, Verfügbarkeit, Standort, Führerschein, Sprachniveau) filtern im ATS vor der Sichtung. ANNAHME. Auswirkung: Pflichtfelder wahrheitsgemäß und vollständig ausfüllen.
3. Fast ein Viertel der befragten Personaler hatte laut Jobcluster Recruiting Trends 2025 kein Bewerbermanagementsystem. SCHLUSSFOLGERUNG: Nicht jede Bewerbung wird maschinell gefiltert, viele landen im Postfach. Quelle: chemanager-online.com (S, Pressebericht).
4. Kennzahlen: Time-to-Hire wird laut DGFP/HTWK Leipzig Recruiting-Strukturen Benchmark-Studie 2025 (736 befragte HR-Personen, Erhebung März bis Juli 2025) von rund 74 Prozent der Unternehmen erhoben, nur 39 Prozent halten sie für besonders relevant; Cost-per-Hire laut Presseberichten rund 47 Prozent. FAKT. Quellen: dgfp.de (P), personalwirtschaft.de (S).
5. Time-to-Hire-Werte schwanken je nach Quelle stark: SmartRecruiters Median 55 Tage für Deutschland (Anbieter), Ordio 30 bis 45 Tage (Anbieter), HRworks 72 Tage ohne Quelle. FAKT (Spanne), Methodik uneinheitlich. Für Cost-per-Hire gilt der oft zitierte Wert 4.700 Euro (IZA-Papier 2013) als historisch; ein aktueller belastbarer deutscher Wert wurde nicht gefunden. Bewerbungen je Stelle: keine belastbare DACH-Zahl gefunden.
6. Folge für Bewerber: Recruiter stehen unter Zeitdruck, Antwort und Terminvorschläge schnell und klar geben. SCHLUSSFOLGERUNG.

### 4.C Red Flags (mit Zahlen)

1. Rechtschreibfehler: Werte schwanken je nach Erhebung. Meinestadt.de: 54 Prozent der Personaler sagen, Fehler verspielen die Chance; t-online-Ranking (2021, Umfrage nicht verifiziert): 53 Prozent; Berufsstart: 57,5 Prozent in offener Mitmach-Umfrage (nicht repräsentativ); iqb.de nennt "ab drei Fehlern ca. 70 Prozent" ohne auffindbare Primärquelle. FAKT (je Quelle), die 70-Prozent-Zahl ist nicht bis zur Primärquelle zurückverfolgbar. Quellen: iqb.de (S), t-online.de (S), berufsstart.de (S).
2. StepStone nennt auffällige Rechtschreibfehler (26 Prozent) als Grund geringer Bewerberqualität. FAKT, Primärstudie nicht im Original geprüft. Quelle: stepstone.de (S, Anbieter).
3. Weitere Standard-Nennungen in Ratgebern und Rankings (ohne eigene Zahlen im Abruf): unvollständige Unterlagen, Serienbrief ohne Stellenbezug, falscher Firmenname oder Ansprechpartner, unseriöse E-Mail-Adresse, unerklärte Lücken, häufige Wechsel, widersprüchliche Daten, überhöhte Titel, Floskeln, zu lang, schlechtes Foto. ANNAHME (breit genannt, kaum quantifiziert).
4. Widersprüche zwischen Lebenslauf, Zeugnis und LinkedIn: gelten als Vertrauensbruch. ANNAHME; Falschangaben können bei zulässigen Fragen zur Anfechtung des Vertrags führen (§ 123 BGB). SCHLUSSFOLGERUNG.
5. Auch Bewerber verwerfen Prozesse: softgarden berichtet, 52 Prozent der Befragten sahen schon von einer Bewerbung ab, weil die Anzeige schlecht formuliert war (Gegenrichtung, zeigt Qualitätsdruck auf beiden Seiten). FAKT. Quelle: via personalwirtschaft.de/iqb.de (S).

### 4.D Green Flags

1. Zuschnitt auf die Stelle: Bezug auf drei bis vier Muss-Kriterien der Anzeige in Anschreiben oder Profilsatz. ANNAHME (breiter Konsens in Ratgebern).
2. Belegte Ergebnisse je Station (Umsatz, Quote, Neukunden, Zyklus, Dealgröße) mit Zeitraum. ANNAHME; im Vertrieb Standarderwartung.
3. Roter Faden von Station zu Station, erkennbare Entwicklung. ANNAHME.
4. Erreichbarkeit und schnelle Antwort, klare Verfügbarkeit (Kündigungsfrist). ANNAHME.
5. Saubere, passende Zeugnisse und stimmige Daten über alle Kanäle. ANNAHME.
6. Hinweis: Bewerber, die KI-Texte unredigiert nutzen, fallen auf: 81,6 Prozent der befragten HR-Profis (Jobseeker, 2025, über 1.000 Befragte, Anbieterumfrage) haben schon KI-geschriebene Bewerbungen erhalten. FAKT, Anbieterquelle. Quelle: jobseeker.com (S).

### 4.E Lücken, kurze Stationen, Probezeitkündigung

1. Schwelle: Ratgeber nennen ab zwei bis drei Monaten ohne erkennbare Tätigkeit eine Lücke, ab drei Monaten Erklärungsbedarf; andere Faustregel: bis sechs Monate nichts erklären, ab zwölf Monaten konkrete Erklärung. Das ist der Widerspruch der Quellen. Es gibt keinen gesetzlichen Schwellenwert. ANNAHME. Quellen: stepstone.de, einstieg.com, skill-sprinters.de (alle S).
2. Umfragedaten: Jobware Umfrage-Report 2017: 95 Prozent der Personaler halten eine kurze Neuorientierungsphase für unproblematisch, 91 Prozent sehen Arbeitslosigkeit allein nicht als Ablehnungsgrund. Eine andere Auswertung derselben Reihe berichtet, 96 Prozent sähen Lücken als nachteilig. Beides stammt aus Zweitberichten, nicht bis zur Originaltabelle geprüft; die Aussagen widersprechen sich scheinbar, vermutlich durch unterschiedliche Fragen (kurze Pause vs. Lücke allgemein). FAKT (als Zitat), Deutung SPEKULATION. Quelle: computerwoche.de, haufe.de (S).
3. Seit der Pandemie: LinkedIn (März 2022, Einführung der Funktion "Career Breaks"): Laut Berichten sind 63 Prozent (oder 67 Prozent, je Bericht) von rund 4.000 befragten Hiring Managern eher bereit, Personen mit Auszeit einzustellen als vor der Pandemie; jeder Fünfte lehnt sie ab; Stichprobengröße wird in Berichten abweichend mit 4.000 oder über 7.000 angegeben. Eine Befragung von über 400 Managern (HBS, 2023) bleibt skeptisch. FAKT (als Berichtsangabe), Primärquelle nicht eingesehen, kein DACH-Bezug. Quellen: news.linkedin.com (P, Pressemitteilung, Zahlen darin nicht geprüft), worklife.news, canadianlawyermag.com (S).
4. Übliche ehrliche Benennungen: berufliche Neuorientierung, Weiterbildung (mit Zertifikat), Familienzeit, Betreuung pflegebedürftiger Angehöriger, Auslandsaufenthalt, Sabbatical, arbeitssuchend. Monate statt nur Jahre angeben. ANNAHME (Konsens der Ratgeber).
5. "Arbeitssuchend": mehrere Ratgeber raten statt "arbeitslos" zu "arbeitssuchend" oder "Neuorientierung". Strittig: Manche raten, kurze Lücken (bis etwa zwei Monate) offen zu lassen und nur im Gespräch zu erklären, andere, jede Lücke kurz zu benennen. Einordnung: Eine kurze, sachliche Zeile ("04/2026 bis 06/2026: Neuorientierung, Fortbildung X") ist weniger riskant als Schweigen, wenn die Lücke direkt vor der Bewerbung liegt. SCHLUSSFOLGERUNG.
6. Recht: Eine Pflicht, Lücken im Lebenslauf zu erklären, besteht nicht; bei zulässigen Fragen im Gespräch darf nicht gelogen werden. Elternzeit ist ein Anspruch aus bestehendem Arbeitsverhältnis (§ 15 BEEG); wer ohne Arbeitsverhältnis Kinder betreut, schreibt "Familienzeit" oder "Kinderbetreuung", nicht "Elternzeit". FAKT (Gesetz), Ratgeberquellen nur Sekundär. Quelle: https://www.gesetze-im-internet.de/beeg/ (P).
7. Kurze Station: Ab etwa drei bis sechs Monaten ohne Zusammenhang gilt sie als erklärungsbedürftig; Faustformel Jobhopping: zwei bis drei Jobs in einem Jahr oder mehrere Stationen unter sechs Monaten. Karrierephase zählt: Einsteiger 1 bis 2 Jahre, danach 3 bis 5 Jahre üblich. ANNAHME (Ratgeber, keine Studie). Quelle: karrierebibel.de (S).
8. Probezeitkündigung: Kündigung in der Probezeit braucht keinen Grund (Frist in der Regel zwei Wochen, § 622 Abs. 3 BGB). FAKT. Quelle: https://www.gesetze-im-internet.de/bgb/__622.html (P).
9. Ehrlich und kurz, Beispielsätze (erfundene Daten):
   - "Die Stelle bei der Musterfirma GmbH war als Neukundenvertrieb ausgeschrieben, tatsächlich lag der Schwerpunkt im Innendienst. Das haben wir in der Probezeit gemeinsam festgestellt und beendet. Mir ist seither wichtig, vor Zusage Aufgaben und Quote zu klären."
   - "Der Wechsel hat die Erwartungen beider Seiten nicht erfüllt. Ich habe daraus gelernt, das Einarbeitungskonzept vor Vertragsabschluss zu erfragen."
   - Nicht: Schuld beim Ex-Arbeitgeber, Details zu Streit.
   Kurz im Lebenslauf aufführen; ein Weglassen lässt eine Lücke, die nachgefragt wird. ANNAHME.

### 4.F Wechselmotive, Cultural Fit, roter Faden

1. Gute Motive: Aufgabenerweiterung, Produkt- oder Marktwechsel mit Bezug zur Zielstelle, Verantwortung, Unternehmensentwicklung, Standortwechsel, Vergrößerung des Kundenkreises. ANNAHME.
2. Warnsignale: Schlechtreden des alten Arbeitgebers, "nur mehr Geld", Wechsel bei erstem Gegenwind. ANNAHME.
3. Muster: "Ich habe in drei Jahren Mittelstandskunden im Bereich Cloud betreut und möchte jetzt größere Kundenprojekte verantworten. Ihre Stelle verbindet beides." (erfunden.)
4. Cultural Fit ist umstritten: Auswahl nach Ähnlichkeit (Ähnlichkeitsfehler, Affinity Bias) benachteiligt Vielfalt; daher wird zunehmend "Culture Add" gefordert. FAKT (Konzeptlage), Beleg für Verbreitung im DACH-Raum nicht gefunden. Quelle: keine Primärquelle gefunden.
5. Branchenwechsel: Gemeinsamen Nenner benennen (Kundentyp, Verkaufszyklus, Beratungsvertrieb, Zahlen) und die übertragbaren Kennzahlen nach oben im Lebenslauf stellen. SCHLUSSFOLGERUNG.

### 4.G Arbeitszeugnisse, Referenzen, Recht

1. Anspruch auf ein Zeugnis: § 109 GewO. Zeugnis muss wahr und wohlwollend sein. FAKT. Quelle: https://www.gesetze-im-internet.de/gewo/__109.html (P).
2. Notenstufen laut Rechtsprechung und Kanzleiartikeln: "stets zu unserer vollsten Zufriedenheit" = sehr gut; "stets zu unserer vollen Zufriedenheit" = gut; "zu unserer vollen Zufriedenheit" = befriedigend (Durchschnitt). Bewerber müssen bessere Noten als befriedigend beweisen; Arbeitgeber schlechtere. BAG, 18.11.2014, 9 AZR 584/13. FAKT. Quellen: https://www.bundesarbeitsgericht.de/?p=1150816 (P), https://www.lto.de/recht/hintergruende/h/bag-urteil-9-azr-584-13-bewertung-arbeitszeugnis-stets-volle-zufriedenheit (S). Zu den untersten Stufen (Note 4 / 5) variieren Ratgeber; Einzelformulierung prüfen.
3. Zwischenzeugnis: Anspruch bei berechtigtem Interesse (z. B. Vorgesetztenwechsel, Bewerbung). ANNAHME, nicht an Primärquelle geprüft.
4. Bei Vorauswahl: Rolle begrenzt, meist erst später im Prozess geprüft; Abgleich von Titel und Aufgaben mit dem Lebenslauf ist üblich. Ein fehlendes Zeugnis ist erklärungsbedürftig, besonders bei längerer Station. ANNAHME.
5. Referenzen und Backgroundchecks: Referenzauskünfte nur mit Zustimmung des Bewerbers (Datenschutz). FAKT (Prinzip DSGVO/BDSG), Primärtext nicht geprüft. Gängig in Führungs- und Vertriebsleiterrollen, in Österreich und der Schweiz mit eigenen Regeln. ANNAHME.
6. AGG: schützt vor Benachteiligung wegen Rasse, ethnischer Herkunft, Geschlecht, Religion, Behinderung, Alter, sexueller Identität (§ 1 AGG). Fragen nach Schwangerschaft sind unzulässig, Fragen nach Vorstrafen nur, wenn die Stelle es verlangt. FAKT. Bewerber müssen eine Schwangerschaft nicht mitteilen. Quellen: https://www.gesetze-im-internet.de/agg/ (P), kanzlei-hasselbach.de (S).
7. Foto: Kein Pflichtbestandteil. 82 Prozent der Unternehmen sahen laut Recruiting Trends 2017 (Staufenbiel Institut) eine Bewerbung erst mit Foto als komplett; Staufenbiel/Kienbaum 2016: 38 Prozent halten es für wichtig; Joblift: 10 Prozent der Bewerber bevorzugen Unterlagen ohne Bild. FAKT (Zahlen alt, 2016/2017). Quelle: personalwirtschaft.de (S). Nach AGG-Logik rechtlich freiwillig. SCHLUSSFOLGERUNG.
8. Nach AGG unzulässige Fragen darf man nicht-wahrheitsgemäß beantworten (Recht zur Lüge), zulässige Fragen müssen wahrheitsgemäß beantwortet werden. FAKT (Rechtsprechungslage, Ratgeberzitate). Quellen: dahag.de, anwaltonline.com (S).

### 4.H Personalvermittler und KI auf Arbeitgeberseite

1. Vermittler (Personalberatung, Headhunter) werden vom Arbeitgeber bezahlt, meist 20 bis 35 Prozent des Bruttojahresgehalts (je Quelle 25 bis 30 oder 25 bis 35), als Erfolgshonorar oder anteilig vorab. FAKT (Spanne aus Ratgebern und Anbieterblogs, keine amtliche Statistik). Quellen: personalwirtschaft.de, leonar.app (S, Anbieter).
2. Für Bewerber: seriöse Vermittler verlangen kein Geld vom Bewerber; Unterlagen nur nach Rücksprache und mit Nennung des Zielunternehmens weitergeben lassen. Das Zielunternehmen sollte spätestens im persönlichen Kontakt genannt werden. Mitgliedschaft im BDU, klare Ansprechpartner, transparentes Verfahren sind Hinweise auf Seriosität. FAKT/ANNAHME. Quelle: ulmato.de, karrierebibel.de (S).
3. Doppelvorstellung (derselbe Bewerber über zwei Vermittler beim selben Unternehmen) kann Provisionsstreit auslösen: Immer schriftlich festhalten, wo man schon vorgestellt wurde. ANNAHME, nicht belegt.
4. Der Bitkom-Befragung (Herbst 2024, veröffentlicht März 2025, 852 Unternehmen ab drei Beschäftigte in Deutschland) zufolge nutzt nur 1 Prozent KI-Screening von Bewerbungen, 4 Prozent KI-Chatbots; eine neuere Bitkom-Erhebung (Jahr nicht eindeutig belegt, vermutlich 2026) nennt 6 Prozent bei Sichtung eingehender Bewerbungen und 12,5 Prozent (jedes achte Unternehmen) KI irgendwo im Bewerbungsprozess. FAKT, beide Zahlen über Sekundärberichte (datev-magazin.de, retail-news.de). Quelle Original: https://www.bitkom.org/Presse/Presseinformation/KI-Einzug-in-Personalabteilungen (P, nicht vollständig eingesehen).
5. Bamberg 2016: 2,4 Prozent der Top-1.000-Unternehmen nutzten Algorithmen zur Bewerberidentifikation. FAKT. Quelle: https://fis.uni-bamberg.de/bitstream/uniba/40578/1/Techniksprungse_A3b.pdf (P). Neuere Bamberger Quoten zur KI-Vorauswahl nicht gefunden.
6. EU-KI-Verordnung (Verordnung (EU) 2024/1689): KI-Systeme für Einstellung und Bewerberauswahl, etwa Lebenslauf-Filter und Ranking, sind Hochrisiko (Anhang III Nr. 4). Betreiber haben Pflichten nach Art. 26 (Nutzung nach Anleitung, menschliche Aufsicht, Information der betroffenen Personen). FAKT. Quellen: https://eur-lex.europa.eu/eli/reg/2024/1689/oj (P), dejure.org (S). Anwendungsdatum strittig: Quellen nennen den 2. August 2026, andere eine Verschiebung auf den 2. Dezember 2027; Stand vor Verwendung amtlich prüfen. Offen.

### 4.I Dos und Don'ts

- Do: Titel, Firma, Zeitraum und je Station ein Ergebnis in klarer Struktur.
- Do: Lücken über einem Quartal mit einem Halbsatz benennen.
- Do: Zeugnisse, Lebenslauf und LinkedIn auf Gleichklang prüfen.
- Do: Probezeitende kurz, neutral, nach vorn gerichtet erklären.
- Do: Vermittlern schriftlich vorgeben, wohin Unterlagen gehen dürfen.
- Don't: Rechtschreibfehler, Serienbrief, falsche Ansprechpartner.
- Don't: Titel aufblähen oder Daten glätten.
- Don't: Alten Arbeitgeber schlechtmachen.
- Don't: "Elternzeit" ohne Arbeitsverhältnis schreiben.
- Don't: Geld an Vermittler zahlen.

### 4.J Strittiges und Mythen

- "6 Sekunden" ist ein Eye-Tracking-Wert von 30 Recruitern aus 2012 (US-Anbieter), keine DACH-Messung; 2018 etwa 7,4 Sekunden, Stichprobe nicht ausgewiesen.
- Schwelle für "Lücke": 2, 3, 6 oder 12 Monate je Ratgeber; keine verbindliche Norm.
- "70 Prozent werfen bei drei Fehlern raus": keine Primärquelle.
- Pandemie-Wirkung auf Lücken: LinkedIn-Zahlen sind Anbieterkommunikation, HBS-Befragung skeptischer.
- Erfolgshonorar: ein älterer Artikel (Computerwoche) nennt es unseriös, andere sehen es als Standard.
- Kündigungsangabe "arbeitssuchend" statt "arbeitslos": reine Formulierungsempfehlung ohne Studie.
- Cultural Fit gegen Culture Add: Debatte ohne DACH-Daten.
- KI-Verordnung: Anwendungsdatum je Quelle unterschiedlich.

### 4.K Quellenliste

- https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/ (Bericht zur TheLadders-Studie 2018, S)
- https://www.theladders.com/career-advice/is-it-true-that-recruiters-reject-a-resume-in-six-seconds (Herausgeber selbst, S)
- https://www.recruiter.com/recruiting/theladders-reveals-research-reporting-that-resumes-spend-six-seconds-with-a-recruiter/ (Bericht 2012, S)
- https://www.ere.net/articles/is-the-6-second-resume-scan-a-myth (Kritik an der Studie, S)
- https://csuglobal.edu/sites/default/files/blog-files/theladders-eyetracking-studyc2.pdf und https://www.bu.edu/com/files/2018/10/TheLadders-EyeTracking-StudyC2.pdf (Original-Studie 2018, P; Inhalt nicht abgerufen)
- https://www.dgfp.de/uploads/documents/FINAL-Recruiting-Struktur-BenchmarkStudie-2025.pdf (Benchmark HR-Kennzahlen, P)
- https://ta.smartrecruiters.com/rs/664-NIC-529/images/Germany Recruiting Benchmarks 2025 Report DE.pdf?version=0 (Time-to-Hire Deutschland, Anbieter, S)
- https://chemanager-online.com/de/news/jobcluster-recruiting-trends-2025-umfrage (Bericht zu Jobcluster 2025, S)
- https://www.bitkom.org/Presse/Presseinformation/KI-Einzug-in-Personalabteilungen (KI im Personalwesen, P)
- https://www.datev-magazin.de/nachrichten-steuern-recht/wirtschaft/die-bewerbung-laeuft-fast-ueberall-schon-digital-aber-meistens-noch-ohne-ki-137629 (Bericht zu Bitkom 2024, S)
- https://fis.uni-bamberg.de/bitstream/uniba/40578/1/Techniksprungse_A3b.pdf (Bamberg Recruiting Trends 2016, P)
- https://eur-lex.europa.eu/eli/reg/2024/1689/oj (KI-Verordnung, P)
- https://www.heuking.de/de/news-events/newsletter-fachbeitraege/artikel/einsatz-kuenstlicher-intelligenz-im-arbeitsverhaeltnis-rechtliche-grenzen-risiken-und-pflichten.html (Kanzleibeitrag zum AI Act, S)
- https://www.bundesarbeitsgericht.de/?p=1150816 (BAG 9 AZR 584/13, P)
- https://www.lto.de/recht/hintergruende/h/bag-urteil-9-azr-584-13-bewertung-arbeitszeugnis-stets-volle-zufriedenheit (Urteilsbesprechung, S)
- https://www.gesetze-im-internet.de/agg/ , https://www.gesetze-im-internet.de/gewo/__109.html , https://www.gesetze-im-internet.de/beeg/ , https://www.gesetze-im-internet.de/bgb/__622.html (Gesetzestexte, P)
- https://news.linkedin.com/2022/march/new-way-to-represent-career-breaks-on-linkedin (Career Breaks 2022, P/Herausgeberquelle)
- https://www.stepstone.de/magazin/artikel/luecke-im-lebenslauf (Lücken, S)
- https://www.computerwoche.de/article/2723700/luecken-im-lebenslauf-sind-jobkiller.html (Jobware-Zitat, S)
- https://www.haufe.de/personal/hr-management/recruiting-personaler-geben-bewerbern-selten-eine-zweite-chance_80_429802.html (Personalerbefragung, S)
- https://karrierebibel.de/jobhopping/ (Jobhopping-Faustregeln, S)
- https://iqb.de/karrieremagazin/bewerbung/darauf-achten-personaler-wirklich-der-lebenslauf/ (43-Sekunden-Behauptung, S)
- https://www.personalwirtschaft.de/?p=167856 (Bewerbungsfoto, S)
- https://www.personalwirtschaft.de/?p=100927 (Personalberater, S)
- https://www.kanzlei-hasselbach.de/blog/unzulaessige-fragen-vorstellungsgespraech/ (zulässige Fragen, S)

## 5. Perspektive Vertriebsleiter

Beleglage: 18 Websuchen. Die Zahlen stammen aus Suchtreffern und Zusammenfassungen, Originalberichte wurden nicht geöffnet. "Primär" bezeichnet hier die Fundstelle beim Herausgeber. Vieles ist Anbieter-Marketing und so gekennzeichnet.

### 5.A Wie Vertriebsleiter rechnen

1. SDR-Rampzeit liegt laut Bridge Group "2025 SDR Models & Metrics" bei rund 3,0 Monaten, Tenure bei 1,9 Jahren (laut Bridge-Group-Seite der höchste Wert seit Anfang der 2010er). FAKT für Tenure (Bridge Group, 2025, Primärquelle, Methodik und Stichprobe nicht geprüft). Rampzeit 3,0 Monate und Attrition 40 % stammen aus einer Sekundärquelle (Paraform); die 40 % ließen sich bei Bridge Group nicht bestätigen. Frühere Ausgaben: 2016 Ramp 3,3 Monate und Tenure 1,4 Jahre, 2020 Ramp 3,1 Monate und Tenure 1,8 Jahre (Sekundärangaben).
   Quellen: https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group (primär, Herausgeber); https://www.paraform.com/insights/how-to-hire-sdrs (sekundär, Anbieter)
2. AE-Quotenerreichung: Bridge Group "2026 AE Models, Motions & Metrics" (10. Ausgabe, laut Suchtreffer 158 B2B-Firmen): 48 % der Reps erreichen die Quote, nach 51 % in 2024. FAKT laut Herausgeberseite, Ausgabedatum und Details nicht selbst geprüft. Median-Quote 960.000 USD und Median-OTE 200.000 USD kommen nur aus einer Sekundärquelle.
   Quelle: https://www.bridgegroupinc.com/research/2026-ae-models-motions-metrics (primär)
3. AE-Rampzeit: Die Angaben widersprechen sich (5,0 bis 6,2 Monate bei Bridge Group laut Sekundärquellen, 5,3 bis 9,8 Monate je Segment bei einem Blog mit unklarer Stichprobe). SPEKULATION als Einzelzahl. Belastbar ist nur: Rampzeit wächst mit Dealgröße und Zyklus (SCHLUSSFOLGERUNG).
4. Kosten einer Fehlbesetzung: Genannt werden 177.171 USD (US, Methode unklar), 6 bis 10 Jahresgehälter (Recruiting-Blog), 30 bis 150 % Jahresgehalt (AU). Keine dieser Zahlen ließ sich bis zu einer Primärstudie zurückverfolgen; Herausgeber sind meist Personaldienstleister. ANNAHME als Größenordnung. Transparentestes Modell: Tomasz Tunguz (2014), Fehlbesetzung nach Monat 3 verzögert den Payback auf rund 8 Monate bei linearer 6-Monats-Rampe. FAKT als Modellrechnung, nicht als Messung.
   Quellen: https://tomtunguz.com/quantifying-cost-bad-hire/ (Modell, Blog); https://salesfolks.com/post/the-real-cost-of-a-sales-mishire (sekundär, Anbieter)
5. Xactly, RepVue, CSO Insights: Zu diesen kam in der Suche kein Primärdokument. Nicht zitieren, bevor die Originalreports geprüft sind. Auch die oft zitierten "27 % Fluktuation (Bridge Group)" und "57 % erreichen Quote (Salesforce)" sind unbelegte Sekundärzitate.
6. Gartner 2024 (1.026 B2B-Verkäufer, Jan bis März 2024): Verkäufer, die mit KI arbeiten, erreichen die Quote 3,7-mal wahrscheinlicher; überforderte Verkäufer 45 % seltener. FAKT, Pressemitteilung (Herausgeber, Methodik knapp). Zeigt: Quote ist die zentrale Messgröße.
   Quelle: https://www.gartner.com/en/newsroom/press-releases/2024-09-16-gartner-sales-survey-reveals-sellers-who-partner-with-ai-re-three-point-seven-times-more-likely-to-meet-quota (primär, Pressemitteilung)
7. Zielgrößen des Vertriebsleiters: Teamquote, Forecast-Genauigkeit, Pipeline-Abdeckung, Fluktuation, Ramp-Zeit. ANNAHME (Praxiskonsens, kein Einzelbeleg). SCHLUSSFOLGERUNG: Jede Neueinstellung belastet erst Kosten und Coaching-Zeit, bevor sie Quote bringt; deshalb zählt Ausfallsicherheit mehr als Glanz.

### 5.B Auswahlkriterien und ihre Belege

Roberge (HubSpot), "The Sales Acceleration Formula" (2015): Fünf Merkmale: Coachability, Curiosity, Prior Success, Intelligence, Work Ethic. FAKT laut mehrerer Buchzusammenfassungen; Originalbuch nicht eingesehen, die Gewichte pro Firma verschieden. Prüfung: Scorecard mit numerischen Bewertungen, Rollenspiel mit Live-Coaching (Kandidat bekommt Feedback und spielt erneut; man schaut, ob er es aufnimmt), Qualität der Fragen für Curiosity. In der Bewerbung zeigen: Erfolg in irgendeinem Feld belegen (Prior Success), Lernbelege (Zertifikate, Selbststudium), eigene Fragen. Quellen: https://nateliason.com/notes/the-sales-acceleration-formula-by-mark-roberge (sekundär); https://www.freshworks.com/crm/sales/resources/sales-acceleration-formula-summary-blog/ (sekundär, Anbieter)

Mayer und Greenberg 1964, HBR "What Makes a Good Salesman": Empathie (Gespür für unausgesprochene Kundenwünsche) und Ego-Drive (persönliches Bedürfnis, den Abschluss zu machen, nicht primär Geld). Erfahrung und gutes Auftreten sind laut Zusammenfassungen schwache Prädiktoren. FAKT, aber nur über Sekundärquellen belegt, Originalartikel nicht geprüft (Feldstudie vor allem bei Versicherungsvertretern, Dauer in Quellen uneinheitlich). Prüfung: Gespräch auf Zuhören und Nachfragen plus Drang zum Abschluss. Zeigen: Beispiel, in dem man Bedarf erkannt und aktiv abgeschlossen hat. Quelle: https://www.thequota.co/articles/what-makes-a-good-salesperson-a-landmark-study-from-the-1960s-still-holds-true-today (sekundär)

Challenger Sale (Dixon und Adamson, CEB, heute Gartner, 2011): Fünf Profile mit Anteil an den Reps und an den Top-Performern: Challenger 23 % / 39 %, Lone Wolf 15 % / 25 %, Hard Worker 22 % / 17 %, Problem Solver 14 % / 12 %, Relationship Builder 26 % / 7 %. Stichprobe laut Sekundärquellen: Start bei etwa 700, dann über 6.000 Reps in rund 90 bis 100 Firmen. Die Prozentzahlen stammen aus einer CEB-Folie, nicht aus dem Buch selbst; andere Seiten nennen abweichende Repanteile (z. B. 27 % und 21 %). Konstant über Quellen: 39 % und 7 %. In komplexen Verkäufen soll der Challenger-Anteil unter Top-Performern auf 54 % steigen (Gartner, Sekundärangabe). FAKT mit Einschränkung: Selbstberichte und Vorgesetztenurteile, keine Validierung als Auswahltest (SCHLUSSFOLGERUNG). Prüfung: Wie viel eigene Sicht und Gegenhalten zeigt der Kandidat im Rollenspiel? Zeigen: Beispiel, in dem man einen Kunden mit neuer Einsicht umgestimmt hat. Quellen: https://www.slideshare.net/slideshow/challengerdata/48044856 (CEB-Folie); https://gtmnow.com/challenger-sales-methodology/ (sekundär)

Metaanalysen:

- Vinchur, Schippmann, Switzer und Roth 1998, Journal of Applied Psychology 83(4): Extraversion und Gewissenhaftigkeit sind die stärksten Persönlichkeitsprädiktoren; Biodata (korrigiertes r = .52) und Sales-Ability-Inventare (.45) sagen Vorgesetztenurteile gut voraus. FAKT, Abstract-Ebene (Quelle zur Studie: https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/57961185, Indexeintrag, sekundär). Der Einzelwert .31 für Gewissenhaftigkeit ließ sich nicht bestätigen und wird nicht genannt.
- Verbeke, Dietz und Verwaal 2011, Journal of the Academy of Marketing Science 39(3): Metaanalyse 1982 bis 2008. Stärkste Zusammenhänge: verkaufsbezogenes Wissen (β = .28), Anpassungsfähigkeit (.27), Rollenunklarheit (minus .25), kognitive Fähigkeit (.23), Work Engagement (.23). FAKT. Quelle: https://repub.eur.nl/pub/20379 (Repository der Autoren, primär/Preprint).
- Schmidt und Hunter 1998, Psychological Bulletin 124(2): Validität für Jobleistung: Arbeitsprobe .54, kognitive Fähigkeit .51, strukturiertes Interview .51; Kombination Fähigkeit plus Interview rund .63 (Angaben schwanken zwischen .63 und .68). Sackett et al. 2021 korrigierten nach unten: strukturiertes Interview etwa .42, kognitive Fähigkeit etwa .31. FAKT, Zahlen über Sekundärseiten; nicht vertriebsspezifisch. Quelle: https://stafforini.com/works/schmidt-1998-validity-and-utility/ (Volltext-Hinweis, primär)
- SCHLUSSFOLGERUNG: Strukturiertes Interview und Arbeitsprobe (Rollenspiel) sind besser belegt als Bauchgefühl; deshalb arbeiten Vertriebsleiter mit Scorecard und Rollenspiel.

Grit und Resilienz: Duckworth-Grit wird in der Praxis oft als Ausdauer gedeutet. Credé, Tynan und Harms 2017 (JPSP, Metaanalyse, 88 Studien, rund 67.000 Personen laut Sekundärquelle): Grit hängt nur schwach mit Leistung zusammen (r etwa .18) und überlappt stark mit Gewissenhaftigkeit (Überlappungswerte in Quellen uneinheitlich). FAKT über Sekundärquellen. Zeigen: statt "ich bin hartnäckig" konkrete Dauerbelege (Zahl der Versuche, Jahre durchgehalten). Quelle: https://www.news.iastate.edu/news/2016/05/18/grit-analysis (Pressemitteilung, sekundär)

Optimismus, Seligman und Schulman 1986 (Journal of Personality and Social Psychology): 94 erfahrene Versicherungsagenten: obere Hälfte im Attributional Style Questionnaire verkaufte in den ersten zwei Jahren 37 % mehr; neu eingestellte optimistische Agenten blieben doppelt so häufig im Job. LIMRA-Angabe der Autoren: 78 % der Neueinsteiger gehen binnen 3 Jahren. FAKT laut Abstract; korrelativ, Versicherungs-Außendienst (Übertragung auf B2B-IT: ANNAHME). Prüfung: Erklärungsstil beim "Verlorener Deal": externe, instabile Ursachen für Rückschläge plus eigener Lernanteil. Quelle: https://researchgate.net/profile/Peter-Schulman/publication/232497771_Explanatory_Style_as_a_Predictor_of_Productivity_and_Quitting_Among_Life_Insurance_Sales_Agents/links/547cc8f70cf2cfe203c1fc7c/Explanatory-Style-as-a-Predictor-of-Productivity-and-Quitting-Among-Life-Insurance-Sales-Agents.pdf (primär, Abstract)

Topgrading (Bradford Smart): Chronologisches Interview über jede Stelle (Erfolge, Misserfolge, Gründe für Wechsel, Vorgesetzte), 4 bis 6 Stunden. Behauptete Trefferquote 75 bis 90 % stammt von Topgrading selbst, ohne unabhängige Prüfung. Das 75-%-Ziel ist ein Benchmark, keine Messung. Anbieter-Marketing. Zeigen: lückenlose, ehrliche Stationen, Wechselgründe ohne Schuldzuweisung. Quelle: https://www.sellingpower.com/2010/01/13/2350/the-top-grading-interview (sekundär)

### 5.C Hunter und Farmer

- Definition (Praxis): Hunter gewinnen Neukunden, Farmer pflegen und erweitern Bestandskunden. FAKT als Sprachgebrauch.
- Herkunft: Das Bild stammt laut Quellen vom Psychotherapeuten Thom Hartmann (Farmer/Hunter-Hypothese zu ADHS), später in Personalauswahl und Vertrieb übertragen. Sekundärangabe, Originalbuch nicht eingesehen. Quelle: https://www.smartcompany.com.au/marketing/cracking-the-sales-myth-of-hunters-farmers/
- Rollenzuordnung (ANNAHME, Marktpraxis): Neukunden: SDR/BDR (Termine), Account Executive (Abschluss). Bestand: Account Manager, Customer Success (Verlängerung, Ausbau). Key Accounts liegen dazwischen.
- Prüfung: Fragen nach Lieblingsphase (Erstkontakt oder Beziehung), Neukundenanteil im Lebenslauf, Umgang mit Ablehnung, Mock Cold Call gegen Account-Review-Szenario. ANNAHME.
- Streitpunkt: Keine belastbare empirische Validierung der Typologie gefunden; Kritiker (Duane Sparks, Sue Barrett) nennen sie "Hooey" bzw. Mythos, in komplexem B2B arbeiten dieselben Leute oft in beiden Modi. Die zwei Ziele (Neugeschäft, Bestandsausbau) bleiben real. FAKT für "keine Studie gefunden" (Suchergebnis), Kritik ist Meinung. Quelle: https://barrett.com.au/blogs/2015/3324/sales-management/cracking-the-sales-myth-of-hunters-farmers (sekundär, Blog)

### 5.D Zahlen im Lebenslauf

Erfahrene Verkäufer (ANNAHME, gestützt durch Ratgeber; Ratgeberquellen sind Anbieter von Bewerbungstools, nicht unabhängig):

- Zielerreichung in Prozent je Jahr, Rang im Team (z. B. "Platz 3 von 12"), Umsatz oder Auftragseingang, durchschnittliche Dealgröße, Zyklus in Wochen, Neukundenanteil, Pipeline-Volumen.
- Vertrauliche Euro-Zahlen als Prozent oder Größenordnung angeben. Beispiel mit erfundenen Daten: "Musterfirma GmbH: 112 % Zielerreichung, Platz 2 von 9, Neukundenanteil 70 %, Ø Deal 40 T Euro, Zyklus 14 Wochen."
- Quellen: https://novoresume.com/de/ressourcen/lebenslauf-beispiele/vertriebsleiter ; https://resufit.com/de/blog/vertrieb-lebenslauf-beispiele-vorlagen-key-account-manager/index.md (beide sekundär, Anbieter)

Einsteiger ohne Erfolgsbilanz (ANNAHME, in Logik von Roberges "Prior Success in jedem Feld" und Mayer/Greenbergs schwachem Erfahrungsbezug begründbar, SCHLUSSFOLGERUNG):

- Aktivitätszahlen (Anrufe pro Tag, Termine pro Woche, Konversionsrate), Nebenjob mit Provision oder Trinkgeld, Leistungssport mit Rangzahlen, eigenes Projekt mit Umsatz, Lernbelege (Zertifikate, Selbststudium zu Produkt und Markt).

### 5.E Die Bewerbung als Pitch

- Länge und Kürze: Anschreiben gilt als Probe der eigenen Outbound-Texte; über 500 Wörter, generisch und ohne Zahl wirken schlecht. Quelle SDR-Ratgeber (Anbieter, sekundär). ANNAHME für DACH: eine Seite. https://syncgtm.com/blog/how-to-write-a-sales-development-cover-letter
- Recherche: Fehlende Firmenrecherche steht auf jeder Warnliste (Recruiting-Anbieter). https://revenue.io/blog/avoid-red-flags-hiring-new-sdrs-inside-sales-reps (sekundär)
- Nachfassen: Rechtzeitiges Nachfassen gilt als Signal; fehlendes als Warnzeichen (selbe Quelle). Zu LinkedIn-Direktansprache und Telefon wurde KEIN belastbarer Beleg gefunden. SPEKULATION bleibt: ein kurzer, höflicher Nachfass nach etwa einer Woche.
- 30-60-90-Tage-Plan: In Ratgebern üblich (Tage 1 bis 30 Analyse und Vertrauen, 31 bis 60 Routinen und Coaching, 61 bis 90 Quote). Anbieter-Blog, ANNAHME als Zusatz, nicht als Pflicht. https://www.cleverly.co/blog/sdr-onboarding-30-60-90-day-outbound-plan
- Betreff: keine Quelle gefunden; ANNAHME: Stellenbezeichnung plus eine Zahl.
- Aussagen deutscher Vertriebsleiter im Original: nicht gefunden. Lücke.

### 5.F Interviewformate, Fragen, Gegenfragen

Formate: Rollenspiel (Produkt verkaufen, Einwand "zu teuer"), Mock Cold Call, Discovery-Rollenspiel, Fallstudie, Präsentation, Probetag. Im DACH-Raum laufen Erstgespräche 45 bis 60 Minuten, Zweitrunden oder Assessment bis drei Stunden (Jobrise, sekundär). Belege zur "Stift"-Aufgabe, zum Probetag und zu Vertriebsleiter-Interviews fanden sich nicht. Quelle: https://jobrise.io/de/blog/vorstellungsgespraech-vertriebsmitarbeiter-fragen-2026/ (sekundär, Anbieter); https://blog.hubspot.de/sales/rollenspiel-verkaufsgespraech (sekundär, Anbieter-Marketing)

Typische Fragen und gute Antworten (ANNAHME, Praxisregel):

- "Wie viel Prozent Ihrer Ziele haben Sie erreicht?" Konkrete Prozentzahl je Jahr, Teamvergleich, Einflussfaktoren ohne Ausrede.
- "Erzählen Sie von einem verlorenen Deal." STAR-Struktur, eigener Anteil, was sich danach geändert hat (stützt sich auf Erklärungsstil, Seligman).
- "Wie bauen Sie Pipeline auf?" Kanäle, Aktivitätszahlen, Konversionsraten, Priorisierung.
- Rollenspiel: Fragen vor Pitch, Einwand nachfragen, aktiver Abschluss mit nächstem Schritt (HubSpot DE, sekundär).

Gegenfragen starker Kandidaten (ANNAHME): Wie viel Prozent des Teams erreichen die Quote? Wie lange ist die Rampzeit und gibt es garantierte Provision währenddessen? Wer liefert Leads, wie ist das Gebiet geschnitten? Verhältnis Fix zu Variabel, Deckelung, Beschleuniger, Auszahlung auf Rechnung oder Zahlungseingang? Wie viele Verkäufer sind in zwölf Monaten gegangen? Quelle: https://www.quotapath.com/blog/top-20-sales-interview-questions-when-hiring-sales-reps (sekundär, Anbieter). Warnung der Quelle: "80 % erreichen die Quote" prüfen über Dealgröße mal Abschlüsse pro Monat.

### 5.G DACH: Vergütung und Gepflogenheiten

- Fix/Variabel: Anbieter nennen 70/30 für SDR und 50/50 für AE. FAKT nur als Anbieteraussage; keine unabhängige Statistik gefunden. Quelle: https://skipcall.io/de/blog/sdr-gehalt-deutschland (sekundär, Anbieter-Marketing).
- Gehaltsdaten (alle sekundär, Methodik unklar, Datenstand 2026, Rohdaten StepStone/Glassdoor/kununu nicht geprüft): SDR Junior OTE 45.000 bis 55.000 Euro, Median rund 53.000 (etwa 42.000 fix, 11.000 variabel); BDR 45.000 bis 65.000 OTE (Jobrise); AE Mid-Market 70.000 bis 110.000 OTE (Jobrise) bzw. 85.000 bis 130.000 (Skipcall); Gehaltsportal-Median AE 4.927 Euro brutto monatlich ohne Provision (gehalt.de/brutto-netto-Rechner). Die Streuung zeigt: nur Spannen nennen, nie Einzelwerte. Quellen: https://jobrise.io/de/blog/tech-sales-jobs-deutschland-sdr-ae/ ; https://www.gehalt.de/beruf/account-executive
- Recht: Probezeit höchstens 6 Monate (Lexware, sekundär). Auch bei hoher Provision muss ein angemessenes Fixum gezahlt werden (versicherungsbote.de, sekundär). Widerrufsvorbehalte laut BAG 12.1.2005 (5 AZR 364/04) in der Regel bis etwa 25 bis 30 % der Gesamtvergütung (Haufe-Sekundärzitat, am Original prüfen). Provisionsregeln schriftlich fixieren. Quellen: https://www.lexware.de/wissen/mitarbeiter-gehalt/probezeit-im-arbeitsvertrag-vereinbaren/ ; https://www.haufe.de/id/beitrag/2-kollektivarbeitsrecht-8-anpassungsvorbehaltteilkuendigung-7-HI16679316.html
- Dienstwagen: keine Quelle gefunden; ANNAHME: im Außendienst und Key Account verbreitet, im Inside Sales selten.
- Sie oder Du: Schriftlich Sie als sichere Wahl; Du im Gespräch nur, wenn der Gegenüber es anbietet; in IT und Startups oft früh Du (karriere.at, computerwoche, beides sekundär). Umfrage rund 1.000 Erwachsene: für 49 % egal, ob Stellenanzeige "du" nutzt. https://www.karriere.at/c/a/qa-bewerbung ; https://www.personalwirtschaft.de/?p=163251
- Zeugnisse und Referenzen: kein Beleg gefunden. ANNAHME: Arbeitszeugnis ist im DACH-Raum Standardbestandteil der Bewerbung, im Vertrieb zählen Zahlen zusätzlich.

### 5.H Was abschreckt

(ANNAHME aus Recruiting-Anbieterquellen, kein Primärbeleg): keine Zahlen im Lebenslauf; Ausreden und Schuldzuweisung bei Zielverfehlung; schlechtes Reden über Ex-Arbeitgeber; vage Antworten; fehlende Firmenrecherche; Verspätung, schwache schriftliche Kommunikation; kein Nachfassen; Titel-Inflation (Titel ohne Verantwortung oder Zahl). Quelle: https://revenue.io/blog/avoid-red-flags-hiring-new-sdrs-inside-sales-reps (sekundär)

### 5.I Dos und Don'ts

- Do: Zielerreichung je Jahr als Prozentzahl nennen. Don't: "erfolgreich im Vertrieb" ohne Zahl.
- Do: Verlorenen Deal mit eigenem Lernanteil erzählen. Don't: Kunde, Markt oder Chef verantwortlich machen.
- Do: Firma und Produkt vorab recherchieren, Bezug im ersten Satz. Don't: Standardanschreiben.
- Do: Im Rollenspiel erst fragen, dann aktiv abschließen. Don't: Pitch ohne Bedarfsfrage.
- Do: Feedback im Rollenspiel sichtbar umsetzen. Don't: verteidigen.
- Do: Fragen zu Teamquote, Rampzeit, Fluktuation, Deckelung stellen. Don't: nur nach Urlaub und Dienstwagen fragen.
- Do: Als Einsteiger Aktivitäts- und Ersatzzahlen bringen. Don't: Titel aufblähen.
- Do: Nach etwa einer Woche kurz nachfassen. Don't: täglich nachhaken.

### 5.J Strittiges und Mythen

- Zahlen zur Fehlbesetzung (6 bis 10 Gehälter u. ä.) stammen aus Anbieterblogs; keine Primärstudie gefunden.
- Challenger-Prozentsätze: aus CEB-Folie, Sekundärseiten weichen ab; Selbstberichtsdaten.
- Hunter/Farmer: keine empirische Validierung gefunden.
- Grit: schwache Zusatzvorhersage über Gewissenhaftigkeit hinaus.
- Topgrading-Trefferquoten: Selbstangaben.
- Schmidt/Hunter 1998: später nach unten korrigiert (Sackett 2021), nicht vertriebsspezifisch.
- Seligman/Schulman: Versicherungsverkauf, korrelativ; Sekundärquellen nennen auch 31 % statt 37 %.
- "Verkaufen Sie mir diesen Stift": kein Beleg für Verbreitung oder Aussagekraft gefunden.
- Gehaltsverhältnisse 70/30 und 50/50: Anbieteraussagen, keine Statistik.

### 5.K Quellenliste

- https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group : SDR-Tenure, Rampzeit (primär, Herausgeber)
- https://www.bridgegroupinc.com/research/2026-ae-models-motions-metrics : AE-Quotenerreichung 48 % (primär, Herausgeber)
- https://www.paraform.com/insights/how-to-hire-sdrs : Zusammenfassung SDR-Zahlen (sekundär)
- https://tomtunguz.com/quantifying-cost-bad-hire/ : Modell Kosten Fehlbesetzung (Blog, Modell)
- https://salesfolks.com/post/the-real-cost-of-a-sales-mishire : Kostenschätzungen (sekundär, Anbieter)
- https://www.gartner.com/en/newsroom/press-releases/2024-09-16-gartner-sales-survey-reveals-sellers-who-partner-with-ai-re-three-point-seven-times-more-likely-to-meet-quota : Gartner-Befragung 2024 (primär, Pressemitteilung)
- https://nateliason.com/notes/the-sales-acceleration-formula-by-mark-roberge : Roberge-Zusammenfassung (sekundär)
- https://www.freshworks.com/crm/sales/resources/sales-acceleration-formula-summary-blog/ : Roberge-Zusammenfassung (sekundär, Anbieter)
- https://www.thequota.co/articles/what-makes-a-good-salesperson-a-landmark-study-from-the-1960s-still-holds-true-today : Mayer/Greenberg (sekundär)
- https://www.slideshare.net/slideshow/challengerdata/48044856 : CEB-Folie Challenger-Anteile (Primärnah, Folie)
- https://gtmnow.com/challenger-sales-methodology/ : Challenger-Überblick (sekundär)
- https://acnpsearch.tweb-dev.unibo.it/singlejournalindex/57961185 : Eintrag Vinchur et al. 1998 (Index, sekundär)
- https://repub.eur.nl/pub/20379 : Verbeke et al. Arbeitspapier (primär, Preprint)
- https://stafforini.com/works/schmidt-1998-validity-and-utility/ : Schmidt/Hunter 1998 (primär)
- https://www.news.iastate.edu/news/2016/05/18/grit-analysis : Credé-Metaanalyse (Pressemitteilung, sekundär)
- https://researchgate.net/profile/Peter-Schulman/publication/232497771_Explanatory_Style_as_a_Predictor_of_Productivity_and_Quitting_Among_Life_Insurance_Sales_Agents/links/547cc8f70cf2cfe203c1fc7c/Explanatory-Style-as-a-Predictor-of-Productivity-and-Quitting-Among-Life-Insurance-Sales-Agents.pdf : Seligman/Schulman 1986 (primär)
- https://www.sellingpower.com/2010/01/13/2350/the-top-grading-interview : Topgrading (sekundär)
- https://www.smartcompany.com.au/marketing/cracking-the-sales-myth-of-hunters-farmers/ : Hunter/Farmer-Kritik und Herkunft (sekundär)
- https://barrett.com.au/blogs/2015/3324/sales-management/cracking-the-sales-myth-of-hunters-farmers : Hunter/Farmer-Kritik (Blog)
- https://novoresume.com/de/ressourcen/lebenslauf-beispiele/vertriebsleiter : Zahlen im Lebenslauf (sekundär, Anbieter)
- https://resufit.com/de/blog/vertrieb-lebenslauf-beispiele-vorlagen-key-account-manager/index.md : Zahlen im Lebenslauf (sekundär, Anbieter)
- https://syncgtm.com/blog/how-to-write-a-sales-development-cover-letter : SDR-Anschreiben (sekundär, Anbieter)
- https://revenue.io/blog/avoid-red-flags-hiring-new-sdrs-inside-sales-reps : Warnzeichen (sekundär, Anbieter)
- https://www.cleverly.co/blog/sdr-onboarding-30-60-90-day-outbound-plan : 30-60-90 (sekundär, Anbieter)
- https://jobrise.io/de/blog/vorstellungsgespraech-vertriebsmitarbeiter-fragen-2026/ : DACH-Interviewablauf (sekundär, Anbieter)
- https://blog.hubspot.de/sales/rollenspiel-verkaufsgespraech : Rollenspiel (sekundär, Anbieter-Marketing)
- https://www.quotapath.com/blog/top-20-sales-interview-questions-when-hiring-sales-reps : Fragen und Gegenfragen (sekundär, Anbieter)
- https://skipcall.io/de/blog/sdr-gehalt-deutschland : SDR-Gehalt, Fix/Variabel (sekundär, Anbieter)
- https://jobrise.io/de/blog/tech-sales-jobs-deutschland-sdr-ae/ : BDR/AE-OTE (sekundär, Anbieter)
- https://www.gehalt.de/beruf/account-executive : AE-Gehaltsspanne (Gehaltsportal, sekundär)
- https://www.lexware.de/wissen/mitarbeiter-gehalt/probezeit-im-arbeitsvertrag-vereinbaren/ : Probezeit (sekundär)
- https://www.haufe.de/id/beitrag/2-kollektivarbeitsrecht-8-anpassungsvorbehaltteilkuendigung-7-HI16679316.html : Widerrufsvorbehalt BAG (sekundär)
- https://www.karriere.at/c/a/qa-bewerbung : Sie/Du (sekundär)
- https://www.personalwirtschaft.de/?p=163251 : Du in Stellenanzeigen, Umfrage (sekundär)

Lücken: Xactly, RepVue, CSO Insights, DePaul-Studie, Barrick und Mount, Dienstwagen, Zeugnisse, LinkedIn-Nachfassen, Aussagen deutscher Vertriebsleiter im Original.

## 6. Spezifika im IT-Vertrieb

Beleglage: Die Websuche lieferte nur Zusammenfassungen. Die Berichte von KeyBanc, Bridge Group und StepStone wurden nicht im Original gelesen. Aussagen ohne Quellennummer sind Praxiswissen und als ANNAHME zu lesen. P = Primärquelle, S = Sekundärquelle. Quellennummern beziehen sich auf 6.L.

### 6.A Geschäftsmodelle und Segmente

Modelle (alle Einträge ANNAHME, Praxiswissen ohne Einzelbeleg, Zykluslängen sind grobe Spannen):

- SaaS: Verkauf von Nutzungsrechten im Abo. Umsatz: wiederkehrend (ARR), Wachstum durch Neukunden, Erweiterung (Upsell, Cross-Sell) und Verlängerung. Zyklus: SMB Tage bis Wochen, Mid-Market 1 bis 4 Monate, Enterprise 6 bis 12 Monate. Gesprächspartner: Fachbereich, IT-Leitung, Einkauf, Datenschutz.
- Cloud und Hyperscaler (AWS, Azure, Google Cloud): Umsatz verbrauchsabhängig (Consumption). Verkäufer werden oft an Verbrauchswachstum gemessen, Marktplätze erlauben Abrechnung über bestehende Cloud-Verträge. Zyklus: länger bei Migrationsprojekten, kurz bei Erweiterung. Partner: Architekten, Cloud-Verantwortliche, FinOps.
- Klassische Lizenzen und Wartung: Einmalige Lizenz plus jährliche Wartung (oft 15 bis 22 Prozent des Listenpreises, ANNAHME). Zyklus 3 bis 12 Monate, Gesprächspartner IT-Leitung und Einkauf.
- Reseller und Lizenzhandel (z. B. Microsoft CSP, Distribution): Umsatz aus Handelsspanne und Services. Margen sind niedrig, Differenzierung über Beratung und Bindung. Zyklus kurz, Volumen hoch.
- Systemhäuser: Mischung aus Hardware, Lizenzen, Projekten und Managed Services. Kunde ist meist der Mittelstand. Bechtle, Cancom, Computacenter sind große Beispiele (Q13, S). Hinweis (FAKT, S): Ein Teil des Cloud- und Lizenzgeschäfts wird nach IFRS 15 netto als Rohertrag gebucht, Umsatzzahlen sind deshalb schwer vergleichbar.
- IT-Dienstleistung und Managed Services: Laufende Pauschalen (Servicevertrag) oder Aufwand. Umsatz planbar, Verkauf über Vertrauen und Referenzen.
- IT-Beratung und Projektgeschäft: Time and Material (Abrechnung nach Aufwand), Festpreis (Risiko beim Anbieter), Rahmenverträge (Abruf über Jahre). Öffentliche Auftraggeber schreiben aus.
- Hardware: Einmalverkauf, niedrige Marge, Projekt- und Preisgetrieben, oft über Distribution.

Segmente (ANNAHME, ohne harte Studie):

- SMB: Dealgröße klein, Zyklus kurz, 1 bis 3 Beteiligte, oft Inhaber entscheidet. Mid-Market: 3 bis 6 Beteiligte, IT-Leitung und Geschäftsführung. Enterprise: viele Beteiligte, formale Freigaben, Einkauf, Security-Review, Zyklus 6 bis 18 Monate.
- Öffentlicher Sektor: Vergabe nach Vergaberecht, Leistungsbeschreibung, Fristen, Bieterfragen. Verkäufer sind eher Bieter- und Partnerbetreuer als freie Akquisiteure. Beziehungsaufbau vor der Ausschreibung ist begrenzt zulässig. SPEKULATION bei Details: nicht geprüft.

Buying Center (Gartner):

- FAKT (S, Q1): Gartner nennt für komplexe B2B-Käufe eine Käufergruppe von 6 bis 10 Entscheidern, Käufer verbringen etwa 17 Prozent der Kaufzeit im Kontakt mit Anbietervertrieb (Umfrage unter 750 Käufern, ältere Gartner-Studie, genaues Jahr nicht bestätigt). Bei mehreren Anbietern entfällt auf jeden ein kleiner Teil (Gartner nennt etwa 5 Prozent bei drei Anbietern).
- FAKT (P, Q2): Gartner Pressemitteilung vom 25.06.2025: 61 Prozent der B2B-Käufer bevorzugen einen Kauf ohne Verkäufer (Befragung August bis September 2024). Eine spätere Befragung (646 Käufer, 2025) nennt 67 Prozent, nur als Zweitbericht gefunden (S, Q3).
- Nicht bestätigt: Angaben wie "11 Beteiligte" oder "5 bis 16 Personen" kursieren mit wechselnder Zuordnung zu Gartner (S, Q4). Sie ließen sich nicht bis zu einer Primärquelle zurückverfolgen. In Texten nur "oft zitiert 6 bis 10 laut Gartner" schreiben.
- FAKT (P, Q5): Gartner 2025: 74 Prozent der Käuferteams zeigen "unhealthy conflict" im Entscheidungsprozess.

### 6.B Rollen und Karrierepfade (alles ANNAHME, Praxis)

- SDR (Sales Development Rep, Innendienst Neukundenansprache), BDR (Business Development Rep): oft synonym, BDR teils outbound auf Zielkonten. Kennzahlen: Anwahlen, Gespräche, gebuchte Termine, qualifizierte Opportunities (SQO). Einstieg: Quereinsteiger aus Service, Handel, Gastronomie, Studium. Weg: AE oder Inside Sales nach 12 bis 24 Monaten.
- Inside Sales (Vertriebsmitarbeiter Innendienst): Abschluss per Telefon und Video, kleinere Deals. Kennzahl: Umsatz, Abschlussquote, Zyklus.
- Account Executive (AE, Neukundengeschäft): Verantwortung für Zyklus bis Abschluss. Kennzahlen: Quota (Jahresziel), Pipeline, Win Rate, Dealgröße.
- Account Manager, Key Account Manager (Vertriebsaußendienst, Kundenbetreuer): Bestandskunden, Erweiterung, Verlängerung. Kennzahlen: NRR, Umsatz je Konto, Forecast.
- Customer Success Manager: Nutzung, Verlängerung, Churn-Vermeidung. Kennzahlen: GRR, NRR, Adoption.
- Presales, Sales Engineer, Solution Consultant: Demo, PoC, Architektur, Ausschreibungsantworten. Kennzahl: technische Gewinnquote, Unterstützung je Deal. Zugang oft über Technik, Support, Beratung.
- Channel, Partner Manager: Betreuung von Resellern, Systemhäusern. Kennzahl: partnergetriebener Umsatz.
- Sales Operations, RevOps: CRM, Forecast, Quoten, Provisionen, Prozesse. Zugang über Analyse, Controlling.
- Hinweis zu Pfaden: Reihenfolge ist nicht verbindlich. Viele Unternehmen trennen SDR und AE streng, kleine Firmen nicht.

### 6.C Methodiken

Herkunftsangaben: Buchtitel und Autor sind FAKT (P, Originalbücher), Details der Methode ANNAHME aus Allgemeinwissen, sofern nichts anderes steht.

1. SPIN Selling: Neil Rackham, Huthwaite, Buch 1988. Datenbasis: Analyse tausender Verkaufsgespräche (oft zitiert 35.000, in dieser Recherche nicht geprüft). Kernidee: Fragen in der Reihenfolge Situation, Problem, Implication (Folgen), Need-payoff (Nutzen der Lösung). Bei großen Deals verkaufen die Erfolgreichen über Folgenfragen statt Produktmerkmale. Einsatz: Bedarfsanalyse in komplexen, teuren Verkäufen. Nachweis: eigene Folgenfrage nennen ("Was kostet Sie ein Systemausfall pro Stunde?").
2. Challenger Sale: Matthew Dixon, Brent Adamson, CEB (heute Gartner), Buch 2011. Kernidee: Erfolgreiche Verkäufer lehren (Teach), passen die Botschaft an (Tailor) und steuern das Gespräch (Take Control). Einsatz: komplexe Lösungsverkäufe, Kunden ohne klaren Bedarf. Nachweis: Beispiel, in dem man dem Kunden eine unerwartete Einsicht lieferte. Hinweis: Die Typologie (fünf Verkäufertypen) stammt aus CEB-Umfragen unter Anbietern, Marketing und Beratung des Verlags prägt die Rezeption.
3. MEDDIC, MEDDPICC: Entstanden bei PTC in den 1990ern (Dick Dunkel, Jack Napoli, unter John McMahon). Genaues Jahr unklar (Q6, S, überwiegend Anbieterseiten). Bestandteile: Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion. MEDDPICC ergänzt Paper Process und Competition. Einsatz: Qualifizierung und Forecast im Enterprise. Nachweis: Jeden Buchstaben an einem echten Deal zeigen, bei fehlender Info ehrlich sagen "Economic Buyer nicht erreicht".
4. BANT: IBM, Kriterien Budget, Authority, Need, Timing. Genaue Herkunft und Jahr nicht geprüft (ANNAHME). Einsatz: schnelle Erstqualifizierung beim SDR. Schwäche: frühe Budgetfrage kann Kunden abschrecken. Nachweis: Gegenbeispiel nennen, wann BANT zu eng ist.
5. Solution Selling: Michael Bosworth, Buch 1994 (Solution Selling: Creating Buyers in Difficult Selling Markets). Kernidee: Kundenproblem erkennen und eine Lösung aufbauen, bevor man Produkte nennt. Nachweis: Problem zuerst beschreiben, dann Lösung.
6. Consultative Selling: Mack Hanan, 1970er. Kernidee: Verkäufer als Berater, der Gewinnbeitrag für den Kunden verspricht. Einsatz: Beratungsgeschäft, Nachweis: Nutzen in Euro statt Features.
7. Value Selling: Sammelbegriff für Verkauf über quantifizierten Kundennutzen, Anbieter wie ValueSelling Associates verwenden den Namen markenrechtlich. Nachweis: Business Case-Beispiel.
8. Sandler: David Sandler, 1960er, Sandler Training. Kernidee: Rollenverteilung auf Augenhöhe, früh über Budget und Entscheidungsprozess sprechen, "Up-front Contract". Nachweis: Wie man ein Gespräch ohne Folgetermin beendet.
9. Command of the Message: Force Management. Kernidee: Kundenprobleme, Nutzen und Differenzierung strukturiert in "Before and After Scenarios". Einsatz: Enterprise-Teams, die dieses Programm eingeführt haben (Anbieter-Methode).
10. Gap Selling: Keenan, Buch 2018. Kernidee: Verkauf als Lücke zwischen Ist und Soll des Kunden, Problem muss belegt sein. Nachweis: Ist-Zustand quantifizieren.
11. Account-Based Selling: Fokus auf definierte Zielkonten und Buying Center, abgestimmt zwischen Marketing und Vertrieb. Nachweis: Kontoplan mit Rollen im Buying Center.
12. Product-Led Growth mit Sales-Assist: Nutzer starten selbst (Free oder Trial), Vertrieb steigt bei Nutzungssignalen ein (Product Qualified Lead). Einsatz: SaaS mit Self-Service. Nachweis: Kenntnis des Unterschieds MQL und PQL.

Im Gespräch: Eine Methode nennen, die man selbst angewendet hat, und eine Schwäche. Keine Aufzählung von Akronymen.

### 6.D Kennzahlen-Glossar

- ARR: annualisierter wiederkehrender Umsatz. MRR: monatlich. ARR = MRR x 12. Ohne Einmalumsätze.
- ACV: durchschnittlicher Jahresvertragswert. TCV: Gesamtwert über die Laufzeit (inklusive Einmalposten).
- NRR (Net Revenue Retention): (Start-ARR + Erweiterung - Abgänge - Downgrades) / Start-ARR. Über 100 Prozent heißt Bestandskunden wachsen. GRR: ohne Erweiterung, höchstens 100 Prozent.
- Churn: Kundenchurn = verlorene Kunden / Kunden am Anfang. Umsatzchurn = verlorener Umsatz / Start-Umsatz.
- CAC: Vertriebs- und Marketingkosten / neue Kunden. LTV: Deckungsbeitrag je Kunde über die Lebensdauer. CAC-Payback: CAC / (neuer ARR x Bruttomarge) in Monaten.
- Pipeline-Coverage: offene Pipeline / Rest-Ziel. Richtwert "3x" ist Faustregel (ANNAHME), die Zahl hängt an der Win Rate: Coverage ca. 1 / Win Rate.
- Win Rate: gewonnene / abgeschlossene Opportunities. Sales Cycle: Tage von Opportunity-Anlage bis Abschluss. Durchschnittliche Dealgröße: Umsatz / gewonnene Deals.
- Quota Attainment: erreichter Umsatz / Quote. Forecast-Genauigkeit: Abweichung zwischen Prognose und Ergebnis.
- SDR-Aktivität: Anwahlen, Gespräche, gebuchte Termine, qualifizierte Opportunities. MQL (Marketing Qualified Lead), SAL (vom Vertrieb angenommen), SQL (vom Vertrieb qualifiziert). Definitionen sind firmenspezifisch.

Benchmarks (alle mit Vorsicht):

- Bridge Group "SDR Models and Metrics Report" 2025 (Anbieter, Beratung, 351 Firmen): 60 Prozent der Reps am Quota, laut Seitenzusammenfassung der niedrigste Wert; Median SDR-OTE 80.000 US-Dollar (Q7, P-nah, nicht im Original geprüft, USA).
- KeyBanc/Sapphire SaaS Survey 2025 (Investoren, Befragung privater SaaS-Firmen): Primärbericht nicht gelesen. Zweitquellen nennen Bruttoretention zwischen etwa 86 und 90 Prozent und NRR um 100 Prozent, widersprüchlich (Q8, S). Nicht als sichere Zahl verwenden.
- CAC-Payback-Median 16 Monate stammt von Benchmarkit (S), nicht von KeyBanc. Verschiedene Definitionen.
- Alle Benchmarks sind US-lastig, Anbieter- oder Investorenquellen, Selbstauskunft.

### 6.E Technik und Business

- Erwartung (ANNAHME): Verkäufer müssen Architektur und Begriffe auf Gesprächsniveau verstehen (Cloud, Schnittstellen, Sicherheit, Betrieb), nicht programmieren. Wer nicht weiter weiß, holt Presales.
- Zusammenarbeit: Presales (Demo, PoC, technische Klärung), Consulting (Einführung), Produktmanagement (Roadmap, keine Zusagen ohne Freigabe), Customer Success (Einführung und Verlängerung), Recht und Datenschutz (AVV, Haftung, Vertragsklauseln), Einkauf.
- Übersetzung: Technikmerkmal, dann Wirkung, dann Euro. Dimensionen: Kosten senken, Risiko senken (Ausfall, Sicherheit, Compliance), Umsatz erhöhen, Zeit sparen. Beispiel mit erfundenen Daten: "Musterfirma spart durch Automatisierung 6 Stunden pro Woche je Mitarbeiter, bei 40 Mitarbeitern ca. 12.000 Euro Personalkosten im Monat."
- Instrumente: Demo (zeigt Funktion am Kundenfall), Proof of Concept (befristeter Test mit vorab vereinbartem Erfolgskriterium), Business Case, ROI (Nutzen minus Kosten, geteilt durch Kosten) und TCO (Gesamtkosten über Lebensdauer inklusive Betrieb, Schulung, Migration), Referenzkunden (besonders im Mittelstand wichtig).
- Typischer Fehler: PoC ohne Erfolgskriterium, ROI ohne Annahmen des Kunden.

### 6.F Werkzeuge

- CRM: Salesforce, HubSpot, Microsoft Dynamics 365, Pipedrive, SAP Sales Cloud. Im Mittelstand und DACH sind Dynamics und SAP verbreitet, HubSpot und Pipedrive bei kleineren Firmen (ANNAHME).
- Sales Engagement: Outreach, Salesloft (Sequenzen, Telefonie). LinkedIn Sales Navigator (Kontakte, Kontosuche). Gong (Gesprächsanalyse). Datenanbieter: ZoomInfo, Cognism, Dealfront (früher Echobot und Leadfeeder) für DACH.
- Ehrlich nennen: Stufe angeben (Nutzer, versiert, Administrator) und Kontext (Teamgröße, Zweck). Beispiel: "HubSpot täglich genutzt, Pipeline-Pflege und Berichte, keine Administration." Nicht schreiben: "Salesforce-Experte" ohne Beleg.
- Kein Werkzeug ist Voraussetzung für den Einstieg, Konzepte (Pipeline-Phasen, Datenpflege) zählen.

### 6.G DACH-Besonderheiten und Recht

- Mittelstand als Käufer: mehr Wert auf Referenzen, persönliche Betreuung, lokale Ansprechpartner (ANNAHME). Zyklen oft länger durch Geschäftsführerentscheidung und IT-Dienstleister als Mittler.
- Datenschutz und DSGVO: Auftragsverarbeitungsvertrag, Standort der Daten, Drittlandtransfer. Hosting in Deutschland oder der EU ist häufig Kaufkriterium (ANNAHME). Betriebsrat hat bei Systemen zur Leistungs- und Verhaltenskontrolle Mitbestimmung (§ 87 Abs. 1 Nr. 6 BetrVG, Gesetzestext nicht in dieser Recherche gelesen, aus Allgemeinwissen).
- Sie oder Du: Im B2B-Erstkontakt Sie, Du erst nach Angebot. Startups und Tech-Firmen duzen oft intern und im Gespräch (ANNAHME).
- Kaltakquise, UWG § 7 Abs. 2: FAKT (P, Q9 Gesetzestext, S, Q10 IHK): Telefonwerbung gegenüber Gewerbetreibenden braucht mindestens eine mutmaßliche Einwilligung, die nur bei konkretem sachlichem Interesse des Angerufenen an genau dem Angebot besteht. Branchenüblichkeit und allgemeiner Sachbezug genügen nicht (BGH, laut IHK zitiert, nicht im Original geprüft). E-Mail-Werbung verlangt ausdrückliche Einwilligung, Ausnahme Bestandskunden nach § 7 Abs. 3 unter vier Voraussetzungen. Bußgelder und Abmahnrisiko: nicht geprüft. Diese Hinweise sind keine Rechtsberatung.
- Marktdaten: FAKT (S, Q11, Presse über Bitkom): Bitkom erwartet laut Halbjahres-Konjunktur Juli 2026 für den ITK-Markt 246,4 Mrd. Euro (plus 4,1 Prozent). Zahlen zu Software und IT-Markt weichen zwischen Presseberichten ab (Software plus 9,9 Prozent, IT-Markt 170,8 Mrd. Euro laut Folien, nur über Zweitbericht). Januar-Prognose: 245,1 Mrd. Euro (plus 4,4 Prozent). Vor Verwendung die Bitkom-Folien lesen (Q12).
- Partner: Bechtle (rund 5,7 Mrd. Euro DACH-Umsatz laut Ranking), Computacenter, Cancom; Microsoft nennt sie als Bezugsquellen (S, Q13). Ranglisten wechseln jährlich.

### 6.H Erwartungen an Bewerber (ANNAHME, Praxis)

Einsteiger (SDR, Junior, Quereinsteiger):

- Erwartet: Kommunikationsstärke, Belastbarkeit bei Absagen, Lernbereitschaft, Grundverständnis von SaaS, Pipeline, Quote. Belege: Zahlen aus früheren Jobs (Anrufe, Termine, Umsatz), Eigenprojekte.
- Begriffe richtig: ARR, MQL und SQL, Discovery, Qualifizierung.
- Fehler: Buzzwords ohne Erklärung, Kaltakquise als "Spam" schönreden, kein Interesse am Produkt.
- Fragen im Gespräch: Rollenspiel Kaltanruf, "Warum Vertrieb?", "Wie gehen Sie mit Absagen um?".

Erfahrene (AE, Key Account, Enterprise):

- Erwartet: eigene Zahlen (Quotenerreichung, Dealgrößen, Zyklen, Win Rate) mit Kontext, Referenz auf Methode, Beteiligte im Buying Center, Umgang mit Einkauf und Recht.
- Fehler: falsche Kennzahlen (ARR mit Einmalumsatz, NRR als Wachstum der Neukunden), Technik statt Kundennutzen, Pipeline nur als Menge. Erfundene oder nicht prüfbare Zahlen fallen bei Referenzprüfung auf.
- Fragen: "Beschreiben Sie Ihren größten Deal von der ersten Anfrage bis zur Unterschrift", "Wo ging ein Deal verloren und warum?", "Wie bauen Sie einen Forecast?".

### 6.I Gehälter

Datenlage schwach: Keine Primärquelle (StepStone, Gehaltsstudie) erreicht. Alle Zahlen sind Selbstauskunft oder Anbieterdaten aus Blogs und Jobbörsen und streuen stark.

- SDR Deutschland 2026: Median etwa 53.000 Euro OTE, davon 42.000 fix, 11.000 variabel; junior 45.000 bis 55.000 OTE bei Verhältnis 70/30 (Q14, Anbieter-Blog, beruft sich auf Glassdoor und StepStone, S). Jobbörse: 42.000 bis 62.000 OTE (Q15, S).
- Account Executive Mid-Market: etwa 70.000 bis 110.000 OTE; Enterprise 110.000 bis 180.000 OTE; Verhältnis oft 50/50 (Q15, S, Anbieter).
- Account Manager (Bestandskunden): etwa 60.000 bis 100.000 OTE (Q15, S). Key Account Manager: keine belastbare Zahl gefunden.
- IT Account Manager Einstieg: 3.380 Euro brutto im Monat (Q16, Gehaltsrechner, S).
- Hinweis: Fixum und Variable je Firma verschieden, Zielgehalt (OTE) setzt volle Quotenerreichung voraus.

### 6.J Dos und Don'ts

- Do: Kennzahlen mit Kontext und Quelle nennen. Don't: Zahlen runden oder erfinden.
- Do: Kundennutzen in Euro oder Stunden ausdrücken. Don't: Featurelisten vortragen.
- Do: Eine Methode am eigenen Deal zeigen. Don't: Akronyme aufzählen.
- Do: Werkzeugkenntnis mit Nutzungsstufe nennen. Don't: "Experte" ohne Beleg.
- Do: Absagen und verlorene Deals ehrlich analysieren. Don't: Schuld beim Kunden suchen.
- Do: Kaltakquise-Regeln (UWG) kennen. Don't: Massen-E-Mails ohne Einwilligung als Erfolg darstellen.
- Do: Presales einbinden und Grenzen nennen. Don't: Technikwissen vortäuschen.

### 6.K Strittiges und Mythen

- "6 bis 10 Entscheider" (Gartner): oft zitiert, Primärquelle nicht prüfbar, andere Zahlen kursieren (S).
- "17 Prozent der Kaufzeit mit Verkäufer": Gartner-Aussage, kein Nachweis für jeden Markt, stammt aus Umfrage zu komplexen Käufen, Jahr unsicher.
- "Rep-free": 61 Prozent (Gartner 2025) heißt Präferenz, nicht Verhalten. 69 Prozent der Käufer prüfen KI-Ergebnisse trotzdem mit Verkäufern (Gartner via Zweitbericht, Q17, S).
- "Pipeline 3x": Faustregel, richtige Coverage hängt von der Win Rate ab.
- "BANT ist veraltet" oder "MEDDIC ist besser": Anbieter und Trainer verkaufen Methoden, es gibt keine belastbare vergleichende Studie (SCHLUSSFOLGERUNG).
- SaaS-Benchmarks: widersprüchlich je nach Quelle und Definition, meist US-Firmen.
- KI ersetzt SDR: Belegt ist nur, dass Gartner KI-Unterstützung bei Verkäufern mit Wachstum verbindet (2,6-fach, Umfrage unter 227 Vertriebsleitern, Mai 2026, Q18, P-Pressemitteilung via Zweitbericht) und dass Rollen neu gestaltet werden sollen. Zur Zahl der SDR-Stellen fand sich keine belastbare Studie. Behauptung "45 Prozent nutzen hybride KI-SDR-Modelle" (ZoomInfo) ohne genannte Studie, SPEKULATION. Längere Zyklen und mehr Beteiligte: nur Zweitquellen mit unklarer Herkunft, nicht belegt. Anbieterkonsolidierung: nicht recherchiert.

### 6.L Quellenliste

- Q1 https://growthmethod.com/gartner-b2b-buying-journey/ : Zusammenfassung Gartner (17 Prozent, 6 bis 10), S.
- Q2 https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience : 61 Prozent rep-free, P.
- Q3 https://www.digitalcommerce360.com/2026/03/17/gartner-b2b-buyers-rep-free-purchasing-ai-reshapes-sales/amp/ : Bericht über spätere Gartner-Umfrage, S.
- Q4 https://www.thestarrconspiracy.com/insights/benchmarks/b2b-buying-committee-benchmarks-2025 : Buying-Committee-Zahlen mit unklarer Herkunft, S.
- Q5 https://www.gartner.com/en/newsroom/press-releases/2025-05-07-gartner-sales-survey-finds-74-percent-of-b2b-buyer-teams-demonstrate-unhealthy-conflict-during-the-decision-process : Konflikt im Käuferteam, P.
- Q6 https://meddicc.com/resources/who-created-meddic : Herkunft MEDDIC, Anbieterseite, S.
- Q7 https://www.bridgegroupinc.com/research/2025-sdr-models-metrics-report-the-bridge-group : SDR-Report 2025, Zusammenfassung, P-nah.
- Q8 https://info.sapphireventures.com/2025-keybanc-capital-markets-sapphire-ventures-saas-survey : SaaS-Survey 2025, Investorenquelle, Bericht nicht gelesen.
- Q9 https://www.gesetze-im-internet.de/uwg_2004/__7.html : UWG § 7, Gesetz, P (Treffer in Suche, Text nicht gelesen).
- Q10 https://www.ihk.de/rhein-neckar/recht/wettbewerbsrecht/lauterer-wettbewerb/werbung-was-ist-erlaubt-938948 : IHK-Merkblatt Werbung, S.
- Q11 https://www.bitkom.org/Presse/Presseinformation/Digitalbranche-weiterhin-stabil : Bitkom Halbjahresprognose, P (Inhalt nur über Suchzusammenfassung).
- Q12 https://www.bitkom.org/sites/main/files/2026-07/bitkom-praesentation-halbjahres-konjunktur-2026.pdf : Bitkom-Folien, P (nicht gelesen).
- Q13 https://www.channelpartner.de/article/4194220/die-top-25-systemhauser-in-deutschland-2026.html : Systemhaus-Ranking, S.
- Q14 https://skipcall.io/de/blog/sdr-gehalt-deutschland : SDR-Gehalt, Anbieter-Blog, S.
- Q15 https://join.com/de/stellenbeschreibungen/sales-development-representative : Gehaltsspannen Jobbörse, S.
- Q16 https://www.brutto-netto-gehaltsrechner.de/berufe/it-account-manager : Gehaltsrechner, S.
- Q17 https://www.barchart.com/story/news/2038403/gartner-survey-finds-69-of-b2b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights : Gartner-Meldung 69 Prozent, S.
- Q18 https://www.businesswire.com/news/home/20260520536156/en/Gartner-Survey-Finds-Sales-Organizations-That-Provide-AI-Enabled-Next-Best-Actions-Are-2.6x-More-Likely-to-Achieve-Commercial-Growth : Gartner-Pressemitteilung KI und Wachstum, P.

Offene Lücken für eine Nachprüfung: Primärbericht KeyBanc 2025, Bridge-Group-AE-Report, StepStone-Gehaltsreport, Gartner-Primärquelle zur Gruppengröße, Rackham-Datenbasis, BANT-Herkunft, Statistik zu KI und SDR-Stellen.

## 7. Arbeitsweise: drei Brillen und Prüfliste vor jeder Abgabe

### 7.1 Ablauf bei jeder Textaufgabe

1. Fakten klären. Was steht in Vertrag, Zeugnis oder früheren Unterlagen, was hat der Kandidat
   bestätigt? Alles andere ist offen. Offene Punkte kommen als Frage in die Abgabe, die Arbeit
   läuft mit der vorsichtigsten Annahme weiter.
2. Stelle und Firma lesen. Was verkauft die Firma, an wen, in welchem Geschäftsmodell (6.A)?
   Welche Rolle ist gemeint (6.B)? Welche Muss-Kriterien nennt die Anzeige, mit welchen Wörtern?
3. Das stärkste Belegbare bestimmen: ein Ergebnis, eine Zahl oder ein Umfang, der zur Stelle
   passt. Das kommt nach vorn (3.A Nr. 2).
4. Entwurf nach Abschnitt 1 schreiben. Ein Gedanke je Satz, schlichte Verben, konkrete Angaben.
5. Die drei Brillen aufsetzen (7.2).
6. Technisch prüfen (7.4).
7. Abgeben, mit der Liste offener Punkte und mit Etikett bei jeder Einschätzung.

### 7.2 Die drei Brillen

Jeder Satz muss vor allen drei Lesern bestehen. Fällt er bei einem durch, wird er geändert oder
gestrichen.

Kritischer Recruiter (Abschnitt 4)

- Erfasst jemand ohne Lesen von Absätzen Rolle, letzte Station und Zeiträume (4.A)?
- Deckt der Text die Muss-Kriterien der Anzeige, mit deren Begriffen, wo sie wahr sind?
- Gibt es ein Warnsignal: Tippfehler, falscher Firmenname, Widerspruch zu Zeugnis oder LinkedIn,
  größerer Titel als im Vertrag, Floskel (4.C)?
- Ist jede Lücke über einem Quartal benannt oder für das Gespräch vorbereitet (4.E)?
- Kann der Recruiter diesen Kandidaten der Fachabteilung vorlegen, ohne selbst ein Risiko
  einzugehen?

Zahlengetriebener Vertriebsleiter (Abschnitte 5 und 6)

- Wo steht die Zahl? Bei Erfahrenen Zielerreichung, Rang, Dealgröße, Zyklus (5.D). Bei Einsteigern
  Aktivitätszahlen oder ein Ersatzbeleg.
- Liest sich die Bewerbung wie ein guter erster Kontakt: Bezug zur Firma, kurz, mit nächstem
  Schritt (5.E)?
- Stimmen die Fachbegriffe (6.D)? Ein falsch verwendeter Begriff wiegt schwerer als ein fehlender.
- Zeigt der Text Kundennutzen und nicht nur Produktmerkmale (6.E)?
- Hält jede Aussage einer Nachfrage im Gespräch stand?

Entscheidungspsychologie (Abschnitt 3)

- Steht das Stärkste im ersten Satz und im oberen Drittel (3.A Nr. 2 und 3)?
- Senkt der Text das Risiko des Lesers durch prüfbare Angaben, oder behauptet er nur
  (3.A Nr. 5 und 7)?
- Ist der sichtbare Schwachpunkt kurz und sachlich benannt, ohne Entschuldigung (3.D)?
- Liest sich der Text leicht: kurze Sätze, bekannte Wörter (3.A Nr. 6)?
- Stimmt der Ton: weder Bittsteller noch Angeber (3.C)?
- Beruht jede Wirkung auf einer wahren Angabe (3.E)?

### 7.3 Prüfliste je Dokument

Lebenslauf

- Titel wie im Vertrag oder Zeugnis. Zeiträume als MM/JJJJ, das Datum steht beim Eintrag.
- Je Station steht oben der Stichpunkt mit Umfang oder Ergebnis.
- Kurzprofil: Der Bezug zur Zielrolle steht im ersten Satz. Kein Wunschsatz am Ende.
- Begriffe der Anzeige dort, wo sie wahr sind. Kein Keyword-Stuffing.
- Eine Seite bei unter fünf Jahren Erfahrung.

Anschreiben und Bewerbungsmail

- Erster Satz: Anlass bei der Firma oder eigenes Ergebnis (2.B). Nie die Betreffzeile wiederholen.
- Jede Aussage führt auf eine Zeile im Lebenslauf zurück.
- Ein sichtbarer Einwand ist in einem Satz vorweggenommen, wenn er die Einladung gefährdet (3.D).
- Startdatum, Erreichbarkeit und Anlagen stimmen.
- Bei Personalvermittlern: Unterlagen nur nach Rücksprache weitergeben lassen (4.H).

Direkte Ansprache über LinkedIn oder E-Mail

- Unter 400 Zeichen, mit einem Bezug, einem Beleg und einer Frage (2.F).
- Wer im Gespräch über Kaltakquise redet, kennt die Rechtslage (6.G).

Nachfassen

- Einmal nach 5 Werktagen bei Startups und Vermittlern, nach 10 bei Konzernen, mit neuem Inhalt.
  Höchstens ein zweites Mal.

Gesprächsvorbereitung

- Die drei schwierigsten Fragen zum Lebenslauf, je mit einer ehrlichen, kurzen Antwort: Lücke,
  kurze Station, fehlende Erfahrung.
- Zu jeder Zahl im Lebenslauf die Herleitung.
- Ein verlorener Auftrag oder Rückschlag mit eigenem Lernanteil (5.F).
- Gegenfragen: Anteil des Teams am Ziel, Einarbeitungszeit, Gebiet, Fixum und variabler Anteil (5.F).
- Eine Methode am eigenen Fall erklären können. Keine Liste von Akronymen (6.C).

### 7.4 Technische Prüfung vor der Abgabe

- `python3 tools/cvkit/ki_check.py <datei>` meldet 0 Treffer.
- Lesereihenfolge mit pdftotext und pdfminer: Titel, Arbeitgeber, Zeitraum, Stichpunkte.
- Metadaten: Autor ist der Kandidat, Sprache Deutsch.
- Keine KI-Kennzeichnung in der Datei: `grep -a -c -i c2pa <datei.pdf>` ergibt 0 (1.C).
- Links ohne Tracking-Parameter.
- Lebenslauf, Zeugnis, Vertrag und LinkedIn nennen dieselben Titel und Daten.
- Text-PDF unter 2 MB, kein Scan (2.D).

### 7.5 Was nie geht

- Eine Zahl, ein Titel oder ein Werkzeug, das nicht belegt oder bestätigt ist.
- Ein Datum verschieben, um eine Lücke zu schließen.
- Absichtliche Fehler, um menschlicher zu wirken.
- Vorgetäuschte Knappheit, etwa "mir liegen andere Angebote vor", wenn es nicht stimmt.
- Ein Text, der nach KI klingt. Er geht zurück.

## 8. Mythen und Strittiges auf einen Blick

Die Zeilen 1, 2, 3 und 12 wurden zusätzlich zur Recherche einzeln nachgeprüft.

| Nr. | Behauptung | Stand | Etikett | Mehr in |
|---|---|---|---|---|
| 1 | Recruiter lesen einen Lebenslauf 6 Sekunden | TheLadders 2012: laut Sekundärberichten 30 Recruiter, rund 6 Sekunden für die erste Sichtung. 2018: 7,4 Sekunden, Teilnehmerzahl nicht ausgewiesen. US-Anbieterstudie, keine DACH-Messung. Gemessen ist die erste Sichtung, nicht die ganze Prüfung. | FAKT für die Messwerte, ANNAHME für die Übertragung | 4.A |
| 2 | 75 % der Lebensläufe sortiert das ATS aus | Keine Primärquelle. Die Zahl geht laut Sekundärtexten auf eine Vertriebsaussage der Firma Preptel zurück, 2012 oder 2013. | nicht belegt | 2.D |
| 3 | KI-Detektoren erkennen KI-Text zuverlässig | OpenAI hat seinen Klassifikator am 20.07.2023 eingestellt. Er erkannte 26 % der KI-Texte und stufte 9 % der menschlichen Texte falsch ein. Liang et al. 2023: 61,3 % Fehlalarm bei Aufsätzen von Nichtmuttersprachlern. | FAKT | 1.C |
| 4 | Absichtliche Fehler machen einen Text menschlich | Kein Beleg. Saubere Grammatik ist laut Wikipedia kein KI-Merkmal. Hausregel: keine absichtlichen Fehler. | Mythos | 1.B |
| 5 | Burstiness beweist menschliche Herkunft | Schreibhilfe für den Rhythmus, kein Beweis. | Mythos | 1.B |
| 6 | Der Gedankenstrich verrät KI | Nur zusammen mit anderen Merkmalen aussagekräftig, im Deutschen normales Schriftbild. Die Hausregel bleibt als Vorsicht: keine Gedankenstriche in Bewerbungstexten. | ANNAHME | 1.A |
| 7 | Recruiter erkennen KI-Texte sofort | Selbsteinschätzung in Umfragen. Bestraft werden generische, unpersönliche und übertriebene Texte. | SCHLUSSFOLGERUNG | 1.D |
| 8 | Das Anschreiben ist tot | StepStone 2025: 55 % der Firmen verlangen eines, 34 % der Recruiter halten es für entscheidend. | FAKT | 2.E |
| 9 | Zahlen im Lebenslauf erhöhen die Einladungsquote um einen festen Prozentsatz | Plausibel, aber ohne unabhängige Messung. Die kursierenden Prozentwerte stammen aus Anbieter-Blogs. | ANNAHME | 2.C |
| 10 | Eine Lücke ist ab zwei Monaten ein Problem | Ratgeber nennen 2, 3, 6 oder 12 Monate. Eine Norm gibt es nicht. | ANNAHME | 4.E |
| 11 | Lücken immer benennen oder immer offen lassen | Die Quellen widersprechen sich. Hausregel: Lücken werden nicht versteckt. Eine Zeile lohnt, wenn es einen wahren, konkreten Inhalt gibt. "Arbeitssuchend" passt nur, wenn der Kandidat sofort anfangen kann. | SCHLUSSFOLGERUNG | 4.E |
| 12 | Challenger sind 40 % der Spitzenverkäufer | CEB-Erhebung mit über 6.000 Verkäufern in rund 90 Firmen: Challenger 39 % der Top-Performer, Relationship Builder 7 %. Selbst- und Vorgesetztenurteile, Anbieterstudie. Die oft genannten 54 % für komplexe Verkäufe sind nur über Zweitquellen belegt. | FAKT mit Einschränkung | 5.B |
| 13 | Verkäufer sind Hunter oder Farmer | Sprachgebrauch ohne gefundene empirische Prüfung. Die beiden Aufgaben, Neugeschäft und Bestand, sind real. | ANNAHME | 5.C |
| 14 | Eine Fehlbesetzung im Vertrieb kostet mehrere Jahresgehälter | Zahlen aus Anbieterblogs, keine Primärstudie. | ANNAHME | 5.A |
| 15 | Grit sagt Verkaufserfolg voraus | Metaanalyse von 2017: schwacher Zusammenhang, starke Überlappung mit Gewissenhaftigkeit. | FAKT über Sekundärquelle | 5.B |
| 16 | Die Pipeline muss dreifach gedeckt sein | Faustregel. Die nötige Deckung hängt an der Abschlussquote. | ANNAHME | 6.D |
| 17 | Im Buying Center sitzen 6 bis 10 Entscheider | Gartner zugeschrieben, nur über Zweitquellen belegt. | FAKT über Sekundärquelle | 6.A |
| 18 | Käufer wollen keinen Verkäufer mehr | Gartner 2025: 61 % bevorzugen einen Kauf ohne Verkäufer. Das ist eine Vorliebe, kein Verhalten. | FAKT | 6.A |
| 19 | Verlustaversion steuert Recruiter | Im Kern gut belegt, für die Personalauswahl ohne eigenen Beleg. | SCHLUSSFOLGERUNG | 3.A |
| 20 | Leicht Lesbares wirkt wahrer | Der Effekt ist klein, eine Replikation von 2025 fand keinen. Kurze Sätze bleiben wegen der kurzen Sichtungszeit trotzdem richtig. | umstritten | 3.E |

### Offene Punkte für eine Nachprüfung

Diese Originale wurden nicht gelesen und sollten vor einer Verwendung als Beleg geprüft werden:

- TheLadders-Studie von 2018 (Teilnehmerzahl, Blickbereiche)
- KeyBanc/Sapphire SaaS Survey 2025 und Bridge Group AE-Report (Benchmarks)
- StepStone Gehaltsreport und weitere Gehaltsstudien für den deutschen IT-Vertrieb
- Gartner-Primärquelle zur Größe des Buying Centers
- Bitkom-Folien zur Halbjahres-Konjunktur 2026
- BAG-Urteil zu Widerrufsvorbehalten bei variabler Vergütung
- Anwendungsdatum der Hochrisiko-Pflichten der KI-Verordnung
- Marktanteile der Bewerbermanagement-Systeme im DACH-Raum
- Eine belastbare deutsche Liste typischer KI-Wendungen
