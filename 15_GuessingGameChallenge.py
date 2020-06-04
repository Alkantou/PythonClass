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

x = random.randint(1, 100)
print(x)
guessing_list = [0]
g = int(input('Enter A number between 1 and 100: '))
dif = abs(g - x)
while dif != 0:
    if dif <= 10:
        print('Warm!')
        guessing_list.append(g)
        g = input('Enter A number between 1 and 100: ')
        dif = abs(g - x)
        if dif > abs(int(g) - int(guessing_list[-1])):
            print('Warmer!')
        else:
            print('Colder!')

    if int(dif) > 10:
        print('Cold!')
        guessing_list.append(g)
        g = input('Enter A number between 1 and 100: ')
        dif = abs(g - x)
print(f'You guessed it in {len(guessing_list)} tries')

