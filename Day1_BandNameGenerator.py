# Add functionality of Band Name Generator Exercise to include random answers
import random
print('\n!!! *** Welcome to the Random Band Name Generator *** !!!\n')

random_numberA = random.randint(1, 4)

if random_numberA == 1:
    answerA = input('Which city did you grow up in? ')
elif random_numberA == 2:
    answerA = input('What was the first word of the street you grew up on? ')
elif random_numberA == 3:
    answerA = (input('What was the name of your first teacher at school? ')) + "'s"
elif random_numberA == 4:
    answerA = input('What was the location of your first holiday? ')


random_numberB = random.randint(1, 4)

if random_numberB == 1:
    answerB = input('What is the name of a pet? ')
elif random_numberB == 2:
    answerB = input('What is your favourite animal? ')
elif random_numberB == 3:
    answerB = input('What is your mums job? ')
elif random_numberB == 4:
    answerB = input('What is your favourite item of clothing? ')

print(f'\nYour band name could be {answerA} {answerB}\n')
