from pydantic import BaseModel, Field, HttpUrl


class TrackInfo(BaseModel):
    """Provide discography details and auxiliary links for a track."""

    album: str = Field(
        ..., examples=["Awesome Mix Vol. 1"], description="Name of the original album."
    )
    year: int = Field(
        ...,
        ge=1960,
        le=2030,
        examples=[1974],
        description="Official release year of the track.",
    )
    duration_seconds: int | None = Field(
        default=None,
        gt=0,
        examples=[178],
        description="Approximate duration expressed in seconds.",
    )
    spotify_url: HttpUrl | None = Field(
        default=None,
        examples=["https://open.spotify.com/track/0y4lG7uMBf9H3lmNwJXilO"],
        description="Optional Spotify link to play the track.",
    )
