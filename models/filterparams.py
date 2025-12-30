from typing import Literal
from pydantic import BaseModel, Field


class FilterParams(BaseModel):
    """Manage pagination, ordering, and optional filters for catalog searches."""

    limit: int = Field(
        50,
        gt=0,
        le=100,
        description="Maximum number of results to return per page.",
    )
    offset: int = Field(
        0,
        ge=0,
        description="Starting position within the catalog for pagination.",
    )
    order_by: Literal["title", "artist", "year"] = Field(
        "title",
        description="Field used to order the results.",
    )
    featured_in: list[str] = Field(
        default_factory=list,
        description="Optional filter by movie titles where the track appears.",
    )
