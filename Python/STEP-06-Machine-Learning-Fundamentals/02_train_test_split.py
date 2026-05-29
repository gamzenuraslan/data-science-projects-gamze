# ---------------------------------------------
# 02 — TRAIN TEST SPLIT
# ---------------------------------------------

# Before training a Machine Learning model,
# we usually split the dataset into:
#
# Training Data → Used to train the model.
# Test Data → Used to evaluate the model.

from sklearn.model_selection import train_test_split

# ---------------------------------------------
# SAMPLE DATASET
# ---------------------------------------------

study_hours = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

exam_scores = [
    45, 50, 55, 60, 70,
    75, 80, 85, 90, 95
]

# ---------------------------------------------
# FEATURES & TARGET
# ---------------------------------------------

# X = input data
# y = output data

X = [[hour] for hour in study_hours]
y = exam_scores

print(X)
print(y)

# ---------------------------------------------
# TRAIN TEST SPLIT
# ---------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data")
print(X_train)
print(y_train)
print("\nTest Data")
print(X_test)
print(y_test)

# ---------------------------------------------
# DATASET SIZE
# ---------------------------------------------

print(f"Total Samples: {len(X)}")
print(f"Training Samples: {len(X_train)}")
print(f"Test Samples: {len(X_test)}")

# ---------------------------------------------
# WHY TRAIN TEST SPLIT?
# ---------------------------------------------

# If we train and test on the same data,
# the model may memorize instead of learning.

# Train → Learn patterns
# Test → Measure performance

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

student_ages = [
    18, 19, 20, 21, 22,
    23, 24, 25, 26, 27
]

student_scores = [
    60, 65, 68, 72, 75,
    80, 84, 88, 90, 95
]

X = [[age] for age in student_ages]
y = student_scores

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nMini Exercise")
print("X Train:", X_train)
print("X Test:", X_test)