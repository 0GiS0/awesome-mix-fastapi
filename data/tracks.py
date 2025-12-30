from models.track import Track
from models.trackinfo import TrackInfo


tracks: list[Track] = [
    Track(
        id=1,
        title="Hooked on a Feeling",
        artist="Blue Swede",
        info=TrackInfo(
            album="Awesome Mix Vol. 1",
            year=1974,
            duration_seconds=176,
            spotify_url="https://open.spotify.com/track/5jrdCoLpJSvHHorevXBATy",
        ),
        featured_in=["Guardians of the Galaxy (2014)"],
        rating=5,
    ),
    Track(
        id=2,
        title="Come and Get Your Love",
        artist="Redbone",
        info=TrackInfo(
            album="Awesome Mix Vol. 1",
            year=1973,
            duration_seconds=196,
            spotify_url="https://open.spotify.com/track/1vX3EP3TRrQwLhOVGslGeq",
        ),
        featured_in=["Guardians of the Galaxy (2014)"],
        rating=5,
    ),
    Track(
        id=3,
        title="Mr. Blue Sky",
        artist="Electric Light Orchestra",
        info=TrackInfo(
            album="Awesome Mix Vol. 2",
            year=1977,
            duration_seconds=303,
            spotify_url="https://open.spotify.com/track/1h2JtFoQAyI1BTCLWg1R0c",
        ),
        featured_in=["Guardians of the Galaxy Vol. 2 (2017)"],
        rating=4,
    ),
    Track(
        id=4,
        title="The Chain",
        artist="Fleetwood Mac",
        info=TrackInfo(
            album="Rumours",
            year=1977,
            duration_seconds=270,
            spotify_url="https://open.spotify.com/track/6CgQLA3IqURfPcM2z1Hly7",
        ),
        featured_in=[
            "Guardians of the Galaxy Vol. 2 (2017)",
            "Avengers: Endgame (2019)",
        ],
        rating=4,
    ),
]
