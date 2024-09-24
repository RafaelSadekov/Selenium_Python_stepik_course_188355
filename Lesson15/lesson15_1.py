from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Initialize driver service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Define wait
wait = WebDriverWait(driver, 10)

# Navigate to the demo page
driver.get('https://demoqa.com/selectable')

# Wait and click the "Grid" tab
GRID = (By.XPATH, "//a[@id='demo-tab-grid']")
wait.until(EC.element_to_be_clickable(GRID)).click()

# Verify that the tab is selected
assert driver.find_element(*GRID).get_attribute('aria-selected') == 'true'

# Define the items in the grid
ONE = (By.XPATH, "//li[text()='One']")
TWO = (By.XPATH, "//li[text()='Two']")
NINE = (By.XPATH, "//li[text()='Nine']")

# Click on the items and assert their 'active' class
for item in [ONE, TWO, NINE]:
    driver.find_element(*item).click()
    assert "active" in driver.find_element(*item).get_attribute("class"), f"Item {item[1]} not selected."

# Print the class attributes
print(driver.find_element(*ONE).get_attribute("class"))
print(driver.find_element(*TWO).get_attribute("class"))
print(driver.find_element(*NINE).get_attribute("class"))

time.sleep(2)

# Unselect the items
for item in [ONE, TWO, NINE]:
    driver.find_element(*item).click()
    assert "active" not in driver.find_element(*item).get_attribute("class"), f"Item {item[1]} still selected."

# Print the class attributes again
print(driver.find_element(*ONE).get_attribute("class"))
print(driver.find_element(*TWO).get_attribute("class"))
print(driver.find_element(*NINE).get_attribute("class"))

time.sleep(2)

# Quit the driver
driver.quit()
