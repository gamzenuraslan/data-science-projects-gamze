# ---------------------------------------------
# 03 — SCATTER PLOT & HISTOGRAM
# ---------------------------------------------

import matplotlib.pyplot as plt

# ---------------------------------------------
# SCATTER PLOT
# ---------------------------------------------

study_hours = [1, 2, 3, 4, 5, 6, 7]
exam_scores = [45, 50, 60, 65, 75, 85, 90]

plt.scatter(study_hours, exam_scores)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.show()

# ---------------------------------------------
# SCATTER PLOT WITH SIZE
# ---------------------------------------------

ages = [18, 20, 22, 24, 26]
salaries = [15000, 18000, 22000, 26000, 30000]
sizes = [100, 200, 300, 400, 500]

plt.scatter(ages, salaries, s=sizes)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.show()

# ---------------------------------------------
# HISTOGRAM
# ---------------------------------------------

scores = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

plt.hist(scores)
plt.title("Exam Score Distribution")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------
# HISTOGRAM WITH BINS
# ---------------------------------------------

plt.hist(scores, bins=5)
plt.title("Score Distribution with Bins")
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.show()

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

heights = [150, 155, 160, 165, 170, 175, 180, 185, 190]

plt.hist(heights, bins=4)
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
plt.show()