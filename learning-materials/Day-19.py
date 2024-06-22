'''
The `range` class in Python is used to generate a sequence of numbers. It's particularly useful in for-loops and other situations where you need a sequence of numbers. The `range` class is very memory efficient as it generates the numbers on demand rather than storing them all in memory.

### Syntax
The basic syntax of the `range` class is:

```python
range(start, stop, step)
```

- `start` (optional): The starting value of the sequence (inclusive). Defaults to 0 if not provided.
- `stop`: The ending value of the sequence (exclusive).
- `step` (optional): The difference between each number in the sequence. Defaults to 1 if not provided.

### Examples

1. **Basic Range**:
   Generating a sequence from 0 to 4.
   ```python
   for i in range(5):
       print(i)
   ```
   Output:
   ```
   0
   1
   2
   3
   4
   ```

2. **Custom Start and Stop**:
   Generating a sequence from 2 to 5.
   ```python
   for i in range(2, 6):
       print(i)
   ```
   Output:
   ```
   2
   3
   4
   5
   ```

3. **Custom Step**:
   Generating a sequence from 0 to 8 with a step of 2.
   ```python
   for i in range(0, 10, 2):
       print(i)
   ```
   Output:
   ```
   0
   2
   4
   6
   8
   ```

4. **Negative Step**:
   Generating a sequence from 5 to 1 with a step of -1.
   ```python
   for i in range(5, 0, -1):
       print(i)
   ```
   Output:
   ```
   5
   4
   3
   2
   1
   ```

5. **Converting `range` to List**:
   Sometimes you may want to see the entire sequence generated by `range`. You can convert it to a list.
   ```python
   list(range(5))
   ```
   Output:
   ```python
   [0, 1, 2, 3, 4]
   ```

### More Demonstrations

Let's demonstrate a few more complex examples:

6. **Using `range` with List Comprehensions**:
   Creating a list of squares of numbers from 0 to 9.
   ```python
   squares = [x**2 for x in range(10)]
   print(squares)
   ```
   Output:
   ```python
   [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
   ```

7. **Finding Even Numbers**:
   Generating a list of even numbers between 1 and 20.
   ```python
   evens = list(range(2, 21, 2))
   print(evens)
   ```
   Output:
   ```python
   [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
   ```

### Memory Efficiency

The `range` object does not store all the values in memory; it generates them on the fly (which is why it is called an iterable). This can be demonstrated by checking the memory usage of a large `range`.

```python
import sys

large_range = range(1000000)
print(sys.getsizeof(large_range))
```
Output:
```
48
```

Here, despite the large size, the `range` object uses very little memory.

### Conclusion

The `range` class in Python is a versatile tool for generating sequences of numbers. It's efficient in terms of both memory and speed, making it a fundamental part of Python programming, especially in loops and list comprehensions.
'''