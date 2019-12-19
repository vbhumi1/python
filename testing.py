from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com')

uname = driver.find_element_by_id('identifierId')
uname.click()
time.sleep(4)

# Relative xpath
unext = driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
unext.click()


driver.find_element_by_name('password').send_keys('password')

# To find text 
text = driver.find_element_by_xpath('//*[@id="downloads"]/a').text

# To verify text is expected or not

if text ! = 'Downloads' : raise AssertionError('Text is not expected')

assert text == 'Downloads', 'Text is not expected'
 
# To save screenshot on current directory
driver.save_screenshot('vijay.png') 

# To save screenshot on particular directory
driver.save_screenshot(r'C:\Users\Vijay\Desktop\Python World\SELENIUM\vijay.png')

# To navigate page to backward
driver.back()

# To navigate page to forward
driver.forward()

# To refresh the page
driver.refresh()

# To scroll down and scroll up
driver.execute_script('window.scrollTo(0,500)')  # To scroll down
driver.execute_script('window.scrollTo(500,0)')  # To scroll Up



# To double click 
from selenium.webdriver.common.action_chains import ActionChains
actions = ActionChains(driver)
obj= driver.find_element_by_xpath('//*[@id="authentication"]/button')
actions.move_to_element(obj)
actions.double_click()
actions.perform()


# To get title name

title = driver.title
assert title == 'Welcome to Python.org' ,' Title is not matched'

# To do zoom operations

driver.execute_script('document.body.style.zoom ="200%"')
driver.execute_script('document.body.style.zoom = "100%"')

# To set window size

driver.set_window_size(100,400)


# To move window position

driver.set_window_position(100,300)
print(driver.window_position())

# To open new tab

driver.execute_script('window_open("https://www.google.com")') # To open lnew tab with new link. But the control is on first tab only.

driver.execute_script('window_open("https://www.python.org","_current")') # To change link in current tab.

# To switch to tab

driver.execute_script("window.open('https://www.google.com')")

# To handle windows we have to give window_handles
window = driver.window_handles
print(window)

# To switch to window we have to give windows handle object. It will switch from right to left
driver.switch_to_window(window[1])

# To switch to window we have give window handle
driver.switch_to_window(driver.window_handles[2])


# To drop down with select
from selenium.webdriver.common.select import Select
a = Select(driver.find_element_by_id('continents'))

a.select_by_visible_text('Australia')
a.select_by_value('AUS')
a.select_by_index(2)


# To Handle Alerts

alert = driver.switch_to.alert()

alert.accept()
alert.dismiss()
alert.send_keys('vijay')

# To select checkbox

obj = driver.find_element_by_id('profession-1')

obj.click()
# To select radio button 
status = driver.find_element_by_id('profession-1').is_selected()
print(status)
if not status: driver.find_element_by_id('profession-1').click()

# To select radiobutton

driver.find_element_by_id('sex-0').click()

# To check  radio button is selected or not
rb = driver.find_element_by_id('sex-0').is_seleccted()
if not rb: driver.find_element_by_id('sex-0').click()


# Different types of locators

# Using Link_text

driver.find_element_by_link_text("Images").click()

# Using partial_link_text

driver.find_element_by_partial_link_text("Img").click()

# Using class_name locators

driver.find_element_by_class_name("gb_g").click()

# Using Tag name
driver.find_element_by_tag_name('a').click()








