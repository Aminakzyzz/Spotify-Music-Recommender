from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure(figsize=(10, 6))
cmap = "inferno"
dot_size = 20
scatter = plt.scatter(projection["x"], projection["y"], c=projection["cluster"], cmap=cmap, s=dot_size)
specific_point = {"x": 3.0, "y": 3.0, "cluster": 1}  # Replace with your specific data
plt.scatter(specific_point["x"], specific_point["y"], c="black", s=300, marker="X")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Scatter Plot")
cbar = plt.colorbar(scatter, label=f"Cluster ({cmap})")
# plt.show()
plt.savefig(f"kNearestSkLearn{cmap}2.png")
