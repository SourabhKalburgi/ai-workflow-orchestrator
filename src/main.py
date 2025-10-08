from src.tools.news_fetcher import NewsFetcher
from src.tools.summarizer import Summarizer
from src.tools.post_formatter import PostFormatter
from src.database.db_service import save_post

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

    # Step 4: Print + Save formatted posts
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
        save_post(post_data)
