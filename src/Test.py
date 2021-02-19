import sys
from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException

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
        if log_enabled:
            print(test_descriptor, "Test Successful.", "Expected Result:", expected)
        return True
    except AssertionError:
        if log_enabled:
            print(test_descriptor, "Test Failed.", "Expected Result:", expected, "Obtained Result:", input)
        return False

def index_page_sign_in_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signInBtn").click()
    return assertCheck("Index-page sign in button test:", driver.current_url, "http://localhost:3000/login")

def index_page_sign_up_button_check():
    driver.get("http://localhost:3000/")
    driver.find_element_by_id("signUpBtn").click()
    return assertCheck("Index-page sign up button test:", driver.current_url, "http://localhost:3000/signup")

def login_page_home_button_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("homebutton").click()
    return assertCheck("Login-page home button test:", driver.current_url, "http://localhost:3000/")

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
        if log_enabled:
            print("Login-page pass-hide button test:", "Test Successful.")
        return True
    except AssertionError:
        if log_enabled:
            print("Login-page pass-hide button test:", "Test Failed.")
        return False

def login_page_sign_up_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("signupLink").click()
    return assertCheck("Login-page sign up link test:", driver.current_url, "http://localhost:3000/signup")

def login_page_help_link_check():
    driver.get("http://localhost:3000/login")
    driver.find_element_by_id("forgotpasswordLink").click()
    return assertCheck("Login-page help link test:", driver.current_url, "http://localhost:3000/resetpass")

def signup_page_login_link_check():
    driver.get("http://localhost:3000/signup")
    driver.find_element_by_id("loginLink").click()
    return assertCheck("Signup-page sign in link test:", driver.current_url, "http://localhost:3000/login")

def input_check():
    driver.get(url_path + login_route)
    if log_enabled:
        print("Login with input: %s, password: %s" % (invalid_input, registered_passwords[0]))
    driver.find_element_by_id("email").send_keys(invalid_input)
    driver.find_element_by_id("pass").send_keys(registered_passwords[0])
    driver.find_element_by_id("loginSubmit").click()
    return assertCheck("Check invalid input test:", driver.find_element_by_id("emailError").get_attribute('innerHTML'), "Please enter a valid e-mail or password.")

def login_script(email, phone, password):
    driver.get(url_path + login_route)
    if email is None:
        if log_enabled:
            print("Login with phone: %s, password: %s" % (phone, password))
        driver.find_element_by_id("email").send_keys(phone)
    else:
        if log_enabled:
            print("Login with email: %s, password: %s" % (email, password))
        driver.find_element_by_id("email").send_keys(email)
    driver.find_element_by_id("pass").send_keys(password)
    driver.find_element_by_id("loginSubmit").click()

def email_check():
    results = { "invalid": [], "unregistered": [], "registered": [] }
    for i  in range(0, len(invalid_emails)):
        login_script(invalid_emails[i], None, registered_passwords[0])
        results["invalid"].append(assertCheck("Check invalid email test %d:" % (i+1), driver.find_element_by_id("emailError").get_attribute('innerHTML'), "Please enter a valid e-mail."))
    for i  in range(0, len(unregistered_emails)):
        login_script(unregistered_emails[i], None, registered_passwords[0])
        results["unregistered"].append(assertCheck("Check unregistered email test %d:" % (i+1), driver.find_element_by_id("loginError").get_attribute('innerHTML'), "There is no such account. Please try signing up."))
    for i  in range(0, len(registered_emails)):
        login_script(registered_emails[i], None, registered_passwords[i])
        results["registered"].append(assertCheck("Check registered email test %d:" % (i+1), driver.find_element_by_tag_name("h1").get_attribute('innerHTML'), "Login Successful. Welcome " + registered_emails[i]))
    return results

def pass_check():
    results = { "invalid": [], "unregistered": [], "registered": [] }
    for i in range(0, len(registered_emails)):
        login_script(registered_emails[i], None, invalid_passwords[i])
        results["invalid"].append(assertCheck("Invalid password test %d:" % (i+1), driver.find_element_by_id("passError").get_attribute("innerText"), "Password should be between 4 and 60 characters long."))
        login_script(registered_emails[i], None, unregistered_passwords[i])
        results["unregistered"].append(assertCheck("Unregistered password test %d:" % (i+1), driver.find_element_by_id("loginError").get_attribute("innerHTML"), "Wrong password. Please try again or reset your password."))
        login_script(registered_emails[i], None, registered_passwords[i])
        results["registered"].append(assertCheck("Registered password test %d:" % (i+1), driver.find_element_by_tag_name("h1").get_attribute("innerHTML"), "Login Successful. Welcome " + registered_emails[i]))
    return results

def phone_check():
    results = { "invalid": [], "unregistered": [], "registered": [] }
    for i  in range(0, len(invalid_phnumbers)):
        login_script(None, invalid_phnumbers[i], registered_passwords[0])
        results["invalid"].append(assertCheck("Check invalid phone test %d:" % (i+1), driver.find_element_by_id("emailError").get_attribute('innerHTML'), "Please enter a valid phone number."))
    for i  in range(0, len(unregistered_phnumbers)):
        login_script(None, unregistered_phnumbers[i], registered_passwords[0])
        results["unregistered"].append(assertCheck("Check unregistered phone test %d:" % (i+1), driver.find_element_by_id("loginError").get_attribute('innerHTML'), "There is no such account. Please try signing up."))
    for i  in range(0, len(registered_phnumbers)):
        login_script(None, registered_phnumbers[i], registered_passwords[i])
        results["registered"].append(assertCheck("Check registered phone test %d:" % (i+1), driver.find_element_by_tag_name("h1").get_attribute('innerHTML'), "Login Successful. Welcome " + registered_emails[i]))
    return results

def compatibility_check():
    allsuccess = True
    if not res_spllc:
        allsuccess = False
        print("\t Signup-page sign in link test failed!")
    if not res_lphbc:
        allsuccess = False
        print("\t Login-page home button test failed!")
    if not res_lpsulc:
        allsuccess = False
        print("\t Login-page sign up link test failed!")
    if not res_lphlc:
        allsuccess = False
        print("\t Login-page help link test failed!")
    if not res_lppbc:
        allsuccess = False
        print("\t Login-page pass-hide button test failed!")
    if not res_inc:
        allsuccess = False
        print("\t Invalid input test failed!")
    for i in range(0, len(res_emc["invalid"])):
        if not res_emc["invalid"][i]:
            allsuccess = False
            print("\t Invalid email test %d failed!" % (i + 1))
    for i in range(0, len(res_emc["unregistered"])):
        if not res_emc["unregistered"][i]:
            allsuccess = False
            print("\t Unregistered email test %d failed!" % (i + 1))
    for i in range(0, len(res_emc["registered"])):
        if not res_emc["registered"][i]:
            allsuccess = False
            print("\t Registered email test %d failed!" % (i + 1))
    for i in range(0, len(res_phc["invalid"])):
        if not res_phc["invalid"][i]:
            allsuccess = False
            print("\t Invalid phone test %d failed!" % (i + 1))
    for i in range(0, len(res_phc["unregistered"])):
        if not res_phc["unregistered"][i]:
            allsuccess = False
            print("\t Unregistered phone test %d failed!" % (i + 1))
    for i in range(0, len(res_phc["registered"])):
        if not res_phc["registered"][i]:
            allsuccess = False
            print("\t Registered phone test %d failed!" % (i + 1))
    for i in range(0, len(res_pac["invalid"])):
        if not res_pac["invalid"][i]:
            allsuccess = False
            print("\t Invalid password test %d failed!" % (i + 1))
    for i in range(0, len(res_pac["unregistered"])):
        if not res_pac["unregistered"][i]:
            allsuccess = False
            print("\t Unregistered password test %d failed!" % (i + 1))
    for i in range(0, len(res_pac["registered"])):
        if not res_pac["registered"][i]:
            allsuccess = False
            print("\t Registered password test %d failed!" % (i + 1))
    if allsuccess:
        print("\t All tests successfully passed!")

if len(sys.argv) < 2:
    print("Please specify a default driver: Chrome/Firefox/Opera")
    sys.exit()

if sys.argv[1] == "Chrome":
    try:
        driver = webdriver.Chrome()
        driver_index = 0
    except SessionNotCreatedException:
        print("The specified browser executables not found! Please install or pick another driver")
        sys.exit()
    except WebDriverException:
        print("The specified driver not found! Please download or pick another driver")
        sys.exit()
elif sys.argv[1] == "Firefox":
    try:
        driver = webdriver.Firefox()
        driver_index = 1
    except SessionNotCreatedException:
        print("The specified browser executables not found! Please install or pick another driver")
        sys.exit()
    except WebDriverException:
        print("The specified driver not found! Please download or pick another driver")
        sys.exit()
elif sys.argv[1] == "Opera":
    try:
        driver = webdriver.Opera()
        driver_index = 2
    except SessionNotCreatedException:
        print("The specified browser executables not found! Please install or pick another driver")
        sys.exit()
    except WebDriverException:
        print("The specified driver not found! Please download or pick another driver")
        sys.exit()
else:
    print("Please specify the default driver correct! Chrome/Firefox/Opera")
    sys.exit()

url_path = "http://localhost:3000/"
login_route = "login"
log_enabled = True
skip = False
for i in range(0, 3):
    if not skip:
        res_spllc = signup_page_login_link_check()
        res_lphbc = login_page_home_button_check()
        res_lpsulc = login_page_sign_up_link_check()
        res_lphlc = login_page_help_link_check()
        res_lppbc = login_page_passhide_button_check()
        res_inc = input_check()
        res_emc = email_check()
        res_phc = phone_check()
        res_pac = pass_check()
        driver.close()
        if driver_index == 0:
            print("Chrome compatibility test:")
            compatibility_check()
        elif driver_index == 1:
            print("Firefox compatibility test:")
            compatibility_check()
        else:
            print("Opera compatibility test:")
            compatibility_check()

    driver_index +=1
    if driver_index == 3:
        driver_index = 0

    skip = False
    if not i == 2:
        if driver_index == 0:
            try:
                driver = webdriver.Chrome()
            except SessionNotCreatedException:
                print("Chrome compatibility test:", "Test Failed. Chrome executables not found")
                skip = True
            except WebDriverException:
                print("Chrome compatibility test:", "Test Failed. Chrome driver not found")
                skip = True
        elif driver_index == 1:
            try:
                driver = webdriver.Firefox()
            except SessionNotCreatedException:
                print("Firefox compatibility test:", "Test Failed. Firefox executables not found")
                skip = True
            except WebDriverException:
                print("Firefox compatibility test:", "Test Failed. Firefox driver not found")
                skip = True
        else:
            try:
                driver = webdriver.Opera()
            except SessionNotCreatedException:
                print("Opera compatibility test:", "Test Failed. Opera executables not found")
                skip = True
            except WebDriverException:
                print("Opera compatibility test:", "Test Failed. Opera driver not found")
                skip = True
        log_enabled = False




