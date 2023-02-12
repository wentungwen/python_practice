class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number+1}: {current_question.text} (True/False): ")
        self.question_number += 1
        self.check_answer(user_answer, current_question)

    def check_answer(self, user_answer, current_question):
        question_answer = current_question.answer
        if current_question.answer == user_answer:
            self.score += 1
            print(f"you are right!\n The correct answer was: {question_answer}\n "
                  f"Your current score is {self.score}/{self.question_number}")
        else:
            print(f"you are wrong!\n The correct answer was: {question_answer}\n "
                  f"Your current score is {self.score}/{self.question_number}")