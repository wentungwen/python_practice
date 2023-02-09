from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
score = 0
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print(f"That is the end of the game! Your score is {quiz.score}")




