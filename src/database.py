import sqlite3
import os


DB_PATH = "database/sentinel_ai.db"


def create_database():
    """Create the database and incidents table if they do not exist."""

    # Create database folder if it doesn't exist
    os.makedirs("database", exist_ok=True)

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            title TEXT,
            link TEXT UNIQUE,
            published TEXT
        )
    """)

    connection.commit()
    connection.close()


def save_incident(source, title, link, published):
    """Save a new incident to the database."""

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO incidents (source, title, link, published)
            VALUES (?, ?, ?, ?)
        """, (source, title, link, published))

        connection.commit()

        print("💾 Incident saved to database.")

    except sqlite3.IntegrityError:
        print("⚠️ Incident already exists in database.")

    finally:
        connection.close()


def incident_exists(link):
    """Check if an incident already exists in the database."""

    connection = sqlite3.connect(DB_PATH)

    cursor = connection.cursor()

    cursor.execute(
        "SELECT id FROM incidents WHERE link = ?",
        (link,)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None