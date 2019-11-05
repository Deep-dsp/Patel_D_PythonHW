
#define python function that takes argument..

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