from selenium import webdriver
import time

driver =webdriver.Chrome()

driver.get("https://www.python.org/")

# To get text based on xpath
text = driver.find_element_by_xpath('//*[@id="downloads"]/a').text
print(text)

# To verify text is expected or not

if text != 'Downloads': raise AssertionError('Text is not expected')

assert text == 'Downloads',  'Text is not expected'

driver.close()