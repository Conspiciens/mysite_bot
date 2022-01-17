from cgitb import text
from distutils import command
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
    "Financial Aid" : "" # True or False 
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

        # Variables 
        self.selectSemester = tk.IntVar()
        self.usernameInput = tk.StringVar()
        self.passwordInput = tk.StringVar()
        self.classNumInput = tk.StringVar()
        self.payNowQues = tk.IntVar()
        self.FAQues = tk.IntVar()


        self.selectSemester.set(0)
        self.payNowQues.set(0)

        # Username 
        self.userLabel = tk.Label(master, text="Username").grid(row=0)
        self.username = tk.Entry(master, textvariable=self.usernameInput).grid(row=0, column=1)

        # Password 
        self.passwordLabel = tk.Label(master, text="Password").grid(row=1)
        self.password = tk.Entry(master, textvariable=self.passwordInput).grid(row=1, column=1)

        # Semester 
        self.semesterLabel = tk.Label(master, text="Select Semester").grid(row=2)
        self.springSemester = tk.Radiobutton(self.master, text="Spring", variable=self.selectSemester, value=1, command=self.fillSemDic).grid(row=2, column=1)
        self.fallSemester = tk.Radiobutton(self.master, text="Fall", variable=self.selectSemester, value=2, command=self.fillSemDic).grid(row=2, column=2)
        self.summerSemester = tk.Radiobutton(self.master, text="Summer", variable=self.selectSemester, value=3, command=self.fillSemDic).grid(row=2, column=3)

        # Classes 
        self.classLabel = tk.Label(self.master, text="Enter Class Num").grid(row=4)
        self.classNum = tk.Entry(self.master, textvariable=self.classNumInput).grid(row=4, column=1)
        self.classInput = tk.Button(self.master, text="Enter", command=self.inputClass).grid(row=4, column=3)

        # Pay 
        self.payLabel = tk.Label(self.master, text="When would like to pay?").grid(row=5)
        self.payNow = tk.Radiobutton(self.master, text="Now", variable=self.payNowQues, value=1, command=self.paymentNowQuestion).grid(row=5, column=1)

        # Financial Aid
        self.FALabel = tk.Label(self.master, text="Financial Aid").grid(row=6, column=0)
        self.FARB = tk.Radiobutton(self.master, text="Yes", variable=self.FAQues, value=1, command=self.FAQuestion).grid(row=6, column=1)
        self.FARB2 = tk.Radiobutton(self.master, text="No", variable=self.FAQues, value=2, command=self.FAQuestion).grid(row=6, column=2) 

        # Page Management Buttons 
        self.submit = tk.Button(self.master, text="Submit", command=self.submitData).grid(row=7, column=1)
        
    def fillSemDic(self):
        if (self.selectSemester.get() == 1):
            loginAndPayInfo["Semester"] = "Spring"
        elif (self.selectSemester.get() == 2): 
            loginAndPayInfo["Semester"] = "Fall"
        elif (self.selectSemester.get() == 3): 
            loginAndPayInfo["Semester"] = "Summer"
    
    def paymentNowQuestion(self):
        if (self.payNowQues.get() == 1):
            loginAndPayInfo["Pay"] = "now"

    def FAQuestion(self):
        if (self.FAQues.get() == 1): 
            loginAndPayInfo["Financial Aid"] = "True"
        elif (self.FAQues.get()== 2): 
            loginAndPayInfo["Financial Aid"] = "False"
    
    def inputClass(self):
        loginAndPayInfo["Classes"].append(self.classNumInput.get())
    
    def submitData(self):
        loginAndPayInfo["Username"] = self.usernameInput.get()
        loginAndPayInfo["Password"] = self.passwordInput.get()



def main(): 
    root = tk.Tk()
    app = fillInfo(root)
    root.mainloop()

    

if __name__ == '__main__':
    main()