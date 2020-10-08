from Selenium.pageobjectmodel.browser import Browser
from Selenium.pageobjectmodel.test.config import Config
from Selenium.pageobjectmodel.pom.landing.landingpage import LandingPage
from Selenium.pageobjectmodel.pom.landing.landingmodal import LandingModal
from Selenium.pageobjectmodel.pom.home.homepage import *
from Selenium.pageobjectmodel.pom.home.pricingpage import *
from Selenium.pageobjectmodel.pom.home.paymentmethod import *


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
        self.driver.get(Config.baseUrl)
        # click on log in button on landing page
        self.driver.click_login_button()
        # wait for login modal to load
        self.driver.wait_for_login_modal()
        # fill in login email and password
        self.driver.enter_login_email()
        self.driver.enter_login_password()
        # click login button
        self.driver.click_to_login()

    def check_balance(self):
        # wait for session balance on homepage to present
        self.driver.wait_for_session_balance_button()
        # check session balance
        return self.driver.get_session_balance()

    def choose_a_plan(self):
        # click on pricing tab
        self.driver.click_pricing_tab()
        # click on first pricing option
        self.driver.click_first_pricing_plan()
        # click on pay by card option

    def make_payment(self):
        self.driver.click_option_paybycard()
        # enter payment information
        self.driver.enter_information()
        # submit payment
        self.driver.submit_payment()

    def relocate_to_homepage(self):
        # relocate to homepage
        self.driver.get_link(Config.homepageURL)

    @staticmethod
    def compare_balance(balance_before, balance_after):
        assert balance_before == balance_after, "Payment Unsuccessful!"


if __name__ == "__main__":
    driver = Browser.get_browser_by_type()
    driver.maximize_window()
    test = TestExecution(driver)
    test.test_purchase_session()