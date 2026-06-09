import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="b6061ea3c0dc49518608f742c36cc60b",
        client_secret="3c00b0fa98b24cfaaacdc58a905c47d5",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-currently-playing user-read-playback-state"
    )
)

current = sp.current_playback()

print(current["item"]["name"])
print(current["item"]["artists"][0]["name"])
print(current["item"]["album"]["images"][0]["url"])
