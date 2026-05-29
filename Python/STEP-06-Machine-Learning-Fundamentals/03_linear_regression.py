# ---------------------------------------------
# 03 — LINEAR REGRESSION
# ---------------------------------------------

# Linear Regression is one of the simplest
# Machine Learning algorithms.

# It is used to predict continuous values.
#
# Examples:
# - House prices
# - Salary prediction
# - Sales forecasting

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ---------------------------------------------
# DATASET
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

X = [[hour] for hour in study_hours]
y = exam_scores

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

model = LinearRegression()

# ---------------------------------------------
# TRAIN MODEL
# ---------------------------------------------

model.fit(X_train, y_train) #Machine Learning'e giriş yaptım denilen yere geldinnn, tebriklerrrr :)))
print("Model trained successfully :)")

# ---------------------------------------------
# PREDICTIONS
# ---------------------------------------------

prediction = model.predict([[6]])
print(f"Predicted score for 6 study hours: {prediction[0]:.2f}") #Sayının virgülden sonra sadece 2 basamak (float) gösterilmesini sağlar.


# Multiple predictions
new_hours = [[2], [5], [8]]
predictions = model.predict(new_hours)

print(predictions)

# ---------------------------------------------
# MODEL INFORMATION
# ---------------------------------------------

print(f"Coefficient: {model.coef_[0]:.2f}") #Çalışma saatinin sınav notunu ne kadar etkilediğini gösteren katsayıdır.
print(f"Intercept: {model.intercept_:.2f}") #Doğrunun y-eksenini kestiği noktadır (matematikteki sabit terim veya \(c\) değeri).
#Kodlarınız ekrana şu çıktıları vermiş olsun:Coefficient: 6.50Intercept: 45.00Bu durumda modelinizin kurduğu formül şudur:
#Not = (6.50 * Saat) + 45.00
#Bir önceki adımda yaptığınız 6 saatlik çalışma tahmini de bu formülle hesaplanır: \((6.50 \times 6) + 45.00 = 84.00\)

# ---------------------------------------------
# TEST DATA PREDICTIONS
# ---------------------------------------------

test_predictions = model.predict(X_test)

print("\nActual Values")
print(y_test)
print("\nPredicted Values")
print(test_predictions)

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

# Predict salary based on years of experience
experience = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

salary = [
    25000, 30000, 35000, 40000, 45000,
    50000, 55000, 60000, 65000, 70000
]

X = [[year] for year in experience]
y = salary

model = LinearRegression()
model.fit(X, y)
predicted_salary = model.predict([[12]])

print(
    f"\nPredicted salary for 12 years experience: "
    f"{predicted_salary[0]:.2f}"
)
