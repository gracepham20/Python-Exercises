from Selenium.pageobjectmodel.pom.base.base_modal import BaseModal
from Selenium.pageobjectmodel.test.config import Config
from selenium.webdriver.common.by import By


class PaymentMethodModal(BaseModal):
    expected_id = "#modal-payment-subscription-engine"

    # CSS Selector
    pricing_modal = ".braintree-card.braintree-form.braintree-sheet"
    available_card = ".braintree-method__label"
    pay_by_another_method_button = ".braintree-large-button"
    pay_by_card_CSS = "div.braintree-option:nth-child(1)"
    card_no_CSS = "input[name='credit-card-number']"
    expiration_date_CSS = "input[name='expiration']"
    cvv_CSS = "input[name='cvv']"
    postal_CSS = "#postal-code"
    pay_now_CSS = "#modal-payment-subscription-engine .modal-footer button"
    purchase_successful_modal_CSS = ".modal-content"

    # iframe id
    card_no_iframe = "braintree-hosted-field-number"
    expiration_date_iframe = "braintree-hosted-field-expirationDate"
    cvv_iframe = "braintree-hosted-field-cvv"
    postal_iframe = "braintree-hosted-field-postalCode"

    def click_option_paybycard(self):
        self.driver.click_on(self.pay_by_card_CSS, timeout=50)

    def submit_payment(self):
        self.driver.click_on(self.pay_now_CSS, timeout=5)

    def wait_for_payment_modal_dismissed(self):
        self.driver.wait_for_modal_dismissed(self.expected_id, timeout=40)

    def check_for_available_card(self):
        try:
            card_available = self.driver.find(self.available_card, By.CSS_SELECTOR, timeout=40)
        except:
            card_available = None
        return card_available

    def pay_by_another_method(self):
        card_available = self.check_for_available_card()
        if card_available is not None:
            self.driver.click_on(self.pay_by_another_method_button, By.CSS_SELECTOR, 30)
        else:
            pass

    def purchase(self):
        self.fill_card(self.card_no_iframe, self.card_no_CSS, Config.card_no)

        # fill card number
        self.fill_card(self.expiration_date_iframe, self.expiration_date_CSS, Config.expiration_date)

        # fill CVV
        self.fill_card(self.cvv_iframe, self.cvv_CSS, Config.cvv)

        # fill postal code
        self.fill_card(self.postal_iframe, self.postal_CSS, Config.postal)

    def fill_card(self, iframe, element, content):
        self.driver.switch_iframe(iframe)
        self.driver.send_data(element, content, timeout=10)
        self.driver.switch_default_content()
