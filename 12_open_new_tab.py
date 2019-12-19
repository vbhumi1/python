from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://selenium-python.readthedocs.io/")
time.sleep(4)
# To open new tab
driver.execute_script("window.open()")
time.sleep(4)
# If you open new tab but control is on first tab only
driver.execute_script("window.open('https://www.pylint.org/','_current')")
time.sleep(4)

driver.close()