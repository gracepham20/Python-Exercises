from behave import *
from selenium import webdriver

from Selenium.pageobjectmodel.driver_api import DriverAPI
from Selenium.pageobjectmodel.pom.home.homepage import HomePage
from Selenium.pageobjectmodel.pom.home.paymentmethod import PaymentMethodModal
from Selenium.pageobjectmodel.pom.home.pricingpage import PricingPage
from Selenium.pageobjectmodel.pom.landing.landingpage import LandingPage
from Selenium.pageobjectmodel.pom.landing.loginmodal import LoginModal
from Selenium.pageobjectmodel.test.config import Config


@given("I'm at the landing page")
def step_impl(context):
    context.browser.get(Config.baseUrl)
    assert LandingPage(context.browser).is_present()


@when("I click on log-in button at the landing page")
def step_impl(context):
    LandingPage(context.browser).click_login_button()


@then("I should see log-in modal pop up")
def step_impl(context):
    assert LoginModal(context.browser).is_present()


@when("I enter login email and password")
def step_impl(context):
    login_modal = LoginModal(context.browser)
    login_modal.enter_login_email(Config.login_email)
    login_modal.enter_login_password(Config.login_pass)


@when("I click log into my account")
def step_impl(context):
    # t = context.table
    # t["user"]
    #print("step1")
    LoginModal(context.browser).click_to_login()


@then("I should be at the home page")
def step_impl(context):
    assert HomePage(context.browser).is_present()


@then("I should be able to get the information about my current session balance")
def step_impl(context):
    context.balance_before = HomePage(context.browser).get_session_balance()


@when("I click on pricing tab")
def step_impl(context):
    HomePage(context.browser).click_pricing_tab()


@then("I should be redirected to pricing page")
def step_impl(context):
    assert PricingPage(context.browser).is_present()


@when("I click on the first pricing plan")
def step_impl(context):
    PricingPage(context.browser).choose_pricing_plan(0)


@then("I should see the payment method modal pop up")
def step_impl(context):
    assert PaymentMethodModal(context.browser).is_present()


@when("I choose to pay with card")
def step_impl(context):
    payment_method_modal = PaymentMethodModal(context.browser)
    payment_method_modal.pay_by_another_method()
    payment_method_modal.click_option_paybycard()
    payment_method_modal.purchase()
    payment_method_modal.submit_payment()


@when("I wait for payment method modal to dismiss")
def step_impl(context):
    PaymentMethodModal(context.browser).wait_for_payment_modal_dismissed()


@when("I relocate to home page")
def step_impl(context):
    context.browser.get(Config.homepageUrl)
    HomePage(context.browser).is_present()


@then("I should see an increase in my session balance")
def step_impl(context):
    balance_after = HomePage(context.browser).get_session_balance()
    assert context.balance_before <= balance_after, "Payment Unsuccessful!"
