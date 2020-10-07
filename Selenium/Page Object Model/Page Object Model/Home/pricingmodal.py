from basemodal import BaseModal
from config import UserInformation


class PricingModalElement:
    # CSS Selector
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


class PricingModal(BaseModal):
    expected_id = "modal-payment-subscription-engine"

    def click_option_paybycard(self):
        self.click_on(PricingModalElement.pay_by_card_CSS)

    def switch_to_iframe(self, iframe_id):
        self.switch_iframe(iframe_id)

    def enter_information(self):
        self.enter_cardno(PricingModalElement.card_no_CSS, UserInformation.card_no)
        self.enter_expiration(PricingModalElement.expiration_date_CSS, UserInformation.expiration_date)
        self.enter_cvv(PricingModalElement.cvv_CSS, UserInformation.cvv)
        self.enter_postalcode(PricingModalElement.postal_CSS, UserInformation.postal)

    def enter_cardno(self, element_css, content):
        self.switch_to_iframe(PricingModalElement.card_no_iframe)
        self.send_data(element_css, content)

    def enter_expiration(self, element_css, content):
        self.switch_to_iframe(PricingModalElement.card_no_iframe)
        self.send_data(element_css, content)

    def enter_cvv(self, element_css, content):
        self.switch_to_iframe(PricingModalElement.card_no_iframe)
        self.send_data(element_css, content)

    def enter_postalcode(self, element_css, content):
        self.switch_to_iframe(PricingModalElement.card_no_iframe)
        self.send_data(element_css, content)

    def submit_payment(self):
        self.click_on(PricingModalElement.pay_now_CSS)
