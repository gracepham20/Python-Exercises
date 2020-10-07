from basepage import BasePage


class LandingPageElement:

    login_option_CSS = "test-login-button"


class LandingPage(BasePage):
    expected_url = "https://www.got-it.io/solutions/excel-chat/"

    def click_login_button(self):
        self.click_on(LandingPageElement.login_option_CSS)


