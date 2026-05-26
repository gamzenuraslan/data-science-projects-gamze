# ---------------------------------------------
# 05 — MAGIC METHODS
# ---------------------------------------------

# Magic methods are special methods in Python.
# They usually start and end with double underscores (__).

# Example:
# __init__
# __str__
# __add__
# __len__

# ---------------------------------------------
# BASIC EXAMPLE
# ---------------------------------------------

print(5 + 3)

print(int.__add__(5, 3))


# ---------------------------------------------
# CUSTOM CLASS
# ---------------------------------------------

class FootballPlayer:

    def __init__(self, name, surname, age):

        self.name = name
        self.surname = surname
        self.age = age


    # Equality check

    def __eq__(self, other):

        return self.name == other.name and self.surname == other.surname


    # Addition

    def __add__(self, other):

        new_name = self.name[0] + other.name[0]
        new_surname = self.surname[0] + other.surname[0]
        new_age = self.age + other.age

        return FootballPlayer(new_name, new_surname, new_age)


    # Greater than

    def __gt__(self, other):

        return self.age > other.age


    # Less than

    def __lt__(self, other):

        return self.age < other.age


# ---------------------------------------------
# OBJECTS
# ---------------------------------------------

player1 = FootballPlayer("Gamze", "Aslan", 22)

player2 = FootballPlayer("Nur", "Aslan", 18)


# ---------------------------------------------
# __eq__
# ---------------------------------------------

print(player1 == player2)


# ---------------------------------------------
# __add__
# ---------------------------------------------

player3 = player1 + player2

print(player3.name)
print(player3.surname)
print(player3.age)


# ---------------------------------------------
# __gt__ & __lt__
# ---------------------------------------------

print(player1 > player2)
print(player1 < player2)


# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

class Number:
    def __init__(self, value):

        self.value = value

    def __add__(self, other):

        return Number(self.value + other.value)

    def __str__(self):

        return f"Value: {self.value}"


number1 = Number(10)
number2 = Number(20)

result = number1 + number2

print(result)