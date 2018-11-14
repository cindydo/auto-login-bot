# author: Cindy Do
# date: 2018-11-14
# description: a basic Python script for automating website login (utilizing Selenium and ChromeDriver).
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# constants

# username
LOGIN_USERNAME = 'username'
# password
LOGIN_PASSWORD = 'password'
# login url
LOGIN_URL = 'https://www.yourwebsitelogin.com'
# username input ID
USERNAME_ID = 'usernameInputId'
# password input ID
PASSWORD_ID = 'passwordInputId'
# login button ID
LOGIN_BUTTON_ID = 'loginButtonId'
# login timeout
LOGIN_TIMEOUT = 600

# open a web browser and navigate to login page

browser = webdriver.Chrome()
browser.get((LOGIN_URL))

# enter username

username = browser.find_element_by_id(USERNAME_ID)
username.send_keys(LOGIN_USERNAME)

# enter password

password = browser.find_element_by_id(PASSWORD_ID)
password.send_keys(LOGIN_PASSWORD)

# sign in

signInButton = browser.find_element_by_id(LOGIN_BUTTON_ID)
signInButton.click()

# wait for successful login (including max. wait time)

try:
	WebDriverWait(browser, LOGIN_TIMEOUT).until_not(EC.url_to_be(LOGIN_URL))
except TimeoutException as ex:
	print(str(ex))