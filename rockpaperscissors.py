#!/usr/bin/env python3
"""Rock Paper Scissors Game | by Ryan Trepanier """
import random as rand

# user needs to make a choice
# random module
# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)

def main():
    """drives the game"""

    options = ["rock", "paper", "scissors"]
    score = [0, 0]
    for round in range(3):
        choice = input("Rock, Paper, or Scissors?\n>").lower()
        if choice in options:
            comp_choice = rand.choice(options)
            print("Your choice:", choice)
            print("Computer's choice:", comp_choice)
            if choice == "rock" and comp_choice == "scissors":
                print("You won!")
                score[0] += 1
            elif choice == "paper" and comp_choice == "rock":
                print("You won!")
                score[0] += 1
            elif choice == "scissors" and comp_choice == "paper":
                print("You won!")
                score[0] += 1
            elif choice == "rock" and comp_choice == "rock":
                print("You tied!")
            elif choice == "paper" and comp_choice == "paper":
                print("You tied!")
            elif choice == "scissors" and comp_choice == "scissors":
                print("You tied!")
            else:
                print("You lost :(")
                score[1] += 1
        else:
            print("Not a valid choice. You lose.")
            score[1] += 1

    print("\n\n\nTotal score:\n", "You ->", score[0],"\n", "CPU ->", score[1])
    if score[0] > score[1]:
        print("Congrats! You beat the computer!")
    elif score[0] < score[1]:
        print("The machines have beaten humanity :(")
    else:
        print("It's a tie!")

main()