from logging import exception, log
from selenium.common.exceptions import ElementNotInteractableException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from dotenv import load_dotenv
import datetime
import os
import time

options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('user-agent = Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')

driver = webdriver.Chrome(chrome_options=options, executable_path="/Users/jojo/Documents/python_learning/mysite_bot_development/chromedriver")
load_dotenv("private.env")



def run_till_time():
    return

def login_MySite(): 
    driver.get("https://mysite.socccd.edu/Portal/Login.aspx")

    # Get the private information from the env file 
    private_username = os.getenv("USERNAME")
    private_password = os.getenv("PASSWORD")
    semester = os.getenv("SEMESTER")
    classes = os.getenv("CLASSES")
    FA = os.getenv("FA")

    # Get Private credit card information 
    payment = os.getenv("PAY")
    creditNum = os.getenv("CREDIT_CARD_NUM")
    expirationMonth = os.getenv("EXPIRATION")
    expirationYear = os.getenv("YEAR")
    CV = os.getenv("CVV2")
    BAPS = os.getenv("BILLINGADDRESS_POSTALCODE")


    
    # Get the textbox within mysite 
    usernameTextBox = driver.find_element(By.ID, "txtUsername")
    passwordTextBox = driver.find_element(By.ID, "txtPassword")

    # Insert password into the textbox of mysite
    usernameTextBox.send_keys(private_username)
    passwordTextBox.send_keys(private_password)

    # Login into mysite website by clicking on login button
    driver.find_element(By.ID, "btnLogin").click()

    # Get the Add/Drop Classes link
    driver.get("https://mysite.socccd.edu/Portal/MySite/Classes/Registration/SelectTerm.aspx")

    # Get the current term and the future term 
    time.sleep(3)
    CS = driver.find_element(By.ID, "ctl00_BodyContent_Term0_TermName").text
    FS = driver.find_element(By.ID, "ctl00_BodyContent_Term1_TermName").text

    # Get the Semster name and check whether the semster are the same 
    if (str(FS.rsplit(" ", 1)[0]) == str(semester)):

        # Click the correct semester 
        driver.find_element(By.ID, "ctl00_BodyContent_Term1_TermName").click()

        # 
        driver.find_element(By.ID, "ctl00_BodyContent_Term1_AddDropClasses").click()

        # selenium.common.exceptions.NoSuchElementException
        # selenium.common.exceptions.NoSuchElementException


        time.sleep(3)
        # Insert all classes into the textbox
        for oneClasses in classes.split(" "): 
            print(oneClasses)
            driver.find_element(By.ID, "ctl00_BodyContent_ucScheduleBuilder_txtTicketNumber").send_keys(oneClasses)
            driver.find_element(By.ID, "ctl00_BodyContent_ucScheduleBuilder_btnAddClass").click()

        time.sleep(5)
        
        # After completed with assigning up for class 
        driver.find_element(By.ID, "ctl00_BodyContent_ucScheduleBuilder_btnNext").click() 

        # Completed with Charges and credits 
        driver.find_element(By.ID, "ctl00_BodyContent_btnNext").click() 

        # ---- ADD ABILITY TO ADD ASB ---- 

        class_pay = driver.find_element(By.ID, "rdbPaymentOptionPayNow").text
        print(class_pay.rsplit(" ")[0])

        # PAY NOW 
        if (str(class_pay.rsplit(" ")[0] == str(payment))):
            driver.find_element(By.ID, "rdbPaymentOptionPayNow").click()

            time.sleep(5)

            # Credit Card Number 
            driver.find_element(By.ID, "txtCreditCardNumber").send_keys(creditNum)

            # CVV2 
            driver.find_element(By.ID, "txtCVV2").send_keys(CV)

            # Billing Address Zip / Postal Code 
            driver.find_element(By.ID, "txtZipCode").send_keys(BAPS)

            # Expiration Date
            expDate = Select(driver.find_element(By.ID, "ddlExpirationMonth"))
            expDate.select_by_visible_text(expirationMonth)

            # Expiration Year 
            expYear = Select(driver.find_element(By.ID, "ddlExpirationYear"))
            expYear.select_by_visible_text(expirationYear)

            # Complete registration 
            driver.find_element(By.ID, "btnMakePaymentLower").click()
        
        # Pay Later
        else: 
            driver.find_element(By.ID, "rdbPaymentOptionPayLater").click()

            # Finanical Aid 
            textFA = driver.find_element(By.XPATH, "//*[@id=\"navLinkFinancialAid\"]/span/label").text 

            if (textFA == FA): 
                driver.find_element(By.ID, "rdbFinAidOptionApplied").click()

            # rdbFinAidOptionPending

            # navLinkCheckMoney



    if (str(CS.rsplit(" ", 1)) == str(semester)):
        return

    # ctl00_BodyContent_ucScheduleBuilder_txtTicketNumber
    # ctl00_BodyContent_Term1_AddDropClasses


    # driver.close()

login_MySite()

