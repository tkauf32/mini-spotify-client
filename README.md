# mini-spotify-client

A lightweight Python Spotify client prototype for the CRTV project.

This repository provides a simple interface for:

- Reading Spotify playback metadata
- Displaying album artwork
- Listing playlists
- Controlling playback (play, pause, next, previous)
- Transferring playback to a Spotify Connect device
- Integrating Spotify into the CRTV media platform

The long-term goal is to use this as the Spotify service layer behind CRTV while keeping the UI, renderer, and media system completely independent.

---

# Features

## Metadata

- Current track
- Artist
- Album
- Album artwork URL
- Playback state
- Playback position

## Playback Control

- Play
- Pause
- Next Track
- Previous Track

## Playlists

- Enumerate all user playlists
- Retrieve playlist metadata
- Retrieve playlist artwork

## Device Management

- List Spotify devices
- Transfer playback between devices
- Integrate with spotifyd on Raspberry Pi

---

# Requirements

- Python 3.10+
- Spotify Premium Account
- Spotify Developer Application

---

# Setup

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install spotipy python-dotenv requests pillow pygame
```

---

# Spotify Developer Setup

Create an application at:

https://developer.spotify.com/dashboard

Add the following Redirect URI:

```text
http://127.0.0.1:8888/callback
```

Create a `.env` file:

```env
SPOTIFY_CLIENT_ID=YOUR_CLIENT_ID
SPOTIFY_CLIENT_SECRET=YOUR_CLIENT_SECRET
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8888/callback
```

---

# Authentication

Authentication is handled through OAuth.

The first run will:

1. Open a browser
2. Prompt for Spotify authorization
3. Store a local token cache

A token cache file will be created:

```text
.spotify_token_cache
```

---

# Available Scripts

## Current Playback

```bash
python test.py
```

Outputs:

```text
Track Name
Artist Name
Album Name
Artwork URL
```

---

## List Playlists

```bash
python list_playlists.py
```

Outputs:

```text
Playlist Name
Playlist ID
Owner
Track Count
Artwork URL
```

---

## Pause Playback

```bash
python pause.py
```

---

## Resume Playback

```bash
python play.py
```

---

## Next Track

```bash
python next.py
```

---

## Previous Track

```bash
python previous.py
```

---

# Raspberry Pi spotifyd Setup

CRTV uses spotifyd as a Spotify Connect endpoint.

Create the config directory:

```bash
mkdir -p ~/.config/spotifyd
```

Create the config file:

```bash
nano ~/.config/spotifyd/spotifyd.conf
```

Paste:

```toml
[global]
device_name = "CRTV"
backend = "alsa"
bitrate = 320
volume_controller = "softvol"
zeroconf_port = 1234
device_type = "speaker"
```

---

## Run spotifyd

If installed through Cargo:

```bash
~/.cargo/bin/spotifyd \
  --no-daemon \
  --config-path ~/.config/spotifyd/spotifyd.conf
```

---

## Verify Audio Devices

If playback does not work:

```bash
aplay -l
```

Use the output to determine the correct ALSA device.

---

# CRTV Architecture

Current architecture:

```text
Spotify API
     │
     ▼
mini-spotify-client
     │
     ▼
CRTV App State
     │
     ▼
Renderer
     ├─ Album Artwork
     ├─ Metadata
     ├─ Visualizations
     └─ UI
```

Spotify is treated as a media source.

The UI and rendering system remain independent from Spotify.

---

# Future Work

- Album artwork caching
- Playback transfer automation
- Playlist browser UI
- Spotify visualizations
- CRT shader effects
- Album-art-based ambient visuals
- Hardware rotary encoder controls
- Full CRTV integration

---

# License

MIT
