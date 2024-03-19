from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple):
        strategy, value = locator
        strategy = strategy.lower()
        supported_strategies = {'id': MobileBy.ID, 'xpath': MobileBy.XPATH}
        
        if strategy not in supported_strategies:
            raise ValueError(f"Unsupported locator strategy: {strategy}. Use: 'id', 'xpath'")
        
        try:
            return self.driver.find_element(supported_strategies[strategy], value)
        except NoSuchElementException:
            raise ValueError(f"Unsupported value: {value}. Please check!")

    @staticmethod
    def click_element(element):
        try:
            element.click()
        except WebDriverException as e:
            raise f'Error clicking element: {e}'
