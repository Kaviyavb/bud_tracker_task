"""
Database configuration for the FastAPI bug tracker application.

This module sets up the SQLAlchemy engine, session maker, and declarative base
for ORM model definitions using SQLite as the database backend.
"""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

from app.core.config import settings

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={
        "check_same_thread": False
    },
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db() -> Generator:
    """
    Dependency to get database session.
    Yields a database session and ensures it's closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
