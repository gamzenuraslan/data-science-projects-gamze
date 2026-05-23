# STEP 1 - Python Basics
"""
Bu bölümde Python'ın temel yapılarını öğreniyoruz.

Konular:
- Print kullanımı
- String işlemleri
- Sayılar ve operatörler
- Listeler
- Koşullu ifadeler
- Döngüler
- Küçük algoritma örnekleri

Amaç:
Python syntax yapısını öğrenmek ve programlama mantığını geliştirmek.
"""

# ---------------------------------------------
# 01 - PRINT & STRINGS
# ---------------------------------------------

# print() ekrana çıktı vermek için kullanılır.
print("Hello Data Science")
print("Python öğrenmeye başlıyoruz!")

# String ifadeler tek tırnak veya çift tırnak ile yazılabilir.
print("Gamze Nur Aslan")
print('Python Basics')

# String içinde tırnak kullanmak istersek escape karakteri kullanabiliriz.
print('Python\'a giriş yapıyoruz.')

# Çok satırlı string yazmak için üç tırnak kullanılır.
print("""Data Science
Python
Machine Learning""")

# \n bir alt satıra geçmek için kullanılır.
print("Python\nData Science")

# \t boşluk/tab bırakmak için kullanılır.
print("Python\tBasics")

# Değişken içinde string tutabiliriz.
message = "Welcome to Python"
print(message)

# String birleştirme
first_name = "Gamze"
last_name = "Aslan"

full_name = first_name + " " + last_name
print(full_name)

# f-string ile daha okunabilir formatlama yapabiliriz.
print(f"Hello, {full_name}!")

# String uzunluğunu bulma
text = "Data Science"
print(len(text))

# String indexleme
print(text[0])      # İlk karakter
print(text[-1])     # Son karakter

# String slicing
print(text[0:4])    # Data
print(text[5:])     # Science
print(text[::-1])   # Tersten yazdırma

# String metotları
city = "gaziantep"

print(city.upper())       # Büyük harfe çevirir
print(city.capitalize())  # İlk harfi büyük yapar
print(city.title())       # Her kelimenin ilk harfini büyük yapar

country = "TÜRKİYE"
print(country.lower())    # Küçük harfe çevirir

# Boşluk temizleme
word = "   Python   "
print(word.strip())

# String içinde arama
sentence = "Python is powerful and easy to learn."
print("Python" in sentence)
print("Java" in sentence)

# String değiştirme
print(sentence.replace("Python", "Data Science"))

# String bölme
technologies = "Python,Data Science,Machine Learning"
print(technologies.split(","))

# String tekrar ettirme
print("Python " * 3)

# format() kullanımı
language = "Python"
field = "Data Science"

print("{} is important for {}.".format(language, field))

# f-string kullanımı
print(f"{language} is important for {field}.")

# Mini örnek
name = "Gamze"
learning_topic = "Python"

print(f"{name} is learning {learning_topic} for Data Science :)")




