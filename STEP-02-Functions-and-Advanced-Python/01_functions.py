# ---------------------------------------------
# 01 — FUNCTIONS
# ---------------------------------------------

# Function definition
def say_hello():
    print("Hello Python")

say_hello()


# Function with parameter
def greet(name):
    print(f"Hello, {name}!")

greet("Gamze")


# Function with multiple parameters
def add_numbers(a, b):
    print(a + b)


add_numbers(10, 20)


# Function with return
def calculate_average(a, b):
    return (a + b) / 2


average = calculate_average(80, 90)

print(f"Average: {average}")


# Default parameter
def introduce(name, language="Python"):
    print(f"{name} is learning {language}.")


introduce("Gamze")
introduce("Gamze", "Data Science")


# Mini Exercise
def discount_price(price, discount):
    result = price - (price * discount / 100)
    return result


final_price = discount_price(1000, 20)

print(f"Final price: {final_price}")