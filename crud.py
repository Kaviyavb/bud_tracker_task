"""
CRUD (Create, Read, Update, Delete) operations for the Issue model.

This module contains all database operations for managing issues in the bug tracker.
Each function operates on the Issue table using SQLAlchemy ORM.

Functions:
- create_issue: Create a new issue
- get_issues: Retrieve all issues
- get_issue_by_id: Retrieve a specific issue by ID
- update_issue: Update an existing issue
- delete_issue: Delete an issue
"""

from typing import List, Optional

from sqlalchemy.orm import Session

from models import Issue
from schemas import IssueCreate, IssueUpdate


def create_issue(db: Session, issue: IssueCreate) -> Issue:
    """
    Create a new issue in the database.

    Args:
        db: SQLAlchemy database session
        issue: IssueCreate schema containing issue data

    Returns:
        Issue: The newly created Issue object with auto-generated ID

    Example:
        issue_data = IssueCreate(
            title="Fix login bug",
            priority="High",
            status="Open"
        )
        new_issue = create_issue(db, issue_data)
    """
    # Convert Pydantic schema to dictionary, excluding unset fields
    db_issue = Issue(**issue.model_dump(exclude_unset=True))

    # Add and commit the new issue to the database
    db.add(db_issue)
    db.commit()

    # Refresh to get the auto-generated ID and any default values
    db.refresh(db_issue)

    return db_issue


def get_issues(db: Session, skip: int = 0, limit: int = 100) -> List[Issue]:
    """
    Retrieve all issues from the database with pagination support.

    Args:
        db: SQLAlchemy database session
        skip: Number of issues to skip (pagination offset)
        limit: Maximum number of issues to return (pagination limit)

    Returns:
        List[Issue]: List of Issue objects

    Example:
        issues = get_issues(db, skip=0, limit=10)
    """
    return db.query(Issue).offset(skip).limit(limit).all()


def get_issue_by_id(db: Session, issue_id: int) -> Optional[Issue]:
    """
    Retrieve a specific issue by its ID.

    Args:
        db: SQLAlchemy database session
        issue_id: The ID of the issue to retrieve

    Returns:
        Optional[Issue]: The Issue object if found, None otherwise

    Example:
        issue = get_issue_by_id(db, issue_id=1)
        if issue:
            print(issue.title)
    """
    return db.query(Issue).filter(Issue.id == issue_id).first()


def update_issue(db: Session, issue_id: int, issue: IssueUpdate) -> Optional[Issue]:
    """
    Update an existing issue with new data.

    Args:
        db: SQLAlchemy database session
        issue_id: The ID of the issue to update
        issue: IssueUpdate schema containing updated issue data (all fields optional)

    Returns:
        Optional[Issue]: The updated Issue object if found, None otherwise

    Example:
        updated_data = IssueUpdate(
            status="In Progress",
            priority="High"
        )
        updated_issue = update_issue(db, issue_id=1, issue=updated_data)
    """
    # Retrieve the existing issue
    db_issue = db.query(Issue).filter(Issue.id == issue_id).first()

    # If not found, return None
    if not db_issue:
        return None

    # Update only the provided fields
    update_data = issue.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_issue, field, value)

    # Commit the changes
    db.commit()

    # Refresh to ensure we have the latest data
    db.refresh(db_issue)

    return db_issue


def delete_issue(db: Session, issue_id: int) -> bool:
    """
    Delete an issue from the database.

    Args:
        db: SQLAlchemy database session
        issue_id: The ID of the issue to delete

    Returns:
        bool: True if the issue was deleted, False if not found

    Example:
        success = delete_issue(db, issue_id=1)
        if success:
            print("Issue deleted successfully")
    """
    # Retrieve the existing issue
    db_issue = db.query(Issue).filter(Issue.id == issue_id).first()

    # If not found, return False
    if not db_issue:
        return False

    # Delete the issue from the session and commit
    db.delete(db_issue)
    db.commit()

    return True
