'''
### Import in Python

The `import` statement is used to include the definitions (functions, classes, variables) from a module into your current namespace. This allows you to reuse code that has been written in other files or modules.

#### Example:
```python
# Importing the math module
import math

# Using the sqrt function from the math module
result = math.sqrt(16)
print(result)  # Output: 4.0
```

### Keywords in Python

Keywords are reserved words in Python that have special meaning. They cannot be used as identifiers (variable names, function names, etc.). Some common keywords include `if`, `else`, `while`, `for`, `def`, `return`, and `import`.

#### Example:
```python
# Using the 'if' keyword
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
```

### Modules, Packages, and Libraries in Python

**Modules**:
A module is a single file (or files) that is imported under one import and used. A module can define functions, classes, and variables, and can also include runnable code.

#### Example:
Create a file named `my_module.py` with the following content:
```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

# Using the module in another file or interactive session
import my_module

print(my_module.greet("Alice"))  # Output: Hello, Alice!
```

**Packages**:
A package is a way of structuring Python’s module namespace by using "dotted module names". A package is a collection of modules in directories that give a package hierarchy.

#### Example:
Create a directory structure like this:
```
my_package/
    __init__.py
    module1.py
    module2.py
```
- `__init__.py` can be empty or can include initialization code for the package.
- `module1.py` and `module2.py` contain your module code.

`module1.py`:
```python
# module1.py
def func1():
    return "Function 1 from module 1"
```

`module2.py`:
```python
# module2.py
def func2():
    return "Function 2 from module 2"
```

Usage:
```python
# Using the package
import my_package.module1
import my_package.module2

print(my_package.module1.func1())  # Output: Function 1 from module 1
print(my_package.module2.func2())  # Output: Function 2 from module 2
```

**Libraries**:
A library is a collection of modules and packages. Libraries are often larger and provide extensive functionality. For example, NumPy is a library that provides many mathematical functions and operations.

#### Example:
```python
# Using the numpy library
import numpy as np

array = np.array([1, 2, 3, 4])
print(array)  # Output: [1 2 3 4]
```

### Demonstrations

Here are some demonstrations of using `import`, keywords, and working with modules, packages, and libraries:

#### Using `import` and a keyword
```python
import datetime

# Using the 'def' keyword to define a function
def current_time():
    return datetime.datetime.now()

print(current_time())  # Output: current date and time
```

#### Creating and using a module
Create a file `utilities.py`:
```python
# utilities.py
def add(a, b):
    return a + b
```
Use this module:
```python
import utilities

print(utilities.add(3, 4))  # Output: 7
```

#### Creating and using a package
Directory structure:
```
mypackage/
    __init__.py
    math_operations.py
    string_operations.py
```
`math_operations.py`:
```python
# math_operations.py
def multiply(a, b):
    return a * b
```
`string_operations.py`:
```python
# string_operations.py
def concatenate(str1, str2):
    return str1 + str2
```
Use the package:
```python
from mypackage import math_operations, string_operations

print(math_operations.multiply(2, 3))  # Output: 6
print(string_operations.concatenate("Hello, ", "World!"))  # Output: Hello, World!
```

These demonstrations show how you can organize and reuse code effectively using modules, packages, and libraries in Python.'''