import sys
import os

sys.path.append(os.path.join(os.getcwd(), "src"))

from textSummarizer.logging import logger

logger.info("Welcome to our custom logging system")