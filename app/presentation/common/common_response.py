from datetime import datetime
from pydantic import BaseModel, Field
from typing import Any, Generic, Optional, TypeVar
from fastapi import HTTPException, status
from typing import Any, Optional, Sequence

T = TypeVar("T")


class CommonResponse(BaseModel, Generic[T]):
    success: bool = True
    data: Optional[T] = None
    timestamp: datetime = Field(default_factory=datetime.now)


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
    error_code: Optional[str] = None
    data: Optional[Any] = None
    timestamp: datetime = Field(default_factory=datetime.now)


class CustomHTTPException(HTTPException):
    """커스텀 HTTP 예외 기본 클래스"""

    status_code: int = status.HTTP_400_BAD_REQUEST  # 기본값 지정

    def __init__(
        self,
        detail: str,
        *,
        error_code: Optional[str] = None,
        data: Optional[Any] = None,
        status_code: Optional[int] = None,
    ):
        self.error_code = error_code
        self.data = data
        if status_code:
            self.status_code = status_code
        super().__init__(status_code=self.status_code, detail=detail)


class NotFoundResourceException(CustomHTTPException):
    """리소스를 찾을 수 없을 때"""

    def __init__(self, id: Any):
        super().__init__(
            detail=f"id: {id} 를 찾을 수 없습니다",
            error_code="NOT_FOUND",
            status_code=status.HTTP_404_NOT_FOUND
        )


class ValidationException(CustomHTTPException):
    """데이터 검증 실패 시"""

    def __init__(self, message: str, validation_errors: Sequence[Any] = []):
        super().__init__(
            detail=message,
            error_code="VALIDATION_ERROR",
            data={"validation_errors": validation_errors},
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


class AccessDeniedException(CustomHTTPException):
    """권한이 없을 때"""

    def __init__(self):
        super().__init__(
            detail="접근할 권한이 없습니다",
            error_code="ACCESS_DENIED",
            status_code=status.HTTP_403_FORBIDDEN
        )
