import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--width=1366")
    firefox_options.add_argument("--height=768")

    driver = webdriver.Firefox(options=firefox_options)
    driver.get(Urls.MAIN_PAGE_URL)

    yield driver

    driver.quit()
