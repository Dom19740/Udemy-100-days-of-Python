# Opens a file and closes it when finished with it
with open("/Documents/Google Drive/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# Open a file and write to it. r = read, w = write, a = append
# with open("new_file.txt", mode="a") as file:
#     file.write("\nNew New text.")

# Absolute File Path
# /Documents/Google Drive/Desktop/my_file.txt

# Relative File Path
# ../../../../Desktop/my_file.txt

