import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin
from PIL import Image, ImageTk


def Home(root, frame1, frame2):

    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

# Frame 2 - Top Navigation
    frame2.configure(bg="#1c3d5a")  # Darker blue for top navigation
    Button(frame2, text="Home", command=lambda: Home(root, frame1, frame2), font=('Helvetica', 12, 'bold'), bg="#2b597e", fg="white").grid(row=0, column=0, padx=5, pady=5)
    Label(frame2, text="Welcome to the F1 Driver Voting System", font=('Helvetica', 14), bg="#1c3d5a", fg="white").grid(row=0, column=1, padx=10)
    frame2.pack(side=TOP, fill=X, pady=10) 
    root.title("F1 Race Voting System Home")
    root.configure(bg="#e1f5fe")


    #Admin Login
    admin = Button(frame1, text="Admin Login", width=15, command = lambda: AdmLogin(root, frame1))

    #Voter Login
    voter = Button(frame1, text="DOTD Voting", width=15, command = lambda: voterLogin(root, frame1))

    #New Tab
    newTab = Button(frame1, text="New Window", width=15, command = lambda: sb_p.call('start python homePage.py', shell=True))

    Label(frame1).grid(row = 2,column = 0)
    Label(frame1).grid(row = 4,column = 0)
    Label(frame1).grid(row = 6,column = 0)
    admin.grid(row = 3, column = 1, columnspan = 2)
    voter.grid(row = 5, column = 1, columnspan = 2)
    newTab.grid(row = 7, column = 1, columnspan = 2)

    frame1.pack()
    root.mainloop()


def new_home():
    root = Tk()
    root.geometry('500x500')

    frame1 = Frame(root)
    frame2 = Frame(root)
    root.configure(bg='dark blue')  # Set main window background to red

    frame1 = Frame(root, bg='light blue')  # Set frame1 background to red
    frame2 = Frame(root, bg='light blue')
    Home(root, frame1, frame2)


if __name__ == "__main__":
    new_home()
