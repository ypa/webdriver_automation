from selenium import webdriver

driver = webdriver.Firefox()

def login(email, pwd):
    """login function"""
    driver.get("http://www.cramster.com")
    login = driver.find_element_by_id("header-login")
    login.find_element_by_name("email").send_keys(email)
    while 1:
        login.find_element_by_name("password").clear()
        login.find_element_by_name("password").send_keys(pwd)
        if login.find_element_by_name("password").value != '' :
            break
    login.find_element_by_name("password").submit()

def check_upgrade_button():
    """verify that Upgrade button is available"""
    try:
        upgrade = driver.find_element_by_link_text("Upgrade Now!")
        upgrade.click()
    except:
        print "Upgrade Now! button is not available."

if __name__ == "__main__":
    login("yan.pye.aung@gmail.com", "abcdabcd")
    check_upgrade_button()
