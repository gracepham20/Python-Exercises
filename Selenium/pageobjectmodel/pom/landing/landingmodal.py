from basemodal import BaseModal
from Test.config import Config
from selenium.webdriver.common.by import By


class LandingModal(BaseModal):
    modal_login_header_CSS = "#modal-login > div > div > div.modal-header > h4"
    login_email_CSS = "input[name='email']"
    login_pass_CSS = "input[name='password']"
    login_button_CSS = "button#login-button"

    expected_id = "modal-login"

    def wait_for_login_modal(self):
        return self.DriverAPI.is_shown_on_page(By.CSS_SELECTOR, LandingModal.modal_login_header_CSS, 20)

    def enter_login_email(self):
        self.send_data(By.CSS_SELECTOR, LandingModal.login_email_CSS, Config.login_email)

    def enter_login_password(self):
        self.send_data(By.CSS_SELECTOR, LandingModal.login_pass_CSS, Config.login_pass)

    def click_login_button(self):
        self.click_on(By.CSS_SELECTOR, LandingModal.login_button_CSS)


