import fitz


def extract_pdf_pages(pdf_path: str) -> list[dict]:
    pages = []

    with fitz.open(pdf_path) as document:
        for page_number, page in enumerate(document, start=1):
            pages.append({
                "text": page.get_text(),
                "page": page_number
            })

    return pages