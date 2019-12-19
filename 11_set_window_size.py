from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
# To get indow size
print(driver.get_window_size())
driver.get("http://selenium-python.readthedocs.io/")

time.sleep(4)
# To set the window size
driver.set_window_size(100,500)
print(driver.get_window_size())
time.sleep(4)
# To set window position
driver.set_window_position(100,650)
time.sleep(4)
print(driver.get_window_size())
time.sleep(4)
driver.close()
