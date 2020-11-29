# inport packages to extend python (just like we extend subline, or Atom, or VSCode)
from random import randint
# [] => this is an array. an array is a special type of container that can hold multipe itmes
# arrays are indexed (their contents get assigned a number)
# The index alwyas starts at 0
choices = ["rock", "paper", "scissors"]
player_lives = 1
AI_lives = 1

total_lives = 1

# this is the player choice
# player = input("choose rock, paper or scissors: ")
player = False;

# define a win or lose funtion
def winorlose(status):
	# print("inside winorlose function; status is: ", status)

	#print("You", status, "! Would you like to play again?")
	#choice = input("Y / N? ")
	if status == "won":
		pre_message = "You are the Yuuuuuuuuuugest winner ever! "
	else:
		pre_message = "You done trumped it, loser! "

	print(pre_message + "Would you like to play again? ")

	choice = input("Y / N? ")

	if choice == "Y" or choice == "y":

		global player_lives
		global AI_lives
		global player

		player_lives = 1
		AI_lives = 1
		player = False

# True and false are Boolean data types -> they are the equivalent of on or off, 1 or 0
player = False

	elif choice == "N" or choice == "n":
		# exit messae and quit
		print("You choose to quit! Better luck next time!")
		exit()

	else:
		print("Make a valid choice - Y or N")
		#this will generate a bug that we need to fix later
		choice = input("Y / N: ")

# set up our game loop
while player is False:
	print("=====================*/ RPS GAME /*======================")
	print("computer Lives:", AI_lives, "/", total_lives)
	print("Computer Lives:", AI_lives, "/", total_lives)
	print("player Lives:", player_lives, "/", total_lives)
	print("=========================================================")

@@ -30,7 +63,7 @@

	# if the player chose to quit, then exit the game
	if player == "quit":
		print("you chose to quit")
		print("you chose to quit, quitter!")
		exit()

	# player = true -> it has a value (rock, paper, or scissors)
@@ -52,67 +85,38 @@
	# always check for negative conditions first (the losing case)
	elif(computer == "rock"):
		if(player == "scissors"):
			print("you lose!")
			player_lives -= 1
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			AI_lives -= 1
			AI_lives = AI_lives - 1

	elif (computer == "paper"):
		if (player == "rock"):
			print("you lose!")
			player_lives -= 1
		if (player == "scissors"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win!")
			AI_lives -= 1
			AI_lives = AI_lives - 1

	elif (computer == "scissors"):
		if (player == "paper"):
			print("you lose!")
			player_lives -= 1
		if (player == "rock"):
			player_lives = player_lives - 1
			print("you lose! player lives: ", player_lives)
		else:
			print("you win")
			AI_lives -= 1
			print("you win!")
			AI_lives = AI_lives - 1

	if player_lives == 0:
		print("You lose! Would you like to play again?")
		choice = input("Y / N? ")

		if choice == "N" or choice == "n":
			print("You chose to quit! Better luck next time!")
			exit()

		elif choice == "Y" or choice == "y":
			# reset the player lives and the AI Lives
			# and set player to False so that our loop will restart
			player_lives = 1
			AI_lives = 1
			player = False
		winorlose("lost")

		else:
			print("Make a valid choice - Y or N")
			#this will generate a bug that we need to fix later
			choice = input("Y / N: ")

	if AI_lives == 0:
		print("You won! Would you like to play again?")
		choice = input("Y / N? ")


		if choice == "N" or choice == "n":
			print("You choose to quit! Better luck next time!")
			exit()
	elif AI_lives == 0:
		winorlose("won")

		elif choice == "Y" or choice == "y":
			# reset the player lives and the AI Lives
			# and set player to False so that our loop will restart
			player_lives = 1
			AI_lives = 1
			player = False

		else:
			print("Make a valid choice - Y or N")
			#this will generate a bug that we need to fix later
			choice = input("Y / N: ")
	else:
		player = False


	print("player has:", player_lives, "lives left")