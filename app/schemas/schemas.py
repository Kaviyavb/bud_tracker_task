"""
Pydantic schemas for the FastAPI bug tracker application.

This module defines request and response schemas for API endpoints.
These use Pydantic models for validation and serialization.

Schemas:
- IssueCreate: Schema for creating a new issue
- IssueResponse: Schema for returning an issue from the API
- IssueUpdate: Schema for updating an existing issue
"""

from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, EmailStr, Field


class IssueCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=255,
        description="Brief title or summary of the issue",
        examples=["Login button not working"]
    )
    description: Optional[str] = Field(
        None,
        max_length=5000,
        description="Detailed description of the issue",
        examples=["When clicking the login button, nothing happens..."]
    )
    priority: Literal["Low", "Medium", "High"] = Field(
        ...,
        description="Priority level of the issue",
        examples=["High"]
    )
    status: Optional[Literal["Open", "In Progress", "Closed"]] = Field(
        "Open",
        description="Current status of the issue",
        examples=["Open"]
    )
    reporter_email: EmailStr = Field(
        ...,
        description="Email address of the person reporting the issue",
        examples=["user@example.com"]
    )


class IssueResponse(BaseModel):
    id: int = Field(
        ...,
        description="Unique issue identifier",
        examples=[1]
    )
    title: str = Field(
        ...,
        description="Brief title or summary of the issue",
        examples=["Login button not working"]
    )
    description: Optional[str] = Field(
        None,
        description="Detailed description of the issue",
        examples=["When clicking the login button, nothing happens..."]
    )
    priority: Literal["Low", "Medium", "High"] = Field(
        ...,
        description="Priority level of the issue",
        examples=["High"]
    )
    status: Literal["Open", "In Progress", "Closed"] = Field(
        ...,
        description="Current status of the issue",
        examples=["Open"]
    )
    reporter_email: EmailStr = Field(
        ...,
        description="Email address of the person reporting the issue",
        examples=["user@example.com"]
    )
    created_at: datetime = Field(
        ...,
        description="Timestamp when the issue was created",
        examples=["2023-12-01T10:00:00Z"]
    )
    updated_at: Optional[datetime] = Field(
        None,
        description="Timestamp when the issue was last updated",
        examples=["2023-12-02T15:30:00Z"]
    )

    model_config = {
        "from_attributes": True
    }


class IssueUpdate(BaseModel):
    title: Optional[str] = Field(
        None,
        min_length=1,
        max_length=255,
        description="Brief title or summary of the issue",
        examples=["Updated login issue title"]
    )
    description: Optional[str] = Field(
        None,
        max_length=5000,
        description="Detailed description of the issue",
        examples=["Updated description with more details..."]
    )
    priority: Optional[Literal["Low", "Medium", "High"]] = Field(
        None,
        description="Priority level of the issue",
        examples=["Medium"]
    )
    status: Optional[Literal["Open", "In Progress", "Closed"]] = Field(
        None,
        description="Current status of the issue",
        examples=["In Progress"]
    )
    reporter_email: Optional[EmailStr] = Field(
        None,
        description="Email address of the person reporting the issue",
        examples=["newuser@example.com"]
    )
