import sqlite3

DATABASE_NAME = "database/sentinel_ai.db"


def create_database():
    """
    Creates the incidents table if it doesn't already exist.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            source TEXT,
            title TEXT,
            link TEXT UNIQUE,
            published TEXT,
            collected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def save_incident(source, title, link, published):
    """
    Saves a security incident into the database.
    """

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO incidents(source, title, link, published)
            VALUES (?, ?, ?, ?)
        """, (source, title, link, published))

        connection.commit()

    except sqlite3.IntegrityError:
        # Duplicate article
        pass

    connection.close()