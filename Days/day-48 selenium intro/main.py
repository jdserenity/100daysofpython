from selenium import webdriver; from selenium.webdriver.common.by import By;

DEBUG = False

options = webdriver.ChromeOptions(); options.add_experimental_option('detach', True); 

d = webdriver.Chrome(options=options)
d.get('https://www.python.org')

event_box = d.find_element(By.CLASS_NAME, 'event-widget')
link_elems = event_box.find_elements(By.TAG_NAME, 'a')[1:]
date_elems = event_box.find_elements(By.TAG_NAME, 'time')

events = [{'name':e.text, 'link':e.get_attribute('href'), 'date': date.get_attribute('datetime').split('T')[0]} for e, date in zip(link_elems, date_elems)]

print(events)

if not DEBUG:
    d.quit()