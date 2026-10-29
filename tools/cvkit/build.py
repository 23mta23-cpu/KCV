"""Builds a modern CV (design + ATS variant) and matching cover letters as HTML.

Usage: python3 build.py <data.json> <out_dir> [letters.json]
Renders nothing itself; pass the produced HTML files to render.mjs.
"""
import base64
import html
import json
import mimetypes
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.environ.get("CVKIT_FONTS", os.path.join(HERE, "fonts"))

NAVY = "#16365C"
ACCENT = "#1E95D4"
INK = "#1E2733"
MUTED = "#46525F"
SIDE_BG = "#EEF3F8"
LINE = "#C9D6E4"

ICONS = {
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 7l-10 6L2 7"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/>',
    "linkedin": '<rect x="2" y="2" width="20" height="20" rx="3"/><path d="M8 11v6M8 7.5v.01M12 17v-6M12 13.5a2.5 2.5 0 0 1 5 0V17"/>',
    "car": '<path d="M5 16h14v-4l-2-5H7l-2 5v4z"/><path d="M5 12h14"/><circle cx="8" cy="17.5" r="1.6"/><circle cx="16" cy="17.5" r="1.6"/>',
    "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
    "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/>',
    "cap": '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
    "grid": '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
}


def icon(name, size="100%"):
    return (f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def e(text):
    return html.escape(text, quote=True)


def rich(text):
    """Escape text; **fett** wird zu <b>fett</b> (für Stichwort-Einstiege in Aufzählungen)."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(text))


def data_uri(path):
    mime = mimetypes.guess_type(path)[0] or "application/octet-stream"
    with open(path, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode()


def font_faces():
    faces = [
        ("Montserrat", 500, "normal", "montserrat-latin-500-normal.woff2"),
        ("Montserrat", 600, "normal", "montserrat-latin-600-normal.woff2"),
        ("Montserrat", 700, "normal", "montserrat-latin-700-normal.woff2"),
        ("Montserrat", 800, "normal", "montserrat-latin-800-normal.woff2"),
        ("Lato", 400, "normal", "lato-latin-400-normal.woff2"),
        ("Lato", 700, "normal", "lato-latin-700-normal.woff2"),
        ("Lato", 400, "italic", "lato-latin-400-italic.woff2"),
    ]
    out = []
    for fam, weight, style, file in faces:
        src = "file://" + os.path.join(FONT_DIR, file)
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{weight};font-style:{style};"
                   f"src:url('{src}') format('woff2');}}")
    return "\n".join(out)


BASE_CSS = f"""
{font_faces()}
@page {{ size: A4; margin: 0; }}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ -webkit-font-smoothing: antialiased; }}
body {{ font-family: 'Lato', sans-serif; color: {INK}; font-size: 9.4pt; line-height: 1.42; }}
.page {{ position: relative; width: 210mm; height: 297mm; overflow: hidden; background: #fff; }}
h1, h2, h3 {{ font-family: 'Montserrat', sans-serif; text-wrap: balance; }}
p, li {{ text-wrap: pretty; }}
a {{ color: inherit; text-decoration: none; }}
.dates {{ font-variant-numeric: tabular-nums; }}
"""


# ---------------------------------------------------------------- Design-Variante
def entries_html(items):
    out = []
    for it in items:
        meta = " · ".join(x for x in [e(it["org"]) if it["org"] else "", ] if x)
        bullets = "".join(f"<li>{rich(b)}</li>" for b in it["bullets"])
        out.append(
            f'<div class="entry"><span class="dot"></span>'
            f'<div class="entry-head"><h3>{e(it["role"])}</h3>'
            f'<span class="dates">{e(it["dates"])}</span></div>'
            + (f'<div class="org">{meta}</div>' if meta else "")
            + (f"<ul>{bullets}</ul>" if bullets else "")
            + "</div>")
    return "".join(out)


def section(icon_name, title, body):
    return (f'<section><div class="sec-head"><span class="sec-icon">{icon(icon_name, "4.2mm")}</span>'
            f'<h2>{e(title)}</h2></div>{body}</section>')


def side_block(title, body):
    return f'<div class="side-block"><h2>{e(title)}</h2>{body}</div>'


def photo_html(d):
    """Rundes Foto; ohne Foto ein Kreis mit Initialen im gleichen Stil."""
    if d.get("photo") and os.path.exists(d["photo"]):
        return f'<img class="photo" src="{data_uri(d["photo"])}" alt="Foto {e(d["name"])}">'
    initials = "".join(p[0] for p in d["name"].split()[:2]).upper()
    return (f'<div class="photo" style="display:flex;align-items:center;justify-content:center;background:{ACCENT};'
            f'color:#fff;font-family:Montserrat;font-weight:800;font-size:30pt">{e(initials)}</div>')


def link_text(text):
    """Profil-URLs nur nach "/in/" umbrechen, nie am Bindestrich (sonst liest pdftotext "max-mustermann123" ohne Bindestrich)."""
    t = e(text)
    if "/in/" in t:
        head, tail = t.split("/in/", 1)
        return f'{head}/in/<wbr><span class="nw">{tail}</span>'
    return t


def design_html(d):
    contact = "".join(
        f'<li><span class="ci">{icon(c["icon"], "3.6mm")}</span>'
        + (f'<a href="{e(c["href"])}">{link_text(c["text"])}</a>' if c.get("href") else f'<span>{e(c["text"])}</span>')
        + "</li>" for c in d["contact"])
    chips = "".join(f'<span class="chip">{e(s)}</span>' for s in d["skills"])
    it = "".join(f"<li>{e(x)}</li>" for x in d["it"])
    langs = "".join(f'<li><b>{e(l["name"])}</b><span>{e(l["level"])}</span></li>' for l in d["languages"])
    industry = "".join(f'<span class="chip soft">{e(s)}</span>' for s in d["industry"])
    css = BASE_CSS + f"""
.band {{ position: absolute; inset: 0 0 auto 0; height: 50mm; background: {NAVY}; z-index: 2; }}
.band::after {{ content: ''; position: absolute; left: 68mm; right: 0; bottom: 0; height: 1.1mm; background: {ACCENT}; }}
.side {{ position: absolute; top: 0; left: 0; width: 68mm; height: 297mm; background: {SIDE_BG}; z-index: 1; }}
.photo {{ position: absolute; z-index: 3; left: 11mm; top: 8mm; width: 46mm; height: 46mm; border-radius: 50%;
         border: 1.6mm solid #fff; object-fit: cover; box-shadow: 0 1.2mm 3mm rgba(10,30,60,.18); }}
.namebox {{ position: absolute; z-index: 3; left: 76mm; right: 12mm; top: 12.5mm; color: #fff; }}
.namebox h1 {{ font-size: 29pt; font-weight: 800; letter-spacing: .045em; text-transform: uppercase; line-height: 1.05; }}
.namebox .title {{ margin-top: 2.6mm; font-family: 'Montserrat'; font-weight: 600; font-size: 9.6pt; letter-spacing: .045em;
                   text-transform: uppercase; color: #BFDDF6; }}
.namebox .target {{ margin-top: 2.2mm; font-size: 9pt; color: #E4EFF9; }}
.side-content {{ position: absolute; z-index: 3; top: 62mm; left: 8mm; width: 52mm; }}
.side-block {{ margin-bottom: 6.2mm; }}
.side-block h2 {{ font-size: 9.6pt; font-weight: 700; letter-spacing: .045em; text-transform: uppercase; color: {NAVY};
                  padding-bottom: 1.6mm; margin-bottom: 1.8mm; border-bottom: .45mm solid {NAVY}; }}
/* Eng an den Inhalt: sonst bildet pdfminer eigene Textboxen und mischt Seitenleiste und Jobs. */
.contact {{ list-style: none; }}
.nw {{ white-space: nowrap; }}
.contact li {{ display: flex; align-items: center; gap: 2.2mm; font-size: 8.1pt; margin-bottom: 2.1mm; word-break: break-word; }}
.contact .ci {{ flex: none; width: 6mm; height: 6mm; border-radius: 50%; background: {NAVY}; color: #fff;
               display: inline-flex; align-items: center; justify-content: center; }}
.chip {{ display: inline-block; background: #fff; border: .25mm solid {LINE}; border-radius: 3mm; padding: .6mm 2.1mm;
         margin: 0 1.1mm 1.4mm 0; font-size: 8pt; line-height: 1.3; color: {INK}; }}
.chip.soft {{ background: transparent; }}
.plain {{ list-style: none; font-size: 8.5pt; }}
.plain li {{ padding-left: 3mm; position: relative; margin-bottom: 1.2mm; }}
.plain li::before {{ content: ''; position: absolute; left: 0; top: 1.9mm; width: 1.3mm; height: 1.3mm; border-radius: 50%; background: {ACCENT}; }}
.langs {{ list-style: none; font-size: 8.5pt; }}
.langs li {{ display: flex; justify-content: space-between; gap: 2mm; padding: 1.1mm 0; border-bottom: .2mm dashed {LINE}; }}
.langs li:last-child {{ border-bottom: 0; }}
.langs span {{ color: {MUTED}; }}
.main {{ position: absolute; z-index: 3; top: 58mm; left: 76mm; width: 122mm; }}
.main::before {{ content: ''; position: absolute; left: 3.6mm; top: 8mm; bottom: 4mm; width: .45mm; background: {LINE}; }}
section {{ position: relative; margin-bottom: 6.6mm; }}
.sec-head {{ display: flex; align-items: center; gap: 3.2mm; margin-bottom: 3mm; }}
.sec-icon {{ flex: none; width: 7.6mm; height: 7.6mm; border-radius: 50%; background: {NAVY}; color: #fff;
            display: inline-flex; align-items: center; justify-content: center; position: relative; z-index: 2; }}
.sec-head h2 {{ flex: 1; font-size: 11.2pt; font-weight: 700; letter-spacing: .045em; text-transform: uppercase;
               color: {ACCENT}; padding-bottom: 1.3mm; border-bottom: .45mm solid {NAVY}; }}
.lead {{ padding-left: 10.8mm; font-size: 9.9pt; line-height: 1.5; color: {INK}; }}
.entry {{ position: relative; padding-left: 10.8mm; margin-bottom: 4.2mm; }}
.entry .dot {{ position: absolute; left: 2.35mm; top: 1.2mm; width: 2.9mm; height: 2.9mm; border-radius: 50%;
              background: #fff; border: .55mm solid {ACCENT}; }}
.entry-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 4mm; }}
.entry h3 {{ font-family: 'Lato'; font-size: 10.8pt; font-weight: 700; color: {NAVY}; }}
.entry .dates {{ flex: none; font-size: 8.8pt; font-weight: 700; color: {ACCENT}; }}
.entry .org {{ font-size: 9.4pt; color: {MUTED}; margin-top: .3mm; }}
.entry ul {{ margin-top: 1.4mm; list-style: none; }}
.entry li b {{ color: {NAVY}; font-weight: 700; }}
.entry li {{ position: relative; padding-left: 3.4mm; margin-bottom: 1.1mm; font-size: 9.6pt; line-height: 1.45; }}
.entry li::before {{ content: ''; position: absolute; left: 0; top: 1.85mm; width: 1.4mm; height: 1.4mm; border-radius: 50%; background: {ACCENT}; }}
"""
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{e(d['meta']['title'])}</title>
<style>{css}</style></head><body><div class="page">
<div class="band"></div><div class="side"></div>
{photo_html(d)}
<header class="namebox"><h1>{e(d['name'])}</h1><div class="title">{e(d['title'])}</div><div class="target">{e(d['target'])}</div></header>
<aside class="side-content">
{side_block('Kontakt', f'<ul class="contact">{contact}</ul>')}
{side_block('Kompetenzen', chips)}
{side_block('IT-Kenntnisse', f'<ul class="plain">{it}</ul>')}
{side_block('Sprachen', f'<ul class="langs">{langs}</ul>')}
{side_block('Branche', industry)}
</aside>
<main class="main">
{section('user', 'Profil', f'<p class="lead">{e(d["profile"])}</p>')}
{section('briefcase', 'Berufserfahrung', entries_html(d['experience']))}
{section('cap', 'Ausbildung', entries_html(d['education']))}
</main>
</div></body></html>"""


# ---------------------------------------------------------------- ATS-Variante
def ats_entries(items):
    out = []
    for it in items:
        meta = "  |  ".join(x for x in [e(it["org"]), f'<span class="d">{e(it["dates"])}</span>' if it["dates"] else ""] if x)
        bullets = "".join(f"<li>{rich(b)}</li>" for b in it["bullets"])
        out.append(f'<div class="a-entry"><h3>{e(it["role"])}</h3><div class="a-meta dates">{meta}</div>'
                   + (f"<ul>{bullets}</ul>" if bullets else "") + "</div>")
    return "".join(out)


def ats_section(icon_name, title, body):
    """Wie im Design: Icon-Kreis, Ueberschrift, Zeitleiste. Alles einspaltig, Lesereihenfolge bleibt linear."""
    return (f'<section><div class="a-head"><span class="a-icon">{icon(icon_name, "3.9mm")}</span>'
            f'<h2>{e(title)}</h2></div><div class="a-list">{body}</div></section>')


def ats_photo(d):
    """Foto oben rechts im Kopf. Ein Bild hat keinen Text, die Lesereihenfolge fuer ATS bleibt gleich."""
    if d.get("photo") and os.path.exists(d["photo"]):
        return f'<img class="a-photo" src="{data_uri(d["photo"])}" alt="Foto {e(d["name"])}">'
    return ""


def ats_html(d):
    contact = "  |  ".join(e(c["text"]) for c in d["contact"][:3]) + "<br>" + "  |  ".join(e(c["text"]) for c in d["contact"][3:])
    css = BASE_CSS + f"""
.a-band {{ position: relative; background: {NAVY}; color: #fff; padding: 11mm 16mm 7mm; border-bottom: 1.1mm solid {ACCENT}; }}
.a-band.has-photo {{ padding-right: 54mm; }}
.a-photo {{ position: absolute; right: 16mm; top: 7mm; width: 32mm; height: 32mm; border-radius: 50%;
           object-fit: cover; border: .9mm solid #fff; background: #fff; }}
.a-band h1 {{ font-size: 25pt; font-weight: 800; letter-spacing: .045em; text-transform: uppercase; }}
.a-band .title {{ margin-top: 1.6mm; font-family: 'Montserrat'; font-weight: 600; font-size: 9.6pt; letter-spacing: .045em; text-transform: uppercase; color: #BFDDF6; }}
.a-band .target {{ margin-top: 1.4mm; font-size: 9pt; color: #E4EFF9; }}
.a-band .contact {{ margin-top: 3mm; font-size: 8.6pt; color: #fff; }}
.a-body {{ padding: 6mm 16mm 0; }}
.a-body section {{ margin-bottom: 5.4mm; }}
.a-head {{ display: flex; align-items: center; gap: 3mm; margin-bottom: 2.6mm; }}
.a-icon {{ flex: none; width: 7mm; height: 7mm; border-radius: 50%; background: {NAVY}; color: #fff;
          display: inline-flex; align-items: center; justify-content: center; }}
.a-body h2 {{ flex: 1; font-size: 10.8pt; font-weight: 700; letter-spacing: .045em; text-transform: uppercase; color: {ACCENT};
             padding-bottom: 1.2mm; border-bottom: .4mm solid {NAVY}; }}
.a-list {{ position: relative; padding-left: 10mm; }}
.a-list::before {{ content: ''; position: absolute; left: 3.3mm; top: .5mm; bottom: 1mm; width: .45mm; background: {LINE}; }}
.a-entry {{ position: relative; margin-bottom: 3mm; }}
.a-entry::before {{ content: ''; position: absolute; left: -8mm; top: 1.1mm; width: 2.7mm; height: 2.7mm; border-radius: 50%;
                   background: #fff; border: .55mm solid {ACCENT}; }}
.a-meta .d {{ font-weight: 700; color: {ACCENT}; }}
.a-entry h3 {{ font-family: 'Lato'; font-size: 10.2pt; font-weight: 700; color: {NAVY}; }}
.a-meta {{ font-size: 9pt; color: {MUTED}; }}
.a-entry ul {{ margin-top: 1.2mm; padding-left: 4.4mm; }}
.a-entry li b {{ font-weight: 700; }}
.a-entry li {{ margin-bottom: 1mm; font-size: 9.6pt; }}
.a-entry li::marker {{ color: {ACCENT}; }}
.kv {{ margin-bottom: 1.6mm; font-size: 9.6pt; }}
.kv b {{ color: {NAVY}; }}
"""
    langs = ", ".join(f'{l["name"]} ({l["level"]})' for l in d["languages"])
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{e(d['meta']['title'])}</title>
<style>{css}</style></head><body><div class="page">
<header class="a-band{' has-photo' if ats_photo(d) else ''}"><h1>{e(d['name'])}</h1><div class="title">{e(d['title'])}</div>
<div class="target">{e(d['target'])}</div><div class="contact">{contact}</div>{ats_photo(d)}</header>
<div class="a-body">
{ats_section('user', 'Profil', f'<p style="font-size:9.8pt">{e(d["profile"])}</p>')}
{ats_section('briefcase', 'Berufserfahrung', ats_entries(d['experience']))}
{ats_section('cap', 'Ausbildung', ats_entries(d['education']))}
{ats_section('grid', 'Kenntnisse', f"""<p class="kv"><b>Kompetenzen:</b> {e(', '.join(d['skills']))}</p>
<p class="kv"><b>IT:</b> {e(', '.join(d['it']))}</p>
<p class="kv"><b>Sprachen:</b> {e(langs)}</p>
<p class="kv"><b>Branche:</b> {e(', '.join(d['industry']))}</p>""")}
</div></div></body></html>"""


# ---------------------------------------------------------------- Anschreiben
def letter_html(d, L, date, attachments=None):
    contact = "  |  ".join(e(c["text"]) for c in d["contact"][:4])
    to = "<br>".join(e(x) for x in L["to"])
    body = "".join(f"<p>{e(p)}</p>" for p in L["body"])
    css = BASE_CSS + f"""
.l-band {{ background: {NAVY}; color: #fff; padding: 10mm 20mm 6mm; border-bottom: 1.1mm solid {ACCENT}; }}
.l-band h1 {{ font-size: 21pt; font-weight: 800; letter-spacing: .045em; text-transform: uppercase; }}
.l-band .title {{ margin-top: 1.2mm; font-family: 'Montserrat'; font-weight: 600; font-size: 8.8pt; letter-spacing: .045em; text-transform: uppercase; color: #BFDDF6; }}
.l-band .contact {{ margin-top: 2.4mm; font-size: 8.4pt; }}
.l-body {{ padding: 12mm 20mm 0 22mm; font-size: 10.4pt; line-height: 1.5; }}
.to {{ margin-bottom: 9mm; }}
.date {{ text-align: right; margin-bottom: 8mm; color: {MUTED}; }}
.subject {{ font-family: 'Montserrat'; font-weight: 700; font-size: 10.6pt; color: {NAVY}; margin-bottom: 6mm; }}
.l-body p {{ margin-bottom: 3.4mm; }}
.sign {{ margin-top: 7mm; }}
.sign .name {{ margin-top: 9mm; font-family: 'Montserrat'; font-weight: 700; color: {NAVY}; }}
.attach {{ margin-top: 9mm; font-size: 8.8pt; color: {MUTED}; }}
"""
    return f"""<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{e(L['subject'])}</title>
<style>{css}</style></head><body><div class="page">
<header class="l-band"><h1>{e(d['name'])}</h1><div class="title">{e(d['title'])}</div><div class="contact">{contact}</div></header>
<div class="l-body"><div class="to">{to}</div><div class="date">{e(date)}</div>
<div class="subject">{e(L['subject'])}</div><p>{e(L['greeting'])}</p>{body}
<div class="sign">{e(L.get("closing", "Mit freundlichen Grüßen"))}<div class="name">{e(d['name'])}</div></div>
<div class="attach">{e(L.get("attachments") or attachments or "Anlagen: Lebenslauf, Zeugnisse")}</div></div></div></body></html>"""


def main():
    data = json.load(open(sys.argv[1], encoding="utf-8"))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    slug = data["name"].replace(" ", "_")
    written = []
    for name, builder in [(f"{slug}_Lebenslauf_Design", design_html), (f"{slug}_Lebenslauf_ATS", ats_html)]:
        p = os.path.join(out, name + ".html")
        open(p, "w", encoding="utf-8").write(builder(data))
        written.append(p)
    if len(sys.argv) > 3:
        letters = json.load(open(sys.argv[3], encoding="utf-8"))
        for key, L in letters["letters"].items():
            p = os.path.join(out, key + ".html")
            open(p, "w", encoding="utf-8").write(letter_html(data, L, letters["date"], letters.get("attachments")))
            written.append(p)
    print("\n".join(written))


if __name__ == "__main__":
    main()
