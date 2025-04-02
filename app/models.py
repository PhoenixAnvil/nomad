from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Backlog(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = None
    product_id: UUID
