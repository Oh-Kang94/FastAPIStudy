# app/entity/base.py
from datetime import datetime

from sqlmodel import Field, SQLModel


# base.py
class TimestampMixin(SQLModel):
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default_factory=datetime.now)
