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
driver.get_cookie("name") # Вернет куку name или любую другую указанную в качестве аргумента
driver.get_cookies() # Вернет список словарей, все куки

driver.get("https://www.freeconferencecall.com/en/us/login")
driver.get_cookies()

driver.add_cookie({
    'name': 'Example', 
    'value': 'Kukushka'
})
print(driver.get_cookie("Example"))

# Тут все аналогично добавлению, просто перед добавлением удаляйте старую куку, 
# используя либо метод delete_cookie("name") для удаления определенной куки, 
# либо delete_all_cookies() для удаления вообще всех куков.

driver.delete_cookie("Example")
driver.add_cookie({
    'name': 'Example',
    'value': 'More'
})

# Для работы с куками, существует специальная библиотека pickle, 
# давайте для начала ее импортируем.

import pickle
# Для начала необходимо залогиниться в какой-либо аккаунт, 
# возьмем все тот же сайт https://www.freeconferencecall.com/en/us/login 
# для примера. Предварительно создав там аккаунт.

driver.get("https://www.freeconferencecall.com/en/us/login")

LOGIN_FIELD = ("xpath", "//input[@id='login_email']")
PASSWORD_FIELD = ("xpath", "//input[@id='password']")
SUBMIT_BUTTON = ("xpath", "//button[@id='loginformsubmit']")

# Логинимся в аккаунт
driver.get("https://www.freeconferencecall.com/en/us/login")
driver.find_element(*LOGIN_FIELD).send_keys("autocheck@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("123")
driver.find_element(*SUBMIT_BUTTON).click()
# После, мы сохраним куки в файл, он должен быть специального
# формата .pkl так как это наиболее корректный способ хранения куков.

# Создадим в проекте папку /cookies и уже в ней автоматически
#  будет создаваться файл с куками cookies.pkl (называйте как угодно)
pickle.dump(driver.get_cookies(), open(os.getcwd() + "/cookies/cookies.pkl", "wb"))

# переиспользовать куки, чтобы больше не вводить каждый раз логин и пароль.

# Открываем страницу логина
driver.get("https://www.freeconferencecall.com/profile")

# Чистим все куки
driver.delete_all_cookies()

# Записываем куки из файла в переменную
cookies = pickle.load(open(os.getcwd()+"/cookies/cookies.pkl", "rb"))

# Добавляем по одной куке из списка
for cookie in cookies:
    driver.add_cookie(cookie)

# Делаем запрос на любую страницу залогиненного пользователя
driver.get("https://www.freeconferencecall.com/profile")