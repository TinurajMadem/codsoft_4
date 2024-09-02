from tkinter import *
import random

def rock():
    global human_score
    global computer_score
    global i
    ch=0
    cc=0
    i+=1
    com_choice = random.choice(choices)
    if com_choice =="scissors":
        human_score+=1
        ch=1
    elif com_choice == "rock":
        ch=1
        cc=1
    else:
        computer_score+=1
        cc=1
    if ch>cc:
        result.config(text="You won this round")
    elif ch==cc:
        result.config(text="This round is a tie")
    else:
       result.config(text="You lose this round")
    round.config(text=f'Round-{i}')
    scoreh.config(text=human_score)
    scorec.config(text=computer_score)
    h_choice.config(text="Rock")
    c_choice.config(text=com_choice)
    new_window()

def paper():
    global human_score
    global computer_score
    global i
    ch=0
    cc=0
    i+=1
    com_choice = random.choice(choices)
    if com_choice == 'rock':
        human_score+=1
        ch=1
    elif com_choice == "paper":
        ch=1
        cc=1
    else:
        computer_score+=1
        cc=1
    if ch>cc:
        result.config(text="You won this round")
    elif ch==cc:
        result.config(text="This round is a tie")
    else:
       result.config(text="You lose this round")
    round.config(text=f'Round-{i}')
    scoreh.config(text=human_score)
    scorec.config(text=computer_score)
    h_choice.config(text="Paper")
    c_choice.config(text=com_choice)
    new_window()

def scissor():
    global human_score
    global computer_score
    global i
    ch=0
    cc=0
    i+=1
    com_choice = random.choice(choices)
    if com_choice == 'paper':
        human_score+=1
        ch=1
    elif com_choice == "scissors":
        ch=1
        cc=1
    else:
        computer_score+=1
        cc=1
    if ch>cc:
        result.config(text="You won this round")
    elif ch==cc:
        result.config(text="This round is a tie")
    else:
       result.config(text="You lose this round")
    round.config(text=f'Round-{i}')
    scoreh.config(text=human_score)
    scorec.config(text=computer_score)
    h_choice.config(text="Scissors")
    c_choice.config(text=com_choice)
    new_window()
    

def yesw():
    rockb.config(state=ACTIVE)
    paperb.config(state=ACTIVE)
    scissorb.config(state=ACTIVE)
    new.destroy()

def new_window():
    global new
    new=Tk()
    new.title("Feedback Window")
    new.config(background="White")
    new.geometry("460x220+520+370")
    ques=Label(new,text="Do you want to continue the game?",font=("Arial",19,'bold'),bg="White")
    ques.place(x=22,y=25)
    rockb.config(state=DISABLED)
    paperb.config(state=DISABLED)
    scissorb.config(state=DISABLED)
    yes=Button(new,
               text="Yes",
               font=("Arial",16,'bold'),
               command=yesw,
               fg="Black",
               bg="#77e8f2",
               activebackground="#77e8f2",
               activeforeground="Black",
               state=ACTIVE,
               relief=RAISED)
    yes.place(x=108,y=105)
    no=Button(new,
               text="No",
               command=end_game,
               font=("Arial",16,'bold'),
               fg="Black",
               bg="#77e8f2",
               activebackground="#77e8f2",
               activeforeground="Black",
               state=ACTIVE,
               relief=RAISED)
    no.place(x=328,y=105)

def end_game():
    window.destroy()
    new.destroy()
    res_win=Tk()
    res_win.title("Result of the game")
    res_win.geometry("480x120+520+330")
    res_win.config(background="White")
    outcome=Label(res_win,text="",font=("Arial",20,'bold'),bg="White")
    outcome.pack(pady=30)
    if human_score>computer_score:
        outcome.config(text="You won the Game")
    elif human_score==computer_score:
        outcome.config(text="It's a tie")
    else:
       outcome.config(text="You lose the Game")

choices = ("rock","paper","scissors")
human_score=0
computer_score=0
i=1
#window related
global window
window=Tk()
window.title("Rock Paper Scissors Game")
logo=PhotoImage(file="rock.png")
rock_icon=PhotoImage(file="Rock_game.png")
window.iconphoto(True,logo)
window.config(background="#0ee8b2")
window.geometry("1920x1080")

#labels section
Title=Label(window,text="ROCK PAPER SCISSORS",font=("Arial",25,'bold'),fg="Red",bg="Yellow",borderwidth=2,relief=RAISED)
Title.place(x=555,y=10)
human_icon = PhotoImage(file="human.png")
Human=Label(window,image=human_icon)
Human.place(x=105,y=100)
computer_icon = PhotoImage(file="computer.png")
Computer=Label(window,image=computer_icon)
Computer.place(x=1175,y=100)
hum_score=Label(window,text="Human Score",font=("Times",19,"bold"),bg="#0ee8b2")
hum_score.place(x=385,y=150)
com_score=Label(window,text="Computer Score",font=("Times",19,"bold"),bg="#0ee8b2")
com_score.place(x=965,y=150)
scoreh=Label(window,text=human_score,font=("Comic Sans MS",45,'bold'),bg="#0ee8b2")
scoreh.place(x=435,y=225)
scorec=Label(window,text=computer_score,font=("Comic Sans MS",45,'bold'),bg="#0ee8b2")
scorec.place(x=1035,y=225)
result=Label(window,text="",font=("Arial",25,"bold"),bg='#0ee8b2')
result.pack(pady=255)
round=Label(window,text="Round-1",font=("Comic Sans MS",23,"bold"),bg="#0ee8b2")
round.place(x=685,y=65)
h_choice=Label(window,text="",font=("Comic Sans MS",19,'bold'),bg="#0ee8b2")
h_choice.place(x=430,y=330)
c_choice=Label(window,text="",font=("Comic Sans MS",19,'bold'),bg="#0ee8b2")
c_choice.place(x=1025,y=330)
#Buttons section
rockb = Button(window,
              text="Rock",
              command=rock,
              font=("Comic Sans MS",19,"bold"),
              fg="Black",
              bg="white",
              activebackground="white",
              activeforeground="Black",
              state=ACTIVE,
              image=rock_icon,
              compound="top")

paperb = Button(window,
              text="Paper",
              command=paper,
              font=("Comic Sans MS",19,"bold"),
              fg="Black",
              bg="white",
              activebackground="white",
              activeforeground="Black",
              state=ACTIVE,
              image=rock_icon,
              compound="top")

scissorb = Button(window,
              text="Scissor",
              command=scissor,
              font=("Comic Sans MS",19,"bold"),
              fg="Black",
              bg="white",
              activebackground="white",
              activeforeground="Black",
              state=ACTIVE,
              image=rock_icon,
              compound="top")



rockb.place(x=65,y=420)
paperb.place(x=630,y=420)
scissorb.place(x=1200,y=420)

#displaying window
window.mainloop()