from app.services.pdf_service import extract_pdf_pages
from app.services.chunk_service import split_text_into_chunks

pdf_path = "data/test_documents/test_document.pdf"

pages = extract_pdf_pages(pdf_path)

all_chunks = []

for page in pages:
    chunks = split_text_into_chunks(
        text=page["text"],
        source="test_document.pdf",
        page=page["page"],
        chunk_size=10,
        overlap=3
    )

    all_chunks.extend(chunks)

for i, chunk in enumerate(all_chunks, start=1):
    print(f"\n===== CHUNK {i} =====")
    print("Source :", chunk["source"])
    print("Page :", chunk["page"])
    print("Texte :", chunk["text"])