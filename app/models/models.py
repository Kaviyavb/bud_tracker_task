"""
SQLAlchemy ORM models for the FastAPI bug tracker application.

This module defines the database models using SQLAlchemy's declarative base.
All models must inherit from the Base class imported from database.py.

Models:
- Issue: Represents a bug or issue in the tracking system
"""

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from app.db.database import Base


class Issue(Base):
    __tablename__ = "issues"
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
        doc="Unique issue identifier"
    )
    title = Column(
        String(255),
        nullable=False,
        index=True,
        doc="Brief title or summary of the issue"
    )
    description = Column(
        String(5000),
        nullable=True,
        doc="Detailed description of the issue"
    )
    priority = Column(
        String(50),
        nullable=False,
        doc="Priority level: Low, Medium, High",
        default="Medium"
    )
    status = Column(
        String(50),
        nullable=False,
        doc="Issue status: Open, In Progress, Closed",
        default="Open"
    )
    reporter_email = Column(
        String(255),
        nullable=False,
        index=True,
        doc="Email address of the person reporting the issue"
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        doc="Timestamp when the issue was created"
    )
    updated_at = Column(
        DateTime,
        nullable=True,
        onupdate=datetime.utcnow,
        doc="Timestamp when the issue was last updated"
    )

    def __repr__(self) -> str:
        return (
            f"<Issue(id={self.id}, title='{self.title}', "
            f"priority='{self.priority}', status='{self.status}', "
            f"reporter_email='{self.reporter_email}')>"
        )
