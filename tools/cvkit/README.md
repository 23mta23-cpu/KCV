# cvkit: moderner Lebenslauf und Anschreiben aus einer Datendatei

Erzeugt aus einer JSON-Datei drei aufeinander abgestimmte Dokumente:

| Datei | Wofür |
|---|---|
| `<Name>_Lebenslauf_Design.pdf` | Zweispaltig mit Foto, Seitenleiste und Zeitleiste. Für E-Mail-Bewerbungen und Ansprechpartner. |
| `<Name>_Lebenslauf_ATS.pdf` | Einspaltig im gleichen Look. Für Online-Portale, weil Bewerbermanagement-Systeme (ATS) sie in der richtigen Reihenfolge lesen. |
| `Anschreiben_*.pdf` | Anschreiben mit gleichem Kopf, gleichen Farben und Schriften. |

Vorschau mit Musterdaten: `examples/vorschau_design-1.png`, `examples/vorschau_ats-1.png`, `examples/vorschau_anschreiben-1.png`.

## Benutzung

```sh
# 1. Schriften holen (SIL Open Font License)
mkdir -p fonts && cd fonts
npm pack @fontsource/montserrat@5.2.8 @fontsource/lato@5.2.7
for t in *.tgz; do tar -xzf "$t" && cp package/files/{montserrat-latin-{500,600,700,800},lato-latin-{400,700}}-normal.woff2 package/files/lato-latin-400-italic.woff2 . 2>/dev/null; rm -rf package; done
cd ..

# 2. HTML erzeugen (Daten + optional Anschreiben)
python3 build.py examples/muster_daten.json out examples/muster_anschreiben.json

# 3. PDFs rendern (Playwright + Chromium)
CVKIT_PLAYWRIGHT=/pfad/zu/@playwright/test/index.mjs CVKIT_CHROMIUM=/pfad/zu/chrome \
  node render.mjs out/Max_Mustermann_Lebenslauf_Design.html out/Max_Mustermann_Lebenslauf_Design.pdf

# 4. Metadaten setzen (Titel, Autor) und komprimieren
python3 finalize.py out/Max_Mustermann_Lebenslauf_Design.pdf "Lebenslauf Max Mustermann" "Max Mustermann"
```

`photo` in der Datendatei ist optional. Ohne Foto erscheint ein Kreis mit Initialen.

**Grußformel im Anschreiben:** Das Feld `closing` ist optional (Standard: „Mit freundlichen Grüßen“). Für Startups, die in der Anzeige duzen, passt `"closing": "Viele Grüße"`.

## Klingt es nach Mensch? `ki_check.py`

```sh
python3 ki_check.py examples/muster_daten.json examples/muster_anschreiben.json   # oder fertige PDFs
```

Das Skript meldet typische Merkmale von KI-Texten. Grundlage sind [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) und Artikel von t3n und all-ai.de. Vor dem Versand sollte es 0 Treffer geben. Die Merkmale sind Hinweise, kein Beweis. Ein Text ohne Treffer braucht trotzdem einen Menschen, der ihn liest.

- Keine Gedankenstriche (– oder —), auch nicht in Betreffzeilen. Zeiträume mit Bindestrich: `07/2023 - 12/2025`.
- Keine Aufzählungen mit fettem Stichwort am Anfang. Wikipedia nennt sie „inline-header lists“. `**…**` funktioniert technisch noch, sollte aber nicht verwendet werden.
- Keine Dreier-Aufzählungen als Stilmittel, kein „nicht nur … sondern“, kein „nicht X, sondern Y“.
- Keine Zusammenfassungssätze („Ich weiß also …“) und kein verstärkendes „Genau …“.
- Kein Lehrsatz am Absatzende („Dabei habe ich gelernt, wie viel …“), keine Gleichsetzung mit „statt“.
- Nicht mit der nacherzählten Anzeige beginnen und sie kurz bestätigen („Diesen Weg suche ich.“).
- Höchstens ein Doppelpunkt im Fließtext eines Anschreibens.
- Selbstlob („lerne schnell“) nur einmal und mit Beleg.
- Keine gestelzten Verben („fungiert als“, „ermöglicht“, „stellt dar“), lieber ist, war, hat.

Zusätzlich zeigt das Skript **Mensch-Signale** als Hinweis, nicht als Treffer: die Streuung der Satzlängen und die Zahl konkreter Zahlen im Brief. Wikipedia nennt im Abschnitt „Signs of human writing“ schlichte Verben und konkrete, ungewöhnliche Details als typisch menschlich. Die Satzlängen-Streuung („burstiness“) ist dagegen ein schwaches Signal, das Detektoren nutzen, aber nicht zuverlässig ist. Absichtliche Fehler bringen nichts: Saubere Grammatik gilt laut Wikipedia nicht als KI-Merkmal.

## Regeln, die aus Tests stammen

- **Laufweite höchstens `.045em`.** Bei breiter Laufweite (z. B. `.17em`) liest pdfminer, die Grundlage vieler ATS-Parser, Überschriften als „B E R U F S E R F A H R U N G“. Das ATS erkennt dann den Abschnitt nicht.
- **Datum nicht rechtsbündig per Tabstopp.** Parser trennen es sonst vom Jobtitel. Hier steht es in der Zeile „Firma | Zeitraum“.
- **Zweispaltige Layouts werden blockweise gemischt gelesen.** Deshalb gibt es die ATS-Variante für Portale.
- **Prüfen vor dem Versand:** `python3 -c "from pdfminer.high_level import extract_text; print(extract_text('datei.pdf'))"` muss die Abschnitte in sinnvoller Reihenfolge zeigen.

## Datenschutz

Echte Bewerberdaten gehören nicht in dieses öffentliche Repository. Datendateien, Fotos und fertige PDFs bleiben im privaten Speicher, z. B. Google Drive.
