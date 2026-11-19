from sentence_transformers import SentenceTransformer

# Charger le modèle d'embeddings
model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def generate_embedding(text: str) -> list[float]:
    """
    Transforme un texte en vecteur numérique.
    """
    embedding = model.encode(text)

    return embedding.tolist()