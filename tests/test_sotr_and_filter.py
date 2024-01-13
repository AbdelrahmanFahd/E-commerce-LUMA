from time import sleep
from pages.home_page import HomePage
from pages.productsPage import ProductsPage
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


def test_user_can_sort_product_by_name(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)
    wait = WebDriverWait(browser, 10)
    action = ActionChains(browser)
    men = browser.find_element(*home_page.men_menu_bar)
    tops = browser.find_element(*home_page.tops_men_bar)
    jackets = browser.find_element(*home_page.jackets_tops_men_bar)
    tanks = browser.find_element(*home_page.tanks_tops_men_bar)

    # Go to Tanks Page
    action.move_to_element(men).move_to_element(tops).move_to_element(jackets).click(tanks).perform()

    # wait until Page load
    wait.until(expected_conditions.presence_of_element_located(products_page.sort_by_title))

    # Select dropDown button and select name
    select = Select(products_page.get_sortBySelector())
    select.select_by_value('name')
    sleep(2)

    # get products name
    product_names = products_page.get_product_names()

    # remove none from names
    product_names = list(filter(None, product_names))

    # Assertion that products sorted successfully
    assert product_names == sorted(product_names), 'Products are not sorted by name'


def test_user_can_sort_product_by_price(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)
    wait = WebDriverWait(browser, 10)
    action = ActionChains(browser)
    men = browser.find_element(*home_page.men_menu_bar)
    tops = browser.find_element(*home_page.tops_men_bar)
    jackets = browser.find_element(*home_page.jackets_tops_men_bar)
    tanks = browser.find_element(*home_page.tanks_tops_men_bar)

    # Go to Tanks Page
    action.move_to_element(men).move_to_element(tops).move_to_element(jackets).click(tanks).perform()

    # wait until Page load
    wait.until(expected_conditions.presence_of_element_located(products_page.sort_by_title))

    # Select dropDown button and select name
    select = Select(products_page.get_sortBySelector())
    select.select_by_value('price')
    sleep(2)

    # get products name
    products_price = products_page.get_products_price()

    # remove none from names
    products_price = list(filter(None, products_price))

    # Assertion that products sorted successfully
    assert products_price == sorted(products_price), 'Products are not sorted by price'


def test_user_can_sort_product_by_style(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)
    wait = WebDriverWait(browser, 10)
    action = ActionChains(browser)
    men = browser.find_element(*home_page.men_menu_bar)
    tops = browser.find_element(*home_page.tops_men_bar)
    jackets = browser.find_element(*home_page.jackets_tops_men_bar)
    tanks = browser.find_element(*home_page.tanks_tops_men_bar)

    # Go to Tanks Page
    action.move_to_element(men).move_to_element(tops).move_to_element(jackets).click(tanks).perform()

    # wait until Page load
    wait.until(expected_conditions.presence_of_element_located(products_page.sort_by_title))

    products_page.click_tank_style()

    wait.until(expected_conditions.presence_of_element_located(products_page.filter_title))

    # Assertion that products sorted successfully
    assert products_page.get_filter_value() == 'Tank', 'Products are not sorted by Style ( Tank )'


def test_user_can_sort_product_by_size(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)
    wait = WebDriverWait(browser, 10)
    action = ActionChains(browser)
    men = browser.find_element(*home_page.men_menu_bar)
    tops = browser.find_element(*home_page.tops_men_bar)
    jackets = browser.find_element(*home_page.jackets_tops_men_bar)
    tanks = browser.find_element(*home_page.tanks_tops_men_bar)

    # Go to Tanks Page
    action.move_to_element(men).move_to_element(tops).move_to_element(jackets).click(tanks).perform()

    # wait until Page load
    wait.until(expected_conditions.presence_of_element_located(products_page.sort_by_title))

    # Click to S Size
    products_page.click_s_size()

    # wait until filter finish
    wait.until(expected_conditions.presence_of_element_located(products_page.filter_title))

    # Assertion that products sorted by size successfully
    assert products_page.get_filter_value() == 'S', 'Products are not sorted by Size ( S )'


def test_user_can_sort_product_by_sale(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)
    wait = WebDriverWait(browser, 10)
    action = ActionChains(browser)
    men = browser.find_element(*home_page.men_menu_bar)
    tops = browser.find_element(*home_page.tops_men_bar)
    jackets = browser.find_element(*home_page.jackets_tops_men_bar)
    tanks = browser.find_element(*home_page.tanks_tops_men_bar)

    # Go to Tanks Page
    action.move_to_element(men).move_to_element(tops).move_to_element(jackets).click(tanks).perform()

    # wait until Page load
    wait.until(expected_conditions.presence_of_element_located(products_page.sort_by_title))

    # Click to S Size
    products_page.click_sale()

    # wait until filter finish
    wait.until(expected_conditions.presence_of_element_located(products_page.filter_title))

    # Assertion that products sorted by size successfully
    assert products_page.get_filter_value() == 'Yes', 'Products are not sorted by Size ( S )'


def test_user_can_clear_filter(browser: WebDriver):
    # definition tha objects
    home_page = HomePage(browser)
    products_page = ProductsPage(browser)
    wait = WebDriverWait(browser, 10)
    action = ActionChains(browser)
    men = browser.find_element(*home_page.men_menu_bar)
    tops = browser.find_element(*home_page.tops_men_bar)
    jackets = browser.find_element(*home_page.jackets_tops_men_bar)
    tanks = browser.find_element(*home_page.tanks_tops_men_bar)

    # Go to Tanks Page
    action.move_to_element(men).move_to_element(tops).move_to_element(jackets).click(tanks).perform()

    # wait until Page load
    wait.until(expected_conditions.presence_of_element_located(products_page.sort_by_title))

    # Click to clear
    products_page.click_style_size_clear()

    try:
        # Attempt to find the element
        browser.find_element(*products_page.filter_title)

        # If the element is found,
        assert False

    except NoSuchElementException:
        # Handle the case where the element is not found
        assert True
