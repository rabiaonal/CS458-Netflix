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
registered_passwords = ["329129293", "1234", "123123123"] #Should be sorted with respect to registered_emails

def index_page_sign_in_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signInBtn").click()
    assertCheck("Index page sign in button test", driver.current_url, "http://localhost:3000/login")

def index_page_sign_up_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signUpBtn").click()
    assertCheck("Index page sign up button test", driver.current_url, "http://localhost:3000/signup")

def assertCheck(test_descriptor, input, expected):
    try:
        assert input == expected
        print(test_descriptor, "Test Successful.", "Expected Result: ", expected)
    except AssertionError:
        print(test_descriptor, "Test Failed.", "Expected Result: ", expected)

def home_button_check():
    pass
def login_page_home_button_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("homebutton").click()
    assertCheck("Login page home button test", driver.current_url, "http://localhost:3000/")

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
        print("Login page pass/hide button test: ", "Test Succesful.")
    except AssertionError:
        print("Login page pass/hide button test: ", "Test Failed.")

def login_page_sign_up_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("signupLink").click()
    assertCheck("Login page sign up link test", driver.current_url, "http://localhost:3000/signup")

def login_page_help_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("forgotpasswordLink").click()
    assertCheck("Login page help up link test", driver.current_url, "http://localhost:3000/forgotpassword")

def signup_page_login_link_check():
    driver.get("http://localhost:3000/signup")
    driver.find_element_by_id("loginLink").click()
    assertCheck("Sign up page login link test", driver.current_url, "http://localhost:3000/login")

def login_script(email, password):
    print("Login with email: %s, password: %s" % (email, password))
    driver.get(url_path + login_route)
    driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginSubmit").click()

def email_check():
    for email in invalid_emails:
        login_script(email, registered_passwords[0])
        email_error = driver.find_element_by_id("emailError")
        assertCheck("Check invalid email", email_error.get_attribute('innerHTML'), "Please enter a valid e‑mail.")

    for email in unregistered_emails:
        login_script(email, registered_passwords[0])
        login_error = driver.find_element_by_id("loginError")
        assertCheck("Check unregistered email", login_error.get_attribute('innerHTML'), "There is no such account. Please try signing up.")

    for i, email in enumerate(registered_emails, start=0):
        login_script(email, registered_passwords[i])
        welcome = driver.find_element_by_tag_name("h1")
        assertCheck("Check registered email", welcome.get_attribute('innerHTML'), "Login Successful. Welcome " + email)

def pass_check():
    for i in range(0, len(registered_emails)):
        login_script(registered_emails[i], invalid_passwords[i])
        assertCheck("Invalid password test %d:" % (i+1), driver.find_element_by_id("passError").get_attribute("innerText"), "Password should be between 4 and 60 characters long.")
        login_script(registered_emails[i], unregistered_passwords[i])
        assertCheck("Unregistered password test %d:" % (i+1), driver.find_element_by_id("loginError").get_attribute("innerHTML"), "Wrong password. Please try again or reset your password.")
        login_script(registered_emails[i], registered_passwords[i])
        assertCheck("Registered password test %d:" % (i+1), driver.find_element_by_tag_name("h1").get_attribute("innerHTML"), "Login Successful. Welcome %s" % (registered_emails[i]))

def phone_check():
    pass

driver = webdriver.Chrome() #Change if another browser or driver to use!
url_path = "http://localhost:3000/"
login_route = "login"
signup_page_login_link_check()
login_page_home_button_check()
login_page_sign_up_link_check()
login_page_help_link_check()
login_page_passhide_button_check()
email_check()
pass_check()
driver.close()


