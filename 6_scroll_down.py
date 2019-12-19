from selenium import webdriver
import time

d = webdriver.Chrome()
d.maximize_window()

d.get("https://www.citibank.co.in/ibank/login/IQPin1.jsp?dOfferCode=LOANONCRED")

time.sleep(3)
# to scroll down 
d.execute_script("window.scrollTo(0,200)")
time.sleep(3)

d.execute_script("window.scrollTo(200,500)")
time.sleep(3)

# To scroll up
d.execute_script("window.scrollTo(500,0)")
time.sleep(3)

d.close()