import json
import pytest
from pages.home_page import HomePage
from pages.product_page import ProductDetailsPage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


def test_user_view_product_details(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    product_page = ProductDetailsPage(browser)
    wait = WebDriverWait(browser, 10)

    # Go to product page
    home_page.click_product()

    # wait until element apper in page (page Loaded)
    wait.until(expected_conditions.presence_of_element_located(product_page.xs_size))

    # assertion Page Title
    assert browser.title == 'Radiant Tee'


def test_user_view_reviews(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    product_page = ProductDetailsPage(browser)
    wait = WebDriverWait(browser, 10)

    # Go to product page
    home_page.click_product()

    # wait until element apper in page (page Loaded)
    wait.until(expected_conditions.presence_of_element_located(product_page.xs_size))

    product_page.click_review_button()

    wait.until(expected_conditions.presence_of_element_located(product_page.review_title))

    # assertion Page Title
    assert 'You\'re reviewing' in product_page.get_review_title()
