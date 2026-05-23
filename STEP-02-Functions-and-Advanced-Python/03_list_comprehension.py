# ---------------------------------------------
# 03 — LIST COMPREHENSION ⚡
# ---------------------------------------------

# Normal loop
numbers = [1, 2, 3, 4, 5]

new_list = []

for number in numbers:
    new_list.append(number * 2)

print(new_list)


# List comprehension
new_list = [number * 2 for number in numbers]

print(new_list)


# Even numbers
even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)


# Square numbers
square_numbers = [number ** 2 for number in numbers]

print(square_numbers)


# String example
names = ["gamze", "python", "data science"]

upper_names = [name.upper() for name in names]

print(upper_names)


# Nested loop
letters = ["A", "B"]
numbers = [1, 2, 3]

result = [(letter, number) for letter in letters for number in numbers]

print(result)


# Conditional expression
numbers = [1, 2, 3, 4, 5]

labels = ["Even" if number % 2 == 0 else "Odd" for number in numbers]

print(labels)


# Mini Exercise
numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)

greater_numbers = [number for number in numbers if number > average]

print(greater_numbers)