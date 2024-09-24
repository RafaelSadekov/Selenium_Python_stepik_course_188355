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

LEFT_CLICK_BUTTON_LOCATOR = ()
DOUBLE_CLICK_BUTTON_LOCATOR = ()
RIGHT_CLICK_BUTTON_LOCATOR = ()
HOVER_BUTTON_LOCATOR = ()

driver.get("https://demoqa.com/buttons")

left_button = driver.find_element(*LEFT_CLICK_BUTTON_LOCATOR)
double_button = driver.find_element(*DOUBLE_CLICK_BUTTON_LOCATOR)
right_button = driver.find_element(*RIGHT_CLICK_BUTTON_LOCATOR)
hover_button = driver.find_element(*HOVER_BUTTON_LOCATOR)

action.move_to_element(left_button).perform()
action.move_to_element(double_button).perform()
action.move_to_element(right_button).perform()

action.click(left_button).pause(2).double_click(double_button).context_click(right_button).perform()
# Для двойной клика, action использует метод double_click()
# Для клика правой кнопкой мыши action использует метод context_click()
# там где нужно подождать, мы вызываем метод pause(время) 

driver.get("https://www.google.com/")

MENU_ITEM_LOCATOR = ()
SUB_LIST_LOCATOR = ()

menu_item = driver.find_element(*MENU_ITEM_LOCATOR)
sub_list = driver.find_element(*SUB_LIST_LOCATOR)

# Для наведения на элемент, action использует метод move_to_element(), 
# где в качестве аргумента принимает веб-элемент для наведения.

action.move_to_element(menu_item) \
    .pause(2) \
    .move_to_element(sub_list) \
    .perform()


# Вариант 1
actions = ActionChains(driver)
actions.move_to_element(web_element1)
actions.click(web_element2)
actions.perform()
# Вариант 2
(
    actions.move_to_element(web_element1)
    .click(web_element2)
    .perform()
)

# Зачастую нам необходимо сначала сделать скролл к элементу, 
# чтобы при попытке взаимодействия с ним не получать разного рода ошибки
# Для этого у action есть метод scroll_to_element()

driver.get("https://clipboardjs.com/")

SOME_ELEMENT_LOCATOR = ("xpath", "//button[@data-clipboard-target='#bar']")

SOME_ELEMENT = driver.find_element(*SOME_ELEMENT_LOCATOR)

action.scroll_to_element(SOME_ELEMENT).perform() # Используем скролл до элемента