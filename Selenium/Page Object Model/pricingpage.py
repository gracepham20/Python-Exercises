from basepage import BasePage


class PricingPageElement:

    option1_button_CSS = ".gi-coverPricing-Inner--Individuals div:nth-child(1) > div > .gi-pricingItem-Button button"


class PricingPage(BasePage):

    def click_first_pricing_plan(self):
        self.click_on(PricingPageElement.option1_button_CSS)
