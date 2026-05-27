# ---------------------------------------------
# 04 — PANDAS DATAFRAME
# ---------------------------------------------

# DataFrame is a two-dimensional data structure in Pandas.
# It looks like a table with rows and columns.

import pandas as pd

# ---------------------------------------------
# CREATING DATAFRAME
# ---------------------------------------------

data = {
    "Name": ["Gamze", "Nur", "Ayse", "Ali"],
    "Age": [22, 25, 21, 28],
    "Department": [
        "Data Science",
        "Python",
        "Machine Learning",
        "AI"
    ],
    "Score": [90, 85, 95, 80]
}

df = pd.DataFrame(data)
print(df)

# ---------------------------------------------
# BASIC INFORMATION
# ---------------------------------------------

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())

# ---------------------------------------------
# SELECTING COLUMNS
# ---------------------------------------------

print(df["Name"])
print(df[["Name", "Score"]])

# ---------------------------------------------
# SELECTING ROWS
# ---------------------------------------------

print(df.iloc[0])
print(df.iloc[1:3])

# ---------------------------------------------
# FILTERING
# ---------------------------------------------

high_scores = df[df["Score"] > 85]
print(high_scores)


# Multiple conditions

result = df[
    (df["Score"] > 85) &
    (df["Age"] < 25)
]

print(result)

# ---------------------------------------------
# ADDING NEW COLUMN
# ---------------------------------------------

df["Passed"] = df["Score"] >= 85
print(df)

# ---------------------------------------------
# SORTING
# ---------------------------------------------

print(df.sort_values("Score"))
print(df.sort_values("Score", ascending=False))

# ---------------------------------------------
# GROUPBY
# ---------------------------------------------

grouped = df.groupby("Department")["Score"].mean()
print(grouped)

# ---------------------------------------------
# DROP COLUMN
# ---------------------------------------------

df = df.drop("Passed", axis=1)
print(df)

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

sales_data = {
    "Product": ["Laptop", "Phone", "Tablet", "Keyboard"],
    "Price": [25000, 15000, 10000, 2000],
    "Sales": [5, 10, 7, 20]
}

sales_df = pd.DataFrame(sales_data)
print(sales_df)

sales_df["Revenue"] = (
    sales_df["Price"] * sales_df["Sales"]
)

print(sales_df)
print(f"Total Revenue: {sales_df['Revenue'].sum()}")