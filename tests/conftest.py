import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    chrome_option = Options()
    # chrome_option.add_argument('--headless')
    driver = webdriver.Firefox()
    driver.get('https://magento.softwaretestingboard.com/')
    driver.maximize_window()
    yield driver
    driver.quit()
