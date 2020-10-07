from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_browser_by_type():
    browser = input("Enter browser using:")
    options = Options()
    options.headless = True
    if browser == "Chrome":
        driver = webdriver.Chrome("drivers/chromedriver", options=options)
    elif browser == "Firefox":
        webdriver.Firefox("drivers/geckodriver", options=options)
    elif browser == "Safari":
        webdriver.Safari()  # ??

