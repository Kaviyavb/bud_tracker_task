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
from sqlalchemy.orm import Session
from models import Issue
from schemas import IssueCreate, IssueUpdate


def create_issue(db: Session, issue: IssueCreate) -> Issue:
    db_issue = Issue(**issue.model_dump(exclude_unset=True))
    db.add(db_issue)
    db.commit()
    db.refresh(db_issue)
    return db_issue


def get_issues(db: Session, skip: int = 0, limit: int = 100) -> List[Issue]:
    return db.query(Issue).offset(skip).limit(limit).all()


def get_issue_by_id(db: Session, issue_id: int) -> Optional[Issue]:
    return db.query(Issue).filter(Issue.id == issue_id).first()


def update_issue(db: Session, issue_id: int, issue: IssueUpdate) -> Optional[Issue]:
    db_issue = db.query(Issue).filter(Issue.id == issue_id).first()
    if not db_issue:
        return None
    update_data = issue.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_issue, field, value)
    db.commit()
    db.refresh(db_issue)
    return db_issue


def delete_issue(db: Session, issue_id: int) -> bool:
    db_issue = db.query(Issue).filter(Issue.id == issue_id).first()
    if not db_issue:
        return False
    db.delete(db_issue)
    db.commit()
    return True
