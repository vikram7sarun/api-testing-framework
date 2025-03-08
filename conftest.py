import logging
import os

# Create a logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging settings
logging.basicConfig(
    filename="logs/api_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Create a logger instance
logger = logging.getLogger(__name__)
