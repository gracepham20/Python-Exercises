from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class DriverAPI:

    def __init__(self, driver):
        self.driver = driver

    def get_link(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click_on(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((method_used, element_method)))
        element.click()
        return element

    def send_data(self, element_method, data, method_used=By.CSS_SELECTOR, timeout=10):
        element = self.find(element_method, method_used, timeout)
        element.send_keys(data)
        return element

    def find(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((method_used, element_method)))

            return element
        except:
            return None

    def switch_iframe(self, iframe_id):
        self.driver.switch_to.frame(iframe_id)

    def switch_default_content(self):
        self.driver.switch_to.default_content()

    def get_text(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        content = self.find(element_method, method_used, timeout)
        return content.text

    def is_present_on_page(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        try:
            self.find(element_method, method_used, timeout)
            return True
        except:
            return False

    def get_current_url(self):
        return self.driver.current_url

    def quit(self):
        self.driver.quit()

    def find_list_element(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((method_used, element_method)))

            return self.driver.find_elements(element_css)
        except:
            return None

    def wait_for_element(self, element_method, method_used=By.CSS_SELECTOR, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((method_used, element_method)))

    def relocate_to_url(self, url):
        time.sleep(20)
        self.driver.get(url)
