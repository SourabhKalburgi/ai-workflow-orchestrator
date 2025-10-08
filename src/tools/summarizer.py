from transformers import pipeline
from src.utils.logger import setup_logger

logger = setup_logger(__name__)

class Summarizer:
    """
    Summarizer Tool using Hugging Face Transformers.
    Takes raw text and generates concise summaries.
    """

    def __init__(self, model_name="google/flan-t5-base"):
        logger.info(f"Loading summarization model: {model_name}")
        self.summarizer = pipeline("summarization", model=model_name, device=-1)  # CPU only

    def summarize(self, texts, max_length=150, min_length=50):
        """
        Summarize a list of texts.
        :param texts: List of strings
        :return: List of summary strings
        """
        summaries = []
        for i, text in enumerate(texts, start=1):
            try:
                logger.info(f"Summarizing article {i}")
                summary = self.summarizer(
                    text,
                    max_length=max_length,
                    min_length=min_length,
                    do_sample=False
                )[0]["summary_text"]
                summaries.append(summary)
            except Exception as e:
                logger.error(f"Error summarizing article {i}: {e}")
                summaries.append("Summary not available.")
        return summaries
