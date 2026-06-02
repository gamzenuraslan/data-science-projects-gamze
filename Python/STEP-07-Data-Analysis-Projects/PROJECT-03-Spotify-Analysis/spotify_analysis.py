import pandas as pd
import matplotlib.pyplot as plt

#print(plt.style.available) #Kullanabileceğiniz tüm hazır grafik temalarının listesini gösterir.
plt.style.use("ggplot") #Grafiği açık gri arka plan ve beyaz kılavuz çizgileriyle modern ve akademik bir tarzda süsler.
#plt.style.use("fivethirtyeight") #Grafiği ünlü veri gazeteciliği sitesi FiveThirtyEight gibi kalın çizgili, göze batan renkli ve açık mavi/gri arka planlı (infografik tarzında) yapar.

df = pd.read_csv("spotify.csv")
print(df.head())

print("---")

print(df.info())

print("---")

print(df.isnull().sum())

print("---")

print(df.shape)

print("---")

df = df.dropna()
print(df.isnull().sum())

print("---")

top_songs = df.sort_values(by=['popularity'], ascending=False)
print(top_songs[['track_name', 'artists', 'popularity']].head(10))

print("---")

df_unique = df.drop_duplicates(subset=["track_name"])
top_songs = df_unique.sort_values(
    by="popularity",
    ascending=False
)

print(
    top_songs[
        ["track_name", "artists", "popularity"]
    ].head(10)
)

print("---")

top_10 = top_songs.head(10).sort_values(by="popularity")

plt.figure(figsize=(12, 6))

plt.barh(
    top_10["track_name"],
    top_10["popularity"],
    color="lightpink"
)

plt.title("Top 10 Most Popular Songs on Spotify")
plt.xlabel("Popularity")
plt.ylabel("Track")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

artist_counts= df['artists'].value_counts()
print(artist_counts.head(10))

print("---")

top_artists = artist_counts.head(10)

plt.figure(figsize=(12, 6))

top_artists.sort_values().plot(
    kind="barh",
    color="lightpink"
)

plt.title("Top 10 Artists by Number of Tracks")
plt.xlabel("Number of Tracks")
plt.ylabel("Artist")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

genre_counts= df['track_genre'].value_counts()
print(genre_counts.head(10))

print("---")

top_genres = genre_counts.head(10)

plt.figure(figsize=(12, 6))

top_genres.sort_values().plot(
    kind="barh",
    color="lightpink"
)

plt.title("Top 10 Spotify Genres")
plt.xlabel("Number of Tracks")
plt.ylabel("Genre")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

explicit_counts = df['explicit'].value_counts()
print(explicit_counts)

print("---")

plt.figure(figsize=(8,5))
explicit_counts.plot(
    kind="barh",
    color="lightpink"
)
plt.title("Explicit vs Non-Explicit Songs")
plt.xlabel("Number of Tracks")
plt.ylabel("Explicit")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

genre_popularity = df.groupby("track_genre")["popularity"].mean()
genre_popularity = genre_popularity.sort_values(ascending=False)
print(genre_popularity.head(10))

print("---")

top_genre_popularity = genre_popularity.head(10).sort_values()
plt.figure(figsize=(12, 6))

top_genre_popularity.plot(
    kind="barh",
    color="lightpink"
)

plt.title("Top 10 Genres by Average Popularity")
plt.xlabel("Average Popularity")
plt.ylabel("Genre")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

plt.figure(figsize=(10, 6))

plt.scatter(
    df["danceability"],
    df["popularity"],
    alpha=0.3,
    color="purple"
)

plt.title("Popularity vs Danceability")
plt.xlabel("Danceability")
plt.ylabel("Popularity")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

plt.figure(figsize=(10, 6))

plt.scatter(
    df["energy"],
    df["popularity"],
    alpha=0.3,
    color="purple"
)

plt.title("Popularity vs Energy")
plt.xlabel("Energy")
plt.ylabel("Popularity")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

genre_valence = df.groupby("track_genre")["valence"].mean()
genre_valence = genre_valence.sort_values(ascending=False)
print(genre_valence.head(10))

print("---")

top_happy_genres = genre_valence.head(10).sort_values()

plt.figure(figsize=(12, 6))

top_happy_genres.plot(
    kind="barh",
    color="lightpink"
)

plt.title("Top 10 Happiest Genres")
plt.xlabel("Average Valence")
plt.ylabel("Genre")

plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    ha="right",
    fontsize=10,
    alpha=0.7
)

plt.tight_layout()
plt.show()

print("---")

numeric_columns = [
    "popularity",
    "danceability",
    "energy",
    "valence",
    "acousticness",
    "tempo"
]

correlation = df[numeric_columns].corr()
print(correlation)