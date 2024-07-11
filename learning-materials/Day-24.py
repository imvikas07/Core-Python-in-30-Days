'''

In Python, a set is an unordered collection of unique elements. Sets are used to store multiple items in a single variable and are particularly useful when you need to ensure that the items are distinct. Here are some key features and characteristics of sets in Python:

1. **Unordered**: The items in a set do not have a defined order. Even if you add items in a specific order, Python will not remember that order.
2. **Unique Elements**: Sets do not allow duplicate elements. If you try to add a duplicate element, it will be ignored.
3. **Mutable**: You can add or remove elements from a set, but the elements themselves must be immutable (e.g., you can add strings or numbers to a set, but not lists or dictionaries).
4. **Set Operations**: Sets support mathematical operations like union, intersection, difference, and symmetric difference.

### Creating a Set

You can create a set by using curly braces `{}` or the `set()` function.

```python
# Creating a set with curly braces
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Creating a set with the set() function
my_set = set([1, 2, 3, 4, 5])
print(my_set)
```

### Adding and Removing Elements

You can add elements to a set using the `add()` method and remove elements using the `remove()` or `discard()` methods.

```python
my_set = {1, 2, 3}

# Adding an element
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Removing an element
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4}

# Removing an element using discard (no error if element not found)
my_set.discard(2)
print(my_set)  # Output: {1, 4}

# Attempting to remove an element not in the set will raise an error
# my_set.remove(99)  # KeyError: 99

# Discarding an element not in the set does not raise an error
my_set.discard(99)  # No error
```

### Set Operations

Sets support a variety of operations that allow for mathematical set theory concepts.

#### Union

The union of two sets is a set containing all elements from both sets. This can be achieved using the `union()` method or the `|` operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Using the | operator
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

#### Intersection

The intersection of two sets is a set containing only the elements that are in both sets. This can be achieved using the `intersection()` method or the `&` operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}

# Using the & operator
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
```

#### Difference

The difference of two sets is a set containing elements that are in the first set but not in the second set. This can be achieved using the `difference()` method or the `-` operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

# Using the - operator
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
```

#### Symmetric Difference

The symmetric difference of two sets is a set containing elements that are in either of the sets, but not in both. This can be achieved using the `symmetric_difference()` method or the `^` operator.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

# Using the ^ operator
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

### Checking Membership

You can check if an element is in a set using the `in` keyword.

```python
my_set = {1, 2, 3, 4, 5}

print(3 in my_set)  # Output: True
print(6 in my_set)  # Output: False
```

### Iterating Through a Set

You can iterate through the elements of a set using a `for` loop.

```python
my_set = {1, 2, 3, 4, 5}

for item in my_set:
    print(item)
```

### Example Demonstration

Let's put all these concepts together in a demonstration.

```python
# Creating sets
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Adding and removing elements
set_a.add(7)
set_a.remove(1)

# Set operations
union_set = set_a | set_b
intersection_set = set_a & set_b
difference_set = set_a - set_b
symmetric_difference_set = set_a ^ set_b

# Membership check
is_member = 5 in set_b

# Iterating through a set
for item in set_a:
    print(item)

# Display results
print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (A - B):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
print("Is 5 in Set B:", is_member)
```

This script demonstrates how to create sets, perform basic operations, and utilize set-specific methods in Python.
'''