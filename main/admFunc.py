import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    #df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    charlesLogo = ImageTk.PhotoImage((Image.open("img/charles.jpg")).resize((35,35),Image.ADAPTIVE))
    charlesImg = Label(frame1, image=charlesLogo).grid(row = 2,column = 0)

    carlosLogo = ImageTk.PhotoImage((Image.open("img/carlos.jpg")).resize((25,38),Image.ADAPTIVE))
    carlosImg = Label(frame1, image=carlosLogo).grid(row = 3,column = 0)

    landoLogo = ImageTk.PhotoImage((Image.open("img/lando.jpg")).resize((45,30),Image.ADAPTIVE))
    landoImg = Label(frame1, image=landoLogo).grid(row = 4,column = 0)

    lewisLogo = ImageTk.PhotoImage((Image.open("img/lewis.jpg")).resize((40,35),Image.ADAPTIVE))
    lewisImg = Label(frame1, image=lewisLogo).grid(row = 5,column = 0)

    oscLogo = ImageTk.PhotoImage((Image.open("img/osc.jpg")).resize((35,25),Image.ADAPTIVE))
    oscImg = Label(frame1, image=oscLogo).grid(row = 6,column = 0)


    Label(frame1, text="Charles Leclerc              :       ", font=('Helvetica', 12, 'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['charles'], font=('Helvetica', 12, 'bold')).grid(row = 2, column = 2)

    Label(frame1, text=" Carlos Sainz            :          ", font=('Helvetica', 12, 'bold')).grid(row = 3, column = 1)
    Label(frame1, text=result['carlos'], font=('Helvetica', 12, 'bold')).grid(row = 3, column = 2)

    Label(frame1, text="Lando Norris              :          ", font=('Helvetica', 12, 'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['lando'], font=('Helvetica', 12, 'bold')).grid(row = 4, column = 2)

    Label(frame1, text="Lewis Hamilton    :          ", font=('Helvetica', 12, 'bold')).grid(row = 5, column = 1)
    Label(frame1, text=result['lewis'], font=('Helvetica', 12, 'bold')).grid(row = 5, column = 2)

    Label(frame1, text="Oscar Piastri            :          ", font=('Helvetica', 12, 'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['oscar'], font=('Helvetica', 12, 'bold')).grid(row = 6, column = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)
