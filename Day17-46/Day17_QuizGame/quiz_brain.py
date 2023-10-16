"""
Write a class called QuizBrain
Write an init method.
Initialise the question_number to 0.
Initialise the question_list to an input.

Q.1: question text. (True/False)?:

Create a method called next_question()
Retrieve the item at the current question_number from the question_list.
Use the input() function to show the user the Question text and ask for the answer.
"""


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text}? (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == "t":
            answer = "true"
        else:
            answer = "false"
        if answer == correct_answer.lower():
            print("CORRECT!")
            self.score += 1
        else:
            print(f"WRONG! The correct answer was {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}")

    def final_score(self):
        print(f"\nQuiz completed. Your final score is {self.score}/{self.question_number}")