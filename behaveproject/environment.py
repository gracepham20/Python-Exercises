from behave import use_fixture
from Selenium.pageobjectmodel.driver_api import DriverAPI
from behaveproject.fixture import *
from Selenium.pageobjectmodel.browsertype import BrowserType


def before_tag(context, tag):
    if tag.startswith("fixture."):
        tag_list = tag.split(".")
        if tag_list[2] == "chrome":
            if tag_list[3] == "True":
                return use_fixture(launch_browser_by_type, context, browser_name=BrowserType.Chrome, headless=True)
            elif tag_list[3] == "False":
                return use_fixture(launch_browser_by_type, context, browser_name=BrowserType.Chrome, headless=False)
        elif tag_list[2] == "firefox":
            if tag_list[3] == "True":
                return use_fixture(launch_browser_by_type, context, browser_name=BrowserType.Firefox, headless=True)
            elif tag_list[3] == "False":
                return use_fixture(launch_browser_by_type, context, browser_name=BrowserType.Firefox, headless=False)
        else:
            return use_fixture(launch_browser_by_type, context, None)


def before_scenario(context, scenario):
    context.scenario_name = scenario.name


def after_step(context, step):
    if step.status == "failed":
        DriverAPI(context.browser).take_screenshot(context.scenario_name, step.name)
