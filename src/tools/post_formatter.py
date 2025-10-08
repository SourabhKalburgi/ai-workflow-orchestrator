import random
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class PostFormatter:
    """
    PostFormatter Tool:
    Converts summaries into LinkedIn-style posts with optional hashtags and call-to-actions.
    """

    def __init__(self):
        # Predefined hashtags to mix into posts
        self.hashtags = [
            "#AI", "#MachineLearning", "#Tech", "#Innovation",
            "#DataScience", "#Automation", "#FutureOfWork", "#AIResearch"
        ]
        # Optional call-to-action phrases
        self.ctas = [
            "What are your thoughts on this?", 
            "Would love to hear your opinion!", 
            "Let's discuss in the comments.", 
            "Share your experiences below."
        ]

    def format_post(self, summary: str) -> str:
        """
        Convert a single summary into a LinkedIn-style post.
        """
        try:
            # Pick 2-3 random hashtags
            tags = " ".join(random.sample(self.hashtags, k=3))

            # Pick a random CTA
            cta = random.choice(self.ctas)

            # Construct the final post
            post = f"{summary}\n\n{tags}\n\n{cta}"
            return post
        except Exception as e:
            logger.error(f"Error formatting post: {e}")
            return summary
