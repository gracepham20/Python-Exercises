from basepage import BasePage


class HomePageElement:

    session_balance_button_CSS = "#test-session-balance-header-button"
    balance_value_button_CSS = "#test-session-balance-header-button > strong"
    pricing_tab_CSS = "#pricing-navlink-landing"


class HomePage(BasePage):
    expected_url = "https://www.got-it.io/solutions/excel-chat/home"

    def wait_for_session_balance_button(self):
        return self.DriverAPI.is_shown_on_page(session_balance_button_CSS)

    def get_session_balance(self):
        self.get_text(HomePageElement.balance_value_button_CSS)

    def click_pricing_tab(self):
        self.click_on(HomePageElement.pricing_tab_CSS)
