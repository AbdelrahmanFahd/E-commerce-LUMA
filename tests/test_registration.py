import json
import pytest
from pages.creataccount import CreatAccount
from pages.forget_password_page import ForgetPassword
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


@pytest.mark.priority(level=1)
def test_signup(browser: WebDriver, data):
    wait = WebDriverWait(browser, 30)
    homepage = HomePage(browser)
    my_account = CreatAccount(browser)
    homepage.click_registartion()
    my_account.enter_regestration_data(first_name=data['firstname'], last_name=data['Lastname'],
                                       password=data['password'],
                                       mail=data['email'])
    wait.until(expected_conditions.presence_of_element_located((By.ID, 'block-collapsible-nav')))

    assert browser.title == 'My Account', 'Title missMatch'


@pytest.mark.priority(level=2)
def test_login_with_valid_data(browser, data):
    homepage = HomePage(browser)
    homepage.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['email'], password=data['password'])
    assert browser.title == 'Home Page', 'Failed to Login'


@pytest.mark.priority(level=2)
def test_login_with_invalid_data(browser, data):
    homepage = HomePage(browser)
    homepage.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['unValid_email'], password=data['unValid_password'])
    wait = WebDriverWait(browser, 5)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '.message-error div')))
    assert 'Please wait and try again later.' in login_page.get_error_message()


@pytest.mark.priority(level=2)
def test_login_with_blank_email_data(browser, data):
    homepage = HomePage(browser)
    homepage.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email='', password=data['unValid_password'])
    wait = WebDriverWait(browser, 5)
    wait.until(expected_conditions.presence_of_element_located(login_page.email_error_message))
    assert 'This is a required field.' in login_page.get_user_error_message()


@pytest.mark.priority(level=2)
def test_login_with_blank_password_data(browser, data):
    homepage = HomePage(browser)
    homepage.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email=data['unValid_email'], password='')
    wait = WebDriverWait(browser, 5)
    wait.until(expected_conditions.presence_of_element_located(login_page.pass_error_message))
    assert 'This is a required field.' in login_page.get_pass_error_message()


@pytest.mark.priority(level=2)
def test_login_with_blank_data(browser, data):
    homepage = HomePage(browser)
    homepage.click_login()
    login_page = LoginPage(browser)
    login_page.fill_data(email='', password='')
    wait = WebDriverWait(browser, 5)
    wait.until(expected_conditions.presence_of_element_located(login_page.pass_error_message))
    assert 'This is a required field.' in login_page.get_user_error_message()
    assert 'This is a required field.' in login_page.get_pass_error_message()


@pytest.mark.priority(level=2)
def test_forget_password(browser):
    homepage = HomePage(browser)
    homepage.click_login()
    login_page = LoginPage(browser)
    login_page.click_forget_password()
    forget_password = ForgetPassword(browser)
    forget_password.enter_email('test@test.com')
    wait = WebDriverWait(browser, 5)
    wait.until(expected_conditions.presence_of_element_located(login_page.success_message))
    assert 'you will receive an email with a link to reset your password.' in login_page.get_success_message()
