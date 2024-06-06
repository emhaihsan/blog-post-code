print("Welcome to Adventure Quest.")
print("Your mission is to find the hidden treasure.")

# Starting the game
choice1 = input('You\'re in a dense forest. You see two paths ahead. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You encounter a river. There is a bridge and a boat. Type "bridge" to cross the bridge or "boat" to take the boat across. \n').lower()
    if choice2 == "bridge":
        choice3 = input("You safely cross the bridge. There are three caves ahead: one dark, one lit, and one with strange noises. Which cave do you enter? Type 'dark', 'lit', or 'noisy'. \n").lower()
        if choice3 == "dark":
            print("You stumble in the darkness and fall into a pit. Game Over.")
        elif choice3 == "lit":
            print("You find a treasure chest filled with gold! You Win!")
        elif choice3 == "noisy":
            print("A group of bats swarms you. Game Over.")
        else:
            print("You chose a cave that doesn't exist. Game Over.")
    else:
        print("The boat capsizes and you drown. Game Over.")
else:
    choice2 = input('You see a tall mountain. You can either climb it or go around it. Type "climb" to climb the mountain or "around" to go around it. \n').lower()
    if choice2 == "climb":
        choice3 = input("You reach the top of the mountain and see a temple. There are three entrances: one guarded by a statue, one by a fire, and one by a lion. Which entrance do you choose? Type 'statue', 'fire', or 'lion'. \n").lower()
        if choice3 == "statue":
            print("The statue comes to life and attacks you. Game Over.")
        elif choice3 == "fire":
            print("You walk through the fire unharmed and find the treasure! You Win!")
        elif choice3 == "lion":
            print("The lion roars and chases you away. Game Over.")
        else:
            print("You chose an entrance that doesn't exist. Game Over.")
    else:
        print("You get lost in the forest and can't find your way back. Game Over.")
