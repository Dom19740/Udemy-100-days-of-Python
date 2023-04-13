import art.caesar_art

print(art.caesar_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(direction, text, shift):

    result = ""
  
    for letter_position in text:

        if letter_position.isalpha():
    
            if direction == "e":
                new_letter_position = (alphabet.index(letter_position) + shift)
                if (new_letter_position > 25):
                    new_letter_position = new_letter_position - 26
            elif direction == "d":
                new_letter_position = (alphabet.index(letter_position) - shift)
                if (new_letter_position < 0):
                    new_letter_position = new_letter_position + 26
            result += (alphabet[new_letter_position])

        else:
            result += letter_position
  
    print(f"\nThe encrypted/decrypted text is \"{result}\"\n")
  
    global go_again
    go_again = input("Type 'y' to go again. Otherwise type 'n'\n")
    while go_again != "y" and go_again != "n":
      go_again = input("Only type 'y' or 'n'\n")


go_again = "y"

while go_again == "y":

  direction = input("\nType 'e' to encrypt, type 'd' to decrypt text:\n")
  
  while direction != "e" and direction != "d":
      direction = input("Only type 'e' to encrypt, type 'd' to decrypt text:\n")
    
  text = input("\nType your message:\n").lower()
  
  shift = (int(input("\nType the shift number:\n"))) % 26

  caesar(direction, text, shift)

print("\nThank you for using Caesar Cipher, Have a nice day!")

