import logging
import os

def setup_logger(name: str):
    """Creates and configures a logger instance."""
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    # File handler
    fh = logging.FileHandler("logs/app.log")
    fh.setLevel(log_level)

    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger
