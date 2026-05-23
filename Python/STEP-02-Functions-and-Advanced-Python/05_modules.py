# ---------------------------------------------
# 05 — MODULES
# ---------------------------------------------

# Importing a module
import math

print(math.sqrt(25))
print(math.factorial(5))


# Importing specific functions
from math import sqrt, factorial

print(sqrt(49))
print(factorial(4))


# Using aliases
import math as m

print(m.pi)
print(m.pow(2, 3))


# Random module
import random

print(random.randint(1, 10))

colors = ["Red", "Blue", "Green", "Black"]

print(random.choice(colors))


# Shuffle
random.shuffle(colors)

print(colors)


# Datetime module
from datetime import datetime

now = datetime.now()

print(now)

print(now.year)
print(now.month)
print(now.day)


# Time formatting
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%H:%M:%S"))


# OS module
import os

print(os.getcwd())


# Mini Exercise
import random

lucky_numbers = []

for i in range(5):
    lucky_numbers.append(random.randint(1, 100))

print(lucky_numbers)

print(f"Lucky number: {random.choice(lucky_numbers)}")