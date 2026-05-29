# ---------------------------------------------
# 05 — MODEL EVALUATION
# ---------------------------------------------

# Model evaluation helps us understand
# how well our Machine Learning model performs.

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# ---------------------------------------------
# REGRESSION EVALUATION
# ---------------------------------------------

study_hours = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

exam_scores = [
    45, 50, 55, 60, 70,
    75, 80, 85, 90, 95
]

X = [[hour] for hour in study_hours]
y = exam_scores

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

regression_model = LinearRegression()
regression_model.fit(X_train, y_train)
predictions = regression_model.predict(X_test)

print("Regression Evaluation")
print("Actual Values:", y_test)
print("Predicted Values:", predictions)

mae = mean_absolute_error(y_test, predictions) #Modelin yaptığı tüm tahminlerin hata paylarının mutlak değerini alır ve ortalamasını hesaplar. Eksileri artıya çevirerek düz bir fark bulur.
#Örnek: mae sonucu 5.2 çıkarsa, modeliniz sınav notlarını ortalama 5.2 puanlık bir yanılma payı ile tahmin ediyor demektir. Anlaşılması ve yorumlanması çok kolaydır.
mse = mean_squared_error(y_test, predictions) #Hataların tek tek karesini alır ve ardından ortalamasını hesaplar.
#Örnek: Bir tahminde 2 puan, diğerinde 10 puan yanıldıysanız; kareleri 4 ve 100 yapar. MSE büyük hatayı çok daha görünür kılar.

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Mean Squared Error: {mse:.2f}")

# ---------------------------------------------
# CLASSIFICATION EVALUATION
# ---------------------------------------------

study_hours = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10
]

results = [
    0, 0, 0, 0, 1,
    1, 1, 1, 1, 1
]

X = [[hour] for hour in study_hours]
y = results

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

classification_model = LogisticRegression()
classification_model.fit(X_train, y_train)
predictions = classification_model.predict(X_test)

print("\nClassification Evaluation")
print("Actual Values:", y_test)
print("Predicted Values:", predictions)

accuracy = accuracy_score(y_test, predictions) #Modelinizin toplam test verileri içinde yüzde kaç oranında doğru tahmin yaptığını gösterir.
matrix = confusion_matrix(y_test, predictions)
"""Doğruluk oranı bazen yanıltıcı olabilir (örneğin verideki herkes "Geçti" ise model herkese "Geçti" diyerek yüksek skor alabilir). 
   Hata matrisi, modelin tam olarak nerede kafasının karıştığını gösteren bir tablodur.
   2x2'lik bir matris (0 ve 1 sınıfları için) ekrana genelde şöyle basılır:
   text[[TN  FP]
        [FN  TP]]
   TN (True Negative): Modelin "0" dediği ve gerçekten "0" olanlar (Doğru Negatif).FP (False Positive): Modelin "1" dediği ama aslında "0" olanlar (Yalan Hatlar / Boşa Alarm).
   FN (False Negative): Modelin "0" dediği ama aslında "1" olanlar (Kaçırılanlar).TP (True Positive): Modelin "1" dediği ve gerçekten "1" olanlar (Doğru Pozitif)."""

print(f"Accuracy Score: {accuracy:.2f}")
print("Confusion Matrix:")
print(matrix)

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

# Salary prediction evaluation
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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)
salary_predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, salary_predictions)

print("\nSalary Prediction Evaluation")
print(f"Mean Absolute Error: {mae:.2f}")