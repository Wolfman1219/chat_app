from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from gensim.summarization import summarize

# Set the path to the Firefox driver executable
webdriver_path = '/home/hasan/Documents/geckodriver'
firefox_options = Options()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--no-sandbox')

def get_text(url):
    driver2 = webdriver.Firefox(service=Service(webdriver_path), options=firefox_options)
    driver2.get(url)
    div_element = driver2.find_element(By.TAG_NAME,"body")
    text = div_element.text
    driver2.quit()
    return text

def get_summary(text, thres = 0.2):
    return summarize(text, thres)