from mySpotify import searchSong


input_text = "hello"
result = searchSong(input_text)


# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# from sklearn.decomposition import PCA
# import numpy as np
# import pandas as pd


# data = pd.read_csv("data.csv")
# song_cluster_pipeline = Pipeline([("scaler", StandardScaler()), ("kmeans", KMeans(n_clusters=20, verbose=False))], verbose=False)
# X = data.select_dtypes(np.number)
# number_cols = list(X.columns)
# song_cluster_pipeline.fit(X)
# song_cluster_labels = song_cluster_pipeline.predict(X)
# data["cluster_label"] = song_cluster_labels

# pca_pipeline = Pipeline([("scaler", StandardScaler()), ("PCA", PCA(n_components=2))])
# song_embedding = pca_pipeline.fit_transform(X)
# projection = pd.DataFrame(columns=["x", "y"], data=song_embedding)


print(result)