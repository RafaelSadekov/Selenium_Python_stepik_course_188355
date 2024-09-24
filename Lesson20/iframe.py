import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=options)

#locator
FROM_NAME_FIELD_LOCATOR = ("xpath", "//*[@id='from-name']")
COPY_TEXT_FIELD_LOCATOR = ("xpath", "//button[text()='Copy Text']")

driver.get("https://testautomationpractice.blogspot.com")
driver.switch_to.frame()
time.sleep(2)
driver.find_element(*FROM_NAME_FIELD_LOCATOR).send_keys("Test")
time.sleep(2)
driver.find_element(*COPY_TEXT_FIELD_LOCATOR).click()
time.sleep(2)