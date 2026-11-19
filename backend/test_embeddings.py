from app.services.embedding_service import generate_embedding

text = "Comment obtenir une attestation de scolarité ?"

embedding = generate_embedding(text)

print("Nombre de dimensions :", len(embedding))
print("Début du vecteur :", embedding[:10])