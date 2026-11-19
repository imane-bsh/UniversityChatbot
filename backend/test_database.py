from app.core.database import get_connection

try:
    connection = get_connection()
    print("Connexion PostgreSQL réussie !")

    connection.close()
    print("Connexion fermée.")

except Exception as error:
    print("Erreur de connexion :", error)