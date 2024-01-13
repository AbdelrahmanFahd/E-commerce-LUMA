import json

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver



@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


def test_unlogged_user_search_product(browser: WebDriver):
    product = 'shirt'
    home_page = HomePage(browser)
    home_page.search_for_product(product)

    assert product in browser.title, 'Can\'t Search for product'


def test_logged_user_search_product(browser: WebDriver, data):
    product = 'shirt'
    home_page = HomePage(browser)
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])
    home_page.search_for_product(product)

    assert product in browser.title, 'Can\'t Search for product'
