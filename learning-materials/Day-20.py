'''
In Python, a list is a built-in data type used to store a collection of items. Lists are ordered, mutable (changeable), and can hold a mix of data types. Here's a detailed explanation and demonstration of lists in Python:

### Creating a List

You can create a list by placing a comma-separated sequence of elements within square brackets `[]`.

```python
# Creating a list of integers
int_list = [1, 2, 3, 4, 5]
print(int_list)

# Creating a list of strings
str_list = ["apple", "banana", "cherry"]
print(str_list)

# Creating a mixed data type list
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)
```

### Accessing List Elements

List elements can be accessed using their index, with the first element having an index of 0.

```python
# Accessing elements in a list
print(int_list[0])  # Output: 1
print(str_list[1])  # Output: banana
print(mixed_list[2])  # Output: 3.14
```

You can also use negative indices to access elements from the end of the list.

```python
# Accessing elements with negative indices
print(int_list[-1])  # Output: 5
print(str_list[-2])  # Output: banana
print(mixed_list[-3])  # Output: hello
```

### Slicing Lists

You can access a range of elements using slicing. The syntax is `list[start:end]`, where `start` is inclusive and `end` is exclusive.

```python
# Slicing a list
print(int_list[1:3])  # Output: [2, 3]
print(str_list[:2])  # Output: ['apple', 'banana']
print(mixed_list[1:])  # Output: ['hello', 3.14, True]
print(int_list[:-2])  # Output: [1, 2, 3]
```

### Modifying Lists

Lists are mutable, so you can change their content.

```python
# Changing elements in a list
int_list[0] = 10
print(int_list)  # Output: [10, 2, 3, 4, 5]

# Adding elements to a list
int_list.append(6)
print(int_list)  # Output: [10, 2, 3, 4, 5, 6]

# Inserting elements at a specific position
int_list.insert(1, 15)
print(int_list)  # Output: [10, 15, 2, 3, 4, 5, 6]

# Removing elements from a list
int_list.remove(15)
print(int_list)  # Output: [10, 2, 3, 4, 5, 6]

# Popping elements from a list
popped_element = int_list.pop()
print(popped_element)  # Output: 6
print(int_list)  # Output: [10, 2, 3, 4, 5]
```

### List Comprehensions

List comprehensions provide a concise way to create lists.

```python
# Creating a list of squares using a list comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]

# Creating a list of even numbers using a list comprehension
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # Output: [2, 4, 6, 8, 10]
```

### Common List Methods

Python lists come with a variety of built-in methods for manipulating and querying lists.

```python
# Copying a list
new_list = int_list.copy()
print(new_list)  # Output: [10, 2, 3, 4, 5]

# Extending a list with another list
new_list.extend([6, 7, 8])
print(new_list)  # Output: [10, 2, 3, 4, 5, 6, 7, 8]

# Finding the index of an element
index_of_four = new_list.index(4)
print(index_of_four)  # Output: 3

# Counting the occurrences of an element
count_of_two = new_list.count(2)
print(count_of_two)  # Output: 1

# Sorting a list
new_list.sort()
print(new_list)  # Output: [2, 3, 4, 5, 6, 7, 8, 10]

# Reversing a list
new_list.reverse()
print(new_list)  # Output: [10, 8, 7, 6, 5, 4, 3, 2]
```

### Combining Lists

You can concatenate lists using the `+` operator or using the `extend` method.

```python
# Concatenating lists using +
combined_list = int_list + str_list
print(combined_list)  # Output: [10, 2, 3, 4, 5, 'apple', 'banana', 'cherry']

# Concatenating lists using extend
int_list.extend(str_list)
print(int_list)  # Output: [10, 2, 3, 4, 5, 'apple', 'banana', 'cherry']
```

### List Nesting

Lists can contain other lists, enabling the creation of nested lists (or lists of lists).

```python
# Creating a nested list
nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list)  # Output: [[1, 2, 3], ['a', 'b', 'c'], [True, False]]

# Accessing elements in a nested list
print(nested_list[0])  # Output: [1, 2, 3]
print(nested_list[1][1])  # Output: b
```

### Summary

Python lists are versatile and powerful, allowing for the storage and manipulation of a collection of items. Their flexibility makes them a fundamental tool in Python programming.

'''