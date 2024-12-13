import logging
from pathlib import Path
from datetime import datetime

# Log Directory and File Setup
LOG_DIR = Path("log")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / f"log_{datetime.now().strftime('%Y-%m-%d')}.log"

# Logging Configuration
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
logging.basicConfig(
    filename=LOG_FILE,
    format=logging_str,
    level=logging.INFO,
)

# Logger Getter Function
def get_logger(name):
    logger = logging.getLogger(name)
    return logger

# Example Usage
if __name__ == "__main__":
    logging = get_logger("AirlineLogger")
   



