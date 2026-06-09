cat > README.md <<'EOF'
# mini-spotify-client

Tiny Python Spotify control/client prototype for CRTV.

## Features

- Read current playback metadata
- List user playlists
- Play / pause / next / previous
- Control playback on an active Spotify device
- Designed to pair with `spotifyd` on a Raspberry Pi

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install spotipy python-dotenv requests pillow pygame


## 1. Create spotifyd config on Pi
```bash
mkdir -p ~/.config/spotifyd
nano ~/.config/spotifyd/spotifyd.conf
```

### Put this in:
```toml
[global]
device_name = "CRTV"
backend = "alsa"
bitrate = 320
volume_controller = "softvol"
zeroconf_port = 1234
device_type = "speaker"
```

Run it:

~/.cargo/bin/spotifyd --no-daemon --config-path ~/.config/spotifyd/spotifyd.conf

If audio device issues happen, run:

aplay -l

and we’ll add the exact device = "hw:...".
