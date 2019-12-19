from selenium import webdriver
import time

d = webdriver.Chrome()

d.get('https://www.python.org/')

time.sleep(5)
d.refresh()
time.sleep(2)
d.refresh()

d.close()