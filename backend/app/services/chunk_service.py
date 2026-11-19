def split_text_into_chunks(
    text: str,
    source: str,
    page: int,
    chunk_size: int = 250,
    overlap: int = 40
) -> list[dict]:

    words = text.split()

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    start = 0

    while start < len(words):
        end = min(start + chunk_size, len(words))

        chunk_text = " ".join(words[start:end])

        chunks.append({
            "text": chunk_text,
            "source": source,
            "page": page
        })

        if end == len(words):
            break

        start = end - overlap

    return chunks 