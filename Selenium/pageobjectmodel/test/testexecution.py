from browser import Browser
from config import Config
from landingpage import *
from landingmodal import *
from homepage import *
from pricingpage import *
from pricingmodal import *

class TestExecution:
    def __init__(self, driver):
        self.driver = driver

    def test_purchase_session(self):
        self.account_login()
        balance_before = self.check_balance()
        self.choose_a_plan()
        self.make_payment()
        self.relocate_to_homepage()
        balance_after = self.check_balance()
        self.compare_balance(balance_before, balance_after)

    def account_login(self):
        # locate to landing page
        self.get(Config.baseUrl)
        # click on log in button on landing page
        self.LandingPage.click_login_button()
        # wait for login modal to load
        self.LandingModal.wait_for_login_modal()
        # fill in login email and password
        self.LandingModal.enter_login_email()
        self.LandingModal.enter_login_password()
        # click login button
        self.LandingModal.click_login_button()

    def check_balance(self):
        # wait for session balance on homepage to present
        self.HomePage.wait_for_session_balance_button()
        # check session balance
        return self.HomePage.get_session_balance()

    def choose_a_plan(self):
        # click on pricing tab
        self.HomePage.click_pricing_tab()
        # click on first pricing option
        self.PricingPage.click_first_pricing_plan()
        # click on pay by card option

    def make_payment(self):
        self.PricingModal.click_option_paybycard()
        # enter payment information
        self.PricingModal.enter_information()
        # submit payment
        self.PricingModal.submit_payment()

    def relocate_to_homepage(self):
        # relocate to homepage
        self.get_link(Config.homepageURL)

    @staticmethod
    def compare_balance(balance_before, balance_after):
        assert balance_before == balance_after, "Payment Unsuccessful!"


if __name__ == "__main__":
    driver = Browser.get_browser_by_type()
    driver.maximize_window()
    test = TestExecution(driver)
    test.test_purchase_session()