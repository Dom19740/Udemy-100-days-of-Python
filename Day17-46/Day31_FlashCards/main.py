from tkinter import *
import pandas
import random

FONT_NAME = "arial"
BG_COLOR = "#B1DDC6"
selected_set = "frequent"
words_to_learn = []
current_card = {}


# ---------------------------- IMPORT AND SORT DATA ------------------------------- #

def import_data(word_set):
    global words_to_learn

    try:
        data = pandas.read_csv(f"data/{word_set}/words_to_learn.csv")

    except FileNotFoundError:
        data = pandas.read_csv(f"data/{word_set}/portuguese_words.csv")

    words_to_learn = data.to_dict(orient="records")
    next_card()


# ---------------------------- CHOOSE DATA SET ------------------------------- #

def get_selected_set(*args):
    selected_word_set = word_set_choice.get()
    import_data(selected_word_set)


# ---------------------------- NEXT CARD ------------------------------- #

def next_card():
    global current_card, timer_flip, timer_next

    # reset timers at each next card
    window.after_cancel(timer_flip)
    window.after_cancel(timer_next)

    # generate a random card
    current_card = random.choice(words_to_learn)

    # update card
    canvas.itemconfig(canvas_image, image=image_card_front)
    canvas.itemconfig(text_title, text="")
    canvas.itemconfig(text_word, fill="white", text=current_card["english"], font=(FONT_NAME, 60, "italic"))

    label_words_in_list.config(text=f"Words in list: {len(words_to_learn)}")

    # timers to flip card and auto show next
    timer_flip = window.after(3000, flip_card)
    timer_next = window.after(6000, next_card)

    return current_card


# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    canvas.itemconfig(canvas_image, image=image_card_back)
    canvas.itemconfig(text_title, fill="black", text=current_card["english"], )
    canvas.itemconfig(text_word, fill="black", text=current_card["portuguese"], font=(FONT_NAME, 60, "bold"))


# ---------------------------- REMOVE CARD ------------------------------- #

def remove_card(word_set):
    words_to_learn.remove(current_card)
    next_card()

    # export data to csv without numbered index
    data_export = pandas.DataFrame(words_to_learn)
    data_export.to_csv(f"data/{word_set}/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #

# welcome screen
welcome = Tk()
welcome.config(padx=50, pady=50, bg=BG_COLOR)

canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
image_card_front = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=image_card_front)
canvas.grid(column=0, row=0, padx=20, pady=20)

welcome_title = canvas.create_text(400, 150, text="!! Welcome to Flashy - Portuguese !!\n"
                                                  "\nThe cards flip automatically\n"
                                                  "\nPress the green button to remove a learnt word"
                                                  "\nPress the red button to skip ahead"
                                                  "\nChoose a new word list from the menu",
                                   fill="white", font=(FONT_NAME, 20, "normal"), justify=CENTER)
welcome_button = Button(canvas, text="Start", font=(FONT_NAME, 40, "bold"), bg=BG_COLOR, command=welcome.destroy)
canvas.create_window(400, 350, window=welcome_button)

welcome.mainloop()


# main interface
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BG_COLOR)

# flip to translation card after 3 secs
timer_flip = window.after(3000, flip_card)
# flip to next card after 3 additional secs
timer_next = window.after(6000, next_card)

# main canvas
canvas = Canvas(width=800, height=526, bg=BG_COLOR, highlightthickness=0)
image_card_front = PhotoImage(file="images/card_back.png")
image_card_back = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=image_card_front)
canvas.grid(column=0, row=1, columnspan=3, rowspan=2, padx=20, pady=20)

text_title = canvas.create_text(400, 150, fill="black", font=(FONT_NAME, 20, "normal"))
text_word = canvas.create_text(400, 250, fill="white", font=(FONT_NAME, 60, "italic"))

label_set_choice = Label(text="Choose word list: ", bg=BG_COLOR, font=(FONT_NAME, 15, "normal"))
label_set_choice.grid(row=0, column=0, sticky="E")

word_set_choice = StringVar(window)
word_set_choice.set("frequent")  # default value
drop_down_list = OptionMenu(window, word_set_choice,
                            "frequent",
                            "animals_nature",
                            "body",
                            "clothes",
                            "date_time",
                            "family",
                            "food",
                            "house",
                            "stuff",
                            "verbs",
                            "words_a-l",
                            "words_m-z",
                            )
drop_down_list.config(text="Timer", bg=BG_COLOR, width=15, font=(FONT_NAME, 15, "normal"))
drop_down_list.grid(row=0, column=1, sticky="W")

label_words_in_list = Label(text=f"Words in list: {len(words_to_learn)}", bg=BG_COLOR,
                            font=(FONT_NAME, 15, "normal"))
label_words_in_list.grid(row=0, column=2, sticky="w")

button_unknown_image = PhotoImage(file="images/wrong.png")
button_unknown = Button(image=button_unknown_image, highlightthickness=0, command=next_card)
button_unknown.grid(row=2, column=3, sticky="N")

button_known_image = PhotoImage(file="images/right.png")
button_known = Button(image=button_known_image, highlightthickness=0,
                      command=lambda: remove_card(word_set_choice.get()))
button_known.grid(row=1, column=3, sticky="S")

word_set_choice.trace("w", get_selected_set)
import_data("frequent")
next_card()

window.mainloop()
