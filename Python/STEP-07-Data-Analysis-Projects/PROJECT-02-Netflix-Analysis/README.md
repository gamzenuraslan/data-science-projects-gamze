# 🎬 PROJECT 02 — Netflix Data Analysis

## Overview

This project explores the Netflix Titles dataset using Python, Pandas, and Matplotlib.

The goal of this project is to analyze Netflix content and extract meaningful insights from movies, TV shows, genres, countries, ratings, and release years.

Throughout this project, I practiced:

* Data exploration
* Data cleaning
* Handling missing values
* Data transformation
* Data visualization
* Insight generation

---

## Dataset

The dataset contains information about Netflix movies and TV shows.

Dataset Source:
📊 Kaggle — Netflix Titles Dataset

https://www.kaggle.com/datasets/shivamb/netflix-shows


### Columns

| Column       | Description           |
| ------------ | --------------------- |
| show_id      | Unique content ID     |
| type         | Movie or TV Show      |
| title        | Content title         |
| director     | Director name         |
| cast         | Cast members          |
| country      | Production country    |
| date_added   | Date added to Netflix |
| release_year | Release year          |
| rating       | Content rating        |
| duration     | Duration              |
| listed_in    | Genre categories      |
| description  | Content description   |

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

### 2. Content Type Analysis

```python
df["type"].value_counts()
```

Analyzed the distribution of:

* Movies
* TV Shows

### 3. Country Analysis

```python
df["country"].value_counts()
```

Identified the countries with the highest number of Netflix titles.

### 4. Genre Analysis

```python
str.split()
explode()
```

Separated multiple genres and analyzed the most popular categories.

### 5. Release Year Analysis

```python
df["release_year"].value_counts()
```

Analyzed how Netflix content production changed over time.

### 6. Rating Analysis

```python
df["rating"].value_counts()
```

Explored the distribution of content ratings.

---

## Key Insights 📊

After analyzing the dataset, I found that:

* Movies significantly outnumber TV Shows on Netflix.
* The United States has the highest number of titles in the dataset.
* India ranks second in content production.
* International Movies is the most common genre.
* Dramas and Comedies are among the most popular categories.
* Netflix content production increased rapidly after 2010.
* TV-MA and TV-14 are the most common content ratings.

---

## What I Learned 🚀

This project helped me practice:

* Working with real-world datasets
* Handling missing values
* Cleaning and transforming data
* Using Pandas for advanced analysis
* Creating visualizations with Matplotlib
* Extracting meaningful insights from data

This project represents another step forward in my Data Analysis journey.

---

## Future Improvements

* Create interactive dashboards
* Perform advanced genre analysis
* Explore content recommendation techniques
* Apply Machine Learning models
* Analyze trends in greater detail

---

## Support ⭐

If you found this project helpful, consider:

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
