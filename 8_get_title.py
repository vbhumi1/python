from selenium import webdriver
import time

d = webdriver.Chrome()
d.get('https://www.naukri.com/')

# To get window title
a=d.title
print("title name: ",a)

#To check the title is same or not
assert a == "Jobs - Recruitment - Job Search - Employment - Job Vacancies - Naukri.com","Not excepted title"

time.sleep(3)
d.close()