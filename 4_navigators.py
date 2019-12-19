from selenium import webdriver
import time

driver = webdriver.Chrome()

# To open URL
driver.get('https://www.python.org/')

time.sleep(4)

# To click on downloads by using xpath locator
driver.find_element_by_xpath('//*[@id="downloads"]/a').click()

time.sleep(5)
# Navigate back to python page
driver.back()

time.sleep(4)
# Navigate forward to downloads page
driver.forward()

driver.close()