import json

import pytest
from pages.home_page import HomePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture
def data() -> dict:
    with open('config.json') as data_file:
        data: dict = json.load(data_file)
    return data


def test_user_can_hover_in_men_tops_tanks_and_select_tanks(browser: WebDriver):
    action = ActionChains(browser)
    home_page = HomePage(browser)

    men = browser.find_element(*home_page.men_menu_bar)
    tops = browser.find_element(*home_page.tops_men_bar)
    jackets = browser.find_element(*home_page.jackets_tops_men_bar)
    tanks = browser.find_element(*home_page.tanks_tops_men_bar)

    action.move_to_element(men)
    action.move_to_element(tops)
    action.move_to_element(jackets)
    action.click(tanks).perform()

    wait = WebDriverWait(browser, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'block-subtitle')))
    assert 'Tanks' in browser.title, 'could not go to Tanks'


def test_user_can_select_sale(browser: WebDriver):
    home_page = HomePage(browser)
    home_page.click_sale_menu()

    assert 'Sale' in browser.title, 'could not go to Tanks'


def test_user_can_hover_in_gear_and_select_watches(browser: WebDriver):
    action = ActionChains(browser)
    home_page = HomePage(browser)

    gear = browser.find_element(*home_page.gear_menu_bar)
    watches = browser.find_element(*home_page.watches_gear_bar)

    action.move_to_element(gear)
    action.click(watches).perform()

    wait = WebDriverWait(browser, 10)
    wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'block-subtitle')))
    assert 'Watches' in browser.title, 'could not go to Watches'
