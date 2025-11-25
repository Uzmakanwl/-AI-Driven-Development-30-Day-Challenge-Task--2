from pypdf import PdfReader

def extract_text_from_pdf(file_path: str) -> str:
    """
    Extracts all text from a PDF file.

    Args:
        file_path (str): The path to the PDF file.

    Returns:
        str: The concatenated text content from all pages of the PDF.
    """
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text
