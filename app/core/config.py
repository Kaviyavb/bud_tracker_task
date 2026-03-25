"""
Configuration settings for the FastAPI Bug Tracker application.

Centralized configuration to avoid hardcoding values.
Uses environment variables with defaults.
"""

import os
from pathlib import Path


class Settings:
    """Application settings loaded from environment variables."""

    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./bugtracker.db"
    )

    # Application
    APP_NAME: str = os.getenv(
        "APP_NAME",
        "Bug Tracker API"
    )
    APP_VERSION: str = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )
    APP_DESCRIPTION: str = os.getenv(
        "APP_DESCRIPTION",
        "A REST API for managing bug tracking issues"
    )

    # Logging
    LOG_FILE_PATH: str = os.getenv(
        "LOG_FILE_PATH",
        str(Path(__file__).parent.parent.parent / "logs" / "app.log")
    )

    # API
    API_PREFIX: str = os.getenv("API_PREFIX", "")
    API_V1_STR: str = os.getenv("API_V1_STR", "/api/v1")

    # CORS (if needed in future)
    BACKEND_CORS_ORIGINS: list = os.getenv(
        "BACKEND_CORS_ORIGINS",
        ["http://localhost:3000", "http://localhost:8080"]
    ).split(",") if os.getenv("BACKEND_CORS_ORIGINS") else []


# Global settings instance
settings = Settings()
