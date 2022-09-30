from http.client import ImproperConnectionState

import random

guesses = []

# computers generates number to ge guessed
myComputer = random.randint(1,70)

player = int(input("Enter a number between 1-70--> "))
guesses.append(player) # store first number entered by player

while player != myComputer:
    if player > myComputer:
        print("number is too high")
    else:
        print("Number is too low: ")
    player = int(input("Enter a number between 1-70: "))
    guesses.append(player) # append numbers entered by player to check them


# player guessed the number right from the first time 
else:
    print("You have guessed right: good job!")
    print("It took you %i guesses. " % len(guesses))
    print("These were your guesses: ")
    print(guesses)