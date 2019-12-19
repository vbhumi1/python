from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.toolsqa.com/automation-practice-form/')
time.sleep(4)
drop = Select(driver.find_element_by_id('continents'))

# Select based on value
# drop.select_by_value('EU')

# Select based on visible text
drop.select_by_visible_text("Europe")

# Select based on index
# drop.select_by_index(2)

driver.close()