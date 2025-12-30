# Importaciones de FastAPI y typing
from fastapi import FastAPI, Query, Path
from typing import Annotated

# Importados datos y modelos definidos por mi
from data.tracks import tracks
from models.filterparams import FilterParams
from models.track import Track


app = FastAPI(title="Awesome Mix Cassette: Guardians of the Galaxy 🚀📼")


@app.get("/")
async def root():
    return {
        "service": "Awesome Mix API",
        "version": "1.0.0",
        "docs": {"swagger": "/docs", "redoc": "/redoc"},
        "resources": {"tracks": "/api/tracks"},
        "status": "ok",
    }


@app.get("/api/tracks")
async def get_tracks():
    return tracks


@app.get("/api/tracks/{track_id}")
async def get_track(
    track_id: Annotated[int, Path(title="The ID of the track to get", ge=1)],
):
    for track in tracks:
        if track.id == track_id:
            return track
    return {"error": "Track not found"}


@app.post("/api/tracks")
async def create_track(track: Track):
    tracks.append(track)
    return track


@app.put("/api/tracks/{track_id}")
async def update_track(
    track_id: Annotated[int, Path(title="The ID of the track to update", ge=1)],
    updated_track: Track,
):
    for index, track in enumerate(tracks):
        if track.id == track_id:
            tracks[index] = updated_track
            return updated_track
    return {"error": "Track not found"}


@app.delete("/api/tracks/{track_id}")
async def delete_track(track_id: int):
    for track in tracks:
        if track.id == track_id:
            tracks.remove(track)
            return {"message": "Track deleted"}
    return {"error": "Track not found"}


@app.get("/api/search")
async def search_tracks(
    filter_query: Annotated[FilterParams, Query()],
    q: Annotated[
        str | None,
        Query(
            title="Search",
            description="Search query for Awesome Mix tracks",
            min_length=2,
            examples=["feeling"],
        ),
    ] = None,
):
    items = tracks

    if q:
        needle = q.lower()
        items = [
            track
            for track in items
            if needle in track.title.lower()
            or needle in track.artist.lower()
            or needle in track.info.album.lower()
        ]

    if filter_query.featured_in:
        requested = {value.lower() for value in filter_query.featured_in}
        items = [
            track
            for track in items
            if any(movie.lower() in requested for movie in track.featured_in)
        ]

    order_key = {
        "title": lambda track: track.title.lower(),
        "artist": lambda track: track.artist.lower(),
        "year": lambda track: track.info.year,
    }.get(filter_query.order_by, lambda track: track.title.lower())

    items = sorted(items, key=order_key)

    total = len(items)
    start = filter_query.offset
    end = start + filter_query.limit

    return {
        "total": total,
        "items": items[start:end],
        "query": q,
        "order_by": filter_query.order_by,
        "featured_in": filter_query.featured_in,
    }
