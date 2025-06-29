import pytest
from selenium import webdriver
from utilities.config_reader import get_config

@pytest.fixture
def setup():
    config = get_config()
    browser = config["browser"]

    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception("Unsupported browser in config.yaml")

    driver.maximize_window()
    yield driver
    driver.quit()
