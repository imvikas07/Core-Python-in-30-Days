'''
Transfer control statements in Python are used to alter the flow of execution within a program. These statements are essential for implementing complex control flow structures. The primary transfer control statements in Python are:

1. **break**
2. **continue**
3. **pass**
4. **return**

Let's delve into each of these statements with demonstrations.

### 1. `break`

The `break` statement is used to exit a loop prematurely. It is typically used within loops to terminate the loop based on a certain condition.

#### Example:
```python
for i in range(1, 11):
    if i == 5:
        print("Breaking the loop at i =", i)
        break
    print(i)
```
**Output:**
```
1
2
3
4
Breaking the loop at i = 5
```

In this example, the loop runs from 1 to 10, but it stops when `i` equals 5 because of the `break` statement.

### 2. `continue`

The `continue` statement is used to skip the rest of the code inside the loop for the current iteration and move to the next iteration.

#### Example:
```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```
**Output:**
```
1
3
5
7
9
```

Here, the loop prints only the odd numbers between 1 and 10 because the `continue` statement skips the even numbers.

### 3. `pass`

The `pass` statement is a null operation; it does nothing when executed. It is useful as a placeholder in places where syntactically some code is required but you don’t want any command or code to execute.

#### Example:
```python
for i in range(5):
    if i % 2 == 0:
        pass  # Placeholder for future code
    else:
        print(i)
```
**Output:**
```
1
3
```

In this case, the `pass` statement does nothing. It's just a placeholder indicating that some code might be added here in the future.

### 4. `return`

The `return` statement is used to exit a function and optionally pass an expression back to the caller.

#### Example:
```python
def find_first_even(numbers):
    for number in numbers:
        if number % 2 == 0:
            return number
    return None

print(find_first_even([1, 3, 5, 7, 8, 10]))  # Output: 8
print(find_first_even([1, 3, 5, 7]))         # Output: None
```
**Output:**
```
8
None
```

In this example, the `find_first_even` function returns the first even number it encounters in the list. If there are no even numbers, it returns `None`.

### Combining Transfer Control Statements

Transfer control statements can be combined to implement more complex control flows.

#### Example:
```python
def process_numbers(numbers):
    result = []
    for number in numbers:
        if number < 0:
            print("Skipping negative number:", number)
            continue
        if number == 0:
            print("Zero encountered, breaking the loop")
            break
        result.append(number)
    return result

print(process_numbers([1, -2, 3, 0, 4, 5]))
```
**Output:**
```
Skipping negative number: -2
Zero encountered, breaking the loop
[1, 3]
```

In this example:
- The `continue` statement skips any negative numbers.
- The `break` statement exits the loop when a zero is encountered.
- The `return` statement returns the result list after the loop is terminated.

### Summary

- **`break`**: Exits the loop prematurely.
- **`continue`**: Skips the current iteration and moves to the next iteration.
- **`pass`**: Does nothing; a placeholder.
- **`return`**: Exits a function and optionally returns a value.

These transfer control statements are fundamental for controlling the flow of execution in Python programs, allowing for more dynamic and responsive code.

'''