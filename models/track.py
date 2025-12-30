from pydantic import BaseModel, Field

from models.trackinfo import TrackInfo


class Track(BaseModel):
    """Describe each song, its origin, and catalog metadata."""

    id: int
    title: str = Field(
        ..., examples=["Hooked on a Feeling"], description="Official track title."
    )
    artist: str = Field(
        ..., examples=["Blue Swede"], description="Primary performer of the song."
    )
    info: TrackInfo
    featured_in: list[str] = Field(
        default_factory=list,
        examples=[["Guardians of the Galaxy (2014)"]],
        description="List of movies where the track appears.",
    )
    rating: int | None = Field(
        default=None,
        ge=1,
        le=5,
        description="Subjective rating on a 1-to-5 star scale.",
    )
