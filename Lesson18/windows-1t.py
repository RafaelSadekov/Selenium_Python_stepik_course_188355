import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


Options = Options()
Options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=Options)

driver.get("https://hyperskill.org/login")

# Клик по кнопке, которая открывает новую вкладку
FOR_BUSINESS_BUTTON = ("xpath", "//a[text()=' For Business ']")
driver.find_element(*FOR_BUSINESS_BUTTON).click()

# Дескриптор - это по сути уникальный идентификатор, который сохраняется в течение одного сеанса.
current_tab = driver.current_window_handle
print(current_tab)
# В большинстве ситуаций, при работе с окнами, необходимо получать
#  все открытые в данный момент окна/вкладки, и сделать это можно обратившись к параметру window_handles.

windows_count = driver.window_handles # Записываем список открытых окон в переменную
print(windows_count) # Выводим на экран полученный список

# Переключение между вкладками
# Рассмотрим еще один пример и напишем следующее:

# Открыть какую-то базовую страницу
# Открыть несколько вкладок
# Получить их количество
# Получить дескриптор открытой вкладки
# Переключиться на любую вкладку используя ее индекс
# Проверить, что вкладка переключилась

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Открытие нескольких вкладок
driver.switch_to.new_window("tab")
driver.switch_to.new_window("tab")
time.sleep(2)

# Шаг 3 - Получение списка открытых вкладок
windows = driver.window_handles
print(len(windows)) # Выведем на экран кол-во открытых вкладок

# Шаг 4 - Получение дескриптора текущего окна для дальнейшей проверки
current_tab = driver.current_window_handle
print("Дескриптор текущей вкладки: ", current_tab)
print("Индекс: ", windows.index(current_tab)) # Получаем индекс вкладки в списке для информативности

# Шаг 5 - Переключение на вкладку по ее индексу
driver.switch_to.window(windows[1])
time.sleep(2)

# Шаг 6 - Проверка, что вкладка переключилась
assert current_tab != driver.current_window_handle, "Вкладка не переключилась"
# Таким образом мы можем переключаться между любым кол-вом вкладок.

# Переключение между окнами

# Шаг 1 - Открыть базовую страницу
driver.get("https://whatismyipaddress.com/")

# Шаг 2 - Получение дескриптора текущего окна
old_window = driver.current_window_handle
print("Дескриптор первого окна: ", old_window)

# Шаг 3 - Открытие и переключение на новое окно
driver.switch_to.new_window("window")

# Шаг 4 - Получение дескриптора нового окна
new_window = driver.current_window_handle
print("Дескриптор второго окна: ", new_window)

# Шаг 5 - Проверка, что окно переключилось
assert new_window == driver.current_window_handle, "Окно не переключилось"
time.sleep(2)

# Шаг 6 - Открытие страницы в новом окне
driver.get("https://vk.com")

# Шаг 7 - Переключение на старое окно
driver.switch_to.window(old_window)

# Шаг 8 - Проверка, что переключились на старое окно
assert old_window == driver.current_window_handle, "Окно не переключилось"

# Шаг 9 - Открытие страницы в старом окне
driver.get("https://ya.ru")

# Шаг 10 - Переключение на новое окно
driver.switch_to.window(new_window)

# Шаг 11 - Закрытие нового окна
driver.close()

# В Selenium существует два способа, чтобы закрыть окна или вкладки

driver.quit() # Закрытие сессии, т.е всего браузера
driver.close() # Закрытие активного окна / вкладки