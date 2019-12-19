from selenium import webdriver
import time

# To open a browser
driver = webdriver.Chrome()

# To maximize window
driver.maximize_window()
time.sleep(2)

# To open URL
driver.get('https://accounts.google.com')

# To enter username based on id locator
uname = driver.find_element_by_id('identifierId')
uname.send_keys("vijayseeyou")

# To click on next button after entering gmail id
unext = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
unext.click()
time.sleep(3)

# To enter password based on name

driver.find_element_by_name('password').send_keys('Virps143@')
time.sleep(5)

# To click on next button after entering password
driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
time.sleep(5)

# To close browser
driver.close()