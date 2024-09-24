import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открытие первой страницы
driver.get("https://vk.com")
time.sleep(5)  # Пауза для загрузки страницы

# Получение и вывод title страницы
current_title = driver.title
print("Текущий заголовок страницы VK:", current_title)

# Открытие второй страницы
driver.get("https://ya.ru")
time.sleep(5)  # Пауза для загрузки страницы

# Получение и вывод title страницы
current_title = driver.title
print("Текущий заголовок страницы Яндекса:", current_title)

# Обратная навигация
driver.back()
time.sleep(5)  # Пауза для обработки команды

# Проверка текущего заголовка страницы после возврата
assert driver.title == 'ВКонтакте | Добро пожаловать', "Некорректное возвращение назад"

# Обновление текущей страницы
driver.refresh()
time.sleep(5)  # Пауза для обновления страницы

# Получение и вывод URL-адреса текущей страницы
url = driver.current_url
print("URL текущей страницы:", url)

# Переход вперед на предыдущую страницу
driver.forward()
time.sleep(5)  # Пауза для обработки команды

# Проверка, что URL-адрес изменился
new_url = driver.current_url
assert new_url != url, "URL не изменился после перехода вперед"

# Закрытие браузера
driver.quit()