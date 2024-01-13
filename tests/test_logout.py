import json
from time import sleep

import pytest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccount
from pages.product_page import ProductDetailsPage
from pages.shopping_cart_page import ShoppingCartPage
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


def test_logged_user_can_logout(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    wait = WebDriverWait(browser, 15)
    my_account_page = MyAccount(browser)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # wait until page loaded
    wait.until(expected_conditions.presence_of_element_located(home_page.customer_menu_toggle))

    # Click on customer menu toggle then logout submenu
    browser.find_element(*home_page.customer_menu_toggle).click()
    browser.find_element(*home_page.logout_menu_toggle).click()

    print(browser.title)
