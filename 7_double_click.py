from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://demo.guru99.com/test/simple_context_menu.html")

# To move cursor on specified element and click

time.sleep(4)
actions = ActionChains(driver)
obj = driver.find_element_by_xpath('//*[@id="authentication"]/button')
actions.move_to_element(obj)
time.sleep(2)
actions.double_click()
actions.perform()
time.sleep(4)
driver.close()