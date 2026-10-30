#!/usr/bin/env python3
"""Sperre gegen personenbezogene Daten in diesem öffentlichen Repo.

Läuft als Claude-Code-Hook (.claude/settings.json) vor `git commit`, `git push` und
GitHub-Schreibzugriffen. Findet er Kontaktdaten, Geburtsdaten, IBAN, Anschriften oder
Dokumentdateien (PDF, Word, Fotos), blockiert er mit Exit 2.
Manuell: python3 scripts/pii_check.py --all
"""
import json
import re
import subprocess
import sys

PATTERNS = {
    "E-Mail-Adresse": re.compile(r"[\w.%+-]+@[\w-]+(?:\.[\w-]+)*\.[a-z]{2,}", re.I),
    "Telefonnummer": re.compile(r"(?<![\d.,])(?:\+49|0049|\b0)[\s/-]?\(?\d{2,5}\)?[\s/-]?\d[\d\s/-]{4,}\d"),
    "Geburtsdatum": re.compile(r"(?:geboren am|geb\. am|geburtsdatum)\W{0,3}\d{1,2}\.\d{1,2}\.\d{4}", re.I),
    "IBAN": re.compile(r"\b[A-Z]{2}\d{2}(?:\s?\d{4}){4}\s?\d{2}\b"),
    "Anschrift": re.compile(r"\w+(?:straße|str\.|weg|gasse|allee|platz)\s*\d+\w?,?\s+\d{5}\b", re.I),
}
# Erfundene Beispieldaten und technische Absender sind erlaubt.
ALLOWED = re.compile(r"example\.(?:com|org|de)|noreply|muster|0000000", re.I)
DOC_FILES = re.compile(r"\.(?:pdf|docx?|odt|jpe?g|heic)$", re.I)


def scan_text(text, where):
    hits = []
    for no, line in enumerate(text.splitlines(), 1):
        if "muster" in line.lower():
            continue
        for kind, rx in PATTERNS.items():
            for m in rx.finditer(line):
                if not ALLOWED.search(m.group()):
                    hits.append(f"{where}:{no}: {kind}")
    return hits


def scan_repo():
    # Alles, was committet werden könnte: getrackt oder neu und nicht ignoriert.
    files = subprocess.run(["git", "ls-files", "-co", "--exclude-standard"],
                           capture_output=True, text=True, check=True).stdout.splitlines()
    hits = []
    for f in files:
        if DOC_FILES.search(f):
            hits.append(f"{f}: Dokument- oder Fotodatei")
            continue
        try:
            data = open(f, "rb").read()
        except OSError:
            continue
        if b"\0" not in data:
            hits += scan_text(data.decode("utf-8", "replace"), f)
    return hits


def main():
    if "--all" in sys.argv:
        hits = scan_repo()
    else:
        event = json.load(sys.stdin)
        tool, inp = event.get("tool_name", ""), event.get("tool_input", {})
        if tool == "Bash":
            if not re.search(r"\bgit\b.*\b(?:commit|push)\b", inp.get("command", "")):
                return 0
            hits = scan_repo()
        elif tool.startswith("mcp__github__"):
            hits = scan_text(json.dumps(inp, ensure_ascii=False), tool)
        else:
            return 0
    if not hits:
        return 0
    print("Blockiert: personenbezogene Daten gehören nicht in dieses öffentliche Repo, "
          "sondern ins Google Drive des Nutzers (siehe CLAUDE.md).", file=sys.stderr)
    print("\n".join(hits[:30]), file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
