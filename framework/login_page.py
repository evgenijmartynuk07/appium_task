from .page import Page
from framework.search.locators import Locator


class LoginPage(Page):

    def login(self, username, password):

        self._find_and_click_element(Locator.LOGIN_BUTTON)

        username_input = self._find_element(Locator.USERNAME_INPUT)
        self._clear_element(username_input)
        self._send_keys_to_element(username_input, username)

        password_input = self._find_element(Locator.PASSWORD_INPUT)
        self._clear_element(password_input)
        self._send_keys_to_element(password_input, password)

        self._find_and_click_element(Locator.SUBMIT_BUTTON)

    def logout(self):
        self._find_and_click_element(Locator.SIDEBAR_BUTTON)

        self._find_and_click_element(Locator.SETTINGS_BUTTON)

        self._find_and_click_element(Locator.LOGOUT_BUTTON)

    def is_logged_in(self):
        try:
            element = self._find_element(Locator.SIDEBAR_BUTTON)
            if element:
                return True
            return False
        except ValueError:
            return False
