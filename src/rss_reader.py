import feedparser

from src.config_loader import load_feeds
from src.database import save_incident, incident_exists
from src.incident_filter import is_security_incident


def fetch_news():

    print("=" * 60)
    print("Sentinel AI - RSS Incident Monitor")
    print("=" * 60)

    feeds = load_feeds()

    for feed in feeds:

        source = feed["name"]
        url = feed["url"]

        print(f"\nChecking: {source}")

        rss = feedparser.parse(url)

        if not rss.entries:
            print("No articles found.")
            continue

        for article in rss.entries[:5]:

            # Skip duplicates already stored
            if incident_exists(article.link):
                print(f"⏭️ Skipping duplicate: {article.title}")
                continue

            # Check whether this is a security-related incident
            if is_security_incident(article.title):

                published = ""

                if hasattr(article, "published"):
                    published = article.published

                print("\n🚨 SECURITY INCIDENT DETECTED")
                print(f"Source : {source}")
                print(f"Title  : {article.title}")
                print(f"Link   : {article.link}")

                if published:
                    print(f"Date   : {published}")

                save_incident(
                    source,
                    article.title,
                    article.link,
                    published
                )

                print("-" * 60)


if __name__ == "__main__":
    fetch_news()