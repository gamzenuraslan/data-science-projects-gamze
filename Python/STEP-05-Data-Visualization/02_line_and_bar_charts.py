# ---------------------------------------------
# 02 — LINE & BAR CHARTS 📊
# ---------------------------------------------

import matplotlib.pyplot as plt

# ---------------------------------------------
# LINE CHART
# ---------------------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [250, 300, 450, 400, 500]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.show()

# ---------------------------------------------
# MULTIPLE LINE CHART
# ---------------------------------------------

expenses = [150, 180, 220, 200, 260]

plt.plot(months, sales, label="Sales")
plt.plot(months, expenses, label="Expenses")
plt.title("Sales vs Expenses")
plt.xlabel("Months")
plt.ylabel("Amount")
plt.legend()
plt.show()

# ---------------------------------------------
# BAR CHART
# ---------------------------------------------

students = ["Ali", "Ayse", "Mehmet", "Gamze"]
scores = [75, 90, 85, 95]

plt.bar(students, scores)
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

# ---------------------------------------------
# HORIZONTAL BAR CHART
# ---------------------------------------------

plt.barh(students, scores)
plt.title("Horizontal Bar Chart")
plt.show()

# ---------------------------------------------
# CUSTOM COLORS
# ---------------------------------------------

colors = ["blue", "green", "orange", "red"]

plt.bar(students, scores, color=colors)
plt.title("Colored Bar Chart")
plt.show()

# ---------------------------------------------
# COMPARISON BAR CHART
# ---------------------------------------------

products = ["Laptop", "Phone", "Tablet"]
sales_2024 = [120, 200, 150]
sales_2025 = [180, 250, 170]

x = range(len(products))

plt.bar(x, sales_2024, width=0.4, label="2024")

plt.bar(
    [i + 0.4 for i in x],
    sales_2025,
    width=0.4,
    label="2025"
)

plt.xticks(
    [i + 0.2 for i in x],
    products
)

plt.legend()
plt.title("Product Sales Comparison")
plt.show()

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visitors = [120, 150, 180, 130, 200]

plt.plot(days, visitors, marker="o")
plt.title("Website Visitors")
plt.xlabel("Days")
plt.ylabel("Visitors")
plt.grid(True)
plt.show()