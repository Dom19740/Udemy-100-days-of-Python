from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


FONT = ("Calibri", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #ç

def generate():

    entry_password.delete(0, END)

    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = ''.join(password_list)

    entry_password.insert(0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    # get the data from the entry widgets
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    is_ok = False

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Fill in all fields")
    else:
        is_ok = messagebox.askokcancel(title="Save", message=f"Website:    {website}\n"
                                                             f"Email:         {email}\n"
                                                             f"Password:  {password}\n\n"
                                                             f"Continue to save?")
    if is_ok:
        # open the file for appending
        with open('data.txt', 'a') as data_file:
            # write the data to the file as a line
            data_file.write(f'{website} | {email} | {password}\n')

        # clear the entry widgets for the next set of data
        entry_website.delete(0, END)
        entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# row 1
label_website = Label(text="Website:", font=FONT)
label_website.grid(row=1, column=0)

entry_website = Entry(width=35)
entry_website.get()
entry_website.focus()
entry_website.grid(row=1, column=1, columnspan=2)

# row 2
label_email = Label(text="Email/User:", font=FONT)
label_email.grid(row=2, column=0)

entry_email = Entry(width=35)
entry_email.insert(0, string="bob@gmail.com")
entry_email.get()
entry_email.grid(row=2, column=1, columnspan=2)

# row 3
label_password = Label(text="Password", font=FONT)
label_password.grid(row=3, column=0)

entry_password = Entry(width=35)
entry_password.get()
entry_password.grid(row=3, column=1, columnspan=2)

button_generate = Button(text="Generate", command=generate, font=FONT)
button_generate.grid(row=3, column=2)

# row 4
button_add = Button(text="Add", command=add, width=10, font=FONT)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()
