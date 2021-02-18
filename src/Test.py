from time import sleep
from selenium import webdriver

invalid_emails = ["emai", "mail", "@ema", "asdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfgasdfga"] #Email must be between 5 and 50 characters
unregistered_emails = ["invaliduser1@gmail.com", "invaliduser2@gmail.com", "invaliduser3@gmail.com"]
registered_emails = ["kenneth@gmail.com", "john@gmail.com", "mary@gmail.com"]

invalid_phnumber = ["0000", "1234", "-().", ""]
unregistered_phnumber = ["5320000001", "5540000002", "5420000003", "5050000004"]
registered_phnumber = ["5550000000", "5551111111", "5552222222"]

invalid_passwords = ["123", "xyz", "...", "0123456789012345678901234567890123456789012345678901234567891"] #Password must be between 4 and 60 characters
unregistered_passwords = ["invalidpassword1", "invalidpassword2", "invalidpassword3"]
registered_passwords = ["329129293", "1234", "123123123"] #Should be sorted with respect to registered_emails

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
    input = driver.find_element_by_id("pass")
    input_type_1 = input.get_attribute("type")
    button.click()
    input_type_2 = input.get_attribute("type")
    button.click()
    input_type_3 = input.get_attribute("type")
    #assertCheck("Login page pass hide button check", driver.current_url, "http://localhost:3000/login")
    try:
        assert (input_type_1 != input_type_2) & (input_type_1 == input_type_3)
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

def email_check():
    for email in invalid_emails:
        driver.get(url_path + "/login")
        email_input = driver.find_element_by_id("email")
        pass_input = driver.find_element_by_id("pass")
        sign_in_button = driver.find_element_by_id("loginBtn")
        email_error = driver.find_element_by_id("emailError")

        email_input.send_keys(email)
        pass_input.send_keys(registered_passwords[0]) #Password will be valid
        sign_in_button.click()
        assertCheck("URL Check", driver.current_url, url_path + "/login")
        assertCheck("Check invalid email", email_error.get_attribute('innerHTML'), "Lütfen geçerli bir e‑posta adresi girin.")


    for email in unregistered_emails:
        driver.get(url_path + "/login")
        email_input = driver.find_element_by_id("email")
        pass_input = driver.find_element_by_id("pass")
        sign_in_button = driver.find_element_by_id("loginBtn")

        email_input.send_keys(email)
        pass_input.send_keys(registered_passwords[0]) #Password will be valid
        sign_in_button.click()

        login_error = driver.find_element_by_id("loginError")
        assertCheck("URL Check", driver.current_url, url_path + "/login")
        assertCheck("Check unregistered email", login_error.get_attribute('innerHTML'), "Böyle bir hesap bulamadık. Lütfen kaydolmayı deneyin.")

    for i, email in enumerate(registered_emails, start=0):
        driver.get(url_path + "/login")
        email_input = driver.find_element_by_id("email")
        pass_input = driver.find_element_by_id("pass")
        sign_in_button = driver.find_element_by_id("loginBtn")

        email_input.send_keys(email)
        pass_input.send_keys(registered_passwords[i]) #Respective valid password
        sign_in_button.click()
        welcome = driver.find_element_by_tag_name("h1")
        assertCheck("Check registered email", welcome.get_attribute('innerHTML'), "Login Successful. Welcome " + email)

def telephonenumber_check():
    pass

def password_check():
    pass

driver = webdriver.Chrome() #Change if another browser or driver to use!
url_path = "http://localhost:3000"
driver.get(url_path + "/")
sleep(2) #Wait 2 secs for localhost to start
driver.find_element_by_id("signInBtn").click()
sleep(1)
email_check()

signup_page_login_link_check()
login_page_help_link_check()
login_page_home_button_check()
login_page_passhide_button_check()
login_page_sign_up_link_check()

driver.close()


