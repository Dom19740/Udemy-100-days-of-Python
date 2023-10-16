from tkinter import *
from quiz_brain import QuizBrain

BG_COLOR = "#375362"
FONT_NAME = "Arial"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # set up main window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=BG_COLOR)

        self.label_score = Label(text="Score: 0", bg=BG_COLOR, fg="white", font=(FONT_NAME, 15, "normal"))
        self.label_score.grid(row=0, column=1)

        # set up canvas
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Question goes here",
                                                     fill="black",
                                                     justify="center",
                                                     font=(FONT_NAME, 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        button_true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=button_true_image, highlightthickness=0, command=self.guess_true)
        self.button_true.grid(row=2, column=0)

        button_false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=button_false_image, highlightthickness=0, command=self.guess_false)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Quiz Completed.\n"
                                                            f"Your final score was: {self.quiz.score}/10")
            self.button_false.config(state="disabled")
            self.button_true.config(state="disabled")
            self.label_score.config(text="")

    def guess_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def guess_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
