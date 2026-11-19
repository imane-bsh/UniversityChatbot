from app.services.embedding_service import generate_embedding
from app.services.vector_service import insert_chunk

text = "Les étudiants peuvent demander une attestation de scolarité."

embedding = generate_embedding(text)

insert_chunk(
    content=text,
    embedding=embedding,
    source="test_document.pdf",
    page=1
)

print("Passage et embedding enregistrés avec succès !")