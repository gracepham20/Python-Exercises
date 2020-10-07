from driver_api import DriverAPI
from basepageobject import BasePageObject


class BasePage(BasePageObject):

    expected_url = ""

    def is_present(self):
        if self.get_current_url() != BasePage.expected_url:  # !!!!!!!!!!!
            return False
        else:
            return True
