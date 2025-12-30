from pydantic import BaseModel, Field

from models.trackinfo import TrackInfo


class Track(BaseModel):
    id: int
    title: str = Field(..., examples=["Hooked on a Feeling"])
    artist: str = Field(..., examples=["Blue Swede"])
    info: TrackInfo
    featured_in: list[str] = Field(
        default_factory=list,
        examples=[["Guardians of the Galaxy (2014)"]],
    )
    rating: int | None = Field(default=None, ge=1, le=5)
