"""Sets PDF metadata and compresses a PDF in place.

Usage: python3 finalize.py <file.pdf> <title> <author> [subject] [keywords]
"""
import sys
from pypdf import PdfReader, PdfWriter

path, title, author = sys.argv[1:4]
subject = sys.argv[4] if len(sys.argv) > 4 else ""
keywords = sys.argv[5] if len(sys.argv) > 5 else ""
writer = PdfWriter(clone_from=PdfReader(path))
for page in writer.pages:
    page.compress_content_streams()
writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
writer.add_metadata({"/Title": title, "/Author": author, "/Subject": subject, "/Keywords": keywords,
                     "/Creator": author, "/Producer": "PDF"})
with open(path, "wb") as f:
    writer.write(f)
