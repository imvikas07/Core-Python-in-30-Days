'''
In Python, the `match` statement is a powerful control flow feature introduced in Python 3.10. It provides pattern matching, which allows you to check a value against a series of patterns and execute code based on which pattern is matched. This is similar to `switch` statements found in other languages, but more flexible and expressive.

### Syntax
The basic syntax of a `match` statement looks like this:

```python
match subject:
    case pattern1:
        # Code to execute if pattern1 matches
    case pattern2:
        # Code to execute if pattern2 matches
    case _:
        # Code to execute if no patterns match (default case)
```

### Components
- **`subject`**: The value you want to match against various patterns.
- **`pattern`**: The patterns you want to match the subject against. Patterns can include literals, variable names, sequences, mappings, classes, and more.
- **`_`**: A wildcard pattern that matches anything. It's typically used as a default case.

### Example
Here is a basic example to illustrate how the `match` statement works:

```python
def describe(value):
    match value:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case [x, y]:
            return f"A list of two elements: {x} and {y}"
        case _:
            return "Something else"

print(describe(0))  # Output: Zero
print(describe(1))  # Output: One
print(describe([2, 3]))  # Output: A list of two elements: 2 and 3
print(describe("hello"))  # Output: Something else
```

### Advanced Usage
Pattern matching can handle more complex scenarios such as deconstructing data structures:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def location(point):
    match point:
        case Point(0, 0):
            return "Origin"
        case Point(x, 0):
            return f"X-axis at {x}"
        case Point(0, y):
            return f"Y-axis at {y}"
        case Point(x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a point"

print(location(Point(0, 0)))  # Output: Origin
print(location(Point(3, 0)))  # Output: X-axis at 3
print(location(Point(0, 4)))  # Output: Y-axis at 4
print(location(Point(3, 4)))  # Output: Point at (3, 4)
```

### Key Points
- **Literal Patterns**: Match against specific values like numbers or strings.
- **Variable Patterns**: Capture parts of the subject into variables.
- **Sequence Patterns**: Match against sequences like lists or tuples.
- **Mapping Patterns**: Match against dictionaries or other mappings.
- **Class Patterns**: Match against objects of specific classes and deconstruct them.
- **Wildcard Pattern `_`**: Matches anything and is typically used as a fallback.

The `match` statement provides a concise and readable way to handle multiple conditions and data deconstruction in Python, making code easier to understand and maintain.

'''