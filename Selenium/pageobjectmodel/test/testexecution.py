from selenium.webdriver.common.by import By
from pageobjectmodel.browser import get_browser_by_type
from pageobjectmodel.test.config import Config
from pageobjectmodel.pom.landing.landingpage import LandingPage
from pageobjectmodel.pom.landing.loginmodal import LoginModal
from pageobjectmodel.pom.home.homepage import HomePage
from pageobjectmodel.pom.home.pricingpage import PricingPage
from pageobjectmodel.pom.home.paymentmethod import PaymentMethodModal
from pageobjectmodel.driver_api import DriverAPI
from pageobjectmodel.browsertype import BrowserType


class TestExecution:

    def __init__(self, driver):
        self.driver = DriverAPI(driver)

    def test_purchase_session(self):
        self.account_login()
        balance_before = self.get_balance_value()
        self.choose_a_plan()
        self.make_payment()
        self.relocate_to_homepage()
        balance_after = self.get_balance_value()
        self.compare_balance(balance_before, balance_after)

    def account_login(self):
        # locate to landing page
        self.driver.get_link(Config.baseUrl)
        # click on log in button on landing page
        lp = LandingPage(self.driver)
        lp.click_login_button()

        lm = LoginModal(self.driver)
        # fill in login email and password
        lm.enter_login_email()
        lm.enter_login_password()
        # click login button
        lm.click_to_login()

    def get_balance_value(self):
        hp = HomePage(self.driver)
        # wait for session balance on homepage to present
        hp.is_present()
        # check session balance
        return hp.get_session_balance()

    def choose_a_plan(self):
        # locate to pricing page
        hp = HomePage(self.driver)
        hp.click_pricing_tab()
        # click on first pricing option
        pp = PricingPage(self.driver)
        pp.choose_pricing_plan()
        # click on pay by card option

    def make_payment(self):
        pm = PaymentMethodModal(self.driver)
        # TestExecution.check_card_availability()
        pm.click_option_paybycard()
        # enter payment information
        pm.enter_information()
        # submit payment
        pm.submit_payment()

    def relocate_to_homepage(self):
        # relocate to homepage
        self.driver.get_link(Config.homepageUrl)

    @staticmethod
    def compare_balance(balance_before, balance_after):
        if balance_before <= balance_after:
            print("Fail")
        else:
            print("Yes")
        #assert balance_before <= balance_after, "Payment Unsuccessful!"

    def check_card_availability(self):

        # check if past purchase method option is available
        try:
            card_available = self.driver.find(PaymentMethodModal.available_card, By.CSS_SELECTOR, timeout=50)
        except:
            card_available = None

        if card_available is not None:
            self.driver.click_on(PaymentMethodModal.pay_by_another_method_button, By.CSS_SELECTOR, 30)
        else:
            pass


if __name__ == "__main__":
    driver = get_browser_by_type(BrowserType.Chrome)
    test = TestExecution(driver)
    test.test_purchase_session()
