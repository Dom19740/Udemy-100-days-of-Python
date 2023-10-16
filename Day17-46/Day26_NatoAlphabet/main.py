# Create a dictionary in this format:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_dict = {row['letter']: row['code'] for (index, row) in data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.test
word = input('Enter a word: ').upper()

# Create a list of code ords corresponding to each letter in letter_list
code_words = [alphabet_dict[letter] for letter in word]
print(code_words)

