from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

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


# ✅ Create Issue
@router.post("/issues", response_model=IssueResponse, status_code=201)
def create_new_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    return create_issue(db=db, issue=issue)


# ✅ Get All Issues
@router.get("/issues", response_model=List[IssueResponse])
def read_issues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_issues(db=db, skip=skip, limit=limit)


# ✅ Get Single Issue
@router.get("/issues/{issue_id}", response_model=IssueResponse)
def read_issue(issue_id: int, db: Session = Depends(get_db)):
    db_issue = get_issue_by_id(db=db, issue_id=issue_id)

    if not db_issue:
        raise HTTPException(status_code=404, detail="Issue not found")

    return db_issue


# ✅ Update Issue
@router.put("/issues/{issue_id}", response_model=IssueResponse)
def update_existing_issue(issue_id: int, issue: IssueUpdate, db: Session = Depends(get_db)):
    db_issue = update_issue(db=db, issue_id=issue_id, issue=issue)

    if not db_issue:
        raise HTTPException(status_code=404, detail="Issue not found")

    return db_issue


# ✅ Delete Issue
@router.delete("/issues/{issue_id}", status_code=204)
def delete_existing_issue(issue_id: int, db: Session = Depends(get_db)):
    success = delete_issue(db=db, issue_id=issue_id)
    if not success:
        raise HTTPException(status_code=404, detail="Issue not found")
    return None


# ✅ Health Check
@router.get("/health")
def health_check():
    return {"status": "healthy", "message": "Bug Tracker API is running"}