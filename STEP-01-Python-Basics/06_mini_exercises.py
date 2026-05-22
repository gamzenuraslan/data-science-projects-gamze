# ---------------------------------------------
# 06 - MINI EXERCISES
# ---------------------------------------------

# Bu bölümde öğrendiğimiz temel Python konularını küçük alıştırmalarla pekiştiriyoruz.

# ---------------------------------------------
# 01 - Kullanıcıdan Veri Alma
# ---------------------------------------------

name = input("Enter your name: ")

print(f"Hello, {name}! Welcome to Python Basics")

# ---------------------------------------------
# 02 - Sayı Alma ve Toplama
# ---------------------------------------------

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

total = number1 + number2

print(f"Total: {total}")

# ---------------------------------------------
# 03 - Ortalama Hesaplama
# ---------------------------------------------

exam1 = int(input("Enter first exam score: "))
exam2 = int(input("Enter second exam score: "))
exam3 = int(input("Enter third exam score: "))

average = (exam1 + exam2 + exam3) / 3

print(f"Average score: {average}")

# ---------------------------------------------
# 04 - Tek / Çift Sayı Kontrolü
# ---------------------------------------------

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# ---------------------------------------------
# 05 - Faktöriyel Hesaplama
# ---------------------------------------------

number = int(input("Enter a number for factorial: "))

factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"{number}! = {factorial}")

# ---------------------------------------------
# 06 - Asal Sayı Kontrolü
# ---------------------------------------------

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

# ---------------------------------------------
# 07 - Basamak Toplamı
# ---------------------------------------------

number = int(input("Enter a number: "))

total = 0

for digit in str(number):
    total += int(digit)

print(f"Digit total: {total}")

# ---------------------------------------------
# 08 - Listedeki En Büyük ve En Küçük Sayı
# ---------------------------------------------

numbers = []

for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print(f"Numbers: {numbers}")
print(f"Maximum number: {max(numbers)}")
print(f"Minimum number: {min(numbers)}")

# ---------------------------------------------
# 09 - Metindeki Harfleri Sayma
# ---------------------------------------------

text = input("Enter a text: ")

letter_count = {}

for letter in text:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

print(letter_count)

# ---------------------------------------------
# END OF STEP 1
# ---------------------------------------------