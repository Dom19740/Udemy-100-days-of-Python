import random

rock = '''
    _____
---(_____)
        (____)
        (_____)
        (____)
---.__(___)

ROCK
'''

paper = '''
    _______
---'   ____)_____
        _________)
        ________)
        ________)
---.________)

PAPER
'''

scissors = '''
    ______
---(______)_____
        ________)
        __________)
        (____)
---._(___)

SCISSORS
'''

game_images = [rock, paper, scissors]

def getComputerChoice(): #function to getComputerChoice

    #write a list with 3 options, and returns 1 option
    options = ['rock', 'paper', 'scissors']
    computerSelection = random.choice(options)
    print(f"Computer chooses: {computerSelection}")
    return computerSelection


def getplayerChoice(choice):  #function to getplayerChoice:

    #convert prompt input to lower case
    playerSelection = choice.lower()

    #get valid response from input
    validResponse = 0
    while validResponse == 0:
        
        if playerSelection == 'rock' or playerSelection == 'paper' or playerSelection == 'scissors':
            return playerSelection
            
        else: #while input isnt rock/paper/scissors, prompt again
            validResponse = 0
            choice = input("Enter ONLY Rock, Paper or Scissors: \n")
            playerSelection = choice.lower()     
    


def playRound(computerSelection, playerSelection): #function to play 1 round
        
    #take 2 parameters playerSelection and computerSelection and compare
    if ((computerSelection == 'rock' and playerSelection == 'scissors') or 
        (computerSelection == 'paper' and playerSelection == 'rock') or
        (computerSelection == 'scissors' and playerSelection == 'paper')):

        #RETURN a string that declares winner
        return 'computerWin'
        
        
    elif ((computerSelection == 'scissors' and playerSelection == 'rock') or
        (computerSelection == 'rock' and playerSelection == 'paper') or
        (computerSelection == 'paper' and playerSelection == 'scissors')):

        #RETURN a string that declares winner
        return 'playerWin'

    else:
        return 'draw'   
    

def game(): #play 5 rounds and keep score 
        
    computerScore = 0
    playerScore = 0
    drawScore = 0

    for i in range(5):
        
        print(f"\nGame No. {i + 1}")

        playerSelection = getplayerChoice(input("Enter Rock, Paper or Scissors: ")) #call getPlayerChoice function
        computerSelection = getComputerChoice();                                    #call getComputerChoice function
        roundResult = playRound(computerSelection, playerSelection);                #call playRound function
        
        if (roundResult == 'computerWin'):
            print('You Lose! ' + computerSelection + ' beats ' + playerSelection)
            computerScore += 1
        
        elif (roundResult == 'playerWin'):
            print('You Win! ' + playerSelection + ' beats ' + computerSelection)
            playerScore += 1
            
        else:
            print("It's a draw!")
            drawScore += 1
                
        
    #print out the winner
    if (computerScore > playerScore):
        print(f"\nYou LOST, {computerScore} - {playerScore}\n")
    elif (playerScore > computerScore):
        print(f"\nYou WON, {playerScore} - {computerScore}\n")
    else:
        print("\nIt was a DRAW, what a waste of everyone's time\n")

game()