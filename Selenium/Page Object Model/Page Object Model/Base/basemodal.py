from driverAPI import DriverAPI
from basepageobject import BasePageObject


class BaseModal(BasePageObject):

    expected_id = ""

    def __init__(self, x: DriverAPI):
        self.driver = x
        assert self.is_present() is True, "Modal Invalid"

    def is_present(self):
        if self.driver.current_url() != BaseModal.expected_id:
            return False
        else:
            return True
