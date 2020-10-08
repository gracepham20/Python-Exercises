from Selenium.pageobjectmodel.pom.base.base_page import BasePage
from Selenium.pageobjectmodel.test.config import Config


class HomePage(BasePage):

    session_balance_button_CSS = "#test-session-balance-header-button"
    balance_value_button_CSS = "#test-session-balance-header-button > strong"
    pricing_tab_CSS = "#pricing-navlink-landing"

    expected_url = Config.homepageUrl

    def is_present(self):
        return self.driver.is_shown_on_page(self.session_balance_button_CSS, 20)

    def get_session_balance(self):
        return self.driver.get_text(self.balance_value_button_CSS, 20)

    def click_pricing_tab(self):
        self.driver.click_on(self.pricing_tab_CSS, 20)

