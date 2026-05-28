# ---------------------------------------------
# 05 — MINI DATA VISUALIZATION PROJECT
# ---------------------------------------------

# In this mini project, we analyze and visualize
# simple sales data using Pandas and Matplotlib.

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------
# CREATE DATASET
# ---------------------------------------------

data = {
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun"
    ],

    "Sales": [250, 320, 400, 380, 500, 550],

    "Expenses": [150, 180, 220, 200, 260, 300]
}

df = pd.DataFrame(data)
print(df)

# ---------------------------------------------
# CREATE PROFIT COLUMN
# ---------------------------------------------

df["Profit"] = df["Sales"] - df["Expenses"]
print(df)

# ---------------------------------------------
# TOTAL SALES & PROFIT
# ---------------------------------------------

print(f"Total Sales: {df['Sales'].sum()}")
print(f"Total Profit: {df['Profit'].sum()}")

# ---------------------------------------------
# BEST SALES MONTH
# ---------------------------------------------

best_month = df[
    df["Sales"] == df["Sales"].max()
]

print(best_month)

# ---------------------------------------------
# SALES LINE CHART
# ---------------------------------------------

plt.plot(
    df["Month"],
    df["Sales"],
    marker="o"
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()

# ---------------------------------------------
# SALES & EXPENSES COMPARISON
# ---------------------------------------------

plt.plot(
    df["Month"],
    df["Sales"],
    label="Sales"
)

plt.plot(
    df["Month"],
    df["Expenses"],
    label="Expenses"
)

plt.title("Sales vs Expenses")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.legend()
plt.show()

# ---------------------------------------------
# PROFIT BAR CHART
# ---------------------------------------------

plt.bar(
    df["Month"],
    df["Profit"]
)

plt.title("Monthly Profit")
plt.xlabel("Month")
plt.ylabel("Profit")
plt.show()

# ---------------------------------------------
# MINI ANALYSIS
# ---------------------------------------------

average_sales = df["Sales"].mean()

print(f"Average Sales: {average_sales}")

high_sales = df[
    df["Sales"] > average_sales
]

print(high_sales)