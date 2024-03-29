import base64
import json
from requests import post, get
import os

pathOfFile = os.path.dirname(os.path.abspath(__file__))




def encrypt(text, key):
    result = ""
    for char in text:
        result += chr((ord(char) + key) % 128)
    return result

def decrypt(text, key):
    return encrypt(text, -key)

Y = "pq?qCCDC>=A;?ql@C=Cnm>pD>?B>Dpop7A?=@;lD?p?on?=>>lB?@Cq@<=D<?=@lD"
X = decrypt(Y,11)
envSplit = X.split(",")
SPOTIFY_CLIENT_ID = envSplit[0]
SPOTIFY_CLIENT_SECRET = envSplit[1]


def get_token():
    auth_string = f"{SPOTIFY_CLIENT_ID}:{SPOTIFY_CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")
    url = "https://accounts.spotify.com/api/token"

    headers = {"Authorization": "Basic " + auth_base64, "Content-Type": "application/x-www-form-urlencoded"}

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


ACCESS_TOKEN = get_token()
AUTH_HEADER = {"Authorization": "Bearer " + ACCESS_TOKEN}


def search(artist_name, search_type):
    url = "https://api.spotify.com/v1/search"
    headers = AUTH_HEADER
    query = f"?q={artist_name}&type={search_type}&limit=1"
    query_url = url + query
    result = get(query_url, headers=headers)
    return result.json()


def getAudioFeatures(id):
    url = f"https://api.spotify.com/v1/audio-features/{id}"
    headers = AUTH_HEADER
    result = get(url, headers=headers)
    return result.json()


def searchArtist(toSearch):
    return search(toSearch, "artist")


def searchSongMetadata(toSearch):
    return search(toSearch, "track")


def searchSong(toSearch):
    songMetaData = searchSongMetadata(toSearch)
    dataToReturn = {}
    song = songMetaData["tracks"]["items"][0]
    dataToReturn["name"] = song["name"]
    dataToReturn["artist"] = song["artists"][0]["name"]
    dataToReturn["album"] = song["album"]["name"]
    dataToReturn["popularity"] = song["popularity"]
    dataToReturn["explicit"] = 1 if song["explicit"] else 0
    dataToReturn["duration_ms"] = song["duration_ms"]
    dataToReturn["year"] = int(song["album"]["release_date"][:4])

    id = song["id"]
    audioFeatures = getAudioFeatures(id)

    for key, value in audioFeatures.items():
        if key not in ["type", "id", "uri", "track_href", "analysis_url"]:
            dataToReturn[key] = value

    return dataToReturn


if __name__ == "__main__":
    out = searchSong("Lucid Dreams")
    print(out)
