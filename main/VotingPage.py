import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Helvetica', 18, 'bold')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Driver of the Day", font=('Helvetica', 18, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "Ferrari\n\nCharles Leclerc", variable = vote, value = "charles", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"charles",client_socket)).grid(row = 2,column = 1)
    charlesLogo = ImageTk.PhotoImage((Image.open("img/charles.jpg")).resize((45,45),Image.BICUBIC))
    charlesImg = Label(frame1, image=charlesLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "Ferrari\n\nCarlos Sainz", variable = vote, value = "carlos", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"carlos",client_socket)).grid(row = 3,column = 1)
    carlosLogo = ImageTk.PhotoImage((Image.open("img/carlos.jpg")).resize((35,48),Image.BILINEAR))
    carlosImg = Label(frame1, image=carlosLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "McLaren\n\nLando Norris", variable = vote, value = "lando", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"lando",client_socket) ).grid(row = 4,column = 1)
    landoLogo = ImageTk.PhotoImage((Image.open("img/lando.jpg")).resize((55,40),Image.ADAPTIVE))
    landoImg = Label(frame1, image=landoLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "Mercedes\n\nLewis Hamilton", variable = vote, value = "ss", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"ss",client_socket)).grid(row = 5,column = 1)
    lewisLogo = ImageTk.PhotoImage((Image.open("img/lewis.jpg")).resize((50,45),Image.ADAPTIVE))
    lewisImg = Label(frame1, image=lewisLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nMcLaren\n\nOscar Piastri  ", variable = vote, value = "oscar", indicator = 0, height = 4, width=15, command = lambda: voteCast(root,frame1,"oscar",client_socket)).grid(row = 6,column = 1)
    oscLogo = ImageTk.PhotoImage((Image.open("img/osc.jpg")).resize((45,35),Image.ADAPTIVE))
    oscImg = Label(frame1, image=oscLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
