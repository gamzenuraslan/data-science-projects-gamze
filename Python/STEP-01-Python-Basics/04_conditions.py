# ---------------------------------------------
# 04 - CONDITIONS
# ---------------------------------------------

# Koşullu ifadeler programın belirli durumlara göre karar vermesini sağlar.

age = 20

# if yapısı
if age >= 18:
    print("You are an adult.")

# if - else yapısı
number = 7

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if - elif - else yapısı
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:
    print("Failed")

# Karşılaştırma operatörleri
x = 10
y = 20

print(x == y)   # Eşit mi?
print(x != y)   # Eşit değil mi?
print(x > y)    # Büyük mü?
print(x < y)    # Küçük mü?
print(x >= y)   # Büyük eşit mi?
print(x <= y)   # Küçük eşit mi?

# Mantıksal operatörler
username = "gamze"
password = "1234"

if username == "gamze" and password == "1234":
    print("Login successful")
else:
    print("Login failed")

# or operatörü
weather = "rainy"

if weather == "rainy" or weather == "snowy":
    print("Take an umbrella")

# not operatörü
is_logged_in = False

if not is_logged_in:
    print("Please login")

# Liste içinde eleman kontrolü
cities = ["Ankara", "Istanbul", "Gaziantep"]

if "Gaziantep" in cities:
    print("City found")

# String karşılaştırma
language = "Python"

if language == "Python":
    print("Welcome to Data Science 🐍")

# İç içe koşullar
age = 22
has_ticket = True

if age >= 18:
    if has_ticket:
        print("You can enter")
    else:
        print("Ticket required")

# Ternary kullanım
number = 10
result = "Positive" if number > 0 else "Negative"
print(result)

# Mini örnek - kullanıcı not sistemi
exam_score = 72

if exam_score >= 85:
    print("Excellent")
elif exam_score >= 70:
    print("Good")
elif exam_score >= 50:
    print("Passed")
else:
    print("Failed")