from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get('https://www.google.com/')
time.sleep(4)

# Using link_text locator
# link_text = driver.find_element_by_link_text('Images')
# link_text.click()

# Using partial_link_text
# partial_link_text = driver.find_element_by_partial_link_text('Ima')
# partial_link_text.click()

#Using class_name locator
# class_name = driver.find_element_by_class_name('gb_g')
# class_name.click()

# Using tag_name locator
tag_name = driver.find_element_by_tag_name('a') # If duplicate tag name is there it will take first tag name
print(tag_name)
tag_name.click()
