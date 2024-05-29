'''
In Python, variable names must follow certain rules to be valid. Here's an overview of the rules, along with examples of valid and invalid variable names:

### Rules for Variable Names

1. **Must begin with a letter (a-z, A-Z) or an underscore (`_`)**
2. **Subsequent characters can be letters, digits (0-9), or underscores**
3. **Cannot be a reserved keyword in Python**
4. **Case-sensitive** (`age`, `Age`, and `AGE` are different variables)

### Valid Variable Names

- `age`
- `Age`
- `_age`
- `age1`
- `first_name`
- `firstName`
- `student1_name`

### Invalid Variable Names

- `1age` (cannot start with a digit)
- `first-name` (hyphen `-` is not allowed)
- `first name` (space is not allowed)
- `@name` (special characters other than `_` are not allowed)
- `class` (cannot use reserved keywords)

### Reserved Keywords

Python has a set of reserved keywords that cannot be used as variable names. Here are some of them:

```python
False, None, True, and, as, assert, async, await, break, class, continue, def, del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, return, try, while, with, yield
```

You can get the full list of keywords by using the `keyword` module:

```python
import keyword
print(keyword.kwlist)
```

### Demonstration of Valid and Invalid Variable Names

```python
# Valid variable names
age = 25
first_name = "Alice"
_last_name = "Smith"
age1 = 30
totalAmount = 1000.50

print(age)
print(first_name)
print(_last_name)
print(age1)
print(totalAmount)

# Invalid variable names (uncommenting these will cause a syntax error)
# 1age = 25
# first-name = "Alice"
# first name = "Alice"
# @name = "Alice"
# class = "Physics"
```

### Type Checking and Assignment

You can check the type of a variable using the `type()` function:

```python
x = 10
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

name = "John"
print(type(name))  # <class 'str'>

is_valid = True
print(type(is_valid))  # <class 'bool'>

items = [1, 2, 3]
print(type(items))  # <class 'list'>
```

### Case Sensitivity

Python variable names are case-sensitive:

```python
name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)  # Alice
print(Name)  # Bob
print(NAME)  # Charlie
```

### Summary

- Variable names must start with a letter or underscore and can contain letters, digits, and underscores.
- Avoid using reserved keywords.
- Variable names are case-sensitive.

Following these rules will help you write clear and error-free Python code.

'''