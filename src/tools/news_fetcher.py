import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from src.utils.logger import setup_logger

# Load environment variables
load_dotenv()
logger = setup_logger(__name__)

class NewsFetcher:
    """
    Tool for fetching recent news articles about a given topic.
    Uses NewsAPI if key available, else falls back to simple web scraping.
    """

    def __init__(self):
        self.api_key = os.getenv("NEWS_API_KEY")
        self.base_url = "https://newsapi.org/v2/everything"
        self.default_topic = os.getenv("DEFAULT_NEWS_TOPIC", "AI")

    def fetch_from_api(self, topic: str):
        """Fetch news using NewsAPI."""
        try:
            params = {
                "q": topic,
                "language": "en",
                "sortBy": "publishedAt",
                "pageSize": 5,
                "apiKey": self.api_key,
            }
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            articles = data.get("articles", [])

            if not articles:
                logger.warning("No articles found from API.")
                return []

            return [
                {
                    "title": a["title"],
                    "description": a["description"],
                    "url": a["url"],
                }
                for a in articles if a["title"] and a["description"]
            ]

        except Exception as e:
            logger.error(f"API fetch error: {e}")
            return []

    def fetch_from_web(self, topic: str):
        """Fallback: scrape Google News if API fails or missing."""
        try:
            url = f"https://news.google.com/search?q={topic}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            articles = soup.find_all("article")[:5]
            results = []

            for art in articles:
                title = art.text.strip()
                link = art.find("a", href=True)
                if link:
                    results.append({
                        "title": title,
                        "url": "https://news.google.com" + link["href"][1:],
                        "description": "No description (scraped)",
                    })
            return results

        except Exception as e:
            logger.error(f"Scraping fallback error: {e}")
            return []

    def get_news(self, topic: str = None):
        """Unified entry point."""
        topic = topic or self.default_topic
        logger.info(f"Fetching news for topic: {topic}")

        if self.api_key:
            news = self.fetch_from_api(topic)
        else:
            news = self.fetch_from_web(topic)

        logger.info(f"Fetched {len(news)} articles.")
        return news
