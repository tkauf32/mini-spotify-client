from spotify_auth import get_spotify

sp = get_spotify()

def iter_playlists():
    page = sp.current_user_playlists(limit=50)

    while page:
        for playlist in page["items"]:
            yield playlist

        if page["next"]:
            page = sp.next(page)
        else:
            page = None

for i, p in enumerate(iter_playlists(), start=1):
    images = p.get("images") or []
    image_url = images[0]["url"] if images else None

    print(f"{i}. {p['name']}")
    print(f"   id: {p['id']}")
    print(f"   owner: {p['owner']['display_name']}")
    print(f"   public: {p['public']}")
    print(f"   collaborative: {p['collaborative']}")
    print(f"   tracks: {p['tracks']['total']}")
    print(f"   image: {image_url}")
    print()
