from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class UserInfoPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def navigate_to_page(self):
        self.driver.get(self.url)

        # selecting preferred language as English
        self.click_english_button()

    def click_english_button(self):
        # using WebDriverWait to wait for the button to be present before interacting with it
        english_button_locator = (
            By.CLASS_NAME, 'button.white--text.v-btn.v-btn--contained.theme--light.v-size--x-large.public-blue')
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(english_button_locator))

        # finding the button and clicking on it
        english_button = self.driver.find_element(*english_button_locator)
        english_button.click()

    def fill_user_information(self, user_config):
        # creating html elements for input
        first_name_input = self.driver.find_element_by_id('first_name')
        last_name_input = self.driver.find_element_by_id('last_name')
        dob_input = self.driver.find_element_by_id('dob')
        ssn_input = self.driver.find_element_by_id('last_four_of_ssn')

        # filling the input fields
        first_name_input.send_keys(user_config.get('first_name', ''))
        last_name_input.send_keys(user_config.get('last_name', ''))
        dob_input.send_keys(user_config.get('dob', ''))
        ssn_input.send_keys(user_config.get('last_four_of_ssn', ''))
