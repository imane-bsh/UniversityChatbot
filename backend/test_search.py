from app.services.embedding_service import generate_embedding
from app.services.search_service import search_similar_chunks

question = "Comment obtenir un certificat d'inscription ?"

question_embedding = generate_embedding(question)

results = search_similar_chunks(question_embedding)

for result in results:
    content, source, page, distance = result

    print("\n--- Résultat ---")
    print("Contenu :", content)
    print("Source :", source)
    print("Page :", page)
    print("Distance :", distance)