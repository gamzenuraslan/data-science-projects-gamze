# ---------------------------------------------
# 04 — CLASSIFICATION
# ---------------------------------------------

# Classification is used when we want to predict
# categories or labels.

# Examples:
# - Pass / Fail
# - Spam / Not Spam
# - Fraud / Not Fraud

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# ---------------------------------------------
# DATASET
# ---------------------------------------------

# Study Hours -> Pass(1) / Fail(0)
study_hours = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

results = [
    0, 0, 0, 0, 1,
    1, 1, 1, 1, 1
]

# ---------------------------------------------
# FEATURES & TARGET
# ---------------------------------------------

X = [[hour] for hour in study_hours]
y = results

# ---------------------------------------------
# TRAIN TEST SPLIT
# ---------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------------------------------------------
# CREATE MODEL
# ---------------------------------------------

model = LogisticRegression()

# ---------------------------------------------
# TRAIN MODEL
# ---------------------------------------------

model.fit(X_train, y_train)
print("Classification model trained successfully!")

# ---------------------------------------------
# PREDICTIONS
# ---------------------------------------------

prediction = model.predict([[3]])
print(f"Prediction for 3 study hours: {prediction[0]}")


prediction = model.predict([[8]])
print(f"Prediction for 8 study hours: {prediction[0]}")

# ---------------------------------------------
# PREDICTION PROBABILITIES
# ---------------------------------------------

probability = model.predict_proba([[6]])

print(probability)
print(
    f"Pass Probability: "
    f"{probability[0][1] * 100:.2f}%"
)

# ---------------------------------------------
# TEST PREDICTIONS
# ---------------------------------------------

predictions = model.predict(X_test)

print("\nActual Values")
print(y_test)
print("\nPredicted Values")
print(predictions)

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

# Age -> Adult(1) / Child(0)
ages = [
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28
]

labels = [
    0, 0, 0, 0, 1,
    1, 1, 1, 1, 1
]

X = [[age] for age in ages]
y = labels

model = LogisticRegression()
model.fit(X, y)
prediction = model.predict([[21]])
print(
    f"\nIs a 21-year-old an adult? "
    f"{prediction[0]}"
)

"""Linear Regression → sayı tahmini (maaş, fiyat, satış)
   Classification → kategori tahmini (evet/hayır, geçti/kaldı, spam/değil)"""