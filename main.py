from select import select
from selectors import SelectSelector
import tkinter as tk; 
import os
from traceback import print_tb

loginAndPayInfo = {
    "Username":"", 
    "Password":"", 
    "Semester":"", 
    "Classes": [], # 
    "Pay":"", # now 
    "Finicial Aid" : "" # True or False 
}

CreditCardInfo = {
    "CCN" : "", 
    "Expiration" : "", 
    "Year" : "", 
    "CVV2" : "", 
    "Billing Address" : ""
}

class fillInfo(tk.Frame):
    def __init__(self, master):
        self.master = master 
        self.selectSemester = tk.IntVar()
        self.selectSemester.set(0)

        self.userLabel = tk.Label(master, text="Username").grid(row=0)
        self.username = tk.Entry(master).grid(row=0, column=1)

        self.passwordLabel = tk.Label(master, text="Password").grid(row=1)
        self.password = tk.Entry(master).grid(row=1, column=1)

        # Determine Semester 
        self.semesterLabel = tk.Label(master, text="Select Semester").grid(row=2)
        self.springSemester = tk.Radiobutton(self.master, text="Spring", variable=self.selectSemester, value=1, command=self.fillSemDic).grid(row=2, column=1)
        self.fallSemester = tk.Radiobutton(self.master, text="Fall", variable=self.selectSemester, value=2, command=self.fillSemDic).grid(row=2, column=2)
        self.summerSemester = tk.Radiobutton(self.master, text="Summer", variable=self.selectSemester, value=3, command=self.fillSemDic).grid(row=2, column=3)

        # Classes 
        self.classLabel = tk.Label(master, text="Enter Class Num").grid(row=4)
        self.classNum = tk.Entry(master).grid(row=4, column=1)

        # 
        
    def fillSemDic(self):
        if (self.selectSemester.get() == 1):
            loginAndPayInfo["Semester"] = "Spring"
        elif (self.selectSemester.get() == 2): 
            loginAndPayInfo["Semester"] = "Fall"
        elif (self.selectSemester.get() == 3): 
            loginAndPayInfo["Semester"] = "Summer"

def main(): 
    root = tk.Tk()
    app = fillInfo(root)
    root.mainloop()

    

if __name__ == '__main__':
    main()