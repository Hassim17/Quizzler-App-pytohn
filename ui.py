from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler Game")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="score:0", bg=THEME_COLOR, fg="white", font=("Courier", 15, "normal"))
        self.score_label.grid(row=1, column=2, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.canvas.grid(row=2, column=1, columnspan=2, padx=20, pady=20)

        self.q_text = self.canvas.create_text(150, 125, text="Question", font=("Ariel", 18, "italic"),
                                              fill=THEME_COLOR, width=280)

        right_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=right_image, bd=0, highlightthickness=0, command=self.is_answer_true)
        self.true_button.grid(row=3, column=1, padx=20, pady=20)

        wrong_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=wrong_image, bd=0, highlightthickness=0, command=self.is_answer_false)
        self.false_button.grid(row=3, column=2, padx=20, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f"Score :{self.quiz.score}")
        self.canvas.configure(bg="White")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.q_text, text=q_text)
        else:
            self.canvas.configure(bg="Orange")
            self.canvas.itemconfig(self.q_text,
                                   text=f"You\'ve Completed the quiz!\nYour Final score : {self.quiz.score}/10")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.window.after(10000, self.window.destroy)

    def is_answer_true(self):
        self.flash(self.quiz.check_answer("True"))

    def is_answer_false(self):
        self.flash(self.quiz.check_answer("False"))

    def flash(self, is_right):
        if is_right:
            self.canvas.configure(bg="Green")
        else:
            self.canvas.configure(bg="Red")

        self.window.after(1000, self.get_next_question)
