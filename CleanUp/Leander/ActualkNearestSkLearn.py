import time

startTime = time.time()

from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
from mySpotify import searchSong

# TODO: NORMALIZE DATA and PLOT PCA

# TOTAL_SONGS_FROM_DATASET = 100  # reduced for testing

K_NEIGHBORS = 10
attributesToDrop = ["id", "artists", "name", "release_date"]


# data = pd.read_csv("data.csv", nrows=100)  # skiprows=range(1, 166666 - 170654) # max 170654 start from 166666
data = pd.read_csv("data.csv")

standardScaler = StandardScaler()

X = data.drop(attributesToDrop, axis=1, inplace=False)

XDataBeforeScaling = {
    "valence": 0.218,
    "year": 2018.0,
    "acousticness": 0.349,
    "danceability": 0.511,
    "duration_ms": 239836.0,
    "energy": 0.5660000000000001,
    "explicit": 1.0,
    "instrumentalness": 0.0,
    "key": 6.0,
    "liveness": 0.34,
    "loudness": -7.23,
    "mode": 0.0,
    "popularity": 89.0,
    "speechiness": 0.2,
    "tempo": 83.90299999999998,
}


# print(f"XDataBeforeScaling = {dict(X.iloc[19209-2])}")
# exit()
X = standardScaler.fit_transform(X)

XAfterScaling = [
    -1.180174006840522,
    1.59013482590464,
    -0.40718695279507683,
    -0.14985779192667356,
    0.07047119485477848,
    0.3123958592792641,
    3.2899554031056244,
    -0.5327705364234788,
    0.2276349473522137,
    0.7674951952594559,
    0.7437776265010027,
    -1.5530073214809366,
    2.637531012520044,
    0.6243516658622421,
    -1.073274524076333,
]


# print(X)
# X = data.select_dtypes(np.number)


kn = NearestNeighbors(n_neighbors=K_NEIGHBORS)
kn.fit(X)


# print(f"DataData={dict(data.iloc[19209-2])}")
# print(f"XData={list(X[19209-2])}")

# exit()


DataData = {
    "valence": 0.218,
    "year": 2018,
    "acousticness": 0.349,
    "artists": "['Juice WRLD']",
    "danceability": 0.511,
    "duration_ms": 239836,
    "energy": 0.5660000000000001,
    "explicit": 1,
    "id": "285pBltuF7vW8TeWk8hdRR",
    "instrumentalness": 0.0,
    "key": 6,
    "liveness": 0.34,
    "loudness": -7.23,
    "mode": 0,
    "name": "Lucid Dreams",
    "popularity": 89,
    "release_date": "2018-12-10",
    "speechiness": 0.2,
    "tempo": 83.90299999999998,
}


songData = {
    "name": "Lucid Dreams",
    "artist": "Juice WRLD",
    "album": "Goodbye & Good Riddance",
    "popularity": 86,
    "explicit": 1,
    "duration_ms": 239836,
    "year": 2018,
    "danceability": 0.511,
    "energy": 0.566,
    "key": 6,
    "loudness": -7.23,
    "mode": 0,
    "speechiness": 0.2,
    "acousticness": 0.349,
    "instrumentalness": 0,
    "liveness": 0.34,
    "valence": 0.218,
    "tempo": 83.903,
    "time_signature": 4,
}


# input_text = "Lucid Dreams"
# songData = searchSong(input_text)
# print(f"songData = {songData}")
# print(inputData.keys())
songAttributesToDrop = ["artist", "name", "album", "time_signature"]
# inputDataPd = pd.DataFrame([songData])
# inputDataPd.drop(songAttributesToDrop, axis=1, inplace=True)


XHeaders = list(XDataBeforeScaling.keys())

orderedSongData = {}

for key in XHeaders:
    orderedSongData[key] = songData[key]

orderedSongData = {
    "valence": 0.218,
    "year": 2018,
    "acousticness": 0.349,
    "danceability": 0.511,
    "duration_ms": 239836,
    "energy": 0.566,
    "explicit": 1,
    "instrumentalness": 0,
    "key": 6,
    "liveness": 0.34,
    "loudness": -7.23,
    "mode": 0,
    "popularity": 86,
    "speechiness": 0.2,
    "tempo": 83.903,
}
# print(f"orderedSongData = {orderedSongData}")


orderedSongDataPd = pd.DataFrame([orderedSongData])


inputDataPdDict = {
    "popularity": 86,
    "explicit": True,
    "duration_ms": 239836,
    "year": "2018",
    "danceability": 0.511,
    "energy": 0.566,
    "key": 6,
    "loudness": -7.23,
    "mode": 0,
    "speechiness": 0.2,
    "acousticness": 0.349,
    "instrumentalness": 0,
    "liveness": 0.34,
    "valence": 0.218,
    "tempo": 83.903,
}
# print(f"inputDataPd = {dict(inputDataPd.iloc[0])}")
# exit()


# print(f"BEFORE SCALING inputDataPd = {dict(inputDataPd.iloc[0])}")
print(f"BEFORE SCALING orderedSongData = {orderedSongData}")

orderedSongDataScaled = standardScaler.transform(orderedSongDataPd)

print(f"AFTER SCALING orderedSongData = {list(orderedSongDataScaled)}")

# AFTERSCALINGorderedSongData = [array([-1.18017401,  1.59013483, -0.40718695, -0.14985779,  0.07047119,
#         0.31239586,  3.2899554 , -0.53277054,  0.22763495,  0.7674952 ,
#         0.74377763, -1.55300732,  2.50008374,  0.62435167, -1.07327452])]


# exit()
# dict(data.iloc[5])


# differentKeys = set(inputDataPd.keys()).difference(X.keys())
# print(differentKeys)
# exit()


# inp = X.iloc[5]
neighboursAndDistances = kn.kneighbors(orderedSongDataScaled, K_NEIGHBORS, return_distance=True)
neighbours = neighboursAndDistances[1]  # [neighbours]
distances = neighboursAndDistances[0]

print("Distances = ", list(distances))

print("Neighbors = ", neighbours)

print("Input:")
print(songData)

print(f"{K_NEIGHBORS} Neighbours:")


songNames = []
for neigbour in neighbours:
    dic = dict(data.iloc[neigbour])
    # print(dic)
    # outStr = f'{dic["name"]} by {dic["artists"]} from {dic["year"]}'
    outStr = dic["name"]
    songNames.append(outStr)

print(songNames)


endTime = time.time()
print(f"[Script finished in: {endTime - startTime} seconds]")


# allAttributes = [
#     "valence",
#     "year",
#     "acousticness",
#     "artists",
#     "danceability",
#     "duration_ms",
#     "energy",
#     "explicit",
#     "id",
#     "instrumentalness",
#     "key",
#     "liveness",
#     "loudness",
#     "mode",
#     "name",
#     "popularity",
#     "release_date",
#     "speechiness",
#     "tempo",
# ]

# attributesToKeep = [
#     "valence",
#     "year",
#     "acousticness",
#     "danceability",
#     "duration_ms",
#     "energy",
#     "explicit",
#     "instrumentalness",
#     "key",
#     "liveness",
#     "loudness",
#     "mode",
#     "popularity",
#     "speechiness",
#     "tempo",
# ]


# keysInput = [
#     "name",
#     "artist",
#     "album",
#     "popularity",
#     "explicit",
#     "duration_ms",
#     "year",
#     "danceability",
#     "energy",
#     "key",
#     "loudness",
#     "mode",
#     "speechiness",
#     "acousticness",
#     "instrumentalness",
#     "liveness",
#     "valence",
#     "tempo",
#     "time_signature",
# ]
