# ---------------------------------------------
# 02 - NUMBERS & OPERATORS
# ---------------------------------------------

# Integer (tam sayı) tanımlama
number1 = 10
number2 = 20

# Toplama işlemi
total = number1 + number2

# Ortalama hesaplama - 2'ye bölmemizin nedeni elimizde 2 sayı olması
average = total / 2

print(f"The total is: {total}")
print(f"The average is: {average}")

# Çıkarma işlemi
subtraction = number2 - number1
print(f"Subtraction result: {subtraction}")

# Çarpma işlemi
multiplication = number1 * number2
print(f"Multiplication result: {multiplication}")

# Bölme işlemi
division = number2 / number1
print(f"Division result: {division}")

# Üs alma işlemi
power = number1 ** 2
print(f"Power result: {power}")

# Mod alma işlemi
remainder = 25 % 4
print(f"Remainder: {remainder}")

# Tam sayı bölmesi
floor_division = 25 // 4
print(f"Floor division result: {floor_division}")

# Float veri tipi
pi = 3.14159
print(type(pi))

# Sayıyı yuvarlama
print(round(pi, 2))

# Mutlak değer alma
negative_number = -50
print(abs(negative_number))

# Veri tipi kontrolü
print(type(number1))
print(type(average))

# String -> Integer dönüşümü
age = "22"
age = int(age)

print(age)
print(type(age))

# Integer -> Float dönüşümü
score = 90
score = float(score)

print(score)
print(type(score))

# Karşılaştırma operatörleri
print(number1 == number2)
print(number1 != number2)
print(number1 < number2)
print(number1 > number2)

# İşlem önceliği
result1 = 4 * 5 - 2
result2 = 4 * (5 - 2)

print(result1)
print(result2)

# Kısa operatör kullanımı
x = 5

x += 10
print(x)

x *= 2
print(x)

# Mini örnek
exam1 = 80
exam2 = 90
exam3 = 100

average_exam = (exam1 + exam2 + exam3) / 3

print(f"Exam average: {average_exam}")