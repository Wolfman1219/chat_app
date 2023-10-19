from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


# Set the path to the Firefox driver executable
webdriver_path = '/home/hasan/Documents/geckodriver'
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')

def get_text(url):
    driver2 = webdriver.Firefox(service=Service(webdriver_path), options=firefox_options)
    driver2.get(url)
    div_element = driver2.find_element_by_tag_name("body")
    text = div_element.text
    driver2.quit()
    return text