from selenium import webdriver

driver=webdriver.Chrome()

# To maximize window
driver.maximize_window()
driver.get('https:\\www.google.com')

# If u want save screenshot in current folder
driver.save_screenshot('vijay.png')

# If u want to save screenshot in different folder

driver.save_screenshot(r'C:\Users\Vijay\Desktop\Python World\SELENIUM\vijay.png')

driver.close()