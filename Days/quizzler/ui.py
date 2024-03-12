from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class UserInterface(Tk):

    def __init__(self, quiz_brain: QuizBrain):
        super().__init__()

        self.quiz = quiz_brain

        self.title("Quizzler")
        self.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)
        self.quiz_question = self.canvas.create_text(150, 125, text='Some Question Text', width=280,
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text='', highlightcolor='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.update_score()

        self.check_img = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=self.check_img, borderwidth=0, command=lambda: self.continue_quiz('true'))
        self.check_button.grid(row=2, column=0)

        self.x_img = PhotoImage(file="./images/false.png")
        self.x_button = Button(image=self.x_img, borderwidth=0, command=lambda: self.continue_quiz('false'))
        self.x_button.grid(row=2, column=1)

        self.display_question(self.quiz.get_next_question_text())

    def continue_quiz(self, answer):
        self.update_score()
        is_correct = self.quiz.check_answer(answer)
        self.give_feedback(is_correct)

        if self.quiz.question_number < len(self.quiz.question_list):

            self.display_question(self.quiz.get_next_question_text())
        else:
            end_text = f'Quiz finished! Your score was {self.quiz.score}/{self.quiz.question_number}.'
            self.display_question(end_text)

            self.check_button.config(state='disabled')
            self.x_button.config(state='disabled')

    def give_feedback(self, is_answer_correct):
        self.canvas.config(bg='green') if is_answer_correct else self.canvas.config(bg='red')

        self.after(500, lambda: self.canvas.config(bg='white'))

    def update_score(self):
        self.score_label.config(text=f'Score: {self.quiz.score}')

    def display_question(self, question_text):
        self.canvas.itemconfig(self.quiz_question, text=question_text)

    def start_mainloop(self):
        self.mainloop()
