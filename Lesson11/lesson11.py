from selenium import webdriver

driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 30)

driver.get('https://omayo.blogspot.com/')
#---------------------------------------------------------------------------
# 1 Дождитесь исчезновения текста This text will disappear
# 2 Дождитесь появления текста в элементе This text is displayed after 10 seconds of wait
# 3 Дождитесь состояния enabled Button 3
# 4 После клика дождитесь состояния disabled My button

#1
text_field1 = ("xpath", "//div[@id='deletesuccess']")
wait.until(EC.invisibility_of_element_located(text_field1), 'Текст не исчез')
print('1.passed')

#2
text_field2 = ("xpath", "//div[@id='delayedText']")
wait.until(EC.visibility_of_element_located(text_field2), 'Текст не появился')
print('2.passed')

#3
button3 = ("xpath", "//input[@id='timerButton']")
wait.until(EC.element_to_be_clickable(button3), 'Кнопка не активна')
print('3.passed')

#4
my_button = ("xpath", "//button[@id='myBtn']")
try_it_button = ("xpath", "//button[text()='Try it']")
wait.until(EC.element_to_be_clickable(try_it_button), 'Кнопка не кликабельна')
driver.find_element(*try_it_button).click()
wait.until(EC.element_attribute_to_include(my_button, 'disabled'), 'Кнопка осталось активной')
print('4.passed')
