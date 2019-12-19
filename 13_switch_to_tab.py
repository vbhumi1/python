from selenium import webdriver
import time

driver= webdriver.Chrome()

driver.get('https://www.pylint.org/')
time.sleep(4)
# To open new window
driver.execute_script('window.open("https://www.google.com")')
time.sleep(4)
driver.execute_script('window.open("http://robotframework.org/")')

# To handle all windows tabs

windows = driver.window_handles
print(windows)
print("titlename: ",driver.title)
time.sleep(4)

driver.switch_to.window(windows[1])
time.sleep(4)
print("new tab title:",driver.title)

driver.switch_to.window(windows[2])
time.sleep(4)
print("new second tab:", driver.title)

driver.switch_to.window(windows[0])
print(driver.title)

driver.close()