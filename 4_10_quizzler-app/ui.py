from tkinter import *
from quiz_brain import QuizBrain

FONT = "Ariel"
BACKGROUND = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("flash card")
        self.window.config(pady=50, padx=50, bg=BACKGROUND)

        # score
        self.score_label = Label(text="score = 0", font=(FONT, 20), bg=BACKGROUND)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=350, height=300, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 120,
                                                     text='self.quiz',
                                                     width=230,
                                                     fill=BACKGROUND,
                                                     font=(FONT, 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        # button
        right_btn_img = PhotoImage(file="images/true.png")
        self.right_btn = Button(image=right_btn_img, highlightthickness=0, border=0, command=self.true_pressed)
        self.right_btn.grid(column=0, row=2)
        wrong_btn_img = PhotoImage(file="images/false.png")
        self.wrong_btn = Button(image=wrong_btn_img, highlightthickness=0, border=0, command=self.false_pressed)
        self.wrong_btn.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="The end.")
            self.right_btn.config(state="disabled")
            self.wrong_btn.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.canvas.after(1000, self.get_next_question)


