import logging
import os

def setup_logging():
    """Configures logging to file and console."""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.FileHandler("trading_bot.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()