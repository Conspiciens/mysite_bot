from cgitb import text
from codeop import CommandCompiler
from distutils import command
from re import X
from select import select
from selectors import SelectSelector
from textwrap import fill
import tkinter as tk;
import os
from tkinter.tix import COLUMN
from traceback import print_tb
from turtle import left
from mysite_bot import login_MySite
from getDriver import IdentifiyPlatform

loginAndPayInfo = {
    "Username":"",
    "Password":"",
    "Semester":"",
    "Classes": [], #
    "Pay":"", # now
    "Financial Aid" : "", # True or False

    "CCN" : "",
    "Expiration" : "",
    "Year" : "",
    "CVV2" : "",
    "postalCode" : ""

    "scheduleDate" : "",
}

class fillInfo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        # Variables
        self.selectSemester = tk.IntVar()
        self.usernameInput = tk.StringVar()
        self.passwordInput = tk.StringVar()
        self.classNumInput = tk.StringVar()
        self.payNowQues = tk.IntVar()
        self.FAQues = tk.IntVar()

        # Variables for Credit Card Info
        self.CCN = tk.StringVar()
        self.expirationMonth = tk.StringVar()
        self.expirationYear = tk.StringVar()
        self.CVV2 = tk.StringVar()
        self.postalCode = tk.StringVar()
        self.date = tk.StringVar()

        self.selectSemester.set(0)
        self.payNowQues.set(0)

        # Basic Information

        # Username
        self.userLabel = tk.Label(master, text="Username")
        self.username = tk.Entry(master, textvariable=self.usernameInput)
        self.userLabel.place(x = 20, y = 20)
        self.username.place(x = 20, y = 42)

        # Password
        self.passwordLabel = tk.Label(master, text="Password")
        self.password = tk.Entry(master, textvariable=self.passwordInput)
        self.passwordLabel.place(x = 20, y = 70)
        self.password.place(x = 20, y = 88)

        # Semester
        self.semesterLabel = tk.Label(master, text="Select Semester")
        self.springSemester = tk.Radiobutton(self.master, text="Spring", variable=self.selectSemester, value=1, command=self.fillSemDic)
        self.fallSemester = tk.Radiobutton(self.master, text="Fall", variable=self.selectSemester, value=2, command=self.fillSemDic)
        self.summerSemester = tk.Radiobutton(self.master, text="Summer", variable=self.selectSemester, value=3, command=self.fillSemDic)
        self.semesterLabel.place(x = 20, y = 118)
        self.springSemester.place(x = 20, y = 135)
        self.fallSemester.place(x = 20, y = 157)
        self.summerSemester.place(x = 20, y = 180)

        # Classes
        self.classLabel = tk.Label(self.master, text="Enter Class Num")
        self.classNum = tk.Entry(self.master, textvariable=self.classNumInput)
        self.classInput = tk.Button(self.master, text="Enter", command=self.inputClass)
        self.classLabel.place(x = 20, y = 210)
        self.classNum.place(x = 20, y = 230)
        self.classInput.place(x = 220, y = 229)

        # Pay
        self.payLabel = tk.Label(self.master, text="When would like to pay?")
        self.payNow = tk.Radiobutton(self.master, text="Now", variable=self.payNowQues, value=1, command=self.paymentNowQuestion)
        self.payLater = tk.Radiobutton(self.master, text="Later", variable=self.paymentNowQuestion, value=0, command=self.paymentNowQuestion)
        self.payLabel.place(x = 20, y = 260)
        self.payLater.place(x = 20, y = 300)
        self.payNow.place(x = 20, y = 280)

        # Financial Aid
        self.FALabel = tk.Label(self.master, text="Financial Aid")
        self.FARB = tk.Radiobutton(self.master, text="Yes", variable=self.FAQues, value=1, command=self.FAQuestion)
        self.FARB2 = tk.Radiobutton(self.master, text="No", variable=self.FAQues, value=2, command=self.FAQuestion)
        self.FALabel.place(x = 20, y = 340)
        self.FARB.place(x = 20, y = 360)
        self.FARB2.place(x = 20, y = 380)

        # Page Management Buttons
        self.submit = tk.Button(self.master, text="Submit", command=self.submitData)
        self.submit.place(x = 20, y = 410)


        # Credit Card Information
        self.cnn = tk.Label(self.master, text="Enter your Credit Card Numer")
        self.ccnEntry = tk.Entry(self.master, textvariable = self.CCN)
        self.cnn.place(x = 500, y = 20)
        self.ccnEntry.place(x = 500, y = 50)

        self.Expiration =  tk.Label(self.master, text="Enter the Date   Ex. \'01 (JAN)\'")
        self.expInput = tk.Entry(self.master, textvariable = self.expirationMonth)
        self.Expiration.place(x = 500, y = 80)
        self.expInput.place(x = 500, y = 110)

        self.yearLabel = tk.Label(self.master, text="Enter the expiration year")
        self.yearInput = tk.Entry(self.master, textvariable = self.expirationYear)
        self.yearLabel.place(x = 500, y = 140)
        self.yearInput.place(x = 500, y = 170)

        self.cvv2Label = tk.Label(self.master, text="Enter your CVV2")
        self.cvv2Input = tk.Entry(self.master, textvariable = self.CVV2)
        self.cvv2Label.place(x = 500, y = 200)
        self.cvv2Input.place(x = 500, y = 230)

        self.postalCodeLabel = tk.Label(self.master, text="Enter your postal code")
        self.postalCodeInput = tk.Entry(self.master, textvariable = self.postalCode)
        self.postalCodeLabel.place(x = 500, y = 260)
        self.postalCodeInput.place(x = 500, y = 290)

        self.getDateLabel = tk.Label(self.master, text="Enter the date of registration")
        self.getDateInput = tk.Entry(self.master, textvariable = self.date)

        self.submitCredit = tk.Button(self.master, text="Submit", command=self.submitCreditInfo)
        self.submitCredit.place(x = 500, y = 320)

        # Button to install Chromedriver
        self.installChromeDriverButton = tk.Label(self.master, text="Install ChromeDriver")
        self.installChromeDriver = tk.Button(self.master, text="Install", command=self.installDriver)
        self.installChromeDriverButton.place(x = 500, y = 400)
        self.installChromeDriver.place(x = 500, y = 430)

    # Change the Semester in the Dictionary
    def fillSemDic(self):
        if (self.selectSemester.get() == 1):
            loginAndPayInfo["Semester"] = "Spring"
        elif (self.selectSemester.get() == 2):
            loginAndPayInfo["Semester"] = "Fall"
        elif (self.selectSemester.get() == 3):
            loginAndPayInfo["Semester"] = "Summer"

    # Change the Payment Question
    def paymentNowQuestion(self):
        if (self.payNowQues.get() == 1):
            loginAndPayInfo["Pay"] = "now"
        elif (self.payNowQues.get() == 0):
            loginAndPayInfo["Pay"] = ""

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

    def submitCreditInfo(self):
        loginAndPayInfo["CCN"] = self.CCN.get()
        loginAndPayInfo["Expiration"] = self.expirationMonth.get()
        loginAndPayInfo["Year"] = self.expirationYear.get()
        loginAndPayInfo["CVV2"] = self.CVV2.get()
        loginAndPayInfo["postalCode"] = self.postalCode.get()

        loginAndPayInfo["scheduleDate"] = self.date.get()

        login_MySite(**loginAndPayInfo)

    def installDriver(self):
        IdentifiyPlatform()

def main():
    root = tk.Tk()
    # app = manageFrames()
    app = fillInfo(root)
    app.mainloop()



if __name__ == '__main__':
    main()
