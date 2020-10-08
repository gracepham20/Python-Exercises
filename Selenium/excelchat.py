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
        self.driver.get(FileInput.baseUrl)

        # click on log in option
        self.driver.find_element(By.ID, FileInput.login_option_CSS).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, FileInput.
                                                                             modal_login_header_CSS)))

        # fill in email and password
        self.driver.find_element(By.CSS_SELECTOR, FileInput.login_email_CSS).send_keys(FileInput.login_email)
        self.driver.find_element(By.CSS_SELECTOR, FileInput.login_pass_CSS).send_keys(FileInput.login_pass)

        # log in
        self.driver.find_element(By.CSS_SELECTOR, FileInput.login_button_CSS).click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, FileInput.
                                                                             session_balance_button_CSS)))

        # check session balance
        self.balance = self.check_balance()

        # choose pricing tab
        self.locate_pricing()

    def purchase(self):
        # fill card number
        self.fill_card(FileInput.card_no_iframe, FileInput.card_no_CSS, FileInput.card_no)

        # fill card number
        self.fill_card(FileInput.expiration_date_iframe, FileInput.expiration_date_CSS, FileInput.expiration_date)

        # fill CVV
        self.fill_card(FileInput.cvv_iframe, FileInput.cvv_CSS, FileInput.cvv)

        # fill postal code
        self.fill_card(FileInput.postal_iframe, FileInput.postal_CSS, FileInput.postal)

        pay_now = self.driver.find_element(By.CSS_SELECTOR, FileInput.pay_now_CSS)
        pay_now.click()

        # check session balance
        WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, FileInput.purchase_successful_modal_CSS)))

        balance_after_purchased = self.check_balance()
        assert self.balance < balance_after_purchased, "Purchase has not been complete!"

    def fill_card(self, iframe, element, keys):
        self.driver.switch_to.frame(iframe)

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

        card = self.driver.find_element(By.CSS_SELECTOR, element)
        card.send_keys(keys)

        # Switch back to the parent frame
        self.driver.switch_to.default_content()

        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".braintree-card.braintree-form.braintree-sheet")))

        # .braintree-large-button (Choose another way to pay option)

    def check_balance(self):
        # locate to homepage
        self.driver.get(FileInput.home_page)

        balance = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, FileInput.balance_value_button_CSS)))

        balance_value = balance.text

        # print number of session balance
        print(f"Number of session balance is {balance_value}")
        return balance_value

    def locate_pricing(self):
        # choose Pricing tab
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, FileInput.pricing_tab_CSS))).click()

        # choose first pricing option
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, FileInput.option1_button_CSS))).click()

        self.check_card_availability()

        # choose option to pay by card
        WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, FileInput.pay_by_card_CSS))).click()

        self.purchase()

    def check_card_availability(self):
        try:
            WebDriverWait(self.driver, 50).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".braintree-method__label")))

            card_available = self.driver.find_element(By.CSS_SELECTOR, ".braintree-method__label")
        except:
            pass

        if card_available is not None:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".braintree-large-button"))).click()
        else:
            pass






if __name__ == '__main__':
    driver = webdriver.Chrome("drivers/chromedriver")
    driver.maximize_window()
    test = ExcelChat(driver)
    test.login()