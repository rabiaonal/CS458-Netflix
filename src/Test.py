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

def assertCheck(test_descriptor, input, expected):
    try:
        assert input == expected
        print(test_descriptor, "Test Succesful.")
    except AssertionError:
        print(test_descriptor, "Test Failed.", "Expected Result: ", expected)

def index_page_sign_in_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signInBtn").click()
    sleep(1)
    assertCheck("Index page sign in button test", driver.current_url, "http://localhost:3000/login")
    #assert driver.current_url == "http://localhost:3000/login"

def index_page_sign_up_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signUpBtn").click()
    sleep(1)
    assertCheck("Index page sign up button test", driver.current_url, "http://localhost:3000/signup")
    #assert driver.current_url == "http://localhost:3000/signup"

def login_page_home_button_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("homebutton").click()
    sleep(1)
    assertCheck("Login page home button test", driver.current_url, "http://localhost:3000/")
    #assert driver.current_url == "http://localhost:3000/"

def login_page_passhide_button_check():
    driver.get("http://localhost:3000/login")
    button = driver.find_element_by_id("passhideBtn")
    button_type_1 = button.get_attribute("type")
    button.click()
    button_type_2 = button.get_attribute("type")
    button.click()
    button_type_3 = button.get_attribute("type")
    #assertCheck("Login page pass hide button check", driver.current_url, "http://localhost:3000/login")
    try:
        assert button_type_1 != button_type_2 & button_type_1 == button_type_3
        print("Login page pass/hide button test: ", "Test Succesful.")
    except AssertionError:
        print("Login page pass/hide button test: ", "Test Failed.")


def login_page_sign_up_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("signupLink").click()
    sleep(1)
    assertCheck("Login page sign up link test", driver.current_url, "http://localhost:3000/signup")
    #assert driver.current_url == "http://localhost:3000/signup"


def login_page_help_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("forgotpasswordLink").click()
    sleep(1)
    assertCheck("Login page help up link test", driver.current_url, "http://localhost:3000/forgotpassword")
    #assert driver.current_url == "http://localhost:3000/forgotpassword"

def signup_page_login_link_check():
    driver.get("http://localhost:3000/signup")
    driver.find_element_by_id("loginLink").click()
    sleep(1)
    assertCheck("Sign up page login link test", driver.current_url, "http://localhost:3000/login")
    #assert driver.current_url == "http://localhost:3000/login"


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


