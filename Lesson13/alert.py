import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get 

# Клик на кнопку, которая вызывает alert
BUTTOM = ("xpath", "//button[@type="button"]")
wait.until(EC.element_to_be_clickable(BUTTOM)).click()
# Ожидание появления alert и запись его в переменную для дальнейшего взаимодействия
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert # Переключение на alert
time.sleep(1)
alert.accept()

driver.get 
BUTTOM_2 = ("xpath", "//button[@type="button"]")
wait.until(EC.element_to_be_clickable(BUTTOM)).click()
alert = wait.until(EC.alert_is_present())
driver.switch_to.alert # Переключение на alert
time.sleep(1)
# ок 
alert.accept()
# или отмена
alert.dismiss()

# Клик на кнопку, которая вызывает alert
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

print(alert.text) # Вывод текста из алерта

# Клик на кнопку, которая вызывает alert
BUTTON_4 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_4)).click()

alert = wait.until(EC.alert_is_present())

driver.switch_to.alert

# Ввод данных в alert
alert.send_keys("Hello world")

# Обязательно либо примите либо отклоните alert после вводад анных
alert.accept()