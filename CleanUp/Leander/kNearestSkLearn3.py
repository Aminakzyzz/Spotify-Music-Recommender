import pandas as pd
from mySpotify import searchSong
import os

data = pd.read_csv("data.csv")


Dict1 = {
    "album": "Scorpion",
    "popularity": 86,
    "explicit": True,
    "duration_ms": 198973,
    "year": "2018",
    "danceability": 0.754,
    "energy": 0.449,
    "key": 7,
    "loudness": -9.211,
    "mode": 1,
    "speechiness": 0.109,
    "acousticness": 0.0332,
    "instrumentalness": 8.29e-05,
    "liveness": 0.552,
    "valence": 0.357,
    "tempo": 77.169,
}


d = data.iloc[0]
d = dict(d)

# songName = d["name"]
# print(songName)
# result = searchSong(songName)
# print(result)

# difference d.keys() and result.keys()
difference = set(d.keys()) - set(Dict1.keys())
print(difference)
# {"artists", "id", "year", "release_date"}
