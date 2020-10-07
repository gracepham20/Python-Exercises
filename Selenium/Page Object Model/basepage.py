from driverAPI import DriverAPI
from basepageobject import BasePageObject


class BasePage(BasePageObject):

    expected_url = "https://www.got-it.io/solutions/excel-chat/pricing/personal"

    def __init__(self, x: DriverAPI):
        self.driver = x
        assert self.is_present() is not False, "Page Invalid"

    def is_present(self):
        if self.driver.current_url() != BasePage.expected_url:
            return False
        else:
            return True

