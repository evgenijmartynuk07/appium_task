from .login_page import LoginPage
from framework.search.locators import Locator


class SideBar(LoginPage):

    def sidebar(self):
        self._find_and_click_element(Locator.SIDEBAR_BUTTON)

    def settings(self):
        self._find_and_click_element(Locator.SETTINGS_BUTTON)

    def help(self):
        self._find_and_click_element(Locator.HELP_BUTTON)

    def logs(self):
        self._find_and_click_element(Locator.LOGS_BUTTON)

    def camera(self):
        self._find_and_click_element(Locator.CAMERA_BUTTON)

    def add_space(self):
        self._find_and_click_element(Locator.ADD_BUTTON)


