'''
In Python, variables are used to store data values. A variable is created the moment you first assign a value to it. Python is a dynamically typed language, which means you don't need to declare the type of a variable explicitly, and the type can change based on the value assigned.

### Basic Variable Types in Python

1. **Integer (`int`)**
   - Whole numbers, both positive and negative, without decimals.
   ```python
   x = 5
   y = -3
   ```

2. **Float (`float`)**
   - Numbers with decimal points.
   ```python
   pi = 3.14
   g = 9.81
   ```

3. **String (`str`)**
   - A sequence of characters enclosed in single or double quotes.
   ```python
   greeting = "Hello, World!"
   name = 'Alice'
   ```

4. **Boolean (`bool`)**
   - Represents one of two values: `True` or `False`.
   ```python
   is_sunny = True
   has_rain = False
   ```

5. **List (`list`)**
   - An ordered collection of items, which can be of different types.
   ```python
   fruits = ["apple", "banana", "cherry"]
   numbers = [1, 2, 3, 4, 5]
   ```

6. **Tuple (`tuple`)**
   - An ordered collection of items that is immutable (cannot be changed after creation).
   ```python
   coordinates = (10.0, 20.0)
   colors = ("red", "green", "blue")
   ```

7. **Dictionary (`dict`)**
   - An unordered collection of key-value pairs.
   ```python
   student = {"name": "John", "age": 21, "grade": "A"}
   ```

8. **Set (`set`)**
   - An unordered collection of unique items.
   ```python
   unique_numbers = {1, 2, 3, 4, 5}
   ```

### Demonstration

Here's a simple Python script demonstrating the use of these variable types:

```python
# Integer
age = 25
print("Age:", age)

# Float
temperature = 36.6
print("Temperature:", temperature)

# String
name = "Alice"
print("Name:", name)

# Boolean
is_student = True
print("Is Student:", is_student)

# List
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Tuple
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)

# Dictionary
student = {"name": "John", "age": 21, "grade": "A"}
print("Student Info:", student)

# Set
unique_numbers = {1, 2, 3, 4, 5}
print("Unique Numbers:", unique_numbers)
```

### Explanation

1. **Integer and Float:**
   - `age` is an integer.
   - `temperature` is a float.

2. **String:**
   - `name` is a string.

3. **Boolean:**
   - `is_student` is a boolean.

4. **List:**
   - `fruits` is a list containing strings.

5. **Tuple:**
   - `coordinates` is a tuple containing two floats.

6. **Dictionary:**
   - `student` is a dictionary containing key-value pairs.

7. **Set:**
   - `unique_numbers` is a set containing integers.

### Type Checking

You can check the type of a variable using the `type()` function:

```python
print(type(age))          # <class 'int'>
print(type(temperature))  # <class 'float'>
print(type(name))         # <class 'str'>
print(type(is_student))   # <class 'bool'>
print(type(fruits))       # <class 'list'>
print(type(coordinates))  # <class 'tuple'>
print(type(student))      # <class 'dict'>
print(type(unique_numbers)) # <class 'set'>
```

This should give you a good overview of the basic variable types and how to use them in Python.

'''