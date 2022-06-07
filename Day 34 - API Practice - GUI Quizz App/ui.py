THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.score_count = 0
        
        #Window
        self.window = Tk()
        self.window.title("Quizzler!")
        self.window.config(bg= THEME_COLOR, padx= 20, pady= 20)
        
        #Buttons
        self.right_button = Button()
        self.right_image = PhotoImage(file="images/true.png")
        self.right_button.config(image=self.right_image, highlightthickness=0, command= self.true_button_command)
        self.right_button.grid(row= 2, column= 0)

        self.wrong_button = Button()
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button.config(image=self.wrong_image, highlightthickness=0, command= self.false_button_command)
        self.wrong_button.grid(row=2, column=1)

        #Score text
        self.score = Label()
        self.score.config(text=f"Score: {self.score_count}", bg= THEME_COLOR, fg= "white")
        self.score.grid(row= 0, column=1)


        #Canvas config
        self.canvas = Canvas(width= 300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question = self.canvas.create_text(
            150, 
            125,
            width= 280, 
            text="Test", 
            font=("Arial", 20, "italic")
            )
        
        self.next_question()



        self.window.mainloop()


    def next_question(self):
        self.canvas.config(bg= "white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text= "Reached the end of the quiz.")
            self.right_button.config(state= "disabled")
            self.wrong_button.config(state= "disabled")

    
    def true_button_command(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_button_command(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    
    



    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score_count += 1
            self.score.config(text= f"Score: {self.score_count}")
        else:
            self.canvas.config(bg="red")
            

        self.window.after(1000, self.next_question)
