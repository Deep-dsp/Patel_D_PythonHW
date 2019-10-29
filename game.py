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
	print("********************************************\n\n")
	print("Choose your weapon!\n\n")
	print("********************************************\n\n")

	player = input("Choose rock, paper or scissors: ")

	print("computer choose:", computer, "\n")
	print("player choose:", player, "\n")

	if player.lower() == "quit":
		exit()

	elif computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("you lose!", computer, "covers", player, "\n")
		else:
			print("you won!", player, "smashes", computer, "\n")


	elif player.lower() == "paper":
		if computer == "scissors":
			print("you lose!", computer, "cuts", player, "\n")
		else:
			print("you won!", player, "smashes", computer, "\n")


	elif player.lower() == "scissors":
		if computer == "rock":
			print("you lose!", computer, "smashes", player, "\n")
		else:
			print("you won!", player, "cuts", computer, "\n")

	else:
		print("That's not a valid choice, Try again!!")

	#need to check all of out conditions after checking for a tie.
	player = False
	computer = choices[randint(0,2)]