import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    """Фикстура для драйвера Chrome."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура для драйвера Firefox."""
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
