from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Calibri", 10, "normal")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #ç

def generate():
    # clear previous entry if there is one
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

    # enter generated password into empty field
    entry_password.insert(0, string=password)

    # copy password to clipboard
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():

    #get website to search for
    search_website = entry_website.get()

    try:
        # open data file and save as dictionary
        with open('data.json', 'r') as data_file:
            # reading data
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")

    else:
        if search_website in data:

            search_email = data[search_website]["email"]
            search_password = data[search_website]["password"]

            copy_password = messagebox.askokcancel(title=f"Site: {search_website}",
                                                   message=f"Email:         {search_email}"
                                                           f"\n"f"Password:  {search_password}"
                                                           f"\n\nCopy password to clipboard")
            if copy_password:
                # copy password to clipboard
                pyperclip.copy(search_password)

        else:
            messagebox.askokcancel(title="Error", message="No Site found")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    is_ok = False

    # get the data from the entry fields
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Fill in all fields")

    else:
        is_ok = messagebox.askokcancel(title="Save", message=f"Site:              {website}\n"
                                                             f"Email:            {email}\n"
                                                             f"Password:    {password}\n\n"
                                                             f"Save and copy password to Clipboard?")
    if is_ok:
        # open the file in read mode
        try:
            with open('data.json', 'r') as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                # saving new data
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
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
label_website = Label(text="Site:", font=FONT)
label_website.grid(row=1, column=0)

entry_website = Entry(width=35)
entry_website.insert(0, string="amazon")
entry_website.get()
entry_website.focus()
entry_website.grid(row=1, column=1)

button_search = Button(text="Search", command=search, font=FONT)
button_search.grid(row=1, column=2)

# row 2
label_email = Label(text="Email/User:", font=FONT)
label_email.grid(row=2, column=0)

entry_email = Entry(width=35)
entry_email.insert(0, string="bob@gmail.com")
entry_email.get()
entry_email.grid(row=2, column=1)

# row 3
label_password = Label(text="Password", font=FONT)
label_password.grid(row=3, column=0)

entry_password = Entry(width=35)
entry_password.get()
entry_password.grid(row=3, column=1)

button_generate = Button(text="Generate", command=generate, font=FONT)
button_generate.grid(row=2, column=2, rowspan=2)

# row 4
button_add = Button(text="Add", command=add, width=10, font=FONT)
button_add.grid(row=4, column=1)

window.mainloop()
