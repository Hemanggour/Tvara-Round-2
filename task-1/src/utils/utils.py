from PyPDF2 import PdfReader


def read_page(filepath):
    reader = PdfReader(filepath)
    page = reader.pages[0]

    return page.extract_text()
