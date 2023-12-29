from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def initialize_webdriver(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    return driver
