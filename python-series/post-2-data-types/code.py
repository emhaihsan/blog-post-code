import math

# 1. Data Types
x = 5
y = -3
print(type(x))  # Output: <class 'int'>

pi = 3.14
negative_float = -2.7
print(type(pi))  # Output: <class 'float'>

greeting = "Hello"
name = 'Python'
print(type(greeting))  # Output: <class 'str'>
print(type(name))  # Output: <class 'str'>

is_python_easy = True
is_java_hard = False
print(type(is_python_easy))  # Output: <class 'bool'>

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.14, True]
print(type(fruits))  # Output: <class 'list'>

# Defines a tuple
coordinates = (10.0, 20.0, 30.0)
print(type(coordinates))  # Output: <class 'tuple'>

# Attempt to change the value in the tuple (this will produce an error)
# coordinates[0] = 40.0
person = {"name": "Alice", "age": 25, "city": "New York"}
print(type(person))  # Output: <class 'dict'>

# 2. Data Types Conversion
num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10
print(type(num_int))  # Output: <class 'int'>

num_str = "10.5"
num_float = float(num_str)
print(num_float)  # Output: 10.5
print(type(num_float))  # Output: <class 'float'>

num = 100
num_str = str(num)
print(num_str)  # Output: "100"
print(type(num_str))  # Output: <class 'str'>

num = 0
bool_val = bool(num)
print(bool_val)  # Output: False
print(type(bool_val))  # Output: <class 'bool'>

# 3. String Manipulation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

word = "Hello"
repeated_word = word * 3
print(repeated_word)  # Output: HelloHelloHello

greeting = "Hello"
first_char = greeting[0]
print(first_char)  # Output: H

text = "Python Programming"
sliced_text = text[0:6]
print(sliced_text)  # Output: Python

message = "Hello World"
upper_message = message.upper()
lower_message = message.lower()
print(upper_message)  # Output: HELLO WORLD
print(lower_message)  # Output: hello world

text = "I love Python"
new_text = text.replace("Python", "coding")
print(new_text)  # Output: I love coding

spaced_text = "   Hello World   "
trimmed_text = spaced_text.strip()
print(trimmed_text)  # Output: Hello World

# 4. String Formatting
name = "Alice"
age = 25
formatted_string = "Hello, my name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: Hello, my name is Alice and I am 25 years old.

formatted_string = "Hello, my name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: Hello, my name is Alice and I am 25 years old.

formatted_string = "Hello, my name is {0} and I am {1} years old.".format(name, age)
print(formatted_string)  # Output: Hello, my name is Alice and I am 25 years old.

formatted_string = "Hello, my name is {name} and I am {age} years old.".format(name=name, age=age)
print(formatted_string)  # Output: Hello, my name is Alice and I am 25 years old.

formatted_string = f"Hello, my name is {name} and I am {age} years old."
print(formatted_string)  # Output: Hello, my name is Alice and I am 25 years old.

radius = 5
area = f"The area of a circle with radius {radius} is {math.pi * radius ** 2:.2f}."
print(area)  # Output: The area of a circle with radius 5 is 78.54.