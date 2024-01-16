from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
import pandas as pd

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


def getRecomendations(searchSongData): 
    originalSearchedSongName = searchSongData["name"]
    orderedSongData = {}
    for key in XHeaders:
        orderedSongData[key] = searchSongData[key]


    orderedSongDataPd = pd.DataFrame([orderedSongData])
    orderedSongDataScaled = standardScaler.transform(orderedSongDataPd)

    neighboursAndDistances = kn.kneighbors(orderedSongDataScaled, K_NEIGHBORS, return_distance=True)
    neighboursIndexes = neighboursAndDistances[1]
    distances = neighboursAndDistances[0][0]
    neighboursIndexes = neighboursIndexes[0]


    songData = []
    for index, neigbour in enumerate(neighboursIndexes):
        dic = dict(data.iloc[neigbour])
        dic["distance"] = distances[index]
        songData.append(dic)

    songNames = [song["name"] for song in songData]


    scaledNeighbours = XScaled[neighboursIndexes]
    plotSongData(XScaled, scaledNeighbours, songNames, originalSearchedSongName)
    return songData


if __name__ == "__main__":
    getRecomendations("My Body Is a Cage")


