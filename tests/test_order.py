import json
import pytest
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductDetailsPage
from pages.shopping_cart_page import ShoppingCartPage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


def test_crate_order(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    product_page = ProductDetailsPage(browser)
    wait = WebDriverWait(browser, 15)
    shopping_cart_page = ShoppingCartPage(browser)
    checkout_page = CheckoutPage(browser)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    browser.get('https://magento.softwaretestingboard.com/customer/account/')

    wait.until(expected_conditions.presence_of_element_located((By.ID, 'block-collapsible-nav')))

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

    # Go to cart
    browser.get('https://magento.softwaretestingboard.com/checkout/cart/')

    # wait until loading element finish
    wait.until(expected_conditions.presence_of_element_located(shopping_cart_page.checkout_button))

    # Click on checkout button
    shopping_cart_page.click_checkout_button()

    # wait until loading page finish
    wait.until(expected_conditions.invisibility_of_element(product_page.loading_mask))

    # wait until shipping next button be clickable and click on it
    wait.until(expected_conditions.element_to_be_clickable(checkout_page.shipping_next_button))
    checkout_page.click_shipping_next_button()

    # wait until loading page finish
    wait.until(expected_conditions.invisibility_of_element(product_page.loading_mask))

    # wait until shipping place order button be clickable and click on it
    wait.until(expected_conditions.element_to_be_clickable(checkout_page.payment_place_order_button))
    checkout_page.click_payment_place_order_button()

    # wait until loading page finish
    wait.until(expected_conditions.invisibility_of_element(product_page.loading_mask))
    wait.until(expected_conditions.element_to_be_clickable(checkout_page.continue_shopping_button))

    # Assertion page Title
    assert 'Success Page' in browser.title
