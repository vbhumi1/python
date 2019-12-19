from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.toolsqa.com/automation-practice-form/')

driver.execute_script('window.scrollTo(0,1000)')
time.sleep(4)

obj = driver.find_element_by_id('profession-1')
obj.click()

time.sleep(4)

driver.close()