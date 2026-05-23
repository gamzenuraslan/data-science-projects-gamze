# ---------------------------------------------
# 05 - LOOPS
# ---------------------------------------------

# Döngüler tekrar eden işlemleri otomatik şekilde yapmamızı sağlar.

# ---------------------------------------------
# FOR LOOP
# ---------------------------------------------

numbers = [10, 20, 30, 40, 50]

# Liste üzerinde gezinme
for number in numbers:
    print(number)

# String üzerinde gezinme
name = "Python"

for letter in name:
    print(letter)

# range() kullanımı
for i in range(5):
    print(i)

# Başlangıç ve bitiş değeri verme
for i in range(1, 6):
    print(i)

# Adım sayısı belirleme
for i in range(0, 10, 2):
    print(i)

# Liste elemanlarını toplama
total = 0

for number in numbers:
    total += number

print(f"Total: {total}")

# continue kullanımı
for number in numbers:
    if number == 30:
        continue

    print(number)

# break kullanımı
for number in numbers:
    if number == 40:
        break

    print(number)

# İç içe döngüler
letters = ["A", "B", "C"]

for letter in letters:
    for number in numbers:
        print(letter, number)

# enumerate() kullanımı
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# ---------------------------------------------
# WHILE LOOP
# ---------------------------------------------

# while belirli bir koşul True olduğu sürece çalışır.

x = 1

while x <= 5:
    print(x)
    x += 1

# Kullanıcıdan sayı alma örneği
counter = 0

while counter < 3:
    print("Python Basics")
    counter += 1

# break kullanımı
number = 1

while True:
    print(number)

    if number == 5:
        break

    number += 1

# continue kullanımı
number = 0

while number < 10:
    number += 1

    if number % 2 == 0:
        continue

    print(number)

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

# 1'den 10'a kadar sayıların karelerini yazdırma

for i in range(1, 11):
    print(f"{i} squared = {i ** 2}")

# Çift sayıları bulma

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# Faktöriyel hesabı

factorial = 1

for i in range(1, 6):
    factorial *= i

print(f"Factorial: {factorial}")