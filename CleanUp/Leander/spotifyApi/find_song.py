import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# import os

with open(".env", "r") as f:
    envText = f.read()
    envSplit = envText.split(",")
    SPOTIFY_CLIENT_ID = envSplit[0]
    SPOTIFY_CLIENT_SECRET = envSplit[1]

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET))


def find_song(name):
    song_data = {}
    results = sp.search(q=f"track: {name}", limit=1)
    if results["tracks"]["items"] == []:
        print("No results found")
        return None

    results = results["tracks"]["items"][0]
    print(results)
    track_id = results["id"]
    audio_features = sp.audio_features(track_id)[0]

    song_data["name"] = [name]
    song_data["explicit"] = [int(results["explicit"])]
    song_data["duration_ms"] = [results["duration_ms"]]
    song_data["popularity"] = [results["popularity"]]

    for key, value in audio_features.items():
        song_data[key] = value

    print(song_data)
    # return pd.DataFrame(song_data)


find_song("The Box")
