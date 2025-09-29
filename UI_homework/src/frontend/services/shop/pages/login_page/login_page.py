import allure

from .....src.base_page.base_page import BasePage


class LoginPageLocators:
    USERNAME_INPUT = '//input[@placeholder="Имя пользователя"]'
    PASSWORD_INPUT = '//input[@placeholder="Пароль"]'
    LOGIN_BTN = '//button[@class="auth-btn"]'
    ERROR_MSG = '//div[@class="error-msg"]'


class LoginPage:

    def __init__(self, base_page: BasePage):
        self._base_page = base_page

    @allure.step("Логин пользователя")
    def login(self, username: str, password: str):
        self._base_page.fill(selector=LoginPageLocators.USERNAME_INPUT, value=username)
        self._base_page.fill(selector=LoginPageLocators.PASSWORD_INPUT, value=password)
        self._base_page.click(selector=LoginPageLocators.LOGIN_BTN)

    @allure.step("Получение сообщения об ошибке")
    def get_error_message(self):
        return self._base_page.get_text(selector=LoginPageLocators.ERROR_MSG)