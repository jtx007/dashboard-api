from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field


class TimestampMixin(SQLModel):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default=None)
