# ---------------------------------------------
# 01 — NUMPY BASICS
# ---------------------------------------------

# NumPy is a Python library used for numerical operations.
# It is especially useful for working with arrays and mathematical calculations.

import numpy as np

# ---------------------------------------------
# CREATING ARRAYS
# ---------------------------------------------

numbers = np.array([10, 20, 30, 40, 50])
print(numbers)


# Array type
print(type(numbers))


# Array dimension
print(numbers.ndim)


# Array shape
print(numbers.shape)


# Array size
print(numbers.size)

# ---------------------------------------------
# BASIC ARRAY OPERATIONS
# ---------------------------------------------

print(numbers + 10)
print(numbers * 2)
print(numbers / 2)

# ---------------------------------------------
# INDEXING
# ---------------------------------------------

print(numbers[0])
print(numbers[-1])

# ---------------------------------------------
# SLICING
# ---------------------------------------------

print(numbers[1:4])
print(numbers[:3])
print(numbers[::2])

# ---------------------------------------------
# 2D ARRAY
# ---------------------------------------------

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(matrix)
print(matrix.ndim)
print(matrix.shape)

# ---------------------------------------------
# 2D ARRAY INDEXING
# ---------------------------------------------

print(matrix[0][0])
print(matrix[1][2])

# ---------------------------------------------
# USEFUL NUMPY FUNCTIONS
# ---------------------------------------------

print(np.zeros(5))
print(np.ones(5))
print(np.arange(1, 10))
print(np.arange(0, 11, 2))
print(np.linspace(0, 1, 5))

# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

grades = np.array([70, 80, 90, 100])
print(f"Average: {np.mean(grades)}")
print(f"Maximum: {np.max(grades)}")
print(f"Minimum: {np.min(grades)}")