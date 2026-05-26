# ---------------------------------------------
# 03 — CLASS METHODS & STATIC METHODS
# ---------------------------------------------

from datetime import date


class Person:

    person_count = 0

    def __init__(self, name, age):

        self.name = name
        self.age = age

        Person.person_count += 1


    # Instance Method
    # Works with object data.

    def show_info(self):
        return f"Name: {self.name} Age: {self.age}"


    # Class Method
    # Works with class variables.

    @classmethod
    def show_person_count(cls):
        return cls.person_count


    # Alternative constructor

    @classmethod
    def create_with_string(cls, data):

        name, age = data.split("-")

        return cls(name, int(age))


    @classmethod
    def calculate_age(cls, name, birth_year):

        current_year = date.today().year

        return cls(name, current_year - birth_year)


    # Static Method
    # Independent helper method.

    @staticmethod
    def is_adult(age):

        return age >= 18


# ---------------------------------------------
# OBJECTS
# ---------------------------------------------

person1 = Person("Gamze", 22)
person2 = Person("Nur", 17)

print(person1.show_info())
print(person2.show_info())


# ---------------------------------------------
# CLASS METHOD
# ---------------------------------------------

print(Person.show_person_count())


# Alternative constructor

person3 = Person.create_with_string("Python-5")

print(person3.show_info())


# Calculate age from birth year

person4 = Person.calculate_age("Aslan", 2003)

print(person4.show_info())


# ---------------------------------------------
# STATIC METHOD
# ---------------------------------------------

print(Person.is_adult(20))
print(Person.is_adult(15))