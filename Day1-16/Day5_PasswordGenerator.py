#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
 

#shuffle letters, nummbers and symbols

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

#take x nr_symbols from each and add to chosen list

chosen_letters = []
chosen_numbers = []
chosen_symbols = []

# loop to iterate over the random list and take the required number of items

for i in range(nr_letters):
    chosen_letters.append(letters[i])

for i in range(nr_numbers):
    chosen_numbers.append(numbers[i])

for i in range(nr_symbols):
    chosen_symbols.append(symbols[i])

#make, shuffle and print chosen list

chosen_letters.extend(chosen_numbers)
chosen_letters.extend(chosen_symbols)

random.shuffle(chosen_letters)

print("".join(chosen_letters))