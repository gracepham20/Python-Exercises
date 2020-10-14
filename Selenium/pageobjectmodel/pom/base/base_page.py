import time

from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Selenium.pageobjectmodel.pom.base.base_po import BasePageObject


class BasePage(BasePageObject):
    expected_url = None

    def is_present(self):
        return self.driver.check_url(self.expected_url)


