import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1) # Создаем обьект ожиданий
action = ActionChains(driver) # Создаем обьект action

driver.get("https://demoqa.com/droppable")

COLLUMN_LOCATOR_A = ("xpath", "//div[@id='draggable']") 
COLLUMN_LOCATOR_B = ("xpath", "//div[@id='droppable']")

A = driver.find_element(*COLLUMN_LOCATOR_A)
B = driver.find_element(*COLLUMN_LOCATOR_B)

time.sleep(2)

action.drag_and_drop(A, B).perform()

time.sleep(2)

driver.get("https://tympanus.net/Development/DragDropInteractions/index.html")

GRID_LOCATOR = ("xpath", "//div[@class='grid__item'][7]")
SIDEBAR_ITEM_LOCATOR = ("xpath", "//div[@class='drop-area__item'][2]")

action.click_and_hold(driver.find_element(*GRID_LOCATOR)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR_ITEM_LOCATOR)) \
    .release() \
    .perform()

time.sleep(2)


# Реализуем саму функцию, она будет принимать в себя 2 локатора и 
# перетаскивать элементы:

driver.get("https://demoqa.com/sortable")

SOURCE_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[1]")
TARGET_LOCATOR = ("xpath", "//div[contains(@class, 'vertical-list')]/div[5]")

def drag_and_drop(source, target):
    SOURCE = driver.find_element(*source) # Находим source-элемент
    TARGET = driver.find_element(*target) # Находим target-элемент
    wait.until(EC.element_to_be_clickable(SOURCE)) # Ждем кликабельности source-элемента
    action.drag_and_drop(SOURCE, TARGET).perform() # Перетаскиваем

drag_and_drop(SOURCE_LOCATOR, TARGET_LOCATOR) # Использование функции

