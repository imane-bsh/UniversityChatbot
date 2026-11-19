from app.core.database import get_connection
from pgvector.psycopg import register_vector


def insert_chunk(content: str, embedding: list[float], source: str, page: int):
    with get_connection() as connection:
        register_vector(connection)

        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO document_chunks (content, embedding, source, page)
                VALUES (%s, %s, %s, %s)
                """,
                (content, embedding, source, page)
            )

        connection.commit()