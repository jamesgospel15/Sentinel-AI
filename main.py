from src.database import create_database
from src.rss_reader import fetch_news

if __name__ == "__main__":
    create_database()
    fetch_news()