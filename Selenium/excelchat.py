from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from fileinput import FileInput


class ExcelChat:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        # open site
        self.driver.maximize_window()
        self.driver.get(FileInput.baseUrl)

        # click on log in option
        self.driver.find_element(By.ID, "test-login-button").click()
        time.sleep(2)

        # fill in email and password
        self.driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys(FileInput.login_email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(FileInput.login_pass)

        # log in
        self.driver.find_element(By.CSS_SELECTOR, "button#login-button").click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#test-session-balance"
                                                                                              "-header-button")))

        # check session balance
        self.check_balance()

        # choose pricing tab
        self.pricing()

    def card(self):
        # fill card number
        self.card_fill(FileInput.card_no_iframe, FileInput.card_no_CSS, FileInput.card_no)

        # fill card number
        self.card_fill(FileInput.expiration_date_iframe, FileInput.expiration_date_CSS, FileInput.expiration_date)

        # fill CVV
        self.card_fill(FileInput.cvv_iframe, FileInput.cvv_CSS, FileInput.cvv)

        # fill postal code
        self.card_fill(FileInput.postal_iframe, FileInput.postal_CSS, FileInput.postal)

        pay_now = self.driver.find_element(By.CSS_SELECTOR, "#modal-payment-subscription-engine > div > div >"
                                                            " .modal-footer > div > button")
        pay_now.click()

        # check session balance
        time.sleep(15)
        self.check_balance()

    def card_fill(self, iframe, element, keys):
        self.driver.switch_to.frame(iframe)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

        card = self.driver.find_element(By.CSS_SELECTOR, element)
        card.send_keys(keys)

        # Switch back to the parent frame
        self.driver.switch_to.default_content()
        time.sleep(2)

    def check_balance(self):
        # locate to homepage
        self.driver.get(FileInput.home_page)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#test-session-balance-header-button > strong")))

        balance = self.driver.find_element(By.CSS_SELECTOR, "#test-session-balance-header-button > strong").text

        # print number of session balance
        print(f"Number of session balance is {balance}")

    def pricing(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#pricing-navlink-landing")))
        # choose Pricing tab
        self.driver.find_element(By.CSS_SELECTOR, "#pricing-navlink-landing").click()

        WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".gi-coverPricing-Inner--Individuals > div > div:nth-child(1) > div > .gi-pricingItem-Button > button")))
        # choose first pricing option
        self.driver.find_element(By.CSS_SELECTOR, ".gi-coverPricing-Inner--Individuals > div > div:nth-child(1) "
                                                  "> div > .gi-pricingItem-Button > button").click()

        WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.braintree-option:nth-child(1)")))
        # choose option to pay by card
        self.driver.find_element(By.CSS_SELECTOR, "div.braintree-option:nth-child(1)").click()

        self.card()


if __name__ == '__main__':
    driver = webdriver.Chrome("drivers/chromedriver")
    test = ExcelChat(driver)
    test.login()