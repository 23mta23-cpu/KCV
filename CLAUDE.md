# KCV: öffentliches Repo

Dieses Repository ist öffentlich. Hier liegen nur Werkzeuge und Regeln, keine Daten realer Personen.

- Nicht ins Repo: Namen, Kontaktdaten, Anschriften, Geburtsdaten, Fotos, Lebensläufe, Anschreiben,
  Zeugnisse, Gehälter oder Bewerbungsstände realer Kandidaten. Das gilt auch für Commit-Nachrichten,
  Issues, Pull Requests und Fallbeschreibungen, aus denen eine Person erkennbar ist.
- Sensible Dokumente gehören ausschließlich ins Google Drive des Nutzers. Arbeitsdateien bleiben im
  Scratchpad der Sitzung.
- Beispiele nur mit erfundenen Daten: Max Mustermann, Musterstadt, example.com, +49 170 0000000.
- `scripts/pii_check.py` läuft als Hook vor jedem `git commit`, `git push` und GitHub-Schreibzugriff.
  Nicht umgehen und nicht abschalten. Meldet er einen Treffer, die Daten aus dem Repo entfernen,
  nicht die Regel lockern. Manuell prüfen: `python3 scripts/pii_check.py --all`.

## Bewerbungstexte: verbindliche Arbeitsgrundlage

Für jede Aufgabe an Lebenslauf, Anschreiben, Bewerbungsmail, Outreach oder Gesprächsvorbereitung
gilt `SALES_RECRUITING_PLAYBOOK.md`. Vor dem Schreiben die passenden Abschnitte lesen, vor der
Abgabe die Prüfliste in Abschnitt 7 abarbeiten.

- Menschlich schreiben, keine KI-Floskeln (Abschnitt 1). Jeder Text läuft durch
  `tools/cvkit/ki_check.py`, Ziel: 0 Treffer.
- Jeden Satz aus drei Blickwinkeln prüfen: kritischer Recruiter (Abschnitt 4), zahlengetriebener
  Vertriebsleiter im IT-Vertrieb (Abschnitte 5 und 6), Entscheidungspsychologie (Abschnitt 3).
- Rangfolge: Die fünf Regeln aus
  `paperclip/recruiting-agentur/package/agents/head-of-recruiting/AGENTS.md` gehen vor. Keine
  erfundenen Fakten, Jobtitel laut Vertrag oder Zeugnis, Lücken nicht verstecken. Wirkung entsteht
  nur aus wahren, belegbaren Angaben.
- Einschätzungen kennzeichnen: FAKT, SCHLUSSFOLGERUNG, ANNAHME, SPEKULATION.
