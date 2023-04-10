from higherlower_art import logo, vs
from higherlower_gamedata import data
import os
import random

start_again = 'y'

while start_again == 'y':
    os.system('cls')
    print(logo)


    #function to pick an entry and pass into new compare_B dictionary
    def select_compare_B():
        choice_B = random.choice(data)
        compare_B = {key: value for key, value in choice_B.items()}

        return choice_B

    compare_B = select_compare_B()


    play_again = True
    start_again = 'y'
    score = 0
    guess = False

    #while lopp to continue playing while guess is correct
    while play_again:

        #pass compare_b into compare_a and choose new compare_b
        compare_A = compare_B
        compare_B = select_compare_B()

        #pick again if they are the same
        while compare_B["follower_count"] == compare_A["follower_count"]:
            compare_B = select_compare_B()

        #print items to compare
        os.system('cls')
        print(logo)

        if guess:
            print(f"You are correct!! Current Score: {score}.\n")
        else:
            print("Current Score: 0\n")

        print(f"COMPARE A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}...")
        print(vs)
        print(f"AGAINST B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}.")
    
        # print(compare_A['follower_count'], compare_B['follower_count']) #DELETE

        #prompt for input guess
        guess = input("\nWho has more follower? Type 'a' or 'b': ")

        #check to see if guess is correct
        if (guess == 'a' and compare_A['follower_count'] > compare_B['follower_count']) or (guess == 'b' and compare_A['follower_count'] < compare_B['follower_count']):
            score += 1
        else:
            print(f"\nSorry, wrong guess!! Final score {score}.")
            play_again = False

    start_again = input("\nWould you like to play again? (y/n) ")

print("\n")