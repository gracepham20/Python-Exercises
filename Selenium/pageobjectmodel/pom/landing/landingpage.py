from Selenium.pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By


class LandingPage(BasePage):
    login_option_CSS = "test-login-button"

    expected_url = "https://www.got-it.io/solutions/excel-chat/"

    def click_login_button(self):
        self.driver.click_on(By.CSS_SELECTOR, LandingPage.login_option_CSS)

