"""
FastAPI application for the Bug Tracker system.

This module defines the REST API endpoints for managing issues in the bug tracker.
All endpoints use dependency injection for database sessions and Pydantic schemas
for request/response validation.

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

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI application
app = FastAPI(
    title="Bug Tracker API",
    description="A REST API for managing bug tracking issues",
    version="1.0.0",
)


@app.post("/issues", response_model=IssueResponse, status_code=201)
def create_new_issue(issue: IssueCreate, db: Session = Depends(get_db)):
    """
    Create a new issue in the bug tracker.

    Args:
        issue: IssueCreate schema containing the issue data
        db: Database session dependency

    Returns:
        IssueResponse: The created issue with auto-generated ID

    Raises:
        HTTPException: If there's an issue with the request data
    """
    db_issue = create_issue(db=db, issue=issue)
    return db_issue


@app.get("/issues", response_model=List[IssueResponse])
def read_issues(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve all issues with pagination support.

    Args:
        skip: Number of issues to skip (pagination offset)
        limit: Maximum number of issues to return (pagination limit)
        db: Database session dependency

    Returns:
        List[IssueResponse]: List of issues
    """
    issues = get_issues(db=db, skip=skip, limit=limit)
    return issues


@app.get("/issues/{issue_id}", response_model=IssueResponse)
def read_issue(issue_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific issue by its ID.

    Args:
        issue_id: The ID of the issue to retrieve
        db: Database session dependency

    Returns:
        IssueResponse: The requested issue

    Raises:
        HTTPException: If the issue is not found (404)
    """
    db_issue = get_issue_by_id(db=db, issue_id=issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return db_issue


@app.put("/issues/{issue_id}", response_model=IssueResponse)
def update_existing_issue(issue_id: int, issue: IssueUpdate, db: Session = Depends(get_db)):
    """
    Update an existing issue with new data.

    Args:
        issue_id: The ID of the issue to update
        issue: IssueUpdate schema containing the updated data (all fields optional)
        db: Database session dependency

    Returns:
        IssueResponse: The updated issue

    Raises:
        HTTPException: If the issue is not found (404)
    """
    db_issue = update_issue(db=db, issue_id=issue_id, issue=issue)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return db_issue


@app.delete("/issues/{issue_id}", status_code=204)
def delete_existing_issue(issue_id: int, db: Session = Depends(get_db)):
    """
    Delete an issue from the bug tracker.

    Args:
        issue_id: The ID of the issue to delete
        db: Database session dependency

    Returns:
        None: 204 No Content response

    Raises:
        HTTPException: If the issue is not found (404)
    """
    success = delete_issue(db=db, issue_id=issue_id)
    if not success:
        raise HTTPException(status_code=404, detail="Issue not found")
    return None  # 204 No Content


# Health check endpoint
@app.get("/health")
def health_check():
    """
    Health check endpoint to verify the API is running.

    Returns:
        dict: Status information
    """
    return {"status": "healthy", "message": "Bug Tracker API is running"}
