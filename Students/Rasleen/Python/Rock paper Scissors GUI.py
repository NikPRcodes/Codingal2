from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

root = Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg='light blue')
root.geometry('1000x1000')

upload = Image.open("C:/Users/hp/Desktop/Codingal/Students/Rasleen/Python/cartoon.jpg")
upload = upload.resize((500,500))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label = Label(root, text="Welcome to Rock, Paper, Scissors!", bg='light blue', font=("Arial", 14))
label.place(relx=0.5, y=100, anchor=CENTER)

def msg():
    MsgBox = messagebox.askquestion("Start Game", "Do you want to play Rock, Paper, Scissors?")
    if MsgBox == 'yes':
        topwin()

btn1 = Button(root, text="Start Game", command=msg, bg="light green", fg="white")
btn1.place(x=200, y=100)

def topwin():
    top = Toplevel()
    top.title("Rock, Paper, Scissors Game")
    top.configure(bg="light grey")
    top.geometry("500x400+50+50")

    result_label = Label(top, text="", bg="light grey", font=("Arial", 12))
    result_label.place(x=150, y=200)

    winner_label = Label(top, text="", bg="light grey", font=("Arial", 14), fg="blue")
    winner_label.place(x=150, y=240)

    def play_game(user_choice):
        options = ['Rock', 'Paper', 'Scissors']
        computer_choice = random.choice(options)
        result_label.config(text=f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            winner_label.config(text="It's a Draw!")
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            winner_label.config(text="You Win!")
        else:
            winner_label.config(text="Computer Wins!")

    btn_rock = Button(top, text="Rock", width=10, bg="light green", fg="white", command=lambda: play_game("Rock"))
    btn_rock.place(x=150, y=50)

    btn_paper = Button(top, text="Paper", width=10, bg="light green", fg="white", command=lambda: play_game("Paper"))
    btn_paper.place(x=150, y=100)

    btn_scissors = Button(top, text="Scissors", width=10, bg="light green", fg="white", command=lambda: play_game("Scissors"))
    btn_scissors.place(x=150, y=150)

    top.mainloop()

root.mainloop()