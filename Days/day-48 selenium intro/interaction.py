from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DEBUG = False
DEPLOY = False

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

d = webdriver.Chrome(options=options)
d.get('https://secure-retreat-92358.herokuapp.com')

for row, data in {'top':'random', 'middle':'person', 'bottom':'not_giving_you_my_data@aol.com'}.items(): 
    d.find_element(By.CLASS_NAME, row).send_keys(data)

d.find_element(By.CLASS_NAME, 'btn').click()

if DEPLOY:
    d.quit()