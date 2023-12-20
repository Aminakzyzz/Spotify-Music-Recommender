from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
from mySpotify import searchSong

# TODO: NORMALIZE DATA and PLOT PCA


K_NEIGHBORS = 10
attributesToDrop = ["id", "artists", "name", "release_date"]

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


data = pd.read_csv("data.csv")


X = data.drop(attributesToDrop, axis=1, inplace=False)
# X = data.select_dtypes(np.number)


kn = NearestNeighbors(n_neighbors=K_NEIGHBORS)
kn.fit(X)


input_text = "hello"
songData = searchSong(input_text)

inputData = songData  # dict(data.iloc[5])


# print(inputData.keys())
# inputData.pop("artist")  # artists
# inputData.pop("name")
# inputData.pop("album")
# inputData.pop("time_signature")
songAttributesToDrop = ["artist", "name", "album", "time_signature"]
inputDataPd = pd.DataFrame([inputData])
inputDataPd.drop(songAttributesToDrop, axis=1, inplace=True)

# differentKeys = set(inputDataPd.keys()).difference(X.keys())
# print(differentKeys)
# exit()


# inp = X.iloc[5]
neighbours = kn.kneighbors(inputDataPd, K_NEIGHBORS, return_distance=False)
neighbours = neighbours[0]  # [neighbours]

print(neighbours)

print("Input:")
# |18914|  0.289,2016,0.336,['Adele'],0.481,295493,0.451,0,4sPmO7WMQUAf45kwMOtONw,0.0,5,0.0872,-6.095,0,Hello,73,2016-06-24,0.0347,157.966
print(inputData)

print(f"{K_NEIGHBORS} Neighbours:")


songNames = []
for neigbour in neighbours:
    dic = dict(data.iloc[neigbour])
    print(neigbour, dic)
    # outStr = f'{dic["name"]} by {dic["artists"]} from {dic["year"]}'
    outStr = dic["name"]
    songNames.append(outStr)

print(songNames)
