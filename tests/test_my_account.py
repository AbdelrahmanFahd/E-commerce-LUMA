import json
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


def test_logged_user_can_view_account_information(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    my_account_page = MyAccount(browser)
    wait = WebDriverWait(browser, 30)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # go to My account
    browser.get('https://magento.softwaretestingboard.com/customer/account/')

    wait.until(expected_conditions.presence_of_element_located((By.ID, 'block-collapsible-nav')))
    assert 'Account Information' in my_account_page.get_page_titles(), 'Could not login successfully'


def test_logged_user_can_view_my_order(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    my_account_page = MyAccount(browser)
    wait = WebDriverWait(browser, 30)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # go to My account
    browser.get('https://magento.softwaretestingboard.com/customer/account/')

    wait.until(expected_conditions.presence_of_element_located((By.ID, 'block-collapsible-nav')))

    my_account_page.click_my_order_page()

    assert 'My Orders' in browser.title, 'Could not view my Order successfully'


def test_logged_user_can_view_my_wish_list(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    my_account_page = MyAccount(browser)
    wait = WebDriverWait(browser, 30)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # go to My account
    browser.get('https://magento.softwaretestingboard.com/customer/account/')

    wait.until(expected_conditions.presence_of_element_located((By.ID, 'block-collapsible-nav')))

    my_account_page.click_my_wish_list_page()

    assert 'My Wish List' in browser.title, 'Could not view my Order successfully'


def test_logged_user_can_add_address_book(browser: WebDriver, data):
    # definition tha objects
    home_page = HomePage(browser)
    my_account_page = MyAccount(browser)
    wait = WebDriverWait(browser, 15)

    # login
    home_page.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])

    # go to My account
    browser.get('https://magento.softwaretestingboard.com/customer/account/')

    wait.until(expected_conditions.presence_of_element_located((By.ID, 'block-collapsible-nav')))

    my_account_page.click_address_book()

    my_account_page.fill_address_data(company='ieee', phone='5551002983', street1='hello', street2='hhhhhh',
                                      street3='kjahsdk', zip='123334', city='cairo', country='AQ',
                                      region='9')

    assert 'Address Book' in browser.title, 'Could not view my Order successfully'
