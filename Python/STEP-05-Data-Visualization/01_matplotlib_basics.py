# ---------------------------------------------
# 01 — MATPLOTLIB BASICS
# ---------------------------------------------

# Matplotlib is one of the most popular libraries
# for data visualization in Python.

import matplotlib.pyplot as plt

# ---------------------------------------------
# BASIC LINE CHART
# ---------------------------------------------

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)
plt.show()

# ---------------------------------------------
# ADDING TITLE & LABELS
# ---------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [250, 300, 450, 400, 500]

plt.plot(months, sales)
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# ---------------------------------------------
# CHANGING LINE STYLE
# ---------------------------------------------

plt.plot(
    months,
    sales,
    linestyle="--",
    marker="o"
)

plt.title("Sales Report")
plt.show()

# ---------------------------------------------
# MULTIPLE LINES
# ---------------------------------------------

expenses = [150, 180, 200, 190, 250]

plt.plot(months, sales, label="Sales")
plt.plot(months, expenses, label="Expenses")
plt.legend()
plt.show()

# ---------------------------------------------
# GRID
# ---------------------------------------------

plt.plot(months, sales)
plt.grid(True)
plt.show()

# ---------------------------------------------
# FIGURE SIZE
# ---------------------------------------------

plt.figure(figsize=(8, 4))
plt.plot(months, sales)
plt.title("Figure Size Example")
plt.show()

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

temperature = [18, 20, 25, 28, 30, 35]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

plt.plot(days, temperature, marker="o")
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature")
plt.show()