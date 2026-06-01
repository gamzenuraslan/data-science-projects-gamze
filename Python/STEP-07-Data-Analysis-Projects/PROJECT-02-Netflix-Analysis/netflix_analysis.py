import pandas as  pd
import matplotlib.pyplot as plt

df = pd.read_csv("netflix_titles.csv")
print(df.head())

print("---")

df.info()

print("---")

print(df.isnull().sum())

print("---")

# Dataset dimensions (rows, columns)
print(df.shape)

print("---")

print(df["type"].value_counts())

print("---")

content_type = df["type"].value_counts()
content_type.plot(kind="bar", color="lightpink")

plt.title("Netflix Content Type Distribution", fontsize=14)
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    horizontalalignment="right",
    fontsize=10,
    alpha=0.7
)
plt.tight_layout()

plt.show()

print("---")

country_counts = df["country"].value_counts()
print(country_counts.head(10))

print("---")

plt.figure(figsize=(10,5))
country_counts.head(10).plot(kind="bar", color="lightpink")
plt.title("Top 10 Countries on Netflix", fontsize=14)
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    horizontalalignment="right",
    fontsize=10,
    alpha=0.7
)
plt.tight_layout()

plt.show()

print("---")

print(df.columns)

print("---")

genre_counts = df["listed_in"].value_counts()
print(genre_counts.head(10))

print("---")

genres = df["listed_in"].str.split(", ")
genres_exploded = genres.explode()
print(genres_exploded.head(20))

print("---")

genre_counts = genres_exploded.value_counts()
print(genre_counts.head(10))
plt.figure(figsize=(10, 5))

genre_counts.head(10).plot(kind="bar", color="lightpink")

plt.title("Top 10 Genres on Netflix", fontsize=14)
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    horizontalalignment="right",
    fontsize=10,
    alpha=0.7
)
plt.tight_layout()

plt.show()
print("---")

year_counts = df["release_year"].value_counts()
year_counts = year_counts.sort_index()
print(year_counts)
plt.figure(figsize=(10,5))

plt.plot(year_counts.index, year_counts.values, marker="o", color="lightpink")

plt.title("Netflix Content Release Over Years", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    horizontalalignment="right",
    fontsize=10,
    alpha=0.7
)
plt.tight_layout()

plt.show()

print("---")

rating_counts = df["rating"].value_counts()
print(rating_counts.head(10))
plt.figure(figsize=(10, 5))

rating_counts.head(10).plot(kind="bar", color="lightpink")

plt.title("Netflix Rating Distribution", fontsize=14)
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.figtext(
    0.99,
    0.01,
    "PeonyCode",
    horizontalalignment="right",
    fontsize=10,
    alpha=0.7
)
plt.tight_layout()

plt.show()
