from os import getcwd
import os
from time import sleep
from selenium import webdriver

invalid_emails = ["emai", "@ema", "mail", "asdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfga"] #Email must be between 5 and 50 characters
unregistered_emails = ["invaliduser1@gmail.com", "invaliduser2@gmail.com", "invaliduser3@gmail.com"]
registered_emails = ["kenneth@gmail.com", "john@gmail.com", "mary@gmail.com"]

invalid_phnumber = ["0000", "1234", "-().", ""]
unregistered_phnumber = ["5320000001", "5540000002", "5420000003", "5050000004"]
registered_phnumber = ["5550000000", "5551111111", "5552222222"]

invalid_passwords = ["123", "xyz", "...", "0123456789012345678901234567890123456789012345678901234567891"] #Password must be between 4 and 60 characters
unregistered_passwords = ["invalidpassword1", "invalidpassword2", "invalidpassword3"]
registered_passwords = ["329129293", "1234", "123123123"]

def home_button_check():
    pass

def help_button_check():
    pass

def signupnow_button_check():
    pass

def passhide_button_check():
    pass


# Check different input combinations
# Check how webpage corresponds to invalid inputs(empty, too many characters)
# Check how webpage corresponds to invalid/unregistered/registered email
# Check how webpage corresponds to invalid/unregistered/registered telephone number
# Check how webpage corresponds to invalid/unregistered/registered password

def email_check():
    email_input = driver.find_element_by_id("email")
    sign_in_button = driver.find_element_by_id("loginBtn")
    email_error = driver.find_element_by_id("emailError")
    for email in invalid_emails:
        email_input.send_keys(email)
        sign_in_button.click()
        sleep(10)

def telephonenumber_check():
    pass

def password_check():
    pass

driver = webdriver.Chrome() #Change if another browser or driver to use!
url_path = "http://localhost:3000/" #getcwd()
sleep(2) #Wait 2 secs for localhost to start
driver.get(url_path + "/index.html")
driver.find_element_by_id("signInBtn").click()

email_check()

driver.close()


