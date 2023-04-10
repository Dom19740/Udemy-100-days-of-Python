from blackjack_art import logo, prize, logo2
import os
import random

#variables to store game wins
player1_total = 0
cpu_total = 0

while True:

    os.system('cls')
    print(logo)

    #cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    #cards = [11, 2, 3, 4, 5, 6, 10]
    cards = [7, 6, 7]

    #make dictionaries to hold cards and scores
    player_cards = {
        "Player1": [],
        "Cpu": [],
    }

    player_scores = {
        "Player1": [],
        "Cpu": [],
    }


    #function to deal 1 card to player_cards and add player_scores
    def deal_card(player):
        player_cards[player].append(random.choice(cards))
        player_scores[player] = sum(player_cards[player])

        if player_scores[player] > 21 and 11 in player_cards[player]:
            player_cards[player].remove(11)
            player_cards[player].append(1)
            player_scores[player] = sum(player_cards[player])  

        return player_cards, player_scores


    #deal 2 player cards, 1 cpu card
    deal_card("Player1")
    deal_card("Player1")
    deal_card("Cpu")


    #function to print cards and totals + convert 11 to 1 if over 21
    def show_cards(player):
        
        if player_scores["Player1"] == 21 and len(
                player_cards["Cpu"]) == 1:
            deal_card("Cpu")
                    
        cards_str = (" + ".join(str(x) for x in player_cards[player]))
        print(f"\n{player} cards are: {cards_str}")
        print(f"{player} score is {player_scores[player]}")
        return player_cards, player_scores

    #show cards after 1st round
    show_cards("Cpu")
    show_cards("Player1")


    #function to assess scores
    def assess_score():

        highest_score = 0
        winner = ""
        hit_stand = ""
        global player1_total
        global cpu_total

        #Player1 Blackjack
        if player_scores["Player1"] == 21 and len(player_cards["Cpu"]) < 2:
 
            deal_card("Cpu")
            show_cards("Cpu")
            print("\nYou have BLACKJACK. Congratulations, You WIN!!")
            player1_total += 1

        elif player_scores["Player1"] == 21 and player_scores["Cpu"] !=21:
 
            while player_scores["Cpu"] < 17:
                deal_card("Cpu")
            if len(player_cards["Player1"]) > 2:
                show_cards("Cpu")
            print("\nYou have 21. Congratulations, You WIN!!")
            player1_total += 1
        
        #Both players same score
        elif player_scores["Player1"] == player_scores["Cpu"]:
            show_cards("Cpu")
            if len(player_cards["Player1"]) == len(player_cards["Cpu"]):
                print("\nIt's a draw, no one wins the hand.")
            elif len(player_cards["Player1"]) < len(player_cards["Cpu"]):
                print("\nYou have less cards. Congratulations, you WIN!!")
            else:
                print("\nYou have more cards. Unlucky you LOSE!!")

        #Cpu over 21, Bust
        elif player_scores["Cpu"] > 21:
            show_cards("Cpu")
            print("\nCpu is BUST, Congratulations, you WIN!!")
            player1_total += 1
        
        #Player1 over 21, Bust
        elif player_scores["Player1"] > 21:
            deal_card("Cpu")
            print("\nYou are BUST, you LOSE!!")
            show_cards("Cpu")
            cpu_total += 1

        #Both players in game, compare scores and print winner
        elif player_scores["Cpu"] > 16 and player_scores["Cpu"] < 22: ##############
            show_cards("Cpu")

            for player in player_scores:
                if player_scores[player] > highest_score:
                    highest_score = player_scores[player]
                    winner = player 
            
            if winner == "Player1":
                print("\nCongratulations, you WIN and get a PRIZE!!")
                print(prize)
                player1_total += 1

            else:
                print("\nCpu WINS, UNLUCKY!!")
                cpu_total += 1

        #prompt to hit for Player1
        else:
            hit_stand = input("\nAnother Card? Type 'h' to Hit or 's' to Stand: ")
            while hit_stand != 'h' and hit_stand != 's':
                hit_stand = input("\nType 'h' to Hit or 's' to Stand: ")

        if hit_stand == "h":
            deal_card("Player1")
            show_cards("Player1")
            assess_score()

        if hit_stand == "s":
            while player_scores["Cpu"] < 17:
                deal_card("Cpu")

            assess_score()

        # print("")
        return player1_total, cpu_total


    #assess scores first time
    player1_total, cpu_total = assess_score()

    # Ask the user if they want to play again
    play_again = input("\nWould you like to play another round? (y/n) ")
    if play_again == 'y':
        print("Starting game again...")
    else:
        if player1_total > cpu_total:
            print(f"\nFinal score {player1_total} : {cpu_total}, Well Done!!")
        elif player1_total < cpu_total:
            print(f"\nFinal score {player1_total} : {cpu_total}, Unlucky!!")
        else:
            print(f"\nFinal score {player1_total} : {cpu_total}, You Broke Even!!")
        break

print(logo2)
print("\nThanks for playing!\n")