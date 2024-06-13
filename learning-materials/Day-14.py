'''Decision control in Python involves making decisions within a program based on certain conditions. The primary constructs for decision control in Python are `if`, `elif`, and `else` statements. Here's an overview of how these constructs work:

1. **`if` Statement**: This is used to test a condition. If the condition is true, the block of code inside the `if` statement will execute.
2. **`elif` Statement**: This is short for "else if". It allows you to check multiple expressions for truth and execute a block of code as soon as one of the conditions is true.
3. **`else` Statement**: This is used to catch anything that isn't caught by the preceding conditions. It executes a block of code if none of the preceding conditions are true.

### Basic Syntax

```python
if condition1:
    # code block to execute if condition1 is true
elif condition2:
    # code block to execute if condition2 is true
else:
    # code block to execute if none of the above conditions are true
```

### Example

Here’s a simple example demonstrating the use of `if`, `elif`, and `else` statements:

```python
age = 18

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

### Nested `if` Statements

You can also nest `if` statements inside other `if` statements to check multiple conditions:

```python
age = 18
has_permission = True

if age < 20:
    if has_permission:
        print("You are a teenager with permission.")
    else:
        print("You are a teenager without permission.")
else:
    print("You are an adult.")
```

### Using Logical Operators

Logical operators like `and`, `or`, and `not` can be used to combine multiple conditions:

```python
age = 18
has_permission = True

if age < 20 and has_permission:
    print("You are a teenager with permission.")
else:
    print("You are either not a teenager or do not have permission.")
```

### Example with User Input

Let's make a more interactive example where the user inputs their age, and we provide a response based on that:

```python
age = int(input("Enter your age: "))

if age < 0:
    print("Age cannot be negative.")
elif age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

### Practice Exercise

Write a Python program that checks whether a number entered by the user is positive, negative, or zero.

```python
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

These examples cover the basics of decision control in Python. You can use these constructs to build more complex logic in your programs.
'''