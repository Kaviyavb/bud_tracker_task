"""
Logging configuration for the FastAPI Bug Tracker application.

This module sets up centralized logging with file output and proper formatting.
Logs API requests, operations, and errors with appropriate levels.
"""

import logging
import os
from logging.handlers import RotatingFileHandler

from app.core.config import settings


def setup_logging():
    """
    Configure logging for the application.

    Sets up:
    - File handler with rotation
    - Console handler for development
    - Proper formatting
    - Log levels
    """
    # Create logs directory if it doesn't exist
    log_dir = os.path.dirname(settings.LOG_FILE_PATH)
    os.makedirs(log_dir, exist_ok=True)

    # Create logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create formatters
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_formatter = logging.Formatter(
        "%(levelname)s - %(message)s"
    )

    # File handler with rotation (10MB max, keep 5 backups)
    file_handler = RotatingFileHandler(
        settings.LOG_FILE_PATH,
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(file_formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # Prevent duplicate logs
    logger.propagate = False

    return logger


# Global logger instance
logger = setup_logging()