from pydantic import BaseModel, Field, HttpUrl


class TrackInfo(BaseModel):
    """Detalles discográficos y enlaces auxiliares de un tema."""

    album: str = Field(
        ..., examples=["Awesome Mix Vol. 1"], description="Nombre del álbum original."
    )
    year: int = Field(
        ...,
        ge=1960,
        le=2030,
        examples=[1974],
        description="Año oficial de publicación del tema.",
    )
    duration_seconds: int | None = Field(
        default=None,
        gt=0,
        examples=[178],
        description="Duración aproximada expresada en segundos.",
    )
    spotify_url: HttpUrl | None = Field(
        default=None,
        examples=["https://open.spotify.com/track/0y4lG7uMBf9H3lmNwJXilO"],
        description="Enlace opcional a Spotify para reproducir la canción.",
    )
