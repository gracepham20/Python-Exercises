from selenium import webdriver
from selenium.webdriver.chrome.options import Options as COptions
from selenium.webdriver.firefox.options import Options as FOptions


def get_browser_by_type():
    browser = input("Enter browser using:")

    if browser == "Chrome":
        options = COptions()
        options.headless = True
        driver = webdriver.Chrome("drivers/chromedriver", options=options)
    elif browser == "Firefox":
        options = FOptions()
        options.headless = True
        driver = webdriver.Firefox("drivers/geckodriver", options=options)
    elif browser == "Safari":
        driver = webdriver.Safari()
