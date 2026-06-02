# 🎵 PROJECT 03 — Spotify Data Analysis

## Overview

This project explores a large Spotify dataset using Python, Pandas, and Matplotlib.

The goal of this project is to analyze music-related data and uncover patterns in song popularity, artists, genres, explicit content, and audio features.

Throughout this project, I practiced:

* Data exploration
* Data cleaning
* Data visualization
* Statistical analysis
* Correlation analysis
* Extracting insights from real-world datasets

---

## Dataset

This project uses the **Spotify Tracks Dataset** from Kaggle.

Dataset Source:

📊 https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset

The dataset contains over **114,000 Spotify tracks** and includes information such as:

* Track Name
* Artist
* Album
* Popularity
* Genre
* Danceability
* Energy
* Valence
* Tempo
* Explicit Content
* Acousticness
* Instrumentalness

---

## Technologies Used

* Python 🐍
* Pandas 📊
* Matplotlib 📈

---

## Project Steps

### 1. Dataset Exploration

```python
df.head()
df.info()
df.shape
df.isnull().sum()
```

Explored dataset structure, data types, and missing values.

---

### 2. Data Cleaning

```python
df = df.dropna()
```

Removed missing values and prepared the dataset for analysis.

---

### 3. Popular Song Analysis

Identified the most popular songs based on Spotify popularity scores.

Visualization:

🎵 Top 10 Most Popular Songs on Spotify

---

### 4. Artist Analysis

Analyzed artists with the highest number of tracks in the dataset.

Visualization:

🎤 Top 10 Artists by Number of Tracks

---

### 5. Genre Analysis

Explored the most common music genres available in the dataset.

Visualization:

🎭 Top 10 Spotify Genres

---

### 6. Explicit Content Analysis

Compared explicit and non-explicit songs.

Visualization:

🚫 Explicit vs Non-Explicit Songs

---

### 7. Genre Popularity Analysis

Calculated average popularity scores by genre.

Visualization:

🔥 Top 10 Genres by Average Popularity

---

### 8. Danceability & Popularity

Analyzed the relationship between danceability and popularity.

Visualization:

💃 Popularity vs Danceability

---

### 9. Energy & Popularity

Explored whether energetic songs tend to be more popular.

Visualization:

⚡ Popularity vs Energy

---

### 10. Valence Analysis

Analyzed genres with the highest average valence scores (happier music).

Visualization:

😊 Top 10 Happiest Genres

---

### 11. Correlation Analysis

Investigated relationships between audio features such as:

* Popularity
* Danceability
* Energy
* Valence
* Acousticness
* Tempo

```python
df[numeric_columns].corr()
```

---

## Key Insights 📊

After analyzing the dataset, I discovered several interesting patterns:

* Some highly popular songs appear across multiple genres.
* A small number of artists contribute a significant number of tracks.
* Certain genres consistently achieve higher popularity scores.
* Danceability and popularity show some positive relationship.
* Energy alone does not guarantee higher popularity.
* Explicit songs represent a smaller portion of the dataset.
* Different genres exhibit noticeably different emotional characteristics through valence scores.

---

## What I Learned 🚀

This project helped me practice:

* Working with large datasets
* Data cleaning techniques
* Grouping and aggregation with Pandas
* Creating professional visualizations
* Performing exploratory data analysis (EDA)
* Understanding relationships between variables
* Extracting meaningful business insights from data

This project represents one of my most comprehensive Data Analysis projects so far.

---

## Future Improvements

* Interactive dashboards with Plotly
* Advanced correlation visualizations
* Recommendation system experiments
* Machine Learning models
* Genre clustering analysis

---

## Support ⭐

If you found this project useful, consider:

⭐ Starring the repository

🍴 Forking the project

👨‍💻 Following my GitHub journey

📚 Reading my Medium articles

Your support motivates me to continue creating Data Science and Data Analysis content.

---

## Connect With Me 🌐

GitHub:

* https://github.com/GamzeNurAslan

Medium:

* https://medium.com/@aslangamzenur079

LinkedIn:

* https://www.linkedin.com/in/gamze-nur-aslan2707/

---

Thank you for visiting this project! 🚀

Made with ❤️ and PeonyCode_GNA 🌸
