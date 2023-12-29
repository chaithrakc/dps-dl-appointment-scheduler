from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def initialize_webdriver(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument('--headless')
    driver = webdriver.Chrome('../chromedriver-win64/chromedriver.exe', options=chrome_options)
    driver.maximize_window()
    return driver
