# import time
# startTime = time.time()
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import pandas as pd
from mySpotify import searchSong
from plotManager import plotSongData


K_NEIGHBORS = 10
attributesToDrop = ["id", "artists", "name", "release_date"]

data = pd.read_csv("data.csv")
standardScaler = StandardScaler()
XRaw = data.drop(attributesToDrop, axis=1, inplace=False)
XHeaders = list(XRaw.keys())
XScaled = standardScaler.fit_transform(XRaw)
kn = NearestNeighbors(n_neighbors=K_NEIGHBORS)
kn.fit(XScaled)
songAttributesToDrop = ["artist", "name", "album", "time_signature"]


# danceibilityValue, tempoValue, popularityValue, energyValue
def getRecomendations(songNameInput):  # , songsCountToReturn=10):
    orderedSongData = {}
    songData = searchSong(songNameInput)
    for key in XHeaders:
        orderedSongData[key] = songData[key]
    orderedSongDataPd = pd.DataFrame([orderedSongData])
    orderedSongDataScaled = standardScaler.transform(orderedSongDataPd)

    neighboursAndDistances = kn.kneighbors(orderedSongDataScaled, K_NEIGHBORS, return_distance=True)
    neighboursIndexes = neighboursAndDistances[1]  # [neighbours]
    distances = neighboursAndDistances[0]
    neighboursIndexes = neighboursIndexes[0]

    print("Distances = ", list(distances))
    print("NeighboursIndexes = ", neighboursIndexes)

    songData = []
    for neigbour in neighboursIndexes:
        # print(neigbour)
        dic = dict(data.iloc[neigbour])
        # print(type(dic))
        songData.append(dic)

    songNames = [song["name"] for song in songData]

    print("songNames = ", songNames)

    scaledNeighbours = XScaled[neighboursIndexes]
    plotSongData(XScaled, scaledNeighbours, songNames)
    return songData


if __name__ == "__main__":
    getRecomendations("My Body Is a Cage")


# {
#     "valence": 0.313,
#     "year": 2007,
#     "acousticness": 0.315,
#     "artists": "['Arcade Fire']",  # X
#     "danceability": 0.296,  # I
#     "duration_ms": 287240,  # X // convert to minutes
#     "energy": 0.502,  # I
#     "explicit": 0,  # X
#     "id": "1rOlTL4pKQ9Y1fURua4AJR",
#     "instrumentalness": 0.0551,
#     "key": 0,
#     "liveness": 0.229,
#     "loudness": -8.652999999999999,  # X
#     "mode": 0,
#     "name": "My Body Is a Cage",  # X
#     "popularity": 62,  # I
#     "release_date": "2007",
#     "speechiness": 0.0336,  # X
#     "tempo": 81.045,  # I
# }
