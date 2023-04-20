from art.higherlower_art import logo, vs
from data.higherlower_gamedata import data
import os
import random

start_again = 'y'

while start_again == 'y':
    os.system('cls')
    print(logo)


    def select_compare_b():
        """pick a random entry and pass it into a new compare_B dictionary"""
        choice_B = random.choice(data)
        compare_B = {key: value for key, value in choice_B.items()}

        return choice_B

    compare_B = select_compare_b()


    keep_playing = True
    start_again = 'y'
    score = 0
    guess = False

    #while loop to continue playing while guess is correct
    while keep_playing:

        # pass compare_b into compare_a and choose new compare_b
        compare_A = compare_B
        compare_B = select_compare_b()

        # pick again if they are the same
        while compare_B["follower_count"] == compare_A["follower_count"]:
            compare_B = select_compare_b()

        os.system('cls')
        print(logo)

        # print score at start
        if guess:
            print(f"You are correct!! Current Score: {score}.\n")
        else:
            print("Current Score: 0\n")

        # print items to compare
        print(f"COMPARE A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}...")
        print(vs)
        print(f"AGAINST B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")

        # prompt for input guess
        print(compare_A['follower_count'], compare_B['follower_count'])  # HINT TO DELETE
        guess = input("\nWho has more followers? Type 'a' or 'b': ").lower()

        # check to see if guess is correct and play again or ask to exit
        if (guess == 'a' and compare_A['follower_count'] > compare_B['follower_count']) or (
                guess == 'b' and compare_A['follower_count'] < compare_B['follower_count']):
            score += 1
        else:
            print(f"\nSorry, wrong guess!! Final score {score}.")
            keep_playing = False

    start_again = input("\n\nWould you like to start again? (y/n) ").lower()

print("\n")
