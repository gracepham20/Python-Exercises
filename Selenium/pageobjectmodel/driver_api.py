from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverAPI:

    def __init__(self, driver):
        self.driver = driver

    def get_link(self, url):
        self.driver.get(url)

    def click_on(self, method_used, element_method, timeout=0):
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((method_used, element_method)))
        element.click()
        return element

    def send_data(self, method_used, element_method, data, timeout=0):
        element = self.find(method_used, element_method, timeout)
        element.send_keys(data)
        return element

    def find(self, method_used, element_css, timeout=0):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((method_used, element_css)))
            return element  # .driver.find_element(By.CSS_SELECTOR, element_css)
        except:
            return None

    def switch_iframe(self, iframe_id):
        self.driver.switch_to.frame(iframe_id)

    def switch_default_content(self):
        self.driver.switch_to.default_content()

    def get_text(self, method_used, element_method, timeout=0):
        content = self.find(method_used, element_method, timeout)
        return content.text

    def is_present_on_page(self, method_used, element_method, timeout=0):
        if self.find(method_used, element_method, timeout) is not None:
            return True
        else:
            return False

    def get_current_url(self):
        return self.driver.current_url
