'''
Comments in Python are text notes within the code that are not executed as part of the program. They are used to explain and document what the code does, making it easier to understand and maintain. Comments can be added in various ways:
'''


### Single-Line Comments
Single-line comments start with a hash symbol (`#`). Everything after the `#` on that line is considered a comment and is ignored by the Python interpreter.

**Example:**
# This is a single-line comment
print("Hello, World!")  # This prints a message to the console

### Multi-Line Comments
Multi-line comments can be written in two ways: using multiple single-line comments or using triple-quoted strings (`'''` or `"""`). Although triple-quoted strings are primarily used for multi-line strings, they can also serve as multi-line comments if they are not assigned to any variable.

**Example using multiple single-line comments:**
```python
# This is a multi-line comment
# written in multiple lines.
# Each line starts with a hash symbol.
print("Hello, World!")
```

**Example using triple-quoted strings:**
```python
"""
This is a multi-line comment.
It is written using triple-quoted strings.
These comments can span multiple lines.
"""
print("Hello, World!")
```

### Practical Example with Comments
Here is a simple Python script with comments that explain each part of the code:

```python
# This program calculates the area of a rectangle

# Define the width of the rectangle
width = 5  # width in meters

# Define the height of the rectangle
height = 10  # height in meters

# Calculate the area of the rectangle
# Area is given by width multiplied by height
area = width * height

# Print the result to the console
print("The area of the rectangle is:", area)
```

In this example:
- The first comment explains the purpose of the program.
- Comments are added to explain the variables `width` and `height`.
- Another comment explains the calculation of the area.
- Finally, a comment describes the print statement.

Using comments effectively helps others (and yourself) understand the code better when revisiting it in the future.