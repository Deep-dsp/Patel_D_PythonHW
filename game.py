#import random package so that we can generate a random choice.
from random import randint

# choices is an array => an array is a containor that can hold multiple value.
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of the these choices.
computer = choices[randint(0,2)] 

# set up the game loop so that we don't have to restart all the time.
player = False

while player is False:
	# set player to True
	player = input("Choose rock, paper or scissors:\n")

	print("computer choose:", computer, "\n")
	print("player choose:", player, "\n")

	if player == "quit":
		exit()

	if computer == player:
		print("tie! no one wins, play again")


	#need to check all of out conditions after checking for a tie.
	player = False
	computer = choices[randint(0,2)]
