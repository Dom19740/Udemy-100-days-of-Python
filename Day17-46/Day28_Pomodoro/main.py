from tkinter import *
import winsound
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
ticks = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global ticks
    global reps
    window.after_cancel(timer)
    label_title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    label_tick.config(text="")
    ticks = ""
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_title.config(text="Break", fg=RED)
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_title.config(text="Break", fg=PINK)
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
    else:
        count_down(work_sec)
        label_title.config(text="Work", fg=GREEN)
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    global ticks

    def change_window_title(new_title):
        window.title(new_title)

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    title_text = canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    window.title(title_text)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            ticks += "✔"
            label_tick.config(text=ticks)

    change_window_title(f"Timer: {count_min}:{count_sec}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomatito Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Use canvas as layers to put time over picture
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
# text from the countdown mechanism
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# set up labels and buttons on grid
label_title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
label_title.grid(column=1, row=0)

label_tick = Label(fg=RED, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
label_tick.grid(column=1, row=3)

button_start = Button(text="Start", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), command=reset_timer)
button_reset.grid(column=2, row=2)

window.mainloop()
