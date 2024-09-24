import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Задание 1. Загрузить любой файл в 'Choose File'.
# Страница для выполнения задания: https://demoqa.com/upload-download
options = webdriver.ChromeOptions()
prefs = {
    "download.default.directory_upgrade": os.getcwd() + "\\downloads",
    "safebrowsing.enabled" : True
        }
# # При настройке "safebrowsing.enabled" : False - нет лишних окон.
# # При настройке "safebrowsing.enabled" : True - нет лишних окон.
# # Но... при настройке "safebrowsing.enabled" : False - мы получим частично загруженные файлы (.crdownload):
# # 5mb script.xml и data.js - Chrome блокирует их скачивание, т.к. безопасный просмотр отключен.
# # А при настройке "safebrowsing.enabled" : True - все файлы будут проверены и могут быть полностью загружены.
# # Чтобы научиться правильно и полностью скачивать файлы проверяйте, как минимум, в папке downloads наличие файлов с расширением .crdownload.
# # Проход кликом по всем ссылкам вовсе не означает, что все эти файлы будут обязательно загружены.

options.add_experimental_option("prefs", prefs)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://demoqa.com/upload-download")
# time.sleep(2)

# driver.find_element('xpath', "//input[@type='file']").send_keys(os.getcwd() + "\\stepik1\\downloads\\sampleFile.jpeg")
# # Нет необходимости в таймерах, так как ожидание завершения загрузки уже заложено в Selenium.
# driver.implicitly_wait(2)  # Дополнительная защита от сбоев
# driver.close()


driver.get('https://the-internet.herokuapp.com/download')
ref_lst = driver.find_elements('xpath', '//a')
for ref in ref_lst[1:-1]:
    print(f'Downloading:  {ref.get_attribute("href")}')
    ref.click()
time.sleep(5)

