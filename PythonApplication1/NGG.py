import random
import os
score = 0
num = 0

def rand():
	global num
	num = random.randint(0,10)
	return game()


def menu():
	psq = input('1. Play     2. Shop     3. Quit    <:')

	if psq == '1':
		return rand()
	elif psq == '2':
		return shop()
	elif psq == '3':
		return gameOver()

def shop():
	print('Balance:', score)
	print('1. Increase Difficulty')
	print('2. Return to Menu') 
	print()
	c = input('<:')
	if c == '1':
		return increaseDif()
	elif c == '2':
		return menu()

def win():
	global score
	score = score + 1
	print('The Number was ', num)
	print('You won! Your new score is: ', score)
	return playAgain()

def playAgain():
	retry = input('Play again?{Y/N}')
	if retry == 'y':
		return rand()
	elif retry == 'n':
		return menu()
	else: 
		return playAgain()



def gameOver():
	a = input('Are you sure you want to quit?{y/n} ')
	if a == 'y':
		print('Cya! Thanks for playing!')
	elif a == 'n':
		return menu()
	else:
		return gameOver()



def game():
	while True:
		guess = int(input('Your guess: '))

		if 1337 == guess:
			return easterEgg()
		elif num == guess:
			return win()
		elif num != guess:
			print('Try again!')
			return game()

def easterEgg():
	print('You found the easter egg!')
	global score
	score = score + 20000
	print('Your score is, ', score)
	return playAgain()

def increaseDif():
	global score
	if score >= 10:
		score = score - 10
		print('Not finished')
	elif score < 10:
		print('Not Finished')
	return shop()

menu()