"""
CRUD (Create, Read, Update, Delete) operations for the Issue model.
Each function operates on the Issue table using SQLAlchemy ORM.

Functions:
- create_issue: Create a new issue
- get_issues: Retrieve all issues
- get_issue_by_id: Retrieve a specific issue by ID
- update_issue: Update an existing issue
- delete_issue: Delete an issue
"""

from typing import List, Optional
from datetime import datetime
from sqlalchemy.orm import Session

from app.core.logging_config import logger
from app.models.models import Issue
from app.schemas.schemas import IssueCreate, IssueUpdate


def create_issue(db: Session, issue: IssueCreate) -> Issue:
    """
    Create a new issue in the database.

    Args:
        db: Database session
        issue: Issue creation data

    Returns:
        Created Issue object

    Raises:
        Exception: If database operation fails
    """
    try:
        db_issue = Issue(**issue.model_dump(exclude_unset=True))
        db.add(db_issue)
        db.commit()
        db.refresh(db_issue)
        logger.info(f"Issue created in database: {db_issue.id}")
        return db_issue
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to create issue in database: {str(e)}")
        raise


def get_issues(db: Session, skip: int = 0, limit: int = 100) -> List[Issue]:
    """
    Retrieve issues from the database with pagination.

    Args:
        db: Database session
        skip: Number of records to skip
        limit: Maximum number of records to return

    Returns:
        List of Issue objects
    """
    try:
        issues = db.query(Issue).offset(skip).limit(limit).all()
        logger.debug(f"Retrieved {len(issues)} issues from database")
        return issues
    except Exception as e:
        logger.error(f"Failed to retrieve issues from database: {str(e)}")
        raise


def get_issue_by_id(db: Session, issue_id: int) -> Optional[Issue]:
    """
    Retrieve a specific issue by ID.

    Args:
        db: Database session
        issue_id: Issue identifier

    Returns:
        Issue object if found, None otherwise
    """
    try:
        issue = db.query(Issue).filter(Issue.id == issue_id).first()
        if issue:
            logger.debug(f"Issue found: {issue_id}")
        else:
            logger.debug(f"Issue not found: {issue_id}")
        return issue
    except Exception as e:
        logger.error(f"Failed to retrieve issue {issue_id} from database: {str(e)}")
        raise


def update_issue(db: Session, issue_id: int, issue: IssueUpdate) -> Optional[Issue]:
    """
    Update an existing issue.

    Args:
        db: Database session
        issue_id: Issue identifier
        issue: Issue update data

    Returns:
        Updated Issue object if found, None otherwise

    Raises:
        Exception: If database operation fails
    """
    try:
        db_issue = db.query(Issue).filter(Issue.id == issue_id).first()
        if not db_issue:
            logger.debug(f"Issue not found for update: {issue_id}")
            return None

        update_data = issue.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_issue, field, value)
        db_issue.updated_at = datetime.utcnow()

        db.commit()
        db.refresh(db_issue)
        logger.info(f"Issue updated in database: {issue_id}")
        return db_issue
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to update issue {issue_id} in database: {str(e)}")
        raise


def delete_issue(db: Session, issue_id: int) -> bool:
    """
    Delete an issue from the database.

    Args:
        db: Database session
        issue_id: Issue identifier

    Returns:
        True if deleted, False if not found

    Raises:
        Exception: If database operation fails
    """
    try:
        db_issue = db.query(Issue).filter(Issue.id == issue_id).first()
        if not db_issue:
            logger.debug(f"Issue not found for deletion: {issue_id}")
            return False

        db.delete(db_issue)
        db.commit()
        logger.info(f"Issue deleted from database: {issue_id}")
        return True
    except Exception as e:
        db.rollback()
        logger.error(f"Failed to delete issue {issue_id} from database: {str(e)}")
        raise
