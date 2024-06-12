# Program to count the number of even numbers in a given range

# Function to count even numbers
def count_even_numbers(start, stop):
    even_count = 0
    for num in range(start, stop + 1):
        if num % 2 == 0:
            even_count += 1
    return even_count

# Input from the user
start = int(input("Enter the start of the range: "))
stop = int(input("Enter the end of the range: "))

# Counting even numbers in the given range
even_count = count_even_numbers(start, stop)

# Printing the result
print(f"There are {even_count} even numbers between {start} and {stop}.")
