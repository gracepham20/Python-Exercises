from pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from pageobjectmodel.test.config import Config
from pageobjectmodel.driver_api import DriverAPI


class LandingPage(BasePage):
    login_option_CSS = "test-login-button"

    expected_url = Config.baseUrl

    def click_login_button(self):
        self.driver.click_on(self.login_option_CSS)
