# ---------------------------------------------
# 05 — DATA ANALYSIS
# ---------------------------------------------

# In this section, we perform a small data analysis
# using Pandas and NumPy.

import pandas as pd
import numpy as np

# ---------------------------------------------
# CREATE DATASET
# ---------------------------------------------

data = {
    "Name": [
        "Gamze",
        "Nur",
        "Ayse",
        "Ali",
        "Mehmet"
    ],

    "Department": [
        "Data Science",
        "AI",
        "Machine Learning",
        "Python",
        "Data Science"
    ],

    "Age": [22, 25, 21, 28, 24],
    "Salary": [25000, 32000, 28000, 22000, 30000],
    "Experience": [1, 3, 2, 1, 4]
}

df = pd.DataFrame(data)
print(df)

# ---------------------------------------------
# BASIC ANALYSIS
# ---------------------------------------------

print(df.head())
print(df.info())
print(df.describe())

# ---------------------------------------------
# AVERAGE SALARY
# ---------------------------------------------

average_salary = df["Salary"].mean()
print(f"Average Salary: {average_salary}")

# ---------------------------------------------
# HIGHEST SALARY
# ---------------------------------------------

highest_salary = df["Salary"].max()
print(f"Highest Salary: {highest_salary}")

# ---------------------------------------------
# FILTERING
# ---------------------------------------------

high_salary = df[df["Salary"] > 27000]
print(high_salary)

# ---------------------------------------------
# GROUPBY
# ---------------------------------------------

department_salary = df.groupby(
    "Department"
)["Salary"].mean()

print(department_salary)

# ---------------------------------------------
# SORTING
# ---------------------------------------------

sorted_salary = df.sort_values(
    "Salary",
    ascending=False
)

print(sorted_salary)

# ---------------------------------------------
# ADD NEW COLUMN
# ---------------------------------------------

df["Bonus"] = df["Salary"] * 0.10

print(df)

# ---------------------------------------------
# MOST EXPERIENCED EMPLOYEE
# ---------------------------------------------

most_experienced = df[
    df["Experience"] == df["Experience"].max()
]

print(most_experienced)

# ---------------------------------------------
# NUMPY ANALYSIS
# ---------------------------------------------

salary_array = np.array(df["Salary"])

print(np.mean(salary_array))
print(np.max(salary_array))
print(np.min(salary_array))

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

# Employees older than 23

older_employees = df[df["Age"] > 23]
print(older_employees)

# Employees in Data Science department

data_science_team = df[
    df["Department"] == "Data Science"
]
print(data_science_team)

# Total salary
print(f"Total Salary: {df['Salary'].sum()}")