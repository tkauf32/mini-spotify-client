from spotify_auth import get_spotify

sp = get_spotify()
sp.pause_playback()
print("paused")
