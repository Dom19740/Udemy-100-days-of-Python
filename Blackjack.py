from blackjack_art import logo
import os
import random


# def play_game():
os.system('cls')
print(logo)

# restart = input("Do you want to play? 'y or 'n': ")



#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#cards = [11, 2, 3, 4, 5, 6, 10]
cards = [10, 5, 1, 11]

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
    return player_cards, player_scores


#deal 2 player cards, 1 cpu card
deal_card("Player1")
deal_card("Player1")
deal_card("Cpu")


#function to print cards and totals + convert 11 to 1 if over 21
def show_cards(player):
    
    if player == "Cpu" and player_scores["Player1"] == 21 and len(
            player_cards["Cpu"]) == 1:
        deal_card("Cpu")
        
    if player_scores[player] > 21 and 11 in player_cards[player]:
        player_cards[player].remove(11)
        player_cards[player].append(1)
        player_scores[player] = sum(player_cards[player])       
                
    cards_str = (" + ".join(str(x) for x in player_cards[player]))
    print(f"\n{player} cards are: {cards_str}")
    # print(player_cards[player])
    print(f"{player} score is {player_scores[player]}")
    return player_cards, player_scores

#show all
show_cards("Cpu")
show_cards("Player1")

# hit_stand = ""


#function to assess scores
def assess_score():

    
    highest_score = 0
    winner = ""
    hit_stand = ""

    if player_scores["Player1"] == 21 and player_cards["Cpu"] and player_scores["Cpu"] !=21:
        print("\nYou have BLACKJACK. Congratulations, You WIN!!")

    elif player_scores["Player1"] == player_scores["Cpu"] and len(player_cards["Player1"]) == len(player_cards["Cpu"]):
        # print(f"hit stand = {hit_stand}")
        # print(player_cards["Player1"]) #DELETE

        if len(player_cards["Player1"]) > 2:
            show_cards("Cpu")
        print("\nIt's a draw, no one wins the hand.")

    elif player_scores["Cpu"] > 21:
        show_cards("Cpu")
        if player_scores["Cpu"] > 21:
            print(player_cards["Cpu"]) #DELETE
            print("\nCpu is BUST, Congratulations, you WIN!!")
       

    elif player_scores["Player1"] > 21:
        deal_card("Cpu")
        show_cards("Cpu")
        print("\nYou are BUST, you LOSE!!")

    elif player_scores["Cpu"] > 16 and player_scores["Cpu"] < 22:
        show_cards("Cpu")

        for player in player_scores:
            if player_scores[player] > highest_score:
                highest_score = player_scores[player]
                winner = player 
        
        if winner == "Player1":
            print("\nCongratulations, you WIN!!")
        else:
            print("\nCpu WINS, UNLUCKY!!")

    else:
        hit_stand = input("\nType 'h' to Hit or 's' to Stand: ")
        while hit_stand != 'h' and hit_stand != 's':
            input("\nType 'h' to Hit or 's' to Stand: ")


    if hit_stand == "h":
        deal_card("Player1")
        show_cards("Player1")
        assess_score()


    if hit_stand == "s":
        while player_scores["Cpu"] < 17:
            deal_card("Cpu")
            # print(player_cards["Cpu"])

        assess_score()
        
    print("")
    # return hit_stand 

assess_score()

# play_game()