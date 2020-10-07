from browsertype import BrowserType


from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions


def get_browser_by_type(browser_name, headless=True) #(browser_name="Chrome", headless=True):
    if browser_name == BrowserType.Chrome:
        options = COptions()
        options.headless = headless
        return webdriver.Chrome("../drivers/chromedriver", options=options)
    elif browser_name == BrowserType.Firefox:
        options = FOptions()
        options.headless = headless
        return webdriver.Firefox("drivers/geckodriver", options=options)
    else:
        return "Browser Invalid"


