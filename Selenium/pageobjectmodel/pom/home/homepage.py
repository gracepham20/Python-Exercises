from base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    session_balance_button_CSS = "#test-session-balance-header-button"
    balance_value_button_CSS = "#test-session-balance-header-button > strong"
    pricing_tab_CSS = "#pricing-navlink-landing"

    expected_url = "https://www.got-it.io/solutions/excel-chat/home"

    def wait_for_session_balance_button(self):
        return self.DriverAPI.is_shown_on_page(By.CSS_SELECTOR, HomePage.session_balance_button_CSS, 20)

    def get_session_balance(self):
        self.get_text(By.CSS_SELECTOR, HomePage.balance_value_button_CSS, 20)

    def click_pricing_tab(self):
        self.click_on(By.CSS_SELECTOR, HomePage.pricing_tab_CSS, 20)

