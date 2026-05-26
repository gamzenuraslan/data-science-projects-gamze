# ---------------------------------------------
# 06 — __str__ & __repr__
# ---------------------------------------------

# __str__
# Returns a readable string for users.

# __repr__
# Returns a more detailed representation for developers.


# ---------------------------------------------
# BASIC EXAMPLES
# ---------------------------------------------

text = "Python"

print(str(text))
print(repr(text))


number = 10 / 3

print(str(number))
print(repr(number))


# ---------------------------------------------
# CUSTOM CLASS
# ---------------------------------------------

class Student:

    def __init__(self, name, field, age):

        self.name = name
        self.field = field
        self.age = age


    # User-friendly output

    def __str__(self):

        return f"Student: {self.name} | Field: {self.field} | Age: {self.age}"


    # Developer-friendly output

    def __repr__(self):

        return f"Student('{self.name}', '{self.field}', {self.age})"


# ---------------------------------------------
# OBJECT
# ---------------------------------------------

student1 = Student("Gamze", "Data Science", 22)


# ---------------------------------------------
# __str__
# ---------------------------------------------

print(student1)


# ---------------------------------------------
# __repr__
# ---------------------------------------------

print(repr(student1))
print(student1.__repr__())


# ---------------------------------------------
# LIST EXAMPLE
# ---------------------------------------------

students = [
    Student("Gamze", "Python", 22),
    Student("Nur", "Machine Learning", 25)
]

print(students)


# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

class Book:

    def __init__(self, title, author):

        self.title = title
        self.author = author


    def __str__(self):

        return f"{self.title} by {self.author}"


    def __repr__(self):

        return f"Book('{self.title}', '{self.author}')"


book1 = Book("Python Basics", "Gamze")

print(book1)
print(repr(book1))