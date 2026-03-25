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
   
    try:
        issues = db.query(Issue).offset(skip).limit(limit).all()
        logger.debug(f"Retrieved {len(issues)} issues from database")
        return issues
    except Exception as e:
        logger.error(f"Failed to retrieve issues from database: {str(e)}")
        raise


def get_issue_by_id(db: Session, issue_id: int) -> Optional[Issue]:
  
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
