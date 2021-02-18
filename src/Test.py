from os import getcwd
import os
from time import sleep
from selenium import webdriver

os.system('start python -m http.server 8000') #Start localhost in another terminal

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

def index_page_sign_in_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signInBtn").click()
    sleep(1)
    assert driver.current_url == "http://localhost:3000/login"

def index_page_sign_up_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signUpBtn").click()
    sleep(1)
    assert driver.current_url == "http://localhost:3000/signup"

def login_page_home_button_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("homebutton").click()
    sleep(2)
    assert driver.current_url == "http://localhost:3000/"

def login_page_passhide_button_check():
    driver.get("http://localhost:3000/login")
    button = driver.find_element_by_id("passhideBtn")
    button_type_1 = button.get_attribute("type")
    button.click()
    button_type_2 = button.get_attribute("type")
    button.click()
    button_type_3 = button.get_attribute("type")
    assert button_type_1 != button_type_2 & button_type_1 == button_type_3


def login_page_sign_up_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("signupLink").click()
    sleep(1)
    assert driver.current_url == "http://localhost:3000/signup"


def login_page_help_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("forgotpasswordLink").click()
    sleep(1)
    assert driver.current_url == "http://localhost:3000/forgotpassword"

def signup_page_login_link_check():
    driver.get("http://localhost:3000/signup")
    driver.find_element_by_id("loginLink").click()
    sleep(1)
    assert driver.current_url == "http://localhost:3000/login"

def invalid_input_check():
    pass

def email_check():
    email_input = driver.find_element_by_id("email")
    sign_in_button = driver.find_element_by_id("loginBtn")
    for email in invalid_emails:
        email_input.send_keys(email)
        sign_in_button.click()
        sleep(10)

def telephonenumber_check():
    pass

def password_check():
    pass

driver = webdriver.Chrome() #Change if another browser or driver to use!
#url_path = "http://localhost:8000/src" #getcwd()
#sleep(2) #Wait 2 secs for localhost to start
#driver.get(url_path + "/index.html")
#driver.find_element_by_id("signInBtn").click()

#email_check()

driver.close()


