'''

In Python, `str` is a built-in class used for representing and manipulating text. An instance of the `str` class is an immutable sequence of Unicode code points. This means that once a string is created, it cannot be changed. Any operations that modify a string will result in a new string being created.

Let's delve into various aspects of the `str` class, along with demonstrations:

### 1. Creating Strings

Strings in Python can be created using single quotes, double quotes, or triple quotes.

```python
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello,
World!'''

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)
```

### 2. String Concatenation and Repetition

Strings can be concatenated using the `+` operator and repeated using the `*` operator.

```python
str1 = "Hello"
str2 = "World"
concatenated = str1 + ", " + str2 + "!"
repeated = str1 * 3

print(concatenated)  # Output: Hello, World!
print(repeated)      # Output: HelloHelloHello
```

### 3. String Indexing and Slicing

Strings can be indexed to access individual characters and sliced to access substrings.

```python
s = "Python"

# Indexing
first_char = s[0]
last_char = s[-1]

# Slicing
substring = s[1:4]

print(first_char)  # Output: P
print(last_char)   # Output: n
print(substring)   # Output: yth
```

### 4. String Methods

Python's `str` class provides various methods for string manipulation. Here are a few commonly used methods:

- `str.upper()`: Converts all characters to uppercase.
- `str.lower()`: Converts all characters to lowercase.
- `str.strip()`: Removes leading and trailing whitespace.
- `str.replace(old, new)`: Replaces occurrences of a substring with another substring.
- `str.split(separator)`: Splits the string into a list of substrings based on the specified separator.
- `str.join(iterable)`: Concatenates a list of strings into a single string, with a specified separator.

```python
s = "  Hello, Python!  "

# Using methods
upper_s = s.upper()
lower_s = s.lower()
stripped_s = s.strip()
replaced_s = s.replace("Python", "World")
split_s = s.split(",")
joined_s = " ".join(["Hello", "World"])

print(upper_s)    # Output:   HELLO, PYTHON!  
print(lower_s)    # Output:   hello, python!  
print(stripped_s) # Output: Hello, Python!
print(replaced_s) # Output:   Hello, World!  
print(split_s)    # Output: ['  Hello', ' Python!  ']
print(joined_s)   # Output: Hello World
```

### 5. String Formatting

Python provides several ways to format strings, including the `%` operator, the `str.format()` method, and f-strings (formatted string literals).

#### Using the `%` Operator

```python
name = "John"
age = 30
formatted_string = "Name: %s, Age: %d" % (name, age)
print(formatted_string)  # Output: Name: John, Age: 30
```

#### Using `str.format()`

```python
formatted_string = "Name: {}, Age: {}".format(name, age)
print(formatted_string)  # Output: Name: John, Age: 30
```

#### Using F-strings (Python 3.6+)

```python
formatted_string = f"Name: {name}, Age: {age}"
print(formatted_string)  # Output: Name: John, Age: 30
```

### 6. Immutability

Strings in Python are immutable. This means that once a string is created, its contents cannot be changed. Any operation that modifies a string will return a new string.

```python
s = "Hello"
s = s.replace("H", "J")

print(s)  # Output: Jello
```

### 7. Multiline Strings

Multiline strings can be created using triple quotes. These are useful for including line breaks within the string.

```python
multiline_string = """This is a
multiline string.
It spans multiple lines."""

print(multiline_string)
```

### 8. Escape Sequences

Escape sequences are used to include special characters within strings. Some common escape sequences are:

- `\n`: Newline
- `\t`: Tab
- `\\`: Backslash
- `\'`: Single quote
- `\"`: Double quote

```python
escaped_string = "Line 1\nLine 2\tTabbed\nBackslash: \\"
print(escaped_string)
```

### 9. Raw Strings

Raw strings treat backslashes as literal characters and do not interpret escape sequences. They are created by prefixing the string with `r`.

```python
raw_string = r"Line 1\nLine 2\tTabbed\nBackslash: \\"
print(raw_string)  # Output: Line 1\nLine 2\tTabbed\nBackslash: \\
```

### 10. Unicode and Encoding

Python `str` instances are sequences of Unicode code points. You can encode and decode strings to and from bytes using the `encode` and `decode` methods.

```python
s = "Hello, World!"
encoded_s = s.encode('utf-8')
decoded_s = encoded_s.decode('utf-8')

print(encoded_s)  # Output: b'Hello, World!'
print(decoded_s)  # Output: Hello, World!
```

Understanding and using the `str` class effectively allows for powerful text processing capabilities in Python. Whether you're manipulating simple text or handling complex data, `str` provides a wide array of tools to work with.

'''