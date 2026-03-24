"""
FastAPI application for the Bug Tracker system.
Endpoints:
- POST /issues: Create a new issue
- GET /issues: Retrieve all issues with pagination
- GET /issues/{id}: Retrieve a specific issue by ID
- PUT /issues/{id}: Update an existing issue
- DELETE /issues/{id}: Delete an issue
"""

from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bug Tracker API",
    description="A REST API for managing bug tracking issues",
    version="1.0.0",
)

# Include routes
app.include_router(router)