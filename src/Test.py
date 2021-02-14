from os import getcwd
from selenium import webdriver

invalid_inputs = ["", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"] #empty-string and 64+ character string

invalid_emails = ["email.com", "invalid_email", ""]
unregistered_emails = ["invaliduser1@gmail.com", "invaliduser2@gmail.com", "invaliduser3@gmail.com", "invaliduser4@gmail.com"]
registered_emails = ["user1@gmail.com", "user2@gmail.com", "user3@gmail.com", "user4@gmail.com"]

invalid_phnumber = ["0555000", "", ""]
unregistered_phnumber = ["05550000001", "05550000002", "05550000003", "05550000004"]
registered_phnumber = ["05330000001", "05330000002", "05330000003", "05330000004"]

invalid_passwords = ["", "", ""]
unregistered_passwords = ["invalidpassword1", "invalidpassword2", "invalidpassword3", "invalidpassword4"]
registered_passwords = ["password1", "password2", "password3", "password4"]


def home_button_check():
    pass

def help_button_check():
    pass

def signupnow_button_check():
    pass

def passhide_button_check():
    pass

def email_check():
    
    #registered_check_cases = ["", "",]
    email_input = driver.find_element_by_id("email")
    for case in invalid_check_cases:
        email_input.send_keys(case)
   

def telephonenumber_check():
    pass

def password_check():
    pass

driver = webdriver.Chrome() #Change if another browser or driver to use!
url_path = getcwd()
driver.get(url_path + "/login.html")

email_check()

#driver.close()


