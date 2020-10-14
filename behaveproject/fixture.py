from behave import fixture
from Selenium.pageobjectmodel.browsertype import BrowserType
from Selenium.pageobjectmodel.browser import get_browser_by_type


@fixture
def launch_browser_by_type(context, browser_name, headless):
    if browser_name == "chrome":
        context.browser = get_browser_by_type(BrowserType.Chrome, headless)
    elif browser_name == "firefox":
        context.browser = get_browser_by_type(BrowserType.Firefox, headless)
    yield context.browser
    context.browser.quit()
