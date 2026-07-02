import feedparser

# Trusted RSS feeds
RSS_FEEDS = {
    "JoyNews": "https://www.myjoyonline.com/feed/",
    "GhanaWeb": "https://www.ghanaweb.com/GhanaHomePage/rss/news.xml",
}

def fetch_news():
    print("=" * 60)
    print("Sentinel AI - RSS Incident Monitor")
    print("=" * 60)

    for source, url in RSS_FEEDS.items():
        print(f"\nChecking: {source}")

        feed = feedparser.parse(url)

        if not feed.entries:
            print("No articles found.")
            continue

        for article in feed.entries[:5]:
            print(f"\nTitle : {article.title}")
            print(f"Link  : {article.link}")

            if hasattr(article, "published"):
                print(f"Date  : {article.published}")

            print("-" * 60)


if __name__ == "__main__":
    fetch_news()