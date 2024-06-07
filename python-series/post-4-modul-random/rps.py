import random

print("Welcome to Rock, Paper, Scissors!")
print("Choose one: 0 for rock, 1 for paper, or 2 for scissors")

# List of choices
choices = ["rock", "paper", "scissors"]

# Randomly select an index for the computer
computer_index = random.randint(0, 2)
computer_choice = choices[computer_index]

# Get player's choice as an index
player_index = int(input("Enter your choice (0, 1, or 2): "))
player_choice = choices[player_index]

# Determine the winner
if player_index == computer_index:
    print(f"Both chose {player_choice}. It's a tie!")
elif (player_index == 0 and computer_index == 2) or \
     (player_index == 1 and computer_index == 0) or \
     (player_index == 2 and computer_index == 1):
    print(f"You chose {player_choice} and the computer chose {computer_choice}. You win!")
else:
    print(f"You chose {player_choice} and the computer chose {computer_choice}. You lose!")
