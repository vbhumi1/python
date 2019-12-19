from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\Users\Vijay\Desktop\Python Final\Selenium\alert_2.html')

driver.find_element_by_xpath('/html/body/button').click()
alert= driver.switch_to.alert

# print(alert.text)

# To accept alerts
alert.accept()

# alert.accept() - To accept the alert
# alert.dismiss() - To decline the alert
# alert.send_keys('vijay') - To enter a value in the alert text box

"""
Link for all alerts

https://www.techbeamers.com/handle-alert-popup-selenium-python/

"""
driver.close()

