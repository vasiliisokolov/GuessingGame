#GuessingGame
import random

print("\t Welcome to Guessing Game!")
print("\nI guessed a natural number from 1 to 100.")
print("Try to guess it!\n")

#start values
the_number = random.randint(1, 100)
guess = int(input("You try: "))
tries = 1

#body
while guess != the_number:
    if guess > the_number:
        print("Less...")
    else:
        print("More...")
    guess = int(input("You try: "))
    tries += 1
print("You won! Answer is ", the_number)
print("You gueesed it for ", tries, "tryes!")
input("\n\nPress Enter to exit!")