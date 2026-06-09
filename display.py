import io
import requests
import pygame
from PIL import Image
import spotipy
from spotipy.oauth2 import SpotifyOAuth

pygame.init()

screen = pygame.display.set_mode(
    (1280, 720),
    pygame.FULLSCREEN
)

font = pygame.font.SysFont(None, 40)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="b6061ea3c0dc49518608f742c36cc60b",
        client_secret="3c00b0fa98b24cfaaacdc58a905c47d5",
        redirect_uri="http://127.0.0.1:8888/callback",
        scope="user-read-currently-playing user-read-playback-state"
    )
)

while True:

    playback = sp.current_playback()

    if playback and playback["item"]:

        item = playback["item"]

        title = item["name"]
        artist = item["artists"][0]["name"]
        art = item["album"]["images"][0]["url"]

        img = Image.open(
            io.BytesIO(
                requests.get(art).content
            )
        )

        mode = img.mode
        size = img.size
        data = img.tobytes()

        surf = pygame.image.fromstring(
            data,
            size,
            mode
        )

        surf = pygame.transform.scale(
            surf,
            screen.get_size()
        )

        screen.blit(surf, (0,0))

        text = font.render(
            f"{title} - {artist}",
            True,
            (255,255,255)
        )

        screen.blit(text, (20,20))

    pygame.display.flip()
