import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys


options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Automation QA (Windows NT 6.1; rv:106.0) Gecko/20100101 Firefox/106.0")
options.page_load_strategy = "normal"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("http://the-internet.herokuapp.com/dropdown") # Страница для работы

DROPDOWN_ELEMENT = ("xpath", "//select[@id='dropdown']")
DROPDOWN = Select(driver.find_element(*DROPDOWN_ELEMENT))

driver.get("https://demoqa.com/select-menu")

DROPDOWN_LOCATOR = ("xpath", "//select[@id='oldSelectMenu']")

DROPDOWN = Select(driver.find_element(*DROPDOWN_LOCATOR)) 

all_options = DROPDOWN.options # Запишем все элементы выпадающего списка

for option in all_options: # Перебор элементов по тексту 
    time.sleep(1)
    DROPDOWN.select_by_visible_text(option.text)

for option in all_options: # Перебор элементов по индексу 
    time.sleep(1)
    DROPDOWN.select_by_index(all_options.index(option))

for option in all_options: # Перебор элементов по value 
    time.sleep(1)
    DROPDOWN.select_by_value(option.get_attribute("value"))

#-----------------------------------------------------------------------------------------------------

from selenium.webdriver import Keys


driver.get("http://the-internet.herokuapp.com/key_presses") # Сайт для работы

KEY_PRESS_INPUT = ("xpath", "//input[@id='target']") # Поле ввода

driver.find_element(*KEY_PRESS_INPUT).send_keys("Hello World") # Ввод текста

driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.COMMAND + "A") # Выделение всего текста

driver.find_element(*KEY_PRESS_INPUT).send_keys(Keys.BACKSPACE) # Удаление выделенного текста

#-----------------------------------------------------------------------------------------------------

# При ее использование будет проверятся система на которой запускается код, и в соответствии с этим будет вызываться либо CONTROL, либо СOMMAND.

import platform

os_name = platform.system()
CMD_CTRL = Keys.COMMAND if os_name == "Darwin" else Keys.CONTROL

driver = webdriver.Chrome()
driver.find_element().send_keys(CMD_CTRL + "A") # Использование

# Копирование и вставка -------------------------------------------------------------------------------

driver.get("https://clipboardjs.com/")

COPY_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")
PASTE_LOCATOR = ("xpath", "//textarea[@id='bar']")

COPY = driver.find_element(*COPY_LOCATOR)
PASTE = driver.find_element(*PASTE_LOCATOR)

PASTE.send_keys(cmd_ctrl + "A") # Выделим все внутри поля
time.sleep(2)
PASTE.send_keys(cmd_ctrl + "X") # Вырежем весь текст
time.sleep(2)
PASTE.send_keys(cmd_ctrl + "V") # Вставим весь текст

# Клик напрямую
# Просто находим элемент внутри (по тексту, да как хотим) и кликаем на него. Полный алгоритм будем следующим:

driver.get("https://demoqa.com/select-menu")

driver.find_element("xpath", "//div[@id='withOptGroup']").click() # Открываем dropdown

driver.find_element("xpath", "//div[@id='withOptGroup']//div[text()='A root option']").click() # Кликаем на элемент внутри

# Создать универсальную функцию для выборки элемента из нашего dropdown

driver.get("https://demoqa.com/select-menu")

driver.find_element("xpath", "//div[@id='withOptGroup']").click() # Открываем dropdown

def choose_dropwdown_element_by_text(text): # Будем искать элемент внутри dropdown по тексту
    elements = driver.find_elements("xpath", "//div[@id='withOptGroup']//div[contains(@id, 'react-select')]")
    for element in elements:
        if text in element.text:
            return element # Возвращаем нужный элемент из dropdown по тексту

choose_dropwdown_element_by_text("Another root option").click() # Кликаем на выбранный элемент

# Работа с мультиселектом -------------------------------------------------------------------------------

driver.get("https://demoqa.com/select-menu")

MULTISELECT = ("xpath", "//input[@id='react-select-4-input']")

driver.find_element(*MULTISELECT).send_keys("Gre")

assert driver.find_element(*MULTISELECT).get_attribute("value") == "Gre", "Текст не введен"

driver.find_element(*MULTISELECT).send_keys(Keys.TAB)