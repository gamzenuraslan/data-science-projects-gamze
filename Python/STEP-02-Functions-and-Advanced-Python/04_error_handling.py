# ---------------------------------------------
# 04 — ERROR HANDLING
# ---------------------------------------------

# Basic try-except
try:
    print(10 / 0)

except:
    print("An error occurred.")


# Catching specific errors
try:
    number = int(input("Enter a number: "))
    print(number)

except ValueError:
    print("Please enter a valid number.")


# Multiple exceptions
try:
    numbers = [1, 2, 3]

    print(numbers[5])

except IndexError:
    print("Index out of range.")

except Exception as error:
    print(error)


# else block
try:
    result = 10 / 2

except:
    print("Error!")

else:
    print("Operation successful.")
    print(result)


# finally block
try:
    file = open("example.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    print("Finally block always works.")


# Raising an error
age = -5

try:

    if age < 0:
        raise ValueError("Age cannot be negative.")

except ValueError as error:
    print(error)


# Mini Exercise
try:
    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))

    result = number1 / number2

    print(f"Result: {result}")

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter only numbers.")

finally:
    print("Calculator finished.")