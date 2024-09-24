import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
user_1 = webdriver.Chrome(options=options)

LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")

user_1.get("https://hyperskill.org/login")

user_1.find_element(*LOGIN_FIELD).send_keys("aleksei@ya.ru")
user_1.find_element(*PASSWORD_FIELD).send_keys("Qwerty1321!")
user_1.find_element(*SUBMIT_BUTTON).click()
time.sleep(5)
user_1.close()

user_2 = webdriver.Chrome(options=options)
user_2.get("https://hyperskill.org/login")

time.sleep(5)
