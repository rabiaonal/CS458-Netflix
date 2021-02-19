from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

invalid_input = ""

invalid_emails = ["emai", "@ema", "mail", "toolongcharacteremailabout50charactersapplicationshouldgiveerror"] #Email must be between 5 and 50 characters
unregistered_emails = ["invaliduser1@gmail.com", "invaliduser2@gmail.com", "invaliduser3@gmail.com"]
registered_emails = ["kenneth@gmail.com", "john@gmail.com", "mary@gmail.com"]

invalid_phnumbers = ["0000", "1234", "+(0)", "555555555555555555555555555555555555555555555555551"]
unregistered_phnumbers = ["5320000001", "5540000002", "5420000003", "5050000004"]
registered_phnumbers = ["5550000000", "5551111111", "5552222222"]

invalid_passwords = ["123", "xyz", "...", "0123456789012345678901234567890123456789012345678901234567891"] #Password must be between 4 and 60 characters
unregistered_passwords = ["invalidpassword1", "invalidpassword2", "invalidpassword3"]
registered_passwords = ["329129293", "1234", "123123123"] #Should be sorted with respect to registered_emails

def assertCheck(test_descriptor, input, expected):
    try:
        assert input == expected
        print(test_descriptor, "Test Successful.", "Expected Result:", expected)
    except AssertionError:
        print(test_descriptor, "Test Failed.", "Expected Result:", expected, "Obtained Result:", input)

def index_page_sign_in_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signInBtn").click()
    assertCheck("Index-page sign in button test:", driver.current_url, "http://localhost:3000/login")

def index_page_sign_up_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signUpBtn").click()
    assertCheck("Index-page sign up button test:", driver.current_url, "http://localhost:3000/signup")

def login_page_home_button_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("homebutton").click()
    assertCheck("Login-page home button test:", driver.current_url, "http://localhost:3000/")

def login_page_passhide_button_check():
    driver.get("http://localhost:3000/login")
    button = driver.find_element_by_id("passhideBtn")
    input = driver.find_element_by_id("pass")
    input_type_1 = input.get_attribute("type")
    button.click()
    input_type_2 = input.get_attribute("type")
    button.click()
    input_type_3 = input.get_attribute("type")
    try:
        assert (input_type_1 != input_type_2) & (input_type_1 == input_type_3)
        print("Login-page pass-hide button test:", "Test Successful.")
    except AssertionError:
        print("Login-page pass-hide button test:", "Test Failed.")

def login_page_sign_up_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("signupLink").click()
    assertCheck("Login-page sign up link test:", driver.current_url, "http://localhost:3000/signup")

def login_page_help_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("forgotpasswordLink").click()
    assertCheck("Login-page help link test:", driver.current_url, "http://localhost:3000/resetpass")

def signup_page_login_link_check():
    driver.get("http://localhost:3000/signup")
    driver.find_element_by_id("loginLink").click()
    assertCheck("Signup-page sign in link test:", driver.current_url, "http://localhost:3000/login")

def input_check():
    driver.get(url_path + login_route)
    print("Login with input: %s, password: %s" % (invalid_input, registered_passwords[0]))
    driver.find_element_by_id("email").send_keys(invalid_input)
    driver.find_element_by_id("pass").send_keys(registered_passwords[0])
    driver.find_element_by_id("loginSubmit").click()
    assertCheck("Check invalid input test:", driver.find_element_by_id("emailError").get_attribute('innerHTML'), "Please enter a valid e-mail or password.")

def login_script(email, phone, password):
    driver.get(url_path + login_route)
    if email is None:
        print("Login with phone: %s, password: %s" % (phone, password))
        driver.find_element_by_id("email").send_keys(phone)
    else:
        print("Login with email: %s, password: %s" % (email, password))
        driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginSubmit").click()

def email_check():
    for i  in range(0, len(invalid_emails)):
        login_script(invalid_emails[i], None, registered_passwords[0])
        assertCheck("Check invalid email test %d:" % (i+1), driver.find_element_by_id("emailError").get_attribute('innerHTML'), "Please enter a valid e-mail.")

    for i  in range(0, len(unregistered_emails)):
        login_script(unregistered_emails[i], None, registered_passwords[0])
        assertCheck("Check unregistered email test %d:" % (i+1), driver.find_element_by_id("loginError").get_attribute('innerHTML'), "There is no such account. Please try signing up.")

    for i  in range(0, len(registered_emails)):
        login_script(registered_emails[i], None, registered_passwords[i])
        assertCheck("Check registered email test %d:" % (i+1), driver.find_element_by_tag_name("h1").get_attribute('innerHTML'), "Login Successful. Welcome " + registered_emails[i])

def pass_check():
    for i in range(0, len(registered_emails)):
        login_script(registered_emails[i], None, invalid_passwords[i])
        assertCheck("Invalid password test %d:" % (i+1), driver.find_element_by_id("passError").get_attribute("innerText"), "Password should be between 4 and 60 characters long.")
        login_script(registered_emails[i], None, unregistered_passwords[i])
        assertCheck("Unregistered password test %d:" % (i+1), driver.find_element_by_id("loginError").get_attribute("innerHTML"), "Wrong password. Please try again or reset your password.")
        login_script(registered_emails[i], None, registered_passwords[i])
        assertCheck("Registered password test %d:" % (i+1), driver.find_element_by_tag_name("h1").get_attribute("innerHTML"), "Login Successful. Welcome " + registered_emails[i])

def phone_check():
    for i  in range(0, len(invalid_phnumbers)):
        login_script(None, invalid_phnumbers[i], registered_passwords[0])
        assertCheck("Check invalid phone test %d:" % (i+1), driver.find_element_by_id("emailError").get_attribute('innerHTML'), "Please enter a valid phone number.")

    for i  in range(0, len(unregistered_phnumbers)):
        login_script(None, unregistered_phnumbers[i], registered_passwords[0])
        assertCheck("Check unregistered phone test %d:" % (i+1), driver.find_element_by_id("loginError").get_attribute('innerHTML'), "There is no such account. Please try signing up.")

    for i  in range(0, len(registered_phnumbers)):
        login_script(None, registered_phnumbers[i], registered_passwords[i])
        assertCheck("Check registered phone test %d:" % (i+1), driver.find_element_by_tag_name("h1").get_attribute('innerHTML'), "Login Successful. Welcome " + registered_emails[i])


def keyboard_functionality_check():
    action = ActionChains(driver)   #Keyboard actions

    #Submit with Enter key test
    driver.get(url_path + login_route)
    driver.find_element_by_id("email").send_keys(registered_emails[0])
    driver.find_element_by_id("pass").send_keys(registered_passwords[0])
    driver.find_element_by_id("pass").send_keys(Keys.ENTER)
    assertCheck("Submit with enter key test %d:" % (1), driver.find_element_by_tag_name("h1").get_attribute('innerHTML'), "Login Successful. Welcome " + registered_emails[0])

    #Copy, paste and select all keyboard shortcuts test (Ctrl + C, Ctrl + V, Ctrl + A)
    driver.get(url_path + login_route)
    driver.find_element_by_id("passhideBtn").click()
    driver.find_element_by_id("pass").send_keys(registered_passwords[0])
    action.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

    driver.find_element_by_id("email").click()
    action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    assertCheck("Copy, paste and select all keyboard shortcuts test %d:" % (1), driver.find_element_by_id("email").get_attribute('value'), registered_passwords[0])

def consecutive_login_check():
    for i in range(7):
        login_script(unregistered_emails[0], None, unregistered_passwords[0])
    assertCheck("Check consecutive login fail %d:" % (1), driver.find_element_by_id("loginError").get_attribute('innerHTML'), "Sorry, something went wrong. Please try again later.")

driver = webdriver.Chrome() #Change if another browser or driver to use!
url_path = "http://localhost:3000/"
login_route = "login"

signup_page_login_link_check()
login_page_home_button_check()
login_page_sign_up_link_check()
login_page_help_link_check()
login_page_passhide_button_check()
input_check()
email_check()
phone_check()
pass_check()
keyboard_functionality_check()
consecutive_login_check()

driver.close()


