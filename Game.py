#IMPORT FROM LIBRARY!
from tkinter import *

#IMPORTING 9 FILES
def StartGame():
    def StartGame(args):
        main_window.destroy()
        
        if args == 1:
            from Units import Hardware
            Hardware.main()
            
        elif args == 2:
            from Units import Internet
            Internet.main()
            
        elif args == 3:
            from Units import Software
            Software.main()
            
        elif args == 4:
            from Units import Data_Types 
            Data_Types.main()
            
        elif args == 5:
            from Units import Data_Structure
            Data_Structure.main()
            
        elif args == 6:
            from Units import Security
            Security.main()
            
        elif args == 7:
            from Units import Programming
            Programming.main()
            
        elif args == 8:
            from Units import Networking
            Networking.main()
            
        elif args == 9:
            from Units import Technology
            Technology.main()

#CREATING BUTTONS, IMAGE & CREATING LABELS FOR IMPORT FILES PAGE!  
    def option():

        lab_img1 = Button(main_window,image=img1,bg='#D3D3D3',border=0,justify='center',)

        easy_label = Label (text = "Easy" , bg ='#D3D3D3' , fg='black', font=("Britannic Bold", 16)).place(x=260, y=15)
        sel_btn1 = Button(text="Hardware",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000",bg="#3cb371",cursor="hand2",command=lambda: StartGame(1),)
        sel_btn2 = Button(text="Internet",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000",bg="#3cb371",cursor="hand2",command=lambda: StartGame(2),)
        sel_btn3 = Button(text="Software",width=20, borderwidth=1, font=("Calibri", 15), fg="#000000", bg="#3cb371",cursor="hand2",command=lambda: StartGame(3),)

        medium_label = Label (text = "Medium" , bg ='#D3D3D3' , fg='black', font=("Britannic Bold", 16)).place(x=245, y=180)
        sel_btn4 = Button(text="Data Types",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000",bg="#ffcc99",cursor="hand2",command=lambda: StartGame(4),)
        sel_btn5 = Button(text="Data Structure",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000", bg="#ffcc99",cursor="hand2",command=lambda: StartGame(5),)
        sel_btn6 = Button(text="Security",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000",bg="#ffcc99",cursor="hand2",command=lambda: StartGame(6),)
        
        hard_label = Label (text = "Hard" , bg ='#D3D3D3' , fg='black', font=("Britannic Bold", 16)).place(x=260, y=345)
        sel_btn7 = Button(text="Programming",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000",bg="#FF7276",cursor="hand2",command=lambda: StartGame(7),)
        sel_btn8 = Button(text="Networking",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000",bg="#FF7276",cursor="hand2",command=lambda: StartGame(8),)
        sel_btn9 = Button(text="Technology",width=20,borderwidth=1,font=("Calibri", 15),fg="#000000",bg="#FF7276",cursor="hand2",command=lambda: StartGame(9),)
        
#POSITIONIG BUTTONS & IMAGE ON START GAME PAGE!
        lab_img1.grid(row=0, column=0, pady=5, padx=70)
        
        sel_btn1.grid(row=1, column=4, pady=(2, 0),)
        sel_btn2.grid(row=2, column=4, pady=(2, 0),)
        sel_btn3.grid(row=3, column=4, pady=(2, 0),)
        
        sel_btn4.grid(row=4, column=4, pady=(40,0),)
        sel_btn5.grid(row=5, column=4, pady=(2, 0),)
        sel_btn6.grid(row=6, column=4, pady=(2, 0),)
        
        sel_btn7.grid(row=7, column=4, pady=(40,0),)
        sel_btn8.grid(row=8, column=4, pady=(2, 0),)
        sel_btn9.grid(row=9, column=4, pady=(2, 0),)

    def show_option():
        start_btn.destroy()
        quit_btn.destroy()
        lab_img.destroy()
        option()

#CREATING HOMEPAGE WINDOW (SIZE, IMAGE, LABEL, BUTTON)!
    main_window = Tk()
    main_window.geometry("600x600+600+100")
    main_window.resizable(0, 0)
    main_window.title("Computing Word Scramble Game!")
    main_window.configure(background="#D3D3D3")
    main_window.iconbitmap(r'computerlogo.ico')

    img0 = PhotoImage(file="computerlogo.png")
    img1 = PhotoImage(file="back.png")

    lab_img = Label(
        main_window,
        image=img0,
        bg="white",
        border="0"
    )
    lab_img.pack(pady=(70, 0))

#Start Button Code & POS
    start_btn = Button(
        main_window,
        text="START",
        width=8,
        height=1,
        fg="white",
        bg="black",
        font=("Arial 12"),
        cursor="hand2",
        command=show_option,
    )
    start_btn.place(x=210, y=470)

#QUIT Button Code & POS
    quit_btn=Button(
        main_window,
        text="QUIT",
        fg="white",
        bg="black",
        font=("Arial 12"),
        width=8,
        height=1,
        cursor="hand2",
        command = main_window.destroy
        )
    quit_btn.place(x=310, y=470)

    main_window.mainloop()
    exit(0)
    
StartGame()

