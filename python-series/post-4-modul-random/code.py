# Define a list
fruits = ["apple", "banana", "cherry", "date"]

# Access elements by index
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

# Access elements by offset (negative index)
print(fruits[-1])  # Output: date
print(fruits[-3])  # Output: banana

# Append an element to the end of the list
fruits.append("elderberry")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Insert an element at a specific index
fruits.insert(1, "blueberry")
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

fruits = ["apple", "banana", "cherry"]
# print(fruits[3])  # IndexError: list index out of range

index = 3
if index < len(fruits):
    print(fruits[index])
else:
    print("Index out of range.")

nested_list = [
    ["apple", "banana"],
    ["cherry", "date"],
    ["elderberry", "fig"]
]

# Access elements in a nested list
print(nested_list[0][1])  # Output: banana
print(nested_list[2][0])  # Output: elderberry

# Append an element to a nested list
nested_list[1].append("grape")
print(nested_list)  # Output: [['apple', 'banana'], ['cherry', 'date', 'grape'], ['elderberry', 'fig']]
