from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

class ExcelChat:

    def open_site(self):
        baseUrl = "https://www.got-it.io/solutions/excel-chat/"
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(baseUrl)

        self.login()

    def login(self):
        # click on log in option
        self.driver.find_element(By.ID, "test-login-button").click()
        time.sleep(2)

        email, password = self.login_fill()
        email.send_keys("grace+ec2@gotitapp.co")
        password.send_keys("Grace123")
        log_in = self.driver.find_element(By.CSS_SELECTOR, "button#login-button")
        log_in.click()

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#test-session-balance"
                                                                                              "-header-button")))

        self.check_balance()
        self.locate_pricing()

    def login_fill(self):
        email = self.driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        password = self.driver.find_element(By.CSS_SELECTOR, "input[name='password']")

        return email, password

    def check_balance(self):
        # locate to homepage
        self.driver.get("https://www.got-it.io/solutions/excel-chat/home")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".u-marginLeft-1")))

        balance = self.driver.find_element(By.CSS_SELECTOR, ".u-marginLeft-1").text

        # print number of session balance
        print(f"Number of session balance is {balance}")

    def locate_pricing(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#pricing-navlink-landing")))
        # choose Pricing tab
        self.driver.find_element(By.CSS_SELECTOR, "#pricing-navlink-landing").click()
        # wait for pricing options page
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-12:nth-child(1) > div:nth-child(1)"
                                                             " > div:nth-child(3) > button:nth-child(1)")))

        self.pricing()

    def pricing(self):
        # choose first pricing option
        self.driver.find_element(By.CSS_SELECTOR, "div.col-12:nth-child(1) > div:nth-child(1)"
                                                  " > div:nth-child(3) > button:nth-child(1)").click()

        WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.braintree-option:nth-child(1)")))
        # choose option to pay by card
        self.driver.find_element(By.CSS_SELECTOR, "div.braintree-option:nth-child(1)").click()

        self.cardnumber_fill()

    def cardnumber_fill(self):
        self.driver.switch_to.frame("braintree-hosted-field-number")
        time.sleep(2)
        card_no = self.driver.find_element(By.CSS_SELECTOR, "input[name='credit-card-number']")
        card_no.send_keys("5555555555554444")

        # Switch back to the parent frame
        self.driver.switch_to.default_content()
        time.sleep(2)

        self.expiration_fill()

    def expiration_fill(self):
        self.driver.switch_to.frame("braintree-hosted-field-expirationDate")
        time.sleep(2)
        expiration_date = self.driver.find_element(By.CSS_SELECTOR, "input[name='expiration']")
        expiration_date.send_keys("08/22")

        # Switch back to the parent frame
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.cvv_fill()

    def cvv_fill(self):
        self.driver.switch_to.frame("braintree-hosted-field-cvv")
        time.sleep(2)
        cvv = self.driver.find_element(By.CSS_SELECTOR, "input[name='cvv']")
        cvv.send_keys("123")

        # Switch back to the parent frame
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.postalcode_fill()

    def postalcode_fill(self):
        self.driver.switch_to.frame("braintree-hosted-field-postalCode")
        time.sleep(2)
        postal = self.driver.find_element(By.CSS_SELECTOR, "#postal-code")
        postal.send_keys("100000")

        # Switch back to the parent frame
        self.driver.switch_to.default_content()
        time.sleep(2)

        self.submit_payment()

    def submit_payment(self):
        pay_now = self.driver.find_element(By.CSS_SELECTOR, ".u-flex > button:nth-child(1)")
        pay_now.click()

        # check session balance
        time.sleep(20)
        self.check_balance()

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    test = ExcelChat()
    test.open_site()
