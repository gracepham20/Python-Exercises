from Selenium.pageobjectmodel.pom.base.base_po import BasePageObject
from Selenium.pageobjectmodel.driver_api import DriverAPI


class BasePage(BasePageObject):

    expected_url = ""

    def is_present(self):
        if self.get_current_url() != BasePage.expected_url:
            return False
        else:
            return True
