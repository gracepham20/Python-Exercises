from pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from pageobjectmodel.test.config import Config


class PricingPage(BasePage):
    purchase_buttons_CSS = ".gi-coverPricing-Inner .btn"

    expected_url = Config.pricingUrl

    def choose_pricing_plan(self, index):
        button_list = self.driver.find_elements(self.purchase_buttons_CSS)
        self.driver.click_on(button_list[index], By.CSS_SELECTOR, 20)
