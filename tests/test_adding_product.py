import json

import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductDetailsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


def test_logged_user_add_product_to_shopping_cart(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    product_page = ProductDetailsPage(browser)
    wait = WebDriverWait(browser, 10)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # Go home
    browser.get('https://magento.softwaretestingboard.com/')
    # Go to product page
    home_page.click_product()

    # wait until element apper in page (page Loaded)
    wait.until(expected_conditions.presence_of_element_located(product_page.xs_size))

    # Adding product to cart
    product_page.adding_product_to_cart()

    # wait until loading element finish
    wait.until(expected_conditions.invisibility_of_element(product_page.loading_mask))

    # Assertion the color of message
    assert 'rgb(51, 51, 51)' in browser.find_element(By.CSS_SELECTOR, '.messages').value_of_css_property('color')


def test_logged_user_add_product_to_wish_list(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    product_page = ProductDetailsPage(browser)
    wait = WebDriverWait(browser, 10)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # Go home
    browser.get('https://magento.softwaretestingboard.com/')

    # Go to product page
    home_page.click_product()

    # wait until element apper in page (page Loaded)
    wait.until(expected_conditions.presence_of_element_located(product_page.xs_size))

    # Get product name
    product_name = browser.title

    # Adding product to cart
    product_page.click_add_to_wish_list()

    # Assertion the product in wish list
    assert product_name in product_page.get_products_name()


def test_logged_user_add_product_to_compare(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    product_page = ProductDetailsPage(browser)
    wait = WebDriverWait(browser, 10)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # Go home
    browser.get('https://magento.softwaretestingboard.com/')

    # Go to product page
    home_page.click_product()

    # wait until element apper in page (page Loaded)
    wait.until(expected_conditions.presence_of_element_located(product_page.xs_size))

    # Get product name
    product_name = browser.title

    # Adding product to cart
    product_page.click_add_to_compare()

    # waiting until adding to compare list
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.messages')))

    # Assertion the product in wish list
    assert 'rgb(51, 51, 51)' in browser.find_element(By.CSS_SELECTOR, '.messages').value_of_css_property('color')
