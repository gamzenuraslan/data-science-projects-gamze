# ---------------------------------------------
# 02 — *args & **kwargs
# ---------------------------------------------

# *args allows us to send multiple positional arguments.
def add_numbers(*numbers):
    print(numbers)
    print(sum(numbers))


add_numbers(10, 20)
add_numbers(1, 2, 3, 4, 5)


# Multiply numbers
def multiply_numbers(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result


print(multiply_numbers(2, 3, 4))


# **kwargs allows us to send multiple keyword arguments.
def student_info(**info):
    print(info)


student_info(name="Gamze", age=22, language="Python")


# Accessing kwargs values
def show_profile(**user):
    print(f"Name: {user['name']}")
    print(f"Field: {user['field']}")


show_profile(name="Gamze", field="Data Science")


# Using args and kwargs together
def full_information(*args, **kwargs):

    print("Args:")
    for arg in args:
        print(arg)

    print("\nKwargs:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


full_information(
    "Python",
    "Machine Learning",
    name="Gamze",
    level="Beginner"
)


# Mini Exercise
def calculate_average(*grades):
    return sum(grades) / len(grades)


average = calculate_average(80, 90, 100)

print(f"Average: {average}")