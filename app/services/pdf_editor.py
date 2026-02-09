import os
from PyPDF2 import PdfMerger
from uuid import uuid4

OUTPUT_DIR = "outputs"

def merge_pdfs(files):
    merger = PdfMerger()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in files:
        merger.append(file)

    output_filename = f"merged_{uuid4().hex}.pdf"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    merger.write(output_path)
    merger.close()

    return output_filename
