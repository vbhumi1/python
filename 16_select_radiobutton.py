from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.toolsqa.com/automation-practice-form/')
driver.execute_script('window.scrollTo(0,900)')

driver.find_element_by_id('sex-0').click()

driver.close()
