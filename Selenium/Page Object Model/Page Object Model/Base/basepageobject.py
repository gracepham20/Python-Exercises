from driverapi import DriverAPI


class BasePageObject:
    def __init__(self, x: DriverAPI):
        self.driver = x
        assert self.is_present() is True, "No page found"

    def is_present(self):
        pass
