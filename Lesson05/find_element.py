import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Переход на нужную страницу
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(3)

try:
    # Найти иконку Wikipedia по имени класса
    wiki_icon = driver.find_element(By.CLASS_NAME, 'wikipedia-icon')
except Exception as e:
    print(f"Ошибка при поиске иконки: {e}")

try:
    # Найти поле ввода Wikipedia по ID
    input_field = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
except Exception as e:
    print(f"Ошибка при поиске поля ввода: {e}")

try:
    # Найти кнопку поиска Wikipedia по классу
    search_button = driver.find_element(By.CLASS_NAME, 'wikipedia-search-button')
except Exception as e:
    print(f"Ошибка при поиске кнопки: {e}")

try:
    # Найти любой другой элемент на странице по тегу
    any_element = driver.find_elements(By.TAG_NAME, 'h1')
except Exception as e:
    print(f"Ошибка при поиске тега: {e}")

# Закрытие браузера
driver.quit()