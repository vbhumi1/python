from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://www.toolsqa.com/automation-practice-form/')

driver.execute_script("window.scrollTo(0,1000)")
time.sleep(2)
# To check radio button is enabled or not
# rb = driver.find_element_by_id("sex-0").is_selected()
# time.sleep(4)
# print('\n:', rb)
# if not rb: driver.find_element_by_id('sex-0').click()

# To check checkbox is clicked or not

obj = driver.find_element_by_id('tool-0')
status = obj.is_selected()
print(' \n\n Check Box :', status)
if not status: obj.click()

driver.close()