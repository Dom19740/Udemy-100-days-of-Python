from tkinter import *


def miles_to_km():
    km = float(entry_miles.get()) * 1.609
    label_result_km.config(text=km)


window = Tk()
window.title("Miles to Km Convertor")
window.config(padx=20, pady=20)

# Entry
entry_miles = Entry(width=7)
entry_miles.insert(END, string="0")
entry_miles.get()
entry_miles.grid(column=1, row=0)

# Label
label_input_miles = Label(text="Miles")
label_input_miles.grid(column=2, row=0)

# Label
label_text1 = Label(text="is equal to")
label_text1.grid(column=0, row=1)

# Label
label_result_km = Label(text="0")
label_result_km.grid(column=1, row=1)

# Label
label_text2 = Label(text="Km")
label_text2.grid(column=2, row=1)

# Button
new_button = Button(text="Calculate", command=miles_to_km)
new_button.grid(column=1, row=2)

window.mainloop()
