from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_extension(r'C:\Users\User\Desktop\extechions.crx')
driver = webdriver.Chrome(options=options)

driver.get('https://www.google.com')
time.sleep(2)
