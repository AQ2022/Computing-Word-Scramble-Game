#IMPORTS FROM LIBRARY
from tkinter import *
from random import *
from tkinter import messagebox

#SCRAMBLE PROGRAMMING WORDS AND CORRECT SOFTWARE WORDS
ProgrammingScrambleWords = ['GORIALTHM', 'GROPRAM', 'PIA', 'GUMENTAR', 'IICAS', 'LENAOOB','GUB', 'RACH', 'JETSOBC', 'DECO', 'ASSCL', 'RRAAY',
                            'CLARADETION','EESSXIONPR','POOL','RITTEIONA', 'SJCRAIPVTA', 'QLS','TCPOMERU ROGRAMP']                                                                                            
ProgrammingCorrectWords =  ['ALGORITHM', 'PROGRAM', 'API', 'ARGUMENT', 'ASCII', 'BOOLEAN','BUG', 'CHAR', 'OBJECTS', 'CODE', 'CLASS', 'ARRAY',
                            'DECLARATION','EXPRESSION','LOOP','ITERATION', 'JAVASCRIPT', 'SQL','COMPUTER PROGRAM']   

ran_num = randrange(0, (len(ProgrammingScrambleWords)))
scramble_rand_word = ProgrammingScrambleWords[ran_num]
points = 0

#IMPORT START GAME HOMEPAGE TO BACK BUTTON! 
def main():
    def back():
        window.destroy()
        import Game
        Game.StartGame()

#CODE FOR ALLOWING NEXT BUTTON TO CHANGE WHEN CLICKED!
    def next():
        global ran_num
        ran_num = randrange(0, (len(ProgrammingScrambleWords)))
        word.configure(text=ProgrammingScrambleWords[ran_num])
        get_input.delete(0, END)
        answertext.configure(text="")

#CODE FOR YOUR RESULT MESSAGEBOX!
    def result():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == ProgrammingCorrectWords[ran_num]:
            points += 10
            score.configure(text="Score Points ➠ " + str(points))
            messagebox.showinfo('My Result', "Correct Answer, Well Done!")
            ran_num = randrange(0, (len(ProgrammingScrambleWords)))
            word.configure(text=ProgrammingScrambleWords[ran_num])
            get_input.delete(0, END)
            answertext.configure(text="")
        else:
            messagebox.showerror("My Result", "Incorrect Answer, Try Again!")
            get_input.delete(0, END)

#CODE TO REVEAL CORRECT ANSWER, IF YOU HAVE THE POINTS!
    def reveal_answer():
        global points
        if points > 9:
            points -= 10
            score.configure(text="Score Points ➠  " + str(points))  
            answertext.configure(text=ProgrammingCorrectWords[ran_num])
        else:
            answertext.configure(text='Sorry\n You Do Not Have Enough Points!')

#CREATING WINDOW FOR HARDWARE (SIZE, IMAGE, LABEL, BUTTON)!
    window = Tk()
    window.geometry("700x500+500+150")
    window.resizable(0, 0)
    window.title("Hard Mode: Programming Word Scramble! ")
    window.configure(background="#D3D3D3")
    window.iconbitmap(r'computerlogo.ico')
    img1 = PhotoImage(file="back.png")
            
#LABELS & BUTTONS
    lab_img1 = Button(window,image=img1,bg='#D3D3D3',border=0,justify='center',command=back,)
    lab_img1.pack(anchor='nw',padx=20, pady=10)

    title= Label(text='Programming',pady=10,bg="#D3D3D3",fg="#FF7276",font="Titillium  25 bold")
    title.pack(anchor="n")
    title.place(x=240, y=0)

    scorereminder= Label(text='Can you guess the Programming scrambled words? \n Remember that you can use your score points to find out the answers!',
                         pady=10,bg="#D3D3D3",fg="black",font="Courier 10 ")
    scorereminder.pack(anchor="n")

    score = Label(text='Score Points',pady=10,fg="#748b97",bg="#D3D3D3",font="Calibri  14 ")
    score.pack(anchor="n")

    word = Label(text=scramble_rand_word,pady=10,bg="#D3D3D3",fg="black",font="Titillium  35 bold")
    word.pack()

    get_input = Entry(font="none 26 bold",border=8,justify='center',)
    get_input.pack()
    get_input.place(x=150, y=220)

    submit = Button(text="Submit",width=18,border=4,font=("", 13),fg="black",bg="#FF7276",command=result,)
    submit.pack()
    submit.place(x=150, y=300)

    next = Button(text="Next",width=18,border=4,fg="black",bg="#FF7276",font=("", 13),command=next,)
    next.pack()
    next.place(x=350, y=300)
    
    answer = Button(text="Answer",width=12,border=4,fg="black",bg="#FF7276",justify='center',font=("", 13),command=reveal_answer,)
    answer.pack()
    answer.place(x=290, y=360)

    answertext= Label(text="",bg="#D3D3D3",fg="#748b97", font="Courier 13",)
    answertext.pack()
    answertext.place(anchor="center", x=350, y=425)

    window.mainloop()

