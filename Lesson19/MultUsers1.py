import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Функция для логина
def login(driver, email, password):
    # Локаторы для полей логина, пароля и кнопки входа
    LOGIN_FIELD = (By.XPATH, "//input[@type='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@type='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")

    # Переход на страницу логина
    driver.get("https://hyperskill.org/login")

    # Ожидание, пока элемент логина не станет доступным, затем ввод email и пароля
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(LOGIN_FIELD)).send_keys(email)
    driver.find_element(*PASSWORD_FIELD).send_keys(password)
    driver.find_element(*SUBMIT_BUTTON).click()

# Настройки Chrome
options = Options()
options.add_argument("--window-size=1920,1080")  # Установка размера окна

# Логин для первого пользователя
user_1 = webdriver.Chrome(options=options)
login(user_1, "aleksei@ya.ru", "Qwerty1321!")
time.sleep(5)  # Ожидание 5 секунд для завершения загрузки страницы
user_1.quit()  # Закрытие браузера полностью

# Действия для второго пользователя (переход на страницу без логина)
user_2 = webdriver.Chrome(options=options)
user_2.get("https://hyperskill.org/login")
time.sleep(5)  # Ожидание 5 секунд для просмотра страницы
user_2.quit()  # Закрытие браузера полностью
