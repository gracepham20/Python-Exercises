from pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from pageobjectmodel.test.config import Config


class PricingPage(BasePage):
    purchase_buttons_CSS = ".gi-coverPricing-Inner .btn"

    expected_url = Config.pricingUrl

    def is_present(self):
        return self.driver.is_present_on_page(self.purchase_buttons_CSS, timeout=30)

    def choose_pricing_plan(self, index):
        button_list = self.driver.find_list_element(self.purchase_buttons_CSS, By.CSS_SELECTOR, 20)
        plan_chosen = button_list[index]
        plan_chosen.click()

