"""
Global exception handlers for the FastAPI Bug Tracker application.

Provides centralized error handling with consistent JSON responses.
"""

from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.core.logging_config import logger


def http_exception_handler(request: Request, exc: HTTPException):
    """
    Handle HTTP exceptions with consistent response format.
    """
    logger.warning(
        f"HTTP Exception: {exc.status_code} - {exc.detail} - Path: {request.url.path}"
    )

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail,
            "details": {
                "status_code": exc.status_code,
                "path": str(request.url.path)
            }
        }
    )


def validation_exception_handler(request: Request, exc: ValidationError):
    """
    Handle Pydantic validation errors with detailed field information.
    """
    logger.warning(
        f"Validation Error: {exc.errors()} - Path: {request.url.path}"
    )

    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation error",
            "details": {
                "errors": exc.errors(),
                "path": str(request.url.path)
            }
        }
    )


def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    """
    Handle database-related exceptions.
    """
    logger.error(
        f"Database Error: {str(exc)} - Path: {request.url.path}",
        exc_info=True
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Database error occurred",
            "details": {
                "error_type": type(exc).__name__,
                "path": str(request.url.path)
            }
        }
    )


def general_exception_handler(request: Request, exc: Exception):
    """
    Handle any unhandled exceptions.
    """
    logger.error(
        f"Unexpected Error: {str(exc)} - Path: {request.url.path}",
        exc_info=True
    )

    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "An unexpected error occurred",
            "details": {
                "error_type": type(exc).__name__,
                "path": str(request.url.path)
            }
        }
    )