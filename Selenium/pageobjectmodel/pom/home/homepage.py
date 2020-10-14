from Selenium.pageobjectmodel.pom.base.base_page import BasePage
from Selenium.pageobjectmodel.test.config import Config


class HomePage(BasePage):
    expected_url = Config.homepageUrl

    balance_value_button_CSS = "#test-session-balance-header-button > strong"
    pricing_tab_CSS = "#pricing-navlink-landing"

    def is_present(self):
        return self.driver.check_url(Config.homepageUrl)

    def get_session_balance(self):
        return self.driver.get_text(self.balance_value_button_CSS, timeout=10)

    def click_pricing_tab(self):
        self.driver.click_on(self.pricing_tab_CSS, timeout=10)
