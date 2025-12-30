from typing import Literal
from pydantic import BaseModel, Field


class FilterParams(BaseModel):
    limit: int = Field(50, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["title", "artist", "year"] = "title"
    featured_in: list[str] = Field(default_factory=list)
