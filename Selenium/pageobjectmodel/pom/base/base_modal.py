from Selenium.pageobjectmodel.pom.base.base_po import BasePageObject


class BaseModal(BasePageObject):

    expected_id = ""

    def is_present(self):
        return self.driver.is_present_on_page(self.expected_id) is True
