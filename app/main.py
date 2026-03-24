"""
FastAPI application for the Bug Tracker system.
Endpoints:
- POST /issues: Create a new issue
- GET /issues: Retrieve all issues with pagination
- GET /issues/{id}: Retrieve a specific issue by ID
- PUT /issues/{id}: Update an existing issue
- DELETE /issues/{id}: Delete an issue
"""

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import create_issue, delete_issue, get_issue_by_id, get_issues, update_issue
from database import get_db, engine
from models import Issue
from schemas import IssueCreate, IssueResponse, IssueUpdate
import models

# database tables
models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Bug Tracker API",
    description="A REST API for managing bug tracking issues",
    version="1.0.0",
)

@app.post("/issues", response_model=IssueResponse, status_code=201)
def create_new_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    db_issue = create_issue(db=db, issue=issue)
    return db_issue

@app.get("/issues", response_model=List[IssueResponse])
def read_issues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    issues = get_issues(db=db, skip=skip, limit=limit)
    return issues


@app.get("/issues/{issue_id}", response_model=IssueResponse)
def read_issue(issue_id: int, db: Session = Depends(get_db)):
    
    db_issue = get_issue_by_id(db=db, issue_id=issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return db_issue


@app.put("/issues/{issue_id}", response_model=IssueResponse)
def update_existing_issue(issue_id: int, issue: IssueUpdate, db: Session = Depends(get_db)):
    db_issue = update_issue(db=db, issue_id=issue_id, issue=issue)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return db_issue


@app.delete("/issues/{issue_id}", status_code=204)
def delete_existing_issue(issue_id: int, db: Session = Depends(get_db)):
    success = delete_issue(db=db, issue_id=issue_id)
    if not success:
        raise HTTPException(status_code=404, detail="Issue not found")
    return None  

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Bug Tracker API is running"}
