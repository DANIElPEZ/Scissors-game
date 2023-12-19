import random

choices = ["rock","paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    player = input("rock, paper, or scissors?: ").lower()

if player == computer:
    print("computer chose: ", computer)
    print("Player chose: ", player) 
    print("Tie!", player) 

elif player == "rock":
    if computer == "paper":
        print("computer chose: ", computer)
        print("Player chose: ", player) 
        print("Computer wins!")
    elif computer == "scissors":
        print("computer chose: ", computer)
        print("Player chose: ", player) 
        print("Player Wins")

elif player == "paper":
    if computer == "rock":
        print("computer chose: ", computer)
        print("Player chose: ", player) 
        print("Player wins!")
    elif computer == "scissors":
        print("computer chose: ", computer)
        print("Player chose: ", player) 
        print("Computer Wins")

elif player == "scissor":
    if computer == "rock":
        print("computer chose: ", computer)
        print("Player chose: ", player) 
        print("Computer wins!")
    elif computer == "paper":
        print("computer chose: ", computer)
        print("Player chose: ", player) 
        print("Player Wins")
