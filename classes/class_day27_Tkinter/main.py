from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


#Button
def button_click():
    # print(entry.get())
    my_label.config(text=entry.get())
    my_label.config(text="Clicked")


button = Button(text="Click Me", command=button_click)
button.grid(column=1, row=1)

new_button = Button(text="Also click me", command=button_click)
new_button.grid(column=2, row=0)

#Entries
entry = Entry(width=20)
entry.insert(END, string="Some new text.")
print(entry.get())
entry.grid(column=3, row=3)









window.mainloop()