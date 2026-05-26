# ---------------------------------------------
# 01 — CLASSES & OBJECTS
# ---------------------------------------------

# Class is a blueprint for creating objects.
class Student:
    pass


student1 = Student()

student1.name = "Gamze"
student1.surname = "Aslan"
student1.age = 22

print(student1.name)
print(student1.surname)
print(student1.age)

# ---------------------------------------------
# __init__ METHOD
# ---------------------------------------------

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


student1 = Student("Gamze", "Aslan", 22)
student2 = Student("Nur", "Aslan", 25)

print(student1.name)
print(student2.name)


# ---------------------------------------------
# INSTANCE METHOD
# ---------------------------------------------

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        return f"Name: {self.name} Surname: {self.surname} Age: {self.age}"


student1 = Student("Gamze", "Aslan", 22)
student2 = Student("Nur", "Aslan", 25)

print(student1.show_info())
print(student2.show_info())


# ---------------------------------------------
# DEFAULT PARAMETER
# ---------------------------------------------

class Student:
    def __init__(self, name, surname, age=0):
        self.name = name
        self.surname = surname
        self.age = age

    def show_info(self):
        return f"Name: {self.name} Surname: {self.surname} Age: {self.age}"


student1 = Student("Gamze", "Aslan")
student2 = Student("Nur", "Aslan", 25)

print(student1.show_info())
print(student2.show_info())