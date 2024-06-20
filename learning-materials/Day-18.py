'''
A for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. This allows you to execute a block of code multiple times. The syntax of a for loop is straightforward and typically looks like this:

```python
for item in sequence:
    # code to execute
```

Here's a simple demonstration using a list:

### Example: Iterating Over a List

```python
# Define a list
fruits = ["apple", "banana", "cherry"]

# Iterate over the list
for fruit in fruits:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

In this example, the for loop iterates over each item in the `fruits` list, and the `print(fruit)` statement inside the loop is executed for each item.

### Example: Using `range()` Function

The `range()` function generates a sequence of numbers, which is useful for creating loops with a specific number of iterations.

```python
# Iterate over a range of numbers from 0 to 4
for i in range(5):
    print(i)
```

**Output:**
```
0
1
2
3
4
```

### Example: Iterating Over a String

You can also iterate over a string, treating each character as an item in the sequence.

```python
# Define a string
message = "Hello"

# Iterate over each character in the string
for char in message:
    print(char)
```

**Output:**
```
H
e
l
l
o
```

### Example: Iterating Over a Dictionary

When iterating over a dictionary, you can access its keys and values.

```python
# Define a dictionary
student_grades = {"Alice": 90, "Bob": 85, "Charlie": 92}

# Iterate over the dictionary items
for name, grade in student_grades.items():
    print(f"{name} scored {grade}")
```

**Output:**
```
Alice scored 90
Bob scored 85
Charlie scored 92
```

### Example: Nested for Loops

You can also use nested for loops to iterate over multi-dimensional data structures, like lists of lists.

```python
# Define a list of lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate over the rows
for row in matrix:
    # Iterate over the columns
    for item in row:
        print(item, end=" ")
    print()  # for a new line after each row
```

**Output:**
```
1 2 3 
4 5 6 
7 8 9 
```

These examples demonstrate the versatility of the for loop in Python, allowing you to iterate over various types of sequences and perform operations on each item in those sequences.

'''