import schedule
import time

from src.database import create_database
from src.rss_reader import fetch_news
from src.logger import logger


def job():

    logger.info("Starting security incident check...")

    print("\nChecking for new incidents...\n")

    try:

        create_database()

        fetch_news()

        logger.info("Security incident check completed successfully.")

    except Exception as e:

        logger.error(f"Error: {e}")

        print(e)


schedule.every(3).minutes.do(job)

print("=" * 60)
print("Sentinel AI Scheduler Started")
print("Monitoring every 3 minutes...")
print("Press CTRL + C to stop.")
print("=" * 60)

logger.info("Sentinel AI Started")

job()

while True:

    schedule.run_pending()

    time.sleep(1)