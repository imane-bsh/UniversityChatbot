import os
import psycopg
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

PASSWORD = quote(os.getenv("DB_PASSWORD", ""), safe="")

DATABASE_URL = (
    f"postgresql://{os.getenv('DB_USER')}:{PASSWORD}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    f"/{os.getenv('DB_NAME')}"
)

def get_connection():
    return psycopg.connect(DATABASE_URL)