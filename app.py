# FastAPI and typing imports
from fastapi import FastAPI, Query, Path
from typing import Annotated

# Local data and models defined within the project
from data.tracks import tracks
from models.filterparams import FilterParams
from models.track import Track


app = FastAPI(title="Awesome Mix Cassette: Guardians of the Galaxy 🚀📼")


@app.get("/")
async def root():
    """Expose basic service metadata and helpful resource links."""
    return {
        "service": "Awesome Mix API",
        "version": "1.0.0",
        "docs": {"swagger": "/docs", "redoc": "/redoc"},
        "resources": {"tracks": "/api/tracks"},
        "status": "ok",
    }


@app.get("/api/tracks")
async def get_tracks():
    """Return the entire catalog of available tracks."""
    return tracks


@app.get("/api/tracks/{track_id}")
async def get_track(
    track_id: Annotated[int, Path(title="The ID of the track to get", ge=1)],
):
    """Look up a track by its identifier and respond with an error when missing."""
    for track in tracks:
        if track.id == track_id:
            return track
    return {"error": "Track not found"}


@app.post("/api/tracks")
async def create_track(track: Track):
    """Insert a new track into memory and return the confirmed object."""
    tracks.append(track)
    return track


@app.put("/api/tracks/{track_id}")
async def update_track(
    track_id: Annotated[int, Path(title="The ID of the track to update", ge=1)],
    updated_track: Track,
):
    """Replace the existing track with the provided data when a match is found."""
    for index, track in enumerate(tracks):
        if track.id == track_id:
            tracks[index] = updated_track
            return updated_track
    return {"error": "Track not found"}


@app.delete("/api/tracks/{track_id}")
async def delete_track(track_id: int):
    """Remove a track from the catalog when the id matches."""
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
    """Filter tracks by free-text search, movie appearances, and dynamic ordering."""
    items = tracks

    if q:
        needle = q.lower()
        # Narrow the list to partial matches in title, artist, or album name.
        items = [
            track
            for track in items
            if needle in track.title.lower()
            or needle in track.artist.lower()
            or needle in track.info.album.lower()
        ]

    if filter_query.featured_in:
        requested = {value.lower() for value in filter_query.featured_in}
        # Keep only the tracks that appear in any of the requested movies.
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

    # Sort the in-memory collection according to the computed key.
    items = sorted(items, key=order_key)

    total = len(items)
    start = filter_query.offset
    end = start + filter_query.limit

    # Return a paginated payload along with query parameters to ease debugging.
    return {
        "total": total,
        "items": items[start:end],
        "query": q,
        "order_by": filter_query.order_by,
        "featured_in": filter_query.featured_in,
    }
