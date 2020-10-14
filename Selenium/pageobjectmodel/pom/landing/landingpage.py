from Selenium.pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from Selenium.pageobjectmodel.test.config import Config
from Selenium.pageobjectmodel.driver_api import DriverAPI


class LandingPage(BasePage):
    login_option_CSS = "#test-login-button"

    expected_url = Config.baseUrl

    def click_login_button(self):
        self.driver.click_on(self.login_option_CSS)

    def is_present(self):
        return self.driver.is_present_on_page(self.login_option_CSS, method_used=By.CSS_SELECTOR, timeout=10)
