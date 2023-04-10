#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from guessthenumber_art import logo
import os
import random

os.system('cls')
print(logo)

#get random number
number = random.randint(1, 100)

print("\nWelcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 100.")
# print(f"Pssst, the correct answer is {number}.")2


difficulty = input("\nChoose a difficulty. 'e' for Easy of 'h' for Hard: ")

while difficulty != 'e' and difficulty != 'h':
    difficulty = input("\nType 'e' for Easy or 'h' for Hard: ")

if difficulty == 'e':
    attempts = 10
    print(f"\nYou have {attempts} attempts remaining to guess the number.")
else:
    attempts = 5
    print(f"\nYou have {attempts} attempts remaining to guess the number.")


def guess_number():
        
        def wrong_guess():
            global attempts
            print(f"You have {attempts -1} attenpts remaining.")
            attempts -=1
            guess_number()


        guess = int(input("\nMake a guess: "))

        if guess == number:
            print(f"\nYou got it! The answer was {number}!!\n")
        elif guess > number and attempts > 1:
            print("Too high! Guess again.")
            wrong_guess()
        elif guess < number and attempts > 1:
            print("Too low! Guess again.")
            wrong_guess()
        else:
            print("Wrong again.")
            print("You ran out of guesses, you lose!\n")
    

guess_number()