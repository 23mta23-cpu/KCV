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
