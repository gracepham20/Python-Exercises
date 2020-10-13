from behave import fixture
from Selenium.pageobjectmodel.browsertype import BrowserType
from Selenium.pageobjectmodel.browser import get_browser_by_type


@fixture
def launch_browser_by_type(context, browser_name, headless=False):
    context.browser = get_browser_by_type(browser_name, headless)
    yield context.browser
    #context.browser.quit()

# def get_browser()
# before tag
