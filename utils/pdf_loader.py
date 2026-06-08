from pypdf import PdfReader


def extract_text_from_pdf(pdf_path):
    """
    Extract all text from PDF
    """

    try:
        reader = PdfReader(pdf_path)
    except Exception as e:
        print(f"Error reading PDF: {e}")

    full_text = ""

    for page in reader.pages:
        text = page.extract_text()

        if text:
            full_text += text + "\n"

    return full_text