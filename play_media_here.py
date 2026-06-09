from spotify_auth import get_spotify
import time

DEVICE_NAME = "CRTV"

sp = get_spotify()

devices = sp.devices()["devices"]

target = None
for d in devices:
    print(d["name"], d["id"], d["is_active"], d["type"])
    if d["name"] == DEVICE_NAME:
        target = d

if not target:
    raise SystemExit("CRTV Spotify device not found. Is spotifyd running?")

device_id = target["id"]

sp.transfer_playback(device_id=device_id, force_play=False)
time.sleep(0.5)

sp.start_playback(
    device_id=device_id,
    context_uri="spotify:playlist:YOUR_PLAYLIST_ID"
)

print("playing on CRTV")
