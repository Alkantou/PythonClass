# # Guessing Game Challenge
#
# Let's use `while` loops to create a guessing game.
#
# The Challenge:
#
# Write a program that picks a random integer from 1 to 100, and
# has players guess the number. The rules are:
#
# 1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# 2. On a player's first turn, if their guess is
#  * within 10 of the number, return "WARM!"
#  * further than 10 away from the number, return "COLD!"
# 3. On all subsequent turns, if a guess is
#  * closer to the number than the previous guess return "WARMER!"
#  * farther from the number than the previous guess, return "COLDER!"
# 4. When the player's guess equals the number, tell them they've guessed
# correctly *and* how many guesses it took!
#
# You can try this from scratch, or follow the steps outlined below. A separate Solution
# notebook has been provided. Good luck!
import random

x = int(random.randint(1, 100))
print(x)
guesses = [0]
input_number = int(input('Enter A number between 1 and 100: '))
differnce = int(abs(input_number - x))
guesses.append(input_number)
switch = False
while differnce != 0:


    if switch == True:

        if differnce < abs(int(x) - int(guesses[-2])):

            print('Warmer!')

            input_number = int(input('Enter A number between 1 and 100: '))

            guesses.append(input_number)

            differnce = abs(input_number - x)

        else:
            print('Colder!')

            input_number = int(input('Enter A number between 1 and 100: '))
            guesses.append(input_number)
            differnce = abs(input_number - x)

    if switch == False:

        if differnce <= 10:
            print('Warm!')

            input_number = int(input('Enter A number between 1 and 100: '))
            guesses.append(input_number)
            differnce = abs(input_number - x)
            switch = True
        else:
            print('Cold!')

            input_number = int(input('Enter A number between 1 and 100: '))
            guesses.append(input_number)
            differnce = abs(input_number - x)
            switch = True


print(f'You guessed it in {len(guesses)} tries')

