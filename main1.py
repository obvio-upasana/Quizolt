import tkinter as tk
from tkinter import ttk,messagebox
from ttkbootstrap import Style

#Personalised Quiz Data
personal_quiz = [
    {
        "question":"What is the capital of China?",
        "choice":["Wuhan","Bejing","Tokyo","Berlin"],
        "ans":"Bejing"
    },
     {
        "question":"What is the color of kiwi?",
        "choice":["Blue","Brown","Red","Green"],
        "ans":"Green"
    },
    {
        "question":"Who won most Gold medals in Olympics ever?",
        "choice":["Russia","USA","China","Eygpt"],
        "ans":"USA"
    },
    {
        "question":"What contains most protein?",
        "choice":["Chicken","Eggs","Almonds","Tuna"],
        "ans":"Chicken"
    }
]
#Follow the pattern, data needs to be changed

def start_quiz():
	start_button.forget()
	next_question.pack()
	next_question()

def show_question():
    question = personal_quiz[current_question]
    question_box.config(text=question["question"])
    choice=question["choice"]
    for i in range(4):
        choice_buttons[i].config(text=choice[i] ,state="normal")
        next_btn.config(state="disabled")

    feedback.config(text="")
    next_btn.config(state="normal")

def check_answer(choice):
     
     question = personal_quiz[current_question]
     selected_choice=choice_buttons[choice].cget("text")

     for button in choice_buttons:
        button.config(state="disabled")
        
     next_btn.config(state="normal")
     if selected_choice==question["ans"]:
         global score
         if score <len(personal_quiz):
             score+=1
         score_label.config(text="Score: {}/{}".format(score, len(personal_quiz)))
         feedback.config(text="Correct!",fg="green")
     else: 
        feedback.config(text="Incorrect!",fg="red")




def next_question():
    global current_question
    current_question +=1
    if current_question < len(personal_quiz):
        show_question()
    else:
        messagebox.showinfo("Quiz is complete!!!!!!","Final Score obtained = {}/{}".format(score, len(personal_quiz)))
        root.destroy()

def clear_frame():
	for widget in personal_quiz.winfo_children():
		widget.destroy()


#For the main window:-
root = tk.Tk()
root.title("Personal Quiz Maker - QuizoIt")
root.geometry("700x550")
style =Style(theme="flatly")

#FOnts
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

#For the Question box:-
question_box = ttk.Label(
    root,
    anchor="center",
    wraplength="550",
    padding=20
)
question_box.pack(pady=10)

#For Different choices box
choice_buttons=[]
for i in range(4):
    button=ttk.Button(
        root, 
        command=lambda i=i :check_answer(i)
    )
    button.pack(pady=7)
    choice_buttons.append(button)

#Correct or Incorrect?
feedback=ttk.Label(
    root, 
    anchor="center",
    padding=15
)
feedback.pack(pady=10)

#For quiz score
score=0
score_label=ttk.Label(
    root, 
    text="Score = 0/4", 
    anchor= "center" ,
    padding=15
)
score_label.pack(pady=10)

#The next button:-
next_btn= ttk.Button(
    root, text="NEXT", command=next_question, state="normal"
)
next_btn.pack(pady=15)

start_button = ttk.Button(root, text="Start Quiz",command=start_quiz)
start_button.pack()
current_question= 0
show_question()
root.mainloop()