import sys
import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from dotenv import load_dotenv


load_dotenv()


service = Service(os.environ['PATH_DRIVER'])
driver = webdriver.Firefox(service=service)
driver.get(os.environ['URL'])

print('Log in to the site.')
time.sleep(30)

pickle.dump(driver.get_cookies(), open('cookies.pkl', 'wb'))

driver.quit()
sys.exit()
