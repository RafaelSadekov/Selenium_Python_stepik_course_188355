from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Импортируем By

# Инициализация веб-драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие первой страницы
driver.get("https://hyperskill.org/login")
time.sleep(2)

# Открытие второй вкладки и переход на VK
driver.switch_to.new_window("tab")
driver.get("https://www.vk.ru/")
time.sleep(2)

# Открытие третьей вкладки и переход на Яндекс
driver.switch_to.new_window("tab")
driver.get("https://www.ya.ru/")
time.sleep(2)

# Получаем все открытые вкладки (handle'ы)
tabs = driver.window_handles

# Переход на каждую вкладку, кликаем на конкретные кнопки и выводим заголовок
# Вкладка 1 - Hyperskill
driver.switch_to.window(tabs[0])
title = driver.title
print(f"Вкладка 1: {title}")
try:
    hyperskill_button = driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/div/ul[1]/li[2]/a')  # Кнопка на Hyperskill
    hyperskill_button.click()
    print("Клик на кнопке в вкладке 1")
except Exception as e:
    print(f"Ошибка при клике на кнопке в вкладке 1: {str(e)}")

# Вкладка 2 - VK
driver.switch_to.window(tabs[1])
title = driver.title
print(f"Вкладка 2: {title}")
try:
    vk_button = driver.find_element(By.XPATH, '//*[@id="bottom_nav"]/div[2]/a[3]')  # Кнопка на VK
    vk_button.click()
    print("Клик на кнопке в вкладке 2")
except Exception as e:
    print(f"Ошибка при клике на кнопке в вкладке 2: {str(e)}")

# Вкладка 3 - Яндекс
driver.switch_to.window(tabs[2])
title = driver.title
print(f"Вкладка 3: {title}")
try:
    ya_button = driver.find_element(By.XPATH, '/html/body/main/div[3]/aside/section/div[1]/a/span')  # Кнопка на Яндекс
    ya_button.click()
    print("Клик на кнопке в вкладке 3")
except Exception as e:
    print(f"Ошибка при клике на кнопке в вкладке 3: {str(e)}")

# Закрываем браузер
time.sleep(2)
driver.quit()
