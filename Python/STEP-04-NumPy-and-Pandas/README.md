# STEP 4 — NumPy & Pandas 📊

Still learning Python even during Eid al-Adha 😄✨

In this step, we officially enter the world of real data.

Using NumPy and Pandas, we start learning:
- data analysis,
- table operations,
- numerical calculations,
- and data manipulation 🚀

NumPy and Pandas are two of the most widely used Python libraries in the fields of Data Science and Machine Learning.

---

## Topics 📚

### 01 — NumPy Basics
- Creating arrays
- Array dimensions
- Indexing & slicing
- Array functions

### 02 — NumPy Operations
- Mathematical operations
- Random numbers
- Reshaping arrays
- Filtering data
- Broadcasting

### 03 — Pandas Series
- Creating Series
- Indexing
- Filtering
- Missing values
- Sorting

### 04 — Pandas DataFrame
- Creating DataFrames
- Selecting rows & columns
- Filtering data
- Groupby operations
- Adding new columns

### 05 — Data Analysis
- Dataset analysis
- Salary analysis
- Groupby analysis
- Sorting data
- Statistical operations

---

## Goal 🎯

The goal of this step is to:
- understand data structures,
- analyze datasets,
- manipulate data efficiently,
- and prepare for real-world Data Science projects.

---

## Mini Example 🚀

```python
import pandas as pd

data = {
    "Name": ["Gamze", "Nur"],
    "Score": [90, 85]
}

df = pd.DataFrame(data)

print(df)