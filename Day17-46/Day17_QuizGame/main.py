from question_model import Question
from data_new import question_data
from quiz_brain import QuizBrain

""" 
question_bank = [
Question(q1, a1)
Question(q2, a2),
etc

Write a for loop to iterate over the question_data.
Create a Question object from each entry in question_data
Append each Question object to the question_bank
"""

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():  # if quiz still has questions remaining:
    quiz.next_question()

quiz.final_score()
