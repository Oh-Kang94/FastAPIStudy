from datetime import datetime
from pydantic import BaseModel
from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")

class CommonResponse(BaseModel, Generic[T]):
    success: bool = True
    data: Optional[T] = None
    timestamp: datetime = datetime.now()
