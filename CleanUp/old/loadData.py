import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as sk

data = pd.read_csv("data/data.csv")
genre_data = pd.read_csv("data/data_by_genres.csv")
year_data = pd.read_csv("data/data_by_year.csv")


plt.figure(figsize=(10, 6))
plt.scatter(data["year"], data["popularity"], alpha=0.5)
plt.title("Popularity vs. Year")
plt.xlabel("Year")
plt.ylabel("Popularity")
plt.grid(True)
plt.show()

# Plotting for 'genre_data' DataFrame
plt.figure(figsize=(12, 8))
genre_counts = genre_data["genres"].value_counts().head(10)
genre_counts.plot(kind="barh", color="skyblue")
plt.title("Top 10 Genres Count")
plt.xlabel("Count")
plt.ylabel("Genres")
plt.show()

# Plotting for 'year_data' DataFrame
plt.figure(figsize=(10, 6))
plt.plot(year_data["year"], year_data["danceability"], label="Danceability", marker="o")
plt.plot(year_data["year"], year_data["energy"], label="Energy", marker="o")
plt.title("Danceability and Energy Over Years")
plt.xlabel("Year")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()


print(f"data.head() = {data.head()}")
print(f"genre_data.head() = {genre_data.head()}")
print(f"year_data.head() = {year_data.head()}")


"""
 data.head() =    valence  year  acousticness                                            artists  ...  popularity  release_date  speechiness    tempo
0   0.0594  1921         0.982  ['Sergei Rachmaninoff', 'James Levine', 'Berli...  ...           4          1921       0.0366   80.954
1   0.9630  1921         0.732                                     ['Dennis Day']  ...           5          1921       0.4150   60.936
2   0.0394  1921         0.961  ['KHP Kridhamardawa Karaton Ngayogyakarta Hadi...  ...           5          1921       0.0339  110.339
3   0.1650  1921         0.967                                   ['Frank Parker']  ...           3          1921       0.0354  100.109
4   0.2530  1921         0.957                                     ['Phil Regan']  ...           2          1921       0.0380  101.665

[5 rows x 19 columns]
genre_data.head() =    mode                  genres  acousticness  danceability   duration_ms    energy  ...   loudness  speechiness       tempo   valence  popularity  key
0     1  21st century classical      0.979333      0.162883  1.602977e+05  0.071317  ... -31.514333     0.040567   75.336500  0.103783   27.833333    61     1                   432hz      0.494780      0.299333  1.048887e+06  0.450678  ... -16.854000     0.076817  120.285667  0.221750   52.500000    52     1                   8-bit      0.762000      0.712000  1.151770e+05  0.818000  ...  -9.180000     0.047000  133.444000  0.975000   48.000000    73     1                      []      0.651417      0.529093  2.328809e+05  0.419146  ... -12.288965     0.107872  112.857352  0.513604   20.859882    74     1              a cappella      0.676557      0.538961  1.906285e+05  0.316434  ... -12.479387     0.082851  112.110362  0.448249   45.820071    7
[5 rows x 14 columns]
year_data.head() =    mode  year  acousticness  danceability    duration_ms    energy  ...   loudness  speechiness       tempo   valence  popularity  key
0     1  1921      0.886896      0.418597  260537.166667  0.231815  ... -17.048667     0.073662  101.531493  0.379327    0.653333    2
1     1  1922      0.938592      0.482042  165469.746479  0.237815  ... -19.275282     0.116655  100.884521  0.535549    0.140845   10
2     1  1923      0.957247      0.577341  177942.362162  0.262406  ... -14.129211     0.093949  114.010730  0.625492    5.389189    0
3     1  1924      0.940200      0.549894  191046.707627  0.344347  ... -14.231343     0.092089  120.689572  0.663725    0.661017   10
4     1  1925      0.962607      0.573863  184986.924460  0.278594  ... -14.146414     0.111918  115.521921  0.621929    2.604317    5

[5 rows x 14 columns]
"""
