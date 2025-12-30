from pydantic import BaseModel, Field, HttpUrl


class TrackInfo(BaseModel):
    album: str = Field(..., examples=["Awesome Mix Vol. 1"])
    year: int = Field(..., ge=1960, le=2030, examples=[1974])
    duration_seconds: int | None = Field(default=None, gt=0, examples=[178])
    spotify_url: HttpUrl | None = Field(
        default=None,
        examples=["https://open.spotify.com/track/0y4lG7uMBf9H3lmNwJXilO"],
    )
