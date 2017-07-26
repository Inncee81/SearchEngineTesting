from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from bs4 import BeautifulSoup

driver = webdriver.Ie("C:\\Users\\user\\Downloads\\IEDriverServer_x64_2.42.0\\IEDriverServer")

driver.get("http://www.naver.com")
