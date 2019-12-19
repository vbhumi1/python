from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://selenium-python.readthedocs.io/")

# To set window position
driver.set_window_position(200,500)
time.sleep(4)

print(driver.get_window_position())
time.sleep(4)
driver.close()