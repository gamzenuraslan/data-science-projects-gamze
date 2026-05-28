# ---------------------------------------------
# 04 — PANDAS VISUALIZATION
# ---------------------------------------------

# Pandas can work together with Matplotlib
# for simple and powerful data visualization.

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------
# CREATE DATAFRAME
# ---------------------------------------------

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [250, 300, 450, 400, 500],
    "Expenses": [150, 180, 220, 200, 260]
}

df = pd.DataFrame(data)

print(df)

# ---------------------------------------------
# LINE CHART
# ---------------------------------------------

df.plot(
    x="Month",
    y="Sales"
)

plt.title("Monthly Sales")
plt.show()

# ---------------------------------------------
# MULTIPLE LINE CHART
# ---------------------------------------------

df.plot(
    x="Month",
    y=["Sales", "Expenses"]
)

plt.title("Sales vs Expenses")
plt.show()

# ---------------------------------------------
# BAR CHART
# ---------------------------------------------

df.plot(
    x="Month",
    y="Sales",
    kind="bar"
)

plt.title("Monthly Sales Bar Chart")
plt.show()

# ---------------------------------------------
# HISTOGRAM
# ---------------------------------------------

df["Sales"].plot(kind="hist")

plt.title("Sales Distribution")
plt.show()

# ---------------------------------------------
# PIE CHART
# ---------------------------------------------

department_data = {
    "Department": [
        "Data Science",
        "AI",
        "Machine Learning",
        "Python"
    ],

    "Students": [40, 25, 20, 15]
}

department_df = pd.DataFrame(department_data)

department_df.plot(
    y="Students",
    labels=department_df["Department"],
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Department Distribution")
plt.ylabel("")
plt.show()

# ---------------------------------------------
# SCATTER PLOT
# ---------------------------------------------

df.plot(
    x="Sales",
    y="Expenses",
    kind="scatter"
)

plt.title("Sales vs Expenses")
plt.show()


# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

students = {
    "Name": ["Ali", "Ayse", "Gamze", "Nur"],
    "Score": [75, 90, 95, 85]
}

student_df = pd.DataFrame(students)

student_df.plot(
    x="Name",
    y="Score",
    kind="bar"
)

plt.title("Student Scores")
plt.show()