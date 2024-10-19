import os
import sys
import logging
from datetime import datetime

# Create a log file with a timestamped name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory path for logs
log_dir = os.path.join(os.getcwd(), "logs")

# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Example log entry
# if __name__ == "__main__":
#     logging.info("Logging started")
