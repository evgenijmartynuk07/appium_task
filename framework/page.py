from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import (
    TimeoutException,
    WebDriverException,
    StaleElementReferenceException,
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:

    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator: tuple):
        strategy, value = locator
        strategy = strategy.lower()
        supported_strategies = {'id': AppiumBy.ID, 'xpath': AppiumBy.XPATH}
        
        if strategy not in supported_strategies:
            raise ValueError(
                f"Unsupported locator strategy: {strategy}. Use: 'id', 'xpath'"
            )
        
        try:
            element = WebDriverWait(self.driver, timeout=10).until(
                EC.presence_of_element_located(
                    (supported_strategies[strategy], value)
                )
            )
            return element
        except TimeoutException:
            raise ValueError(
                f"Unsupported value: {value} or {strategy}. Please check!"
            )

    def _clear_element(self, element):
        try:
            element.clear()
        except StaleElementReferenceException:
            element = self._find_element(element)
            element.clear()

    def _send_keys_to_element(self, element, keys):
        try:
            element.send_keys(keys)
        except StaleElementReferenceException:
            element = self._find_element(element)
            element.send_keys(keys)

    def get_back(self):
        self.driver.back()

    @staticmethod
    def _click_element(element):
        try:
            element.click()
        except WebDriverException as e:
            raise f'Error clicking element: {e}'

    def _find_and_click_element(self, element_locator):
        element = self._find_element(element_locator)
        if element:
            self._click_element(element)
