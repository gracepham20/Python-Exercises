class FileInput:
    # url
    baseUrl = "https://www.got-it.io/solutions/excel-chat/"
    home_page = "https://www.got-it.io/solutions/excel-chat/home"

    # personal information
    login_email = "grace+ec2@gotitapp.co"
    login_pass = "Grace123"
    card_no = "5555555555554444"
    expiration_date = "08/22"
    cvv = "123"
    postal = "100000"

    # CSS selector
    login_option_CSS = "test-login-button"
    modal_login_header_CSS = "#modal-login > div > div > div.modal-header > h4"
    login_email_CSS = "input[name='email']"
    pricing_tab_CSS = "#pricing-navlink-landing"
    login_pass_CSS = "input[name='password']"
    login_button_CSS = "button#login-button"
    session_balance_button_CSS = "#test-session-balance-header-button"
    balance_value_button_CSS = "#test-session-balance-header-button > strong"
    option1_button_CSS = ".gi-coverPricing-Inner--Individuals > div > div:nth-child(1) > div " \
                         "> .gi-pricingItem-Button > button"
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




