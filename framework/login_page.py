from .page import Page
from framework.search.locators import Locator


class LoginPage(Page):

    def login(self, username, password):

        self.find_and_click_element(Locator.LOGIN_BUTTON)

        username_input = self.find_element(Locator.USERNAME_INPUT)
        self.clear_element(username_input)
        self.send_keys_to_element(username_input, username)

        password_input = self.find_element(Locator.PASSWORD_INPUT)
        self.clear_element(password_input)
        self.send_keys_to_element(password_input, password)

        self.find_and_click_element(Locator.SUBMIT_BUTTON)

    def logout(self):
        self.find_and_click_element(Locator.SIDEBAR_BUTTON)

        self.find_and_click_element(Locator.SETTINGS_BUTTON)

        self.find_and_click_element(Locator.LOGOUT_BUTTON)

    def is_logged_in(self):
        try:
            element = self.find_element(Locator.SIDEBAR_BUTTON)
            return bool(element)
        except ValueError:
            return False
