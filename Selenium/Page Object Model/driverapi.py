from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverAPI:

    def __init__(self, driver):
        self.driver = driver

    def get_link(self, url):
        self.driver.get(url)

    def click_on(self, element_css):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, element_css)))
        element.click()
        return element

    def send_data(self, element_css, data):
        element = self.find(element_css)
        element.send_keys(data)
        return element

    def find(self, element_css):
        element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_css)))
        return element  # .driver.find_element(By.CSS_SELECTOR, element_css)

    def switch_iframe(self, iframe_id):
        self.driver.switch_to.frame(iframe_id)

    def switch_default_content(self, element_default_content_css):
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, element_default_content_css)))

    def get_text(self, element_css):
        content = self.driver.find(element_css)
        return content.text

    def is_shown_on_page(self, element_css):
        if self.find(element_css) is not None:
            return True
        else:
            return False
