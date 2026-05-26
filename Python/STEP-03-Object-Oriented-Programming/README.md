# STEP 3 — Object Oriented Programming 🧠

In this step, we start learning one of the most important concepts in Python:

Object Oriented Programming (OOP).

OOP helps us write:
- cleaner code,
- reusable structures,
- scalable projects,
- and more organized applications.

Most real-world Python projects use OOP concepts.

---

## Topics 📚

### 01 — Classes & Objects
- Creating classes
- Creating objects
- `__init__`
- Instance methods

### 02 — Instance & Class Variables
- Instance variables
- Class variables
- Shared data between objects

### 03 — Class Methods & Static Methods
- `@classmethod`
- `@staticmethod`
- Alternative constructors

### 04 — Inheritance
- Parent & child classes
- Method overriding
- `super()`
- `isinstance()` & `issubclass()`

### 05 — Magic Methods
- `__add__`
- `__eq__`
- `__gt__`
- `__lt__`

### 06 — __str__ & __repr__
- User-friendly output
- Developer-friendly output
- Object representation

---

## Goal 🎯

The goal of this step is to:
- understand how objects work,
- build reusable code structures,
- and improve software design thinking.

---

## Mini Example 🚀

```python
class Student:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello {self.name}"


student1 = Student("Gamze")

print(student1.say_hello())