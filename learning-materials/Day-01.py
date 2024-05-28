### Introduction to Python: Day 1

#### What is Python?
'''
Python is a high-level, interpreted, general-purpose programming language known for its simplicity and readability. Created by Guido van Rossum and first released in 1991, 
Python emphasizes code readability with its use of significant whitespace. Its syntax is clear and intuitive, making it an excellent choice for beginners while also being powerful enough for experienced programmers.
'''

#### Key Features of Python:
'''
1. **Readability:** Python’s syntax is designed to be readable and straightforward.
2. **Interpreted Language:** Python code is executed line-by-line, which makes debugging easier.
3. **Dynamically Typed:** Variables in Python do not need an explicit declaration to reserve memory space.
4. **Versatile:** Suitable for web development, data analysis, artificial intelligence, scientific computing, and more.
5. **Extensive Libraries:** Python has a vast standard library and an active community contributing to many third-party libraries.

'''
#### Setting Up Python
'''

1. **Installation:**
   - Download the latest version of Python from [python.org](https://www.python.org/).
   - Follow the installation instructions for your operating system (Windows, macOS, or Linux).
   - Ensure that Python is added to your system’s PATH.

2. **Integrated Development Environment (IDE):**
   - While you can write Python code in any text editor, IDEs like PyCharm, VSCode, and Jupyter Notebooks offer features that make coding easier, such as syntax highlighting, debugging tools, and project management.

#### Writing Your First Python Program

Let's start with the traditional "Hello, World!" program to get a feel for Python’s syntax.

1. **Creating a Python File:**
   - Open your text editor or IDE.
   - Create a new file and save it with a `.py` extension (e.g., `hello.py`).

2. **Writing the Code:**
   - Type the following code into your file:

   ```python
   print("Hello, World!")
   ```

3. **Running the Program:**
   - Open your terminal or command prompt.
   - Navigate to the directory where your `hello.py` file is saved.
   - Run the program by typing:
     ```sh
     python hello.py
     ```
'''

'''

#### Basic Concepts

1. **Variables and Data Types:**

   ```python
   # String
   name = "Alice"
   # Integer
   age = 30
   # Float
   height = 5.5
   # Boolean
   is_student = True
   ```

2. **Comments:**
   - Use the `#` symbol to add comments to your code.

   ```python
   # This is a single-line comment
   ```

3. **Basic Operations:**

   ```python
   # Arithmetic operations
   sum = 10 + 5
   difference = 10 - 5
   product = 10 * 5
   quotient = 10 / 5
   ```

4. **Control Structures:**

   - **If Statements:**

     ```python
     if age > 18:
         print("Adult")
     else:
         print("Minor")
     ```

   - **Loops:**

     ```python
     # For Loop
     for i in range(5):
         print(i)

     # While Loop
     count = 0
     while count < 5:
         print(count)
         count += 1
     ```

5. **Functions:**

   ```python
   def greet(name):
       return f"Hello, {name}!"

   print(greet("Alice"))
   ```

   '''
