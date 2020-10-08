import time

from pageobjectmodel.pom.base.base_po import BasePageObject


class BasePage(BasePageObject):
    expected_url = ""

    def is_present(self):
        time.sleep(5)
        if self.driver.get_current_url() != self.expected_url:
            return False
        else:
            return True
