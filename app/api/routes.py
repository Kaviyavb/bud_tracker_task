from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.logging_config import logger
from app.db.database import get_db
from app.schemas.schemas import IssueCreate, IssueUpdate, IssueResponse
from app.services.crud import (
    create_issue,
    get_issues,
    get_issue_by_id,
    update_issue,
    delete_issue
)

router = APIRouter()


#  Create Issue
@router.post("/issues", response_model=IssueResponse, status_code=201)
def create_new_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    logger.info(f"Creating new issue: {issue.title}")
    try:
        result = create_issue(db=db, issue=issue)
        logger.info(f"Issue created successfully with ID: {result.id}")
        return result
    except Exception as e:
        logger.error(f"Failed to create issue: {str(e)}")
        raise


# Get All Issues
@router.get("/issues", response_model=List[IssueResponse])
def read_issues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.info(f"Fetching issues: skip={skip}, limit={limit}")
    try:
        result = get_issues(db=db, skip=skip, limit=limit)
        logger.info(f"Retrieved {len(result)} issues")
        return result
    except Exception as e:
        logger.error(f"Failed to fetch issues: {str(e)}")
        raise


#Get Single Issue
@router.get("/issues/{issue_id}", response_model=IssueResponse)
def read_issue(issue_id: int, db: Session = Depends(get_db)):
    logger.info(f"Fetching issue with ID: {issue_id}")
    try:
        result = get_issue_by_id(db=db, issue_id=issue_id)
        if not result:
            logger.warning(f"Issue not found: {issue_id}")
            raise HTTPException(status_code=404, detail="Issue not found")
        logger.info(f"Issue retrieved: {issue_id}")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to fetch issue {issue_id}: {str(e)}")
        raise


#Update Issue
@router.put("/issues/{issue_id}", response_model=IssueResponse)
def update_existing_issue(issue_id: int, issue: IssueUpdate, db: Session = Depends(get_db)):
    logger.info(f"Updating issue {issue_id}")
    try:
        result = update_issue(db=db, issue_id=issue_id, issue=issue)
        if not result:
            logger.warning(f"Issue not found for update: {issue_id}")
            raise HTTPException(status_code=404, detail="Issue not found")
        logger.info(f"Issue updated successfully: {issue_id}")
        return result
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to update issue {issue_id}: {str(e)}")
        raise


# Delete Issue
@router.delete("/issues/{issue_id}", status_code=204)
def delete_existing_issue(issue_id: int, db: Session = Depends(get_db)):
    logger.info(f"Deleting issue {issue_id}")
    try:
        success = delete_issue(db=db, issue_id=issue_id)
        if not success:
            logger.warning(f"Issue not found for deletion: {issue_id}")
            raise HTTPException(status_code=404, detail="Issue not found")
        logger.info(f"Issue deleted successfully: {issue_id}")
        return None
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to delete issue {issue_id}: {str(e)}")
        raise


# Health Check
@router.get("/health")
def health_check():
    logger.info("Health check requested")
    return {"status": "healthy", "message": "Bug Tracker API is running"}