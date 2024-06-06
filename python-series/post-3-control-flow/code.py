# Example 1: Check if age qualifies as an adult
age = 18

if age >= 18:
    print("You are an adult.")  # Output: You are an adult.
else:
    print("You are not an adult.")

# Example 2: Grading based on score with nested if
score = 85

if score >= 90:
    print("Grade: A")
else:
    if score >= 80:
        print("Grade: B")  # Output: Grade: B
    else:
        print("Grade: C")

# Example 3: Grading based on score with elif
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")  # Output: Grade: B
else:
    print("Grade: C")

# Example 4: Multiple independent if statements
score = 85
attendance = 90

if score >= 80:
    print("Passed the exam.")  # Output: Passed the exam.
if attendance >= 85:
    print("Good attendance.")  # Output: Good attendance.

# Example 5: Using logical AND to check multiple conditions
score = 85
attendance = 90

if score >= 80 and attendance >= 85:
    print("Excellent student.")  # Output: Excellent student.

# Example 6: Using logical OR to check multiple conditions
score = 70
attendance = 90

if score >= 80 or attendance >= 85:
    print("Good student.")  # Output: Good student.

# Example 7: Using logical NOT to invert a condition
is_raining = False

if not is_raining:
    print("Let's go for a walk.")  # Output: Let's go for a walk.
