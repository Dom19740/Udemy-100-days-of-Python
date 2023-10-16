# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

#  Open letter template
with open("./Input/Letters/starting_letter.txt", mode="r") as letter_file:
    letter_template = letter_file.read()

# Open invited names txt and save as a list
invited_names_txt = open("./Input/Names/invited_names.txt", "r")
original_list = invited_names_txt.readlines()

# Remove the \n in the list entries
modified_list = [entry.strip() for entry in original_list]

# for each name in the list, generate a letter from template by using replace and save
for name in modified_list:
    letter = letter_template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as name_file:
        name_file.write(letter)