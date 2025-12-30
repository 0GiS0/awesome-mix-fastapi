from typing import Literal
from pydantic import BaseModel, Field


class FilterParams(BaseModel):
    """Controla paginación, ordenación y filtros opcionales para la búsqueda."""

    limit: int = Field(
        50,
        gt=0,
        le=100,
        description="Número máximo de resultados a devolver por página.",
    )
    offset: int = Field(
        0,
        ge=0,
        description="Posición inicial dentro del catálogo para la paginación.",
    )
    order_by: Literal["title", "artist", "year"] = Field(
        "title",
        description="Campo que se utilizará para ordenar los resultados.",
    )
    featured_in: list[str] = Field(
        default_factory=list,
        description="Filtro opcional por títulos de películas en las que aparece el tema.",
    )
