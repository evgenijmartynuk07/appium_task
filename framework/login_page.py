from .page import Page


class LoginPage(Page):
    EMAIL_INPUT = ('id', 'com.ajaxsystems:id/authLoginEmail')
    PASSWORD_INPUT = ('id', 'com.ajaxsystems:id/authLoginPassword')
    LOGIN_BUTTON = ('id', 'com.ajaxsystems:id/authLogin')

    def login(self, username, password):
        self.find_element(self.EMAIL_INPUT).send_keys(username)

        self.find_element(self.PASSWORD_INPUT).send_keys(password)

        self.click_element(self.LOGIN_BUTTON)
