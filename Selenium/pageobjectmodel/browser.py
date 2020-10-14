from Selenium.pageobjectmodel.browsertype import BrowserType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions


def get_browser_by_type(browser_name, headless=False):
    if browser_name == BrowserType.Chrome:
        options = COptions()
        options.headless = headless
        return webdriver.Chrome(options=options, executable_path="../../PycharmProjects/Python-Exercises/Selenium"
                                                                 "/drivers/chromedriver")
    elif browser_name == BrowserType.Firefox:
        options = FOptions()
        options.headless = headless
        return webdriver.Firefox(executable_path="../../PyCharmProjects/Python-Exercises/Selenium/drivers/geckodriver"
                                 , options=options)
    else:
        assert (browser_name is BrowserType.Chrome) or (browser_name is BrowserType.Firefox), "Browser Invalid"
