from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import os
import datetime


def plotSongData(XScaled, songDatasScaled, songNames, originalSearchedSongName):
    song_cluster_pipeline = Pipeline([("scaler", StandardScaler()), ("kmeans", KMeans(n_clusters=20, verbose=False))], verbose=False)
    song_cluster_pipeline.fit(XScaled)
    song_cluster_labels = song_cluster_pipeline.predict(XScaled)

    pca_pipeline = Pipeline([("scaler", StandardScaler()), ("PCA", PCA(n_components=2))])
    song_embedding = pca_pipeline.fit_transform(XScaled)
    projection = pd.DataFrame(columns=["x", "y"], data=song_embedding)
    plt.style.use("dark_background")
    plt.figure(figsize=(10, 6))
    cmap = "inferno"
    dot_size = 20
    plt.scatter(projection["x"], projection["y"], c=song_cluster_labels, cmap=cmap, s=dot_size)
    outputPlotPoints = pca_pipeline.fit_transform(songDatasScaled)
    outputPlotPoints


    for i, plotPoint in enumerate(outputPlotPoints):
        plt.scatter(plotPoint[0], plotPoint[1], c="yellow", s=300, marker="X")
        plt.text(plotPoint[0], plotPoint[1], songNames[i], color="#430000", fontsize=8, ha="center", va="center", path_effects=[pe.withStroke(linewidth=2, foreground="yellow")])

    firstPoint = outputPlotPoints[0]
    x = firstPoint[0] + firstPoint[0] / 10
    y = firstPoint[1] + firstPoint[1] / 10

    plt.scatter(x, y, c="blue", s=300, marker="X")
    plt.text(x, y, originalSearchedSongName, color="#430000", fontsize=15, ha="center", va="center", path_effects=[pe.withStroke(linewidth=4, foreground="blue")])

    imageName = f"plot.png"
    dateString = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if os.path.exists(imageName):
        os.rename(imageName, f"plotOld_{dateString}.png")

    plt.axis("off")
    plt.tight_layout()
    plt.savefig(imageName, bbox_inches="tight", transparent=True)
