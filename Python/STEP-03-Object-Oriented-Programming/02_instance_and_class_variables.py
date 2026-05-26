# ---------------------------------------------
# 02 — INSTANCE & CLASS VARIABLES
# ---------------------------------------------

# Class variables are shared by all objects.
# Instance variables belong to each object separately.

class Employee:

    # Class variables
    company = "Google"
    employee_count = 0
    raise_rate = 1.2

    def __init__(self, name, salary):

        # Instance variables
        self.name = name
        self.salary = salary

        Employee.employee_count += 1

    def show_info(self):
        return f"Name: {self.name} Salary: {self.salary}"


employee1 = Employee("Gamze", 5000)
employee2 = Employee("Nur", 8000)

print(employee1.show_info())
print(employee2.show_info())


# ---------------------------------------------
# ACCESSING CLASS VARIABLES
# ---------------------------------------------

print(Employee.company)

print(employee1.company)
print(employee2.company)


# Total employee count

print(Employee.employee_count)


# ---------------------------------------------
# CHANGING CLASS VARIABLES
# ---------------------------------------------

print(Employee.raise_rate)

employee1.raise_rate = 1.5

print(employee1.raise_rate)
print(employee2.raise_rate)
print(Employee.raise_rate)


# ---------------------------------------------
# __dict__
# ---------------------------------------------

print(employee1.__dict__)
print(employee2.__dict__)
print(Employee.__dict__)


# ---------------------------------------------
# MINI EXERCISE
# ---------------------------------------------

class Student:

    school = "Data Science Academy"
    student_count = 0

    def __init__(self, name):

        self.name = name

        Student.student_count += 1


student1 = Student("Gamze")
student2 = Student("Python")

print(student1.name)
print(student2.name)

print(Student.student_count)
print(Student.school)