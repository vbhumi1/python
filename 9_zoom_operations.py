from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("http://selenium-python.readthedocs.io/")
time.sleep(4)

# To zoom in and zoom out webpage
driver.execute_script("document.body.style.zoom='200%'")
time.sleep(5)
driver.execute_script("document.body.style.zoom='100%'")
time.sleep(3)
driver.close()


