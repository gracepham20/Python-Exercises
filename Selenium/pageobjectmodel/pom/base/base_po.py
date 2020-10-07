class BasePageObject:
    def __init__(self, driver):
        self.driver = driver
        assert self.is_present() is True, "Page/ Modal Invalid"

    def is_present(self):
        pass
