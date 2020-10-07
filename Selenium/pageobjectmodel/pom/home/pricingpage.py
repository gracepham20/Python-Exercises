from base_page import BasePage
from selenium.webdriver.common.by import By


class PricingPage(BasePage):
    option1_button_CSS = ".gi-coverPricing-Inner--Individuals div:nth-child(1) > div > .gi-pricingItem-Button button"

    expected_url = "https://www.got-it.io/solutions/excel-chat/pricing/personal"

    def click_first_pricing_plan(self):
        self.click_on(By.CSS_SELECTOR, PricingPage.option1_button_CSS, 20)
