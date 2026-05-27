# ---------------------------------------------
# 02 — NUMPY OPERATIONS
# ---------------------------------------------

import numpy as np

# ---------------------------------------------
# ARRAY OPERATIONS
# ---------------------------------------------

array1 = np.array([1, 2, 3, 4])
array2 = np.array([10, 20, 30, 40])

print(array1 + array2)
print(array2 - array1)
print(array1 * array2)
print(array2 / array1)

# ---------------------------------------------
# MATHEMATICAL OPERATIONS
# ---------------------------------------------

numbers = np.array([4, 9, 16, 25])

print(np.sqrt(numbers))
print(np.mean(numbers))
print(np.sum(numbers))
print(np.max(numbers))
print(np.min(numbers))

# ---------------------------------------------
# RANDOM NUMBERS
# ---------------------------------------------

random_numbers = np.random.randint(1, 100, 5)
print(random_numbers)

# Random float values

random_float = np.random.rand(5)
print(random_float)

# ---------------------------------------------
# RESHAPING ARRAYS
# ---------------------------------------------

numbers = np.arange(1, 13)
print(numbers)
matrix = numbers.reshape(3, 4)
print(matrix)

# ---------------------------------------------
# FLATTEN ARRAY
# ---------------------------------------------

print(matrix.flatten())

# ---------------------------------------------
# FILTERING
# ---------------------------------------------

numbers = np.array([10, 15, 20, 25, 30])
result = numbers[numbers > 20]
print(result)

# Even numbers

even_numbers = numbers[numbers % 2 == 0]
print(even_numbers)

# ---------------------------------------------
# BROADCASTING
# ---------------------------------------------

numbers = np.array([1, 2, 3, 4])
print(numbers + 100)

# ---------------------------------------------
# AGGREGATION
# ---------------------------------------------

grades = np.array([70, 80, 90, 100])

print(np.mean(grades))
print(np.std(grades))
print(np.var(grades))

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

sales = np.array([250, 300, 400, 150, 500])

print(f"Total Sales: {np.sum(sales)}")
print(f"Average Sales: {np.mean(sales)}")
print(f"Best Sale: {np.max(sales)}")