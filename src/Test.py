from os import getcwd
from selenium import webdriver

def home_button_check():
    pass

def help_button_check():
    pass

def signupnow_button_check():
    pass

def passhide_button_check():
    pass

def email_check():
    invalid_check_cases = ["admin.tr", "invalid_email"]
    unregistered_check_cases = ["burak.mutlu@gmail.com", "oguzhan.angin@gmail.com", "nursu.savaskan@gmail.com", "rabia.onal@gmail.com"]
    #registered_check_cases = ["", "",]
    email_input = driver.find_element_by_id("email")
    for case in check_cases:
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


