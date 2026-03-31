from docling.document_converter import DocumentConverter


def read_doc(filepath):
    source = filepath
    converter = DocumentConverter()
    doc = converter.convert(source).document.export_to_text()

    return doc
