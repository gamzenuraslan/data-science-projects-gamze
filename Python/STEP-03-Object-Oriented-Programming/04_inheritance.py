# ---------------------------------------------
# 04 — INHERITANCE
# ---------------------------------------------

# Inheritance allows one class to use properties and methods of another class.

class Employee:

    raise_rate = 1.1

    def __init__(self, name, surname, salary):

        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name.lower() + surname.lower() + "@company.com"

    def show_info(self):

        return f"Name: {self.name} Surname: {self.surname} Salary: {self.salary} Email: {self.email}"


# Developer class inherits from Employee.

class Developer(Employee):

    raise_rate = 1.5

    def __init__(self, name, surname, salary, language):

        super().__init__(name, surname, salary)

        self.language = language

    def show_info(self):

        return f"Name: {self.name} Surname: {self.surname} Salary: {self.salary} Email: {self.email} Language: {self.language}"

    def show_language(self):

        return f"Programming Language: {self.language}"


employee1 = Employee("Gamze", "Aslan", 5000)

developer1 = Developer("Nur", "Aslan", 10000, "Python")

print(employee1.show_info())
print(developer1.show_info())

print(developer1.show_language())


# ---------------------------------------------
# METHOD OVERRIDING
# ---------------------------------------------

print(employee1.raise_rate)
print(developer1.raise_rate)


# ---------------------------------------------
# MANAGER CLASS
# ---------------------------------------------

class Manager(Employee):

    def __init__(self, name, surname, salary, employees=None):

        super().__init__(name, surname, salary)

        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):

        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):

        if employee in self.employees:
            self.employees.remove(employee)

    def show_employees(self):

        for employee in self.employees:
            print(employee.show_info())


manager1 = Manager("Ayse", "Yilmaz", 20000)

manager1.add_employee(employee1)
manager1.add_employee(developer1)

manager1.show_employees()


# ---------------------------------------------
# isinstance() & issubclass()
# ---------------------------------------------

print(isinstance(developer1, Developer))
print(isinstance(developer1, Employee))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))