# STEP 6 — Machine Learning Fundamentals 🤖

In this step, we take our first real steps into Machine Learning.

After learning Python, NumPy, Pandas, and Data Visualization, we now start building simple models that can learn from data and make predictions.

Machine Learning allows computers to:
- learn patterns from data,
- make predictions,
- classify information,
- and support decision-making processes.

---

## Topics 📚

### 01 — Introduction to Machine Learning
- What is Machine Learning?
- Traditional programming vs Machine Learning
- Supervised Learning
- Unsupervised Learning
- Reinforcement Learning

### 02 — Train Test Split
- Training data
- Test data
- Features and target values
- Why splitting data matters

### 03 — Linear Regression
- Regression problems
- Creating a Linear Regression model
- Training the model
- Making predictions

### 04 — Classification
- Classification problems
- Logistic Regression
- Predicting categories
- Prediction probabilities

### 05 — Model Evaluation
- Regression evaluation
- Classification evaluation
- Mean Absolute Error
- Mean Squared Error
- Accuracy Score
- Confusion Matrix

---

## Goal 🎯

The goal of this step is to:
- understand the basic logic of Machine Learning,
- train simple models,
- make predictions,
- and evaluate model performance.

---

## Mini Example 🚀

```python
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [45, 55, 65, 75, 85]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)