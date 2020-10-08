from Selenium.pageobjectmodel.pom.base.base_modal import BaseModal
from Selenium.pageobjectmodel.test.config import Config
from selenium.webdriver.common.by import By


class LoginModal(BaseModal):
    modal_login_header_CSS = "#modal-login > div > div > div.modal-header > h4"
    login_email_CSS = "input[name='email']"
    login_pass_CSS = "input[name='password']"
    login_button_CSS = "button#login-button"

    expected_id = "modal-login"

    def enter_login_email(self):
        self.driver.send_data(self.login_email_CSS, Config.login_email)

    def enter_login_password(self):
        self.driver.send_data(self.login_pass_CSS, Config.login_pass)

    def click_to_login(self):
        self.driver.click_on(self.login_button_CSS)
