from pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from pageobjectmodel.test.config import Config


class PricingPage(BasePage):
    purchase_buttons_CSS = ".gi-coverPricing-Inner--Individuals div:nth-child(1) > div > .gi-pricingItem-Button button"

    expected_url = Config.pricingUrl

    def choose_pricing_plan(self):

        self.driver.click_on(self.purchase_buttons_CSS, timeout=30)
