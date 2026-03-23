"""
Database configuration for the FastAPI bug tracker application.

This module sets up the SQLAlchemy engine, session maker, and declarative base
for ORM model definitions using SQLite as the database backend.

Key Components:
- SQLALCHEMY_DATABASE_URL: SQLite database file path
- engine: SQLAlchemy engine with optimized settings
- SessionLocal: Session factory for creating database sessions
- Base: Declarative base class for all ORM models
- get_db(): FastAPI dependency for injecting sessions into endpoints
"""

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.pool import StaticPool

# ============================================================================
# DATABASE CONFIGURATION
# ============================================================================

# SQLite database file path (relative to project root)
SQLALCHEMY_DATABASE_URL = "sqlite:///./bugtracker.db"

# ============================================================================
# ENGINE CONFIGURATION
# ============================================================================

# Create SQLAlchemy engine with optimized settings for SQLite + FastAPI
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # SQLite connection arguments
    connect_args={
        # Disable thread-safety check for multi-threaded FastAPI environment
        "check_same_thread": False
    },
   
)

# ============================================================================
# SESSION CONFIGURATION
# ============================================================================

# Create a configured session factory
# Each instance provides a database session with optimized settings
SessionLocal = sessionmaker(
    # Disable autocommit mode for explicit transaction control
    autocommit=False,
    # Prevent automatic flush before queries
    autoflush=False,
    # Bind this session maker to the engine
    bind=engine,
)

# ============================================================================
# ORM BASE CLASS
# ============================================================================

# Declarative base for all ORM model classes
# All database models must inherit from this class
Base = declarative_base()

# ============================================================================
# DEPENDENCY INJECTION
# ============================================================================


def get_db() -> Generator:
    """
    FastAPI dependency to provide a database session for each request.

    Yields:
        SessionLocal: A SQLAlchemy database session

    Example:
        @app.get("/items")
        def read_items(db: Session = Depends(get_db)):
            return db.query(Item).all()

    Notes:
        - Automatically closes the session after the request completes
        - Ensures proper resource cleanup even if an exception occurs
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
