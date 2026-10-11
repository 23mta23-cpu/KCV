"""Findet typische Merkmale von KI-Texten in Bewerbungsunterlagen.

Grundlage: Wikipedia "Signs of AI writing", t3n und all-ai.de (Stand 2026). Die Merkmale sind
Hinweise, kein Beweis. Ziel ist ein Text, der nach einem Menschen klingt und für ATS sauber bleibt.

Usage: python3 ki_check.py <datei.json|datei.txt|datei.pdf> [...]
JSON: cvkit-Daten (profile/experience/education) oder Anschreiben ({"letters": {...}}).
"""
import json
import re
import sys

RULES = [
    ("Gedankenstrich (– oder —)", r"[–—]"),
    ("Pfeil", r"[→⇒]"),
    ("Fettdruck-Markierung", r"\*\*"),
    ("'nicht nur ... sondern'", r"\bnicht nur\b[^.]*\bsondern\b"),
    ("korrektive Formel 'nicht X, sondern Y'", r"\bnicht\b[^.,]{1,40},\s*sondern\b"),
    ("'Genau ...' als Verstärker", r"(^|[.!?]\s+|,\s*)[Gg]enau (so|das|da|diese[nmrs]?|der|die|den)\b"),
    ("Zusammenfassung 'Ich weiß also'", r"\b[Ii]ch weiß (also|daher|deshalb)\b"),
    ("Floskel 'ein wichtiger Grund'", r"\bein wichtiger Grund\b"),
    ("Grußformel 'Hallo liebe(s)'", r"\bHallo lieb"),
    ("Werbewort", r"\b(begeister\w*|spannend\w*|Leidenschaft\w*|leidenschaftlich\w*|Herausforderung\w*|innovativ\w*|dynamisch\w*|maßgeschneidert\w*|ganzheitlich\w*|Mehrwert\w*|nahtlos\w*|facettenreich\w*|Synergie\w*|auf Augenhöhe|hiermit bewerbe|mit großem Interesse|darüber hinaus|des Weiteren|abschließend|zusammenfassend|kurz gesagt)\b"),
    ("Lehrsatz am Absatzende", r"\b[Dd]abei habe ich (gelernt|gesehen|erlebt)\b"),
    ("Gleichsetzung mit 'statt'", r"\bstatt\b"),
    ("Kurzbestätigung nach Anzeigen-Zitat", r"(^|[.!?]\s+)(Diesen Weg (suche|möchte|will)|Das trifft auf mich zu|So will ich arbeiten|Ich bin einer)\b"),
    ("gestelztes Verb statt ist/hat", r"\b(ermöglich\w*|gewährleist\w*|fungier\w*|stellt\s+\w+\s+dar|dient als|zeichne[nt]? sich|unterstreich\w*|verdeutlich\w*)\b"),
    ("Selbstlob ohne Beleg", r"\b(lerne schnell|arbeite mich schnell ein|teamfähig|belastbar|zielstrebig|kommunikationsstark)\b"),
]


def texts(path):
    if path.endswith(".pdf"):
        from pdfminer.high_level import extract_text
        yield path, extract_text(path), "text"
        return
    raw = open(path, encoding="utf-8").read()
    if not path.endswith(".json"):
        yield path, raw, "text"
        return
    data = json.loads(raw)
    if "letters" in data:
        for key, letter in data["letters"].items():
            parts = [letter.get("subject", ""), letter.get("greeting", "")] + letter["body"]
            yield key, "\n".join(parts), "brief"
        return
    parts = [data.get("title", ""), data.get("target", ""), data.get("profile", "")]
    for section in ("experience", "education"):
        for item in data.get(section, []):
            parts += [item.get("role", ""), item.get("org", ""), item.get("dates", "")] + item.get("bullets", [])
    parts += data.get("skills", [])
    yield path, "\n".join(parts), "cv"


def check(name, text, kind="brief"):
    findings = []
    for label, pattern in RULES:
        for m in re.finditer(pattern, text, re.I | re.M):
            start = max(0, m.start() - 40)
            findings.append((label, text[start:m.end() + 40].replace("\n", " ")))
    colons = sum(1 for line in text.split("\n")[2:] for _ in re.finditer(r":\s+[A-ZÄÖÜa-zäöü]", line))
    if colons > 1 and kind == "brief":
        findings.append(("viele Doppelpunkte", f"{colons} Doppelpunkte im Fließtext"))
    triads = re.findall(r"\b\w+, \w+(?: \w+)? und \w+", text)
    if len(triads) > 2:
        findings.append(("viele Dreier-Aufzählungen", f"{len(triads)}x, z. B. '{triads[0]}'"))
    return findings


def signals(text):
    """Positive Merkmale menschlicher Texte. Nur Hinweise, sie zaehlen nicht als Treffer.

    Wikipedia ("Signs of human writing"): schlichte Verben wie ist/hat, konkrete und ungewoehnliche
    Details. Satzrhythmus ("burstiness") ist ein schwaches Signal, aber billig zu pruefen.
    """
    body = "\n".join(text.split("\n")[2:]) if text.count("\n") > 2 else text
    lengths = [len(s.split()) for s in re.split(r"(?<=[.!?])\s+", body.strip()) if len(s.split()) > 1]
    if len(lengths) < 4:
        return None
    mean = sum(lengths) / len(lengths)
    spread = (sum((n - mean) ** 2 for n in lengths) / len(lengths)) ** 0.5 / mean
    numbers = len(re.findall(r"(?<![\w°])\d+(?:[.,]\d+)?(?![\d°])", body))
    tips = []
    if spread < 0.3:
        tips.append("Rhythmus eher gleichfoermig, einen sehr kurzen oder einen langen Satz einbauen")
    if numbers == 0:
        tips.append("keine Zahl, ein konkretes Detail ergaenzen, das nur der Kandidat kennt")
    line = f"Satzlaengen {min(lengths)} bis {max(lengths)} Woerter, Streuung {spread:.2f}, Zahlen {numbers}"
    return line + (" | Tipp: " + "; ".join(tips) if tips else "")


def main():
    total = 0
    for path in sys.argv[1:]:
        for name, text, kind in texts(path):
            found = check(name, text, kind)
            total += len(found)
            print(f"{name}: {'ok' if not found else str(len(found)) + ' Treffer'}")
            for label, snippet in found:
                print(f"   - {label}: ...{snippet}...")
            info = signals(text) if kind != "cv" else None
            if info:
                print(f"   Mensch-Signale: {info}")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
