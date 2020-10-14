from Selenium.pageobjectmodel.pom.base.base_page import BasePage
from selenium.webdriver.common.by import By
from Selenium.pageobjectmodel.test.config import Config


class PricingPage(BasePage):
    purchase_buttons_CSS = ".gi-coverPricing-Inner .btn"

    expected_url = Config.pricingUrl

    def is_present(self):
        return self.driver.check_url(Config.pricingUrl)

    def choose_pricing_plan(self, index):
        button_list = self.driver.find_list_element(self.purchase_buttons_CSS, By.CSS_SELECTOR, 10)
        plan_chosen = button_list[index]
        plan_chosen.click()
