# 📊 PROJECT 01 — Sales Data Analysis

## Overview

This is my first Data Analysis project using Python, Pandas, and Matplotlib.

The goal of this project is to analyze a simple sales dataset and extract meaningful insights from the data.

Throughout this project, I practiced:

* Reading CSV files
* Exploring datasets
* Creating new features
* Performing statistical analysis
* Filtering data
* Visualizing data with charts

---

## Dataset

The dataset contains monthly sales and expense information.

### Columns

| Column   | Description        |
| -------- | ------------------ |
| Month    | Month name         |
| Sales    | Total sales amount |
| Expenses | Total expenses     |
| Profit   | Sales - Expenses   |

---

## Technologies Used

* Python 🐍
* Pandas 📊
* Matplotlib 📈

---

## Project Steps

### 1. Reading the Dataset

```python
df = pd.read_csv("sales_data.csv")
```

### 2. Exploring the Dataset

```python
df.head()
df.info()
df.describe()
```

### 3. Creating a New Column

```python
df["Profit"] = df["Sales"] - df["Expenses"]
```

### 4. Statistical Analysis

* Total Sales
* Total Profit
* Average Sales
* Average Profit
* Best Sales Month
* Worst Sales Month

### 5. Data Visualization

```python
plt.plot(df["Month"], df["Sales"], marker="o")
```

---

## Key Insights 📊

After analyzing the dataset, I found that:

* December had the highest sales performance.
* January had the lowest sales performance.
* Sales generally increased throughout the year.
* Profit increased alongside sales.
* Higher sales months generated higher profits.

---

## What I Learned 🚀

This project helped me practice:

* Working with real datasets
* Using Pandas for data analysis
* Creating new columns
* Filtering data
* Generating insights from data
* Building visualizations with Matplotlib

This project marks my first step into real-world data analysis.

---

## Future Improvements

* Add more visualizations
* Analyze larger datasets
* Perform trend analysis
* Create interactive dashboards

---

## Support ⭐

If you found this project helpful, consider:

⭐ Starring the repository

🍴 Forking the project

👨‍💻 Following my GitHub journey

📚 Reading my Medium articles

Your support motivates me to continue learning and sharing my Data Science journey.

---

## Connect With Me 🌐

GitHub:
- https://github.com/GamzeNurAslan

Medium:
- https://medium.com/@aslangamzenur079

LinkedIn:
- https://www.linkedin.com/in/gamze-nur-aslan2707/

---

Thank you for visiting this project! 🚀

Made with ❤️ and PeonyCode_GNA