# ---------------------------------------------
# 03 — PANDAS SERIES
# ---------------------------------------------

# Pandas is one of the most important libraries in Data Science.
# Series is a one-dimensional labeled data structure.

import pandas as pd
import numpy as np

# ---------------------------------------------
# CREATING SERIES
# ---------------------------------------------

numbers = pd.Series([10, 20, 30, 40, 50])
print(numbers)

# ---------------------------------------------
# SERIES VALUES & INDEX
# ---------------------------------------------

print(numbers.values)
print(numbers.index)

# ---------------------------------------------
# CUSTOM INDEX
# ---------------------------------------------

students = pd.Series(
    [85, 90, 78],
    index=["Ali", "Ayse", "Mehmet"]
)

print(students)

# Accessing values
print(students["Ali"])
print(students["Ayse"])

# ---------------------------------------------
# SERIES OPERATIONS
# ---------------------------------------------

print(students + 10)
print(students.mean())
print(students.max())
print(students.min())

# ---------------------------------------------
# FILTERING
# ---------------------------------------------

print(students[students > 80])

# ---------------------------------------------
# STRING SERIES
# ---------------------------------------------

languages = pd.Series([
    "Python",
    "Java",
    "C++",
    "JavaScript"
])

print(languages)
print(languages.str.upper())
print(languages.str.lower())

# ---------------------------------------------
# CHECKING NULL VALUES
# ---------------------------------------------

data = pd.Series([10, np.nan, 30, np.nan, 50])

print(data)
print(data.isnull())
print(data.notnull())

# Fill missing values

print(data.fillna(0))

# ---------------------------------------------
# SORTING
# ---------------------------------------------

numbers = pd.Series([50, 10, 30, 20])

print(numbers.sort_values())
print(numbers.sort_values(ascending=False))

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

expenses = pd.Series(
    [150, 300, 200, 450],
    index=["Food", "Transport", "Books", "Shopping"]
)

print(expenses)
print(f"Total Expense: {expenses.sum()}")
print(f"Average Expense: {expenses.mean()}")
print(expenses[expenses > 200])