from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple):

        strategy, value = locator
        try:
            if strategy.lower() == "id":
                element = self.driver.find_element(MobileBy.ID, value)
            elif strategy.lower() == 'xpath':
                element = self.driver.find_element(MobileBy.XPATH, value)
            else:
                raise ValueError(
                    f"Unsupported locator strategy: {strategy}. "
                    f"Use: 'id', 'xpatch'"
                )
            return element
        except NoSuchElementException:
            raise ValueError(
                f"Unsupported value: {value}. Please check!"
            )

    @staticmethod
    def click_element(element):
        try:
            element.click()
        except WebDriverException as e:
            raise f'Error: {e}'

