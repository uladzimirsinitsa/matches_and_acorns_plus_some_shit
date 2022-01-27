
import os
import sys
import time
import pickle

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from bs4 import BeautifulSoup


load_dotenv()

service = Service(PATH_DRIVER)
driver = webdriver.Firefox(service=service)
driver.get(URL)
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)