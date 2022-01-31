
import os
import sys
import time
import pickle

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()


PATH_DRIVER = os.environ['PATH_DRIVER']
URL = os.environ['URL']


service = Service(PATH_DRIVER)
driver = webdriver.Firefox(service=service)
driver.get(URL)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)


def get_full_page(url='https://jj1ba0.blogabet.com/'):
    driver.get(url)
    while True:
        try:
            time.sleep(1)
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="last_item"]/a').click()
        except:
            time.sleep(1)
            continue


def main():
    get_full_page()
    


if __name__ == '__main__':
    main()
    #sys.exit()
    