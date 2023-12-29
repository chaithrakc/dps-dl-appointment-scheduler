from selenium.webdriver.common.by import By


class UserInfoPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def navigate_to_page(self):
        self.driver.get(self.url)

        # selecting preferred language as English
        self.click_english_button()

    def click_english_button(self):
        english_button = self.driver.find_element(By.XPATH, "//button/span[text()='English']")
        english_button.click()

    def fill_user_information(self, user_config):
        self.navigate_to_page()

        # creating html elements for input
        first_name_input = self.driver.find_element(By.XPATH, "//label[text()='First Name']/following-sibling::input")
        last_name_input = self.driver.find_element(By.XPATH, "//label[text()='Last Name']/following-sibling::input")
        dob_input = self.driver.find_element(By.ID, 'dob')
        ssn_input = self.driver.find_element(By.ID, 'last4Ssn')

        # filling the input fields
        first_name_input.send_keys(user_config.get('first_name', ''))
        last_name_input.send_keys(user_config.get('last_name', ''))
        dob_input.send_keys(user_config.get('dob', ''))
        ssn_input.send_keys(user_config.get('last_four_of_ssn', ''))

        # log on
        self.click_log_on_button()
        print('Successfully completed filling out user info...')

    def click_log_on_button(self):
        log_on_button = self.driver.find_element(By.XPATH, "//button/span[text()='Log On']")
        log_on_button.click()
