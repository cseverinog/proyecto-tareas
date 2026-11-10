import os

import psycopg
from psycopg.rows import dict_row


DATABASE_URL = os.getenv("DATABASE_URL")


def get_connection():
    if not DATABASE_URL:
        raise psycopg.OperationalError(
            "DATABASE_URL no está configurada. Defínala mediante el entorno."
        )
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)


def create_schema():
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tareas (
                id SERIAL PRIMARY KEY,
                titulo VARCHAR(200) NOT NULL,
                completada BOOLEAN NOT NULL DEFAULT FALSE,
                creada_en TIMESTAMPTZ NOT NULL DEFAULT NOW()
            )
            """
        )


def create_task(title):
    create_schema()
    with get_connection() as connection:
        return connection.execute(
            """
            INSERT INTO tareas (titulo)
            VALUES (%s)
            RETURNING id, titulo, completada, creada_en
            """,
            (title,),
        ).fetchone()


def list_tasks():
    create_schema()
    with get_connection() as connection:
        return connection.execute(
            """
            SELECT id, titulo, completada, creada_en
            FROM tareas
            ORDER BY id
            """
        ).fetchall()


def complete_task(task_id):
    create_schema()
    with get_connection() as connection:
        return connection.execute(
            """
            UPDATE tareas
            SET completada = TRUE
            WHERE id = %s
            RETURNING id, titulo, completada, creada_en
            """,
            (task_id,),
        ).fetchone()
