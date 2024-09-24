import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

#     Задание 1:

# Заполнить все текстовые поля данными (почистить поля перед заполнением).
# Проверить, что данные действительно введены, используя get_attribute() и assert.
# Страница для выполнения задания: https://demoqa.com/text-box

driver.get("https://demoqa.com/text-box")

user_name_element = driver.find_element('xpath', '//input[@id="userName"]')
user_email_element = driver.find_element('xpath', "//input[@type='email']")
current_address_element = driver.find_element('xpath', "//textarea[@placeholder='Current Address']")
permanent_address_element = driver.find_element('xpath', "//textarea[@id='permanentAddress']")

user_name_element.clear()
user_email_element.clear()
current_address_element.clear()
permanent_address_element.clear()

assert user_name_element.get_attribute('value') == "", "Поле 'userName' не пустое"
assert user_email_element.get_attribute('value') == "", "Поле 'userEmail' не пустое"
assert current_address_element.get_attribute('value') == "", "Поле 'currentAddress' не пустое"
assert permanent_address_element.get_attribute('value') == "", "Поле 'permanentAddress' не пустое"

user_name_element.send_keys("John")
user_email_element.send_keys("john@gmail.com")
current_address_element.send_keys("Moscow")
permanent_address_element.send_keys("Moscow2")

user_name_element_value = user_name_element.get_attribute('value')
user_email_element_value = user_email_element.get_attribute('value')
current_address_element_value = current_address_element.get_attribute('value')
permanent_address_element_value = permanent_address_element.get_attribute('value')

assert user_name_element_value == "John", "Пользователь не найден"
assert user_email_element_value == "john@gmail.com", "Пользователь не найден"
assert current_address_element_value == "Moscow", "Пользователь не найден"
assert permanent_address_element_value == "Moscow2", "Пользователь не найден"
print("Пользователь найден")

time.sleep(2)
driver.quit()

# Задание 2:

# Прокликать все ссылки со статус-кодами на странице, используя алгоритм перебора элементов.
# После каждого клика возвращаться на стартовую страницу.
# Страница для выполнения задания: http://the-internet.herokuapp.com/status_codes

driver.get("https://the-internet.herokuapp.com/status_codes")
status_codes = driver.find_elements('xpath', "(//li/a)")
for codes in status_codes:
    codes.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)
