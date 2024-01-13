from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import os

data = pd.read_csv("data.csv")
song_cluster_pipeline = Pipeline([("scaler", StandardScaler()), ("kmeans", KMeans(n_clusters=20, verbose=False))], verbose=False)
X = data.select_dtypes(np.number)
number_cols = list(X.columns)
song_cluster_pipeline.fit(X)
song_cluster_labels = song_cluster_pipeline.predict(X)
data["cluster_label"] = song_cluster_labels

pca_pipeline = Pipeline([("scaler", StandardScaler()), ("PCA", PCA(n_components=2))])
song_embedding = pca_pipeline.fit_transform(X)
projection = pd.DataFrame(columns=["x", "y"], data=song_embedding)
projection["title"] = data["name"]
projection["cluster"] = data["cluster_label"]


plt.style.use("dark_background")
plt.figure(figsize=(10, 6))
cmap = "inferno"
dot_size = 20
scatter = plt.scatter(projection["x"], projection["y"], c=projection["cluster"], cmap=cmap, s=dot_size)

##NEW
XHead = X.head(3)
outputPlotPoints = pca_pipeline.fit_transform(XHead)
outputPlotPoints
##NEW
myData = data.head(len(XHead))

for i, plotPoint in enumerate(outputPlotPoints):
    plt.scatter(plotPoint[0], plotPoint[1], c="yellow", s=300, marker="X")
    # XHead.index[i]
    dataI = myData.iloc[i]
    dataI = dict(dataI)
    # print(dataI)
    songName = dataI["name"]
    # truncate songName
    songName = songName[:10]
    plt.text(plotPoint[0], plotPoint[1], songName, color="#430000", fontsize=8, ha="center", va="center", path_effects=[pe.withStroke(linewidth=2, foreground="yellow")])


# cbar = plt.colorbar(scatter, label=f"Cluster ({cmap})")


# plt.show()
imageName = f"kNearestSkLearn{cmap}tig5.png"
plt.axis("off")
plt.tight_layout()
plt.savefig(imageName, bbox_inches="tight", transparent=True)
# plt.savefig(imageName)
os.startfile(imageName)
