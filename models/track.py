"""Representación Pydantic de un registro musical expuesto por la API."""

from pydantic import BaseModel, Field

from models.trackinfo import TrackInfo


class Track(BaseModel):
    """Describe cada canción, su origen y metadatos de catálogo."""

    id: int
    title: str = Field(
        ..., examples=["Hooked on a Feeling"], description="Título oficial del tema."
    )
    artist: str = Field(
        ..., examples=["Blue Swede"], description="Principal intérprete de la canción."
    )
    info: TrackInfo
    featured_in: list[str] = Field(
        default_factory=list,
        examples=[["Guardians of the Galaxy (2014)"]],
        description="Listado de películas en las que suena el tema.",
    )
    rating: int | None = Field(
        default=None,
        ge=1,
        le=5,
        description="Valoración subjetiva en una escala de 1 a 5 estrellas.",
    )
