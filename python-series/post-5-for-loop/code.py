# Define a list of fruits
fruits = ["apple", "banana", "cherry"]

# Iterate through the list and print each fruit
for fruit in fruits:
    print(fruit)

# Iterate through a sequence of numbers from 0 to 4
for i in range(5):
    print(i)

# Print range object
print(range(5))

# Convert range object to list to see the numbers
print(list(range(5)))

# Iterate through a sequence of numbers from 1 to 9 with a step of 2
for i in range(1, 10, 2):
    print(i)

# Iterate through a sequence of numbers from 5 to 1
for i in range(5, 0, -1):
    print(i)

# Example using else with for loop
for i in range(5):
    print(i)
else:
    print("Loop finished successfully!")

# Example using break and continue
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Iterate through each character in a string
word = "Python"
for char in word:
    print(char)
