from src.pages.date_selection_page import DateSelectionPage
from src.pages.location_page import LocationPage
from src.pages.user_info_page import UserInfoPage
from src.utils.config_reader import read_config
from src.utils.selenium_utils import initialize_webdriver


def schedule_appointment():
    # reading user and app configurations
    user_config = read_config('../config.properties', 'user')
    app_config = read_config('../config.properties', 'app')

    driver = initialize_webdriver()  # initializing the webdriver

    try:
        # page 1: filling out user information
        user_info_page = UserInfoPage(driver, app_config['url'])
        user_info_page.fill_user_information(user_config)

        # page 2: providing email and zip code to find nearest DPS
        location_page = LocationPage(driver)
        location_page.find_nearest_dps(user_config['email'], user_config['zip_code'])

        # page 3: selecting the date for the appointment
        date_selection_page = DateSelectionPage(driver)
        date_selection_page.select_appointment_date(user_config['desired_date'])

    finally:
        driver.quit()  # closing the web driver


if __name__ == "__main__":
    schedule_appointment()
