from app.core.database import get_connection
from pgvector.psycopg import register_vector


def search_similar_chunks(question_embedding: list[float], limit: int = 3):
    with get_connection() as connection:
        register_vector(connection)

        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT content, source, page,
                       embedding <=> %s::vector AS distance
                FROM document_chunks
                ORDER BY embedding <=> %s::vector
                LIMIT %s
                """,
                (question_embedding, question_embedding, limit)
            )

            return cursor.fetchall()