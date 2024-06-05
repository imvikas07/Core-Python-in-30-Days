'''
Operators in Python are special symbols or keywords that perform operations on operands (values or variables). Here's a detailed explanation of each type of operator in Python, along with demonstrations:

### 1. Arithmetic Operators
Arithmetic operators are used to perform mathematical operations.

- **Addition (`+`)**: Adds two numbers.
  ```python
  a = 5
  b = 3
  result = a + b
  print(result)  # Output: 8
  ```

- **Subtraction (`-`)**: Subtracts the second number from the first.
  ```python
  result = a - b
  print(result)  # Output: 2
  ```

- **Multiplication (`*`)**: Multiplies two numbers.
  ```python
  result = a * b
  print(result)  # Output: 15
  ```

- **Division (`/`)**: Divides the first number by the second (returns a float).
  ```python
  result = a / b
  print(result)  # Output: 1.6666666666666667
  ```

- **Floor Division (`//`)**: Divides the first number by the second (returns an integer).
  ```python
  result = a // b
  print(result)  # Output: 1
  ```

- **Modulus (`%`)**: Returns the remainder of the division.
  ```python
  result = a % b
  print(result)  # Output: 2
  ```

- **Exponentiation (`**`)**: Raises the first number to the power of the second.
  ```python
  result = a ** b
  print(result)  # Output: 125
  ```

### 2. Comparison Operators
Comparison operators compare two values and return a boolean result (`True` or `False`).

- **Equal (`==`)**: Checks if two values are equal.
  ```python
  result = (a == b)
  print(result)  # Output: False
  ```

- **Not Equal (`!=`)**: Checks if two values are not equal.
  ```python
  result = (a != b)
  print(result)  # Output: True
  ```

- **Greater Than (`>`)**: Checks if the first value is greater than the second.
  ```python
  result = (a > b)
  print(result)  # Output: True
  ```

- **Less Than (`<`)**: Checks if the first value is less than the second.
  ```python
  result = (a < b)
  print(result)  # Output: False
  ```

- **Greater Than or Equal To (`>=`)**: Checks if the first value is greater than or equal to the second.
  ```python
  result = (a >= b)
  print(result)  # Output: True
  ```

- **Less Than or Equal To (`<=`)**: Checks if the first value is less than or equal to the second.
  ```python
  result = (a <= b)
  print(result)  # Output: False
  ```

### 3. Logical Operators
Logical operators are used to combine conditional statements.

- **AND (`and`)**: Returns `True` if both statements are true.
  ```python
  x = True
  y = False
  result = x and y
  print(result)  # Output: False
  ```

- **OR (`or`)**: Returns `True` if one of the statements is true.
  ```python
  result = x or y
  print(result)  # Output: True
  ```

- **NOT (`not`)**: Reverses the result, returns `False` if the result is true.
  ```python
  result = not x
  print(result)  # Output: False
  ```

### 4. Assignment Operators
Assignment operators are used to assign values to variables.

- **Equals (`=`)**: Assigns value from right side operands to left side operand.
  ```python
  c = 10
  print(c)  # Output: 10
  ```

- **Add and Assign (`+=`)**: Adds right operand to the left operand and assigns the result to the left operand.
  ```python
  c += 5
  print(c)  # Output: 15
  ```

- **Subtract and Assign (`-=`)**: Subtracts right operand from the left operand and assigns the result to the left operand.
  ```python
  c -= 3
  print(c)  # Output: 12
  ```

- **Multiply and Assign (`*=`)**: Multiplies left operand with the right operand and assigns the result to the left operand.
  ```python
  c *= 2
  print(c)  # Output: 24
  ```

- **Divide and Assign (`/=`)**: Divides left operand by the right operand and assigns the result to the left operand.
  ```python
  c /= 4
  print(c)  # Output: 6.0
  ```

- **Modulus and Assign (`%=`)**: Takes modulus using two operands and assigns the result to the left operand.
  ```python
  c %= 5
  print(c)  # Output: 1.0
  ```

### 5. Bitwise Operators
Bitwise operators perform operations on binary numbers.

- **AND (`&`)**: Performs bitwise AND.
  ```python
  a = 10  # 1010 in binary
  b = 4   # 0100 in binary
  result = a & b
  print(result)  # Output: 0
  ```

- **OR (`|`)**: Performs bitwise OR.
  ```python
  result = a | b
  print(result)  # Output: 14 (1110 in binary)
  ```

- **XOR (`^`)**: Performs bitwise XOR.
  ```python
  result = a ^ b
  print(result)  # Output: 14 (1110 in binary)
  ```

- **NOT (`~`)**: Performs bitwise NOT.
  ```python
  result = ~a
  print(result)  # Output: -11
  ```

- **Left Shift (`<<`)**: Shifts bits to the left.
  ```python
  result = a << 2
  print(result)  # Output: 40 (101000 in binary)
  ```

- **Right Shift (`>>`)**: Shifts bits to the right.
  ```python
  result = a >> 2
  print(result)  # Output: 2 (10 in binary)
  ```

### 6. Membership Operators
Membership operators test for membership in a sequence (e.g., strings, lists, tuples).

- **In (`in`)**: Returns `True` if a value is found in the sequence.
  ```python
  my_list = [1, 2, 3, 4]
  result = 3 in my_list
  print(result)  # Output: True
  ```

- **Not In (`not in`)**: Returns `True` if a value is not found in the sequence.
  ```python
  result = 5 not in my_list
  print(result)  # Output: True
  ```

### 7. Identity Operators
Identity operators compare the memory locations of two objects.

- **Is (`is`)**: Returns `True` if two variables point to the same object.
  ```python
  x = ["apple", "banana"]
  y = x
  result = (x is y)
  print(result)  # Output: True
  ```

- **Is Not (`is not`)**: Returns `True` if two variables do not point to the same object.
  ```python
  y = ["apple", "banana"]
  result = (x is not y)
  print(result)  # Output: True
  ```

These are the basic operators in Python. Each type of operator serves a specific purpose and is crucial for performing various operations in your programs. Understanding how to use them effectively will greatly enhance your ability to write functional and efficient Python code.

'''