from basepageobject import BasePageObject


class BaseModal(BasePageObject):

    expected_id = ""

    def is_present(self):
        return self.driver.is_shown_on_page(self.expected_id) is True
