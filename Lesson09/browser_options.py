import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Опции браузера - это по сути его настройки перед запуском (возможности браузера), в будущем, мы разберем много разных опций, но начнем с самых распространенных.

options = webdriver.ChromeOptions()
options.add_argument("--headless") # запускает браузер в режиме без графического интерфейса. 
options.add_argument("--incognito") #  запускает браузер в режиме инкогнито (приватного просмотра). Это позволяет тестировать поведение сайта без использования кэша и сохраненных данных.
options.add_argument("--ignore-certificate-errors") # игнорирует ошибки сертификата SSL при загрузке защищенных (HTTPS) страниц.
options.add_argument("--window-size=X,Y") # устанавливает размер окна браузера. Можно указать ширину и высоту в пикселях. Например, --window-size=1280,800.
options.add_argument("--disable-cache") # отключает кэширование в браузере. Это позволяет загружать каждый ресурс (например, изображения, стили, скрипты) с сервера при каждой загрузке страницы.
options.add_argument("--start-maximized") # запускаем браузер в полноэкранном режимерно из-за того, что мы хотим запустить браузер в полноэкранном режиме.
options.add_argument("--disable-notifications") # отключаем всплывающие подсказки.  
options.add_argument("--disable-extensions")    # отключаем расширения, которые могут нам помешаться при запуске браузера.
options.add_argument("--disable-gpu") # отключаем графический интерфейс браузера.
options.add_argument("--disable-infobars") # отключаем всплывающие подсказки.
options.add_argument("--disable-popup-blocking") # отключаем всплывающие подсказки.
options.add_argument("--disable-notifications") # отключаем всплывающие подсказки.
# переопределяет стратегию загрузки страницы. Возможны следующие стратегии: 'eager', 'normal', 'none'.
options.page_load_strategy = 'normal' # используется по дефолту и ожидает загрузки всех ресурсов (картинки, js-код, шрифты и т.д) на странице.
options.page_load_strategy = 'eager' # ожидает только готовности загрузки DOM (html-структуры), но при этом картинки и прочее может до сих пор грузиться.
options.page_load_strategy = 'none' # Вообще ничего не ждет


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)