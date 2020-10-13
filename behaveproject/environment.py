from behave import use_fixture
from Selenium.pageobjectmodel.driver_api import DriverAPI
from behaveproject.fixture import *
from Selenium.pageobjectmodel.browsertype import BrowserType


def before_tag(context, tag):
    tag_list = tag.split(".")
    if tag_list[2] == "chrome":
        return use_fixture(launch_browser_by_type, context, browser_name=BrowserType.Chrome)
        # if tag_list[3] == "True":
        #     use_fixture(get_browser_by_type, context=BrowserType.Chrome, headless=True)
        # elif tag_list[3] == "False":
        #     use_fixture(get_browser_by_type, context=BrowserType.Chrome, headless=False)
    elif tag_list[2] == "firefox":
        return use_fixture(launch_browser_by_type, BrowserType.Firefox)
    else:
        return use_fixture(launch_browser_by_type, None)


def before_scenario(context, scenario):
    context.scenario_name = scenario.name


def after_step(context, step):
    context.step_name = step.name
    if step.status == "failed":
        DriverAPI(context.browser).take_screenshot(context.scenario_name, context.step_name)
