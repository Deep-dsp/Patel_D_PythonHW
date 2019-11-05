#import random package so that we can generate a random choice.
from random import randint
from gameFunctions import winlose


# st up some variables for player and AI lives
player_lives = 5
computer_lives = 5

# choices is an array => an array is a containor that can hold multiple value.
choices = ["rock", "paper", "scissors"]

# set the computer variable to one of the these choices.
computer = choices[randint(0,2)] 

# set up the game loop so that we don't have to restart all the time.
player = False

def winorlose(status):
	print("Called win or lose")
	print("*********************************")

	print("you", status, "Would you like to play again ??")

	choice = input("Y / N")
	print(choice)

	if (choice is "N") or (choice is "n"):
		print("you choose to quit.")
		exit()

	elif (choice is "y") or (choice is "Y"):
		# reset the game so that we can start all over again
		global computer
		global computer_lives
		global player
		global player_lives 
		
		player_lives = 5
		computer_lives = 5
		player = False
		computer = choices[randint(0,2)]

while player is False:
	# set player to True
	print("********************************************\n")
	print("Computer lives: ", computer_lives,"/5\n")
	print("player lives: ", player_lives,"/5\n")
	print("Choose your weapon!\n\n")
	print("********************************************\n")

	player = input("Choose rock, paper or scissors: ")
	player = player.lower()

	print("computer choose:", computer, "\n")
	print("player choose:", player, "\n")

	if player.lower() == "quit":
		exit()

	elif computer == player:
		print("tie! no one wins, play again")

	elif player.lower() == "rock":
		if computer == "paper":
			print("you lose!", computer, "covers", player, "\n")
			player_lives = player_lives - 1
			
		else:
			print("you won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1
			
	elif player.lower() == "paper":
		if computer == "scissors":
			print("you lose!", computer, "cuts", player, "\n")
			player_lives = player_lives - 1
			
		else:
			print("you won!", player, "smashes", computer, "\n")
			computer_lives = computer_lives - 1
			


	elif player.lower() == "scissors":
		if computer == "rock":
			print("you lose!", computer, "smashes", player, "\n")
			player_lives = player_lives - 1
			
		else:
			print("you won!", player, "cuts", computer, "\n")
			computer_lives = computer_lives - 1
		

	else:
		print("That's not a valid choice, Try again!!")


	# handle all lives lost for player or AI
	if player_lives is 0:
		winlose.winorlose("loose")
		# print("out of lives! you suck at this game. would you like to play it again?")
		# choice = input("Y / N")
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("you choose to quit.")
		# 	exit()

		# elif (choice is "y") or (choice is "Y"):
		# 	# reset the game so that we can start all over again
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices[randint(0,2)]


	elif computer_lives is 0:
		winlose.winorlose("won")
		# print("computer lives is out of lives! you suck at this game. would you like to play it again?")
		# choice = input("Y / N\n")
		# print(choice)

		# if (choice is "N") or (choice is "n"):
		# 	print("you choose to quit.")
		# 	exit()

		# elif (choice is "y") or (choice is "Y"):
		# 	# reset the game so that we can start all over again
		# 	player_lives = 5
		# 	computer_lives = 5
		# 	player = False
		# 	computer = choices[randint(0,2)]

	else:
		#need to check all of out conditions after checking for a tie.
		player = False
		computer = choices[randint(0,2)]