import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

load_dotenv(override=True)

def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )

    return connection

def buscar_lead_por_id(lead_id):
    conn = get_connection()

    cursor = conn.cursor(cursor_factory=RealDictCursor)

    cursor.execute("""
        SELECT
            id,
            nome,
            email,
            empresa,
            interesse,
            mensagem,
            status,
            origem,
            categoria,
            prioridade,
            criado_em
        FROM leads
        WHERE id=%s;
    """, (lead_id,))

    lead = cursor.fetchone()

    cursor.close()
    conn.close()

    return lead
