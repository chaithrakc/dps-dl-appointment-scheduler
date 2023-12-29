from selenium.webdriver.common.by import By
import time


class LocationPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self):
        new_appoint_button = self.driver.find_element(By.XPATH, "// span[text() = 'New Appointment']")
        new_appoint_button.click()
        time.sleep(10)  # wait for the next page to load
        service_button = self.driver.find_element(By.XPATH, "//button[text()='Apply for first time Texas DL/Permit']")
        service_button.click()

    def find_nearest_dps(self, email, mobile_number, zip_code):
        self.navigate_to_page()

        # creating HTML input elements
        cell_phone_input = self.driver.find_element(By.XPATH, "//label[text()='Cell Phone']/following-sibling::input")
        email_input = self.driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
        verify_email_input = self.driver.find_element(By.XPATH, "//label[text()='Verify Email']/following-sibling::input")
        text_message_checkbox = self.driver.find_element(By.XPATH, "//label[text()='I prefer to receive notifications via text message']/preceding-sibling::div/input")
        zip_input = self.driver.find_element(By.XPATH, "//label[text()='Zip Code']/following-sibling::input")

        # filling the input fields
        cell_phone_input.send_keys(mobile_number)
        email_input.send_keys(email)
        verify_email_input.send_keys(email)
        text_message_checkbox.click()
        zip_input.send_keys(zip_code)

        next_button = self.driver.find_element(By.XPATH, "//button/span[text()=' Next ']")
        next_button.click()
