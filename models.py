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
    """
    Issue model representing a bug or task in the tracking system.

    Attributes:
        id: Unique identifier for the issue (primary key)
        title: Brief title/summary of the issue (indexed for fast lookups)
        description: Detailed description of the issue (optional)
        priority: Priority level of the issue (Low, Medium, High)
        status: Current status of the issue (Open, In Progress, Closed)

    Table:
        issues: The database table name
    """

    __tablename__ = "issues"

    # Primary key - unique identifier for each issue
    id = Column(
        Integer,
        primary_key=True,
        index=True,
        autoincrement=True,
        doc="Unique issue identifier"
    )

    # Issue title - indexed for efficient searching
    title = Column(
        String(255),
        nullable=False,
        index=True,
        doc="Brief title or summary of the issue"
    )

    # Issue description - optional, can be null
    description = Column(
        String(5000),
        nullable=True,
        doc="Detailed description of the issue"
    )

    # Priority level - required field
    # Expected values: "Low", "Medium", "High"
    priority = Column(
        String(50),
        nullable=False,
        doc="Priority level: Low, Medium, High",
        default="Medium"
    )

    # Current status - required field
    # Expected values: "Open", "In Progress", "Closed"
    status = Column(
        String(50),
        nullable=False,
        doc="Issue status: Open, In Progress, Closed",
        default ="open"
    )

    def __repr__(self) -> str:
        """String representation of the Issue object."""
        return (
            f"<Issue(id={self.id}, title='{self.title}', "
            f"priority='{self.priority}', status='{self.status}')>"
        )
