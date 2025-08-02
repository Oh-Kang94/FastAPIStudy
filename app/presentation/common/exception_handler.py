from datetime import datetime
from fastapi import HTTPException, Request, status
from typing import Any, Optional, Sequence
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from pydantic import BaseModel, Field

from app.presentation.common.common_response import CustomHTTPException, ErrorResponse


async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
    """CustomHTTPException 처리"""
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(ErrorResponse(
            message=exc.detail,
            error_code=exc.error_code,
            data=exc.data,
        ))
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """RequestValidationError 처리"""
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(ErrorResponse(
            message="입력값이 잘못되었습니다",
            error_code="VALIDATION_ERROR",
            data=parse_validation_errors(exc.errors())
        ))
    )


def parse_validation_errors(errors: Sequence[Any]) -> list[dict[str, str]]:
    parsed = []
    for error in errors:
        loc = error.get("loc", [])
        field = loc[-1] if loc else "unknown"
        msg = error.get("msg", "")
        err_type = error.get("type", "")

        parsed.append({
            "field": field,
            "message": msg,
            "type": err_type,
        })
    return parsed


async def general_exception_handler(request: Request, exc: Exception):
    """기타 예외 처리 (500)"""
    import os
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=jsonable_encoder(ErrorResponse(
            message="서버 내부 오류가 발생했습니다",
            error_code="INTERNAL_SERVER_ERROR",
            data=str(exc) if debug_mode else None,
        ))
    )
