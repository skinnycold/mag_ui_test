from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from pages.create_account_page import CreateAccountPage
from pages.customer_login_page import CustomerLoginPage

@pytest.fixture()
def driver():
    options = Options()
    options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver


@pytest.fixture()
def account_page(driver):
    init_page = CreateAccountPage(driver)
    return init_page

@pytest.fixture()
def login_page(driver):
    return CustomerLoginPage(driver)