from behave import use_fixture
from Selenium.pageobjectmodel.driver_api import DriverAPI
from Selenium.pageobjectmodel.test.config import Config
from behaveproject.fixture import *


def before_tag(context, tag):

    if tag.startswith("fixture."):
        tag_list = tag.split(".")
        if len(tag_list) != 4:
            assert "Tag Invalid"
        else:
            browser_name = tag_list[2]
            headless = tag_list[3]
            return use_fixture(launch_browser_by_type, context, browser_name=browser_name, headless=headless)


def before_scenario(context, scenario):
    context.scenario_name = scenario.name


def after_step(context, step):
    if step.status == "failed":
        scenario_step_name = f"{context.scenario_name}_{step.name}"
        DriverAPI(context.browser).take_screenshot(scenario_step_name, Config.screenshot_directory)
