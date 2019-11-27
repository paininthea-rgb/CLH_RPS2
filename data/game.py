# import the random package so that we can generate a random choice
import random

# set up some variables for player and AI lives
player_lives = 0
computer_lives = 0


# choices is an array => an array is a container that can hold multiple values
# arrays are 0-based -> first entry is 0, 2nd is 1, 3rd is 2 etc

def Choose_Option():
    user_choice = input("Choose Rock, Paper Scissors:  ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("I don't understand, try again.")
        Choose_Option()
    return user_choice


# set the computer variable to one of these choices (0, 1 or 2)
# computer = choices[randint(0, 2)]
def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


# set up the game loop so that we don't have to restart all the time
while True:
    print("")
    user_choice = Choose_Option()
    comp_choice = Computer_Option()
    print("")
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. The computer chose rock. You tied.")
        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You lose.")
            computer_lives += 1
        elif comp_choice == "s":
            print("You chose rock. The computer chose scissors. You win.")
            player_lives += 1
    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper. The computer chose rock. You win.")
            player_lives += 1
        elif comp_choice == "p":
            print("You chose paper. The computer chose paper. You tied.")
        elif comp_choice == "s":
            print("You chose paper. The computer chose scissors. You lose.")
            computer_lives += 1
    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. The computer chose rock. You lose.")
            computer_lives += 1
        elif comp_choice == "p":
            print("You chose scissors. The computer chose paper. You win.")
            player_lives += 1
        elif comp_choice == "s":
            print("You chose scissors. The computer chose scissors. You tied.")

    # handle all lives lost for player or AI
    print("")
    print("Player wins:" + str(player_lives))
    print("Computer wins:" + str(computer_lives))
    print("")

    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
