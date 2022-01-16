from cgitb import text
from tkinter import *
import tkinter as tk; 

if __name__ == '__main__':
    root = tk.Tk()
    springTrue = tk.IntVar()

    tk.Label(root, text="Username").grid(row=0)
    tk.Label(root, text="Password").grid(row=1)

    c1 = tk.Checkbutton(root, text="Spring Semster", variable=springTrue, onvalue=1, offvalue=0).grid(row=2)
    print(springTrue)
    #  tk.Label(root, text="Credit Card Number").grid(row=1)

    username = tk.Entry(root)
    password = tk.Entry(root)


    username.grid(row=0, column=1)
    password.grid(row=1, column=1)


    root.mainloop()