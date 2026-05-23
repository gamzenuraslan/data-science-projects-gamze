# STEP 2 — Functions & Advanced Python

In this step, we move beyond basic Python syntax and start learning more powerful and reusable programming structures.

This section focuses on:
- writing cleaner code,
- understanding functions,
- improving problem-solving skills,
- and learning more Pythonic ways to work with data.

---

## Topics 📚

### 01 — Functions
- Function definition
- Parameters
- Return values
- Default parameters

### 02 — *args & **kwargs
- Positional arguments
- Keyword arguments
- Flexible function structures

### 03 — List Comprehension
- Cleaner list creation
- Filtering data
- Nested loops
- Conditional expressions

### 04 — Error Handling
- try / except
- else & finally
- Catching specific errors
- Raising exceptions

### 05 — Modules
- Importing modules
- Using built-in Python modules
- math, random, datetime, os

---

## Goal 🎯

The goal of this step is to:
- write more organized code,
- avoid repetitive structures,
- and better understand Python logic.

---

## Mini Example 🚀

```python
def calculate_average(*grades):
    return sum(grades) / len(grades)

print(calculate_average(80, 90, 100))