# ---------------------------------------------
# 01 — INTRODUCTION TO MACHINE LEARNING
# ---------------------------------------------

# Machine Learning is a field of Artificial Intelligence.
# It allows computers to learn from data and make predictions.

# Instead of writing rules manually, we train models with data.

# Example:
# Traditional programming:
# input + rules = output

# Machine Learning:
# input + output = rules/model


# ---------------------------------------------
# TYPES OF MACHINE LEARNING
# ---------------------------------------------

# 1. Supervised Learning
# The model learns from labeled data.
# Example: Predicting house prices.

# 2. Unsupervised Learning
# The model finds patterns in unlabeled data.
# Example: Customer segmentation.

# 3. Reinforcement Learning
# The model learns by trial and error.
# Example: Game-playing AI.


# ---------------------------------------------
# SIMPLE DATASET EXAMPLE
# ---------------------------------------------

# Study hours and exam scores

study_hours = [1, 2, 3, 4, 5]
exam_scores = [45, 55, 65, 75, 85]

print(study_hours)
print(exam_scores)

# ---------------------------------------------
# BASIC IDEA
# ---------------------------------------------

# As study hours increase, exam scores also increase.
# A machine learning model can learn this pattern.

for hour, score in zip(study_hours, exam_scores):
    print(f"Study Hours: {hour} | Exam Score: {score}")

# ---------------------------------------------
# SIMPLE PREDICTION LOGIC
# ---------------------------------------------

# This is not a real ML model yet.
# It is just a simple rule to understand prediction logic.

def predict_score(study_hour):
    return 35 + (study_hour * 10)

predicted_score = predict_score(6)
print(f"Predicted score for 6 study hours: {predicted_score}")

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

new_hours = [2, 4, 6, 8]

for hour in new_hours:
    prediction = predict_score(hour)

    print(f"If you study {hour} hours, predicted score is {prediction}")