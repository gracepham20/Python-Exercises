from Selenium.pageobjectmodel.driver_api import DriverAPI


class BasePageObject:
    def __init__(self, driver: DriverAPI):
        self.driver = DriverAPI(driver)
        assert self.is_present() is True, "Page/ Modal Invalid"

    def is_present(self):
        pass
