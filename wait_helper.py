from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WaitHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def wait_for_element_visible(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"Element not visible: {locator}")
            return None

    def wait_for_element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            print(f"Element not clickable: {locator}")
            return None

    def wait_for_title_contains(self, text):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.title_contains(text)
            )
        except TimeoutException:
            print(f"Title does not contain text: {text}")
            return False
