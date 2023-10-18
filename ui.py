THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window =Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 20, pady= 20,bg=THEME_COLOR)

        self.score = Label(text="score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150,125,width =280 ,text="potato",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1, column=0, columnspan=2,pady =50)

        tick_image =PhotoImage(file = "images/true.png")
        self.tick_button = Button(image=tick_image,highlightthickness=0,command = self.enter_true)
        self.tick_button.grid(row=2,column = 0)

        ex_image = PhotoImage(file="images/false.png")
        self.ex_button = Button(image=ex_image,highlightthickness=0,command= self.enter_false)
        self.ex_button.grid(row=2, column=1)

        self.get_next()
        self.window.mainloop()

    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz")
            self.tick_button.config(state="disabled")
            self.ex_button.config(state="disabled")
    def enter_false(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)
    def enter_true(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next)

    def change_screen(self):
        pass