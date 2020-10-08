from Selenium.pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from Selenium.pageobjectmodel.test.config import Config


class PricingPage(BasePage):
    purchases_button_CSS = ".gi-coverPricing-Inner .btn"

    expected_url = Config.pricingUrl

    def choose_pricing_plan(self, index):
        button_list = self.driver.find_elements(self.purchases_button_CSS)
        self.driver.click_on(button_list[index], 20)
