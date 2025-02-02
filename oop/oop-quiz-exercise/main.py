# Day 17
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.stillHasQuestion():
    quiz.nextQuestion()

print("You have completed the quiz")
print(f'Your score is {quiz.score}/{quiz.questionNumber}')