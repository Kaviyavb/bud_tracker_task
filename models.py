"""
SQLAlchemy ORM models for the FastAPI bug tracker application.

This module defines the database models using SQLAlchemy's declarative base.
All models must inherit from the Base class imported from database.py.

Models:
- Issue: Represents a bug or issue in the tracking system
"""

from sqlalchemy import Column, Integer, String 
from database import Base


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
        default ="open"
    )

    def __repr__(self) -> str:
        return (
            f"<Issue(id={self.id}, title='{self.title}', "
            f"priority='{self.priority}', status='{self.status}')>"
        )
