"""
Pydantic schemas for the FastAPI bug tracker application.

This module defines request and response schemas for API endpoints.
These use Pydantic models for validation and serialization.

Schemas:
- IssueCreate: Schema for creating a new issue
- IssueResponse: Schema for returning an issue from the API
"""

from typing import Literal, Optional

from pydantic import BaseModel, Field


class IssueCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Brief title or summary of the issue"
    )
    description: Optional[str] = Field(
        None,
        max_length=5000,
        description="Detailed description of the issue"
    )
    priority: Literal["Low", "Medium", "High"] = Field(
        ...,
        description="Priority level: Low, Medium, High"
    )
    status: Optional[Literal["Open", "In Progress", "Closed"]] = Field(
        "Open",
        description="Issue status: Open, In Progress, Closed"
    )


class IssueResponse(BaseModel):
    id: int = Field(
        ...,
        description="Unique issue identifier"
    )
    title: str = Field(
        ...,
        description="Brief title or summary of the issue"
    )
    description: Optional[str] = Field(
        None,
        description="Detailed description of the issue"
    )
    priority: Literal["Low", "Medium", "High"] = Field(
        ...,
        description="Priority level: Low, Medium, High"
    )
    status: Literal["Open", "In Progress", "Closed"] = Field(
        ...,
        description="Issue status: Open, In Progress, Closed"
    )
    model_config = {
        "from_attributes": True
    }


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
        max_length=255,
        description="Brief title or summary of the issue"
    )
    description: Optional[str] = Field(
        None,
        max_length=5000,
        description="Detailed description of the issue"
    )
    priority: Optional[Literal["Low", "Medium", "High"]] = Field(
        None,
        description="Priority level: Low, Medium, High"
    )
    status: Optional[Literal["Open", "In Progress", "Closed"]] = Field(
        None,
        description="Issue status: Open, In Progress, Closed"
    )
