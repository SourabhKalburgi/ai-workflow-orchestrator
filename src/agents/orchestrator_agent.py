from src.tools.news_fetcher import NewsFetcher
from src.tools.summarizer import Summarizer
from src.tools.post_formatter import PostFormatter
from src.database.db_service import save_post
import requests

# --- Telegram Configuration ---
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_to_telegram(message: str):
    """Send a single message to Telegram chat."""
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"  # optional for better formatting
    }
    try:
        response = requests.post(TELEGRAM_API_URL, data=payload)
        if response.status_code != 200:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    # Step 1: Fetch news
    topic = "AI"
    fetcher = NewsFetcher()
    articles = fetcher.get_news(topic)

    # Step 2: Summarize news
    summarizer = Summarizer()
    texts = [a["description"] or a["title"] for a in articles]
    summaries = summarizer.summarize(texts)

    # Step 3: Format posts
    formatter = PostFormatter()
    posts = [formatter.format_post(summary) for summary in summaries]

    # Step 4: Save + Send posts
    for i, (article, summary, formatted_post) in enumerate(zip(articles, summaries, posts), start=1):
        article_title = article.get("title")
        article_url = article.get("url")
        summary_text = summary

        print(f"--- Post {i} ---")
        print(formatted_post)
        print("\n")

        post_data = {
            "topic": topic,
            "title": article_title,
            "summary": summary_text,
            "formatted_post": formatted_post,
            "source_url": article_url
        }

        # Save to MongoDB
        save_post(post_data)

        # Send to Telegram
        message = f"*{article_title}*\n\n{formatted_post}\n[Read more]({article_url})"
        send_to_telegram(message)
