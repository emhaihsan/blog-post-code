import random

def main():
    # The computer selects a random number between 1 and 100
    target_number = random.randint(1, 100)
    guess = None

    print("Welcome to the number guessing game!")
    print("I have chosen a number between 1 and 100.")
    print("Try to guess the number!")

    while guess != target_number:
        # The user enters their guess
        guess = int(input("Enter your guess: "))

        # Checking the user's guess
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number.")

if __name__ == "__main__":
    main()
