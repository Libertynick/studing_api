from typing import Optional

import allure

from frontend_tests_lesson.src.frontend.src.base_page.base_page import BasePage
from frontend_tests_lesson.src.utils.validations.assert_wrappers import assert_eq

INVALID_CREDS_ERROR_MSG = "Invalid credentials"


class LoginPageLocators:
    USERNAME_INPUT = 'input[placeholder="Имя пользователя"]'
    PASSWORD_INPUT = 'input[placeholder="Пароль"]'
    LOGIN_BTN = '//button[@class="auth-btn"]'
    ERROR_MSG = '.error-msg123'


class LoginPage:

    def __init__(self, base_page: BasePage):
        self._base_page = base_page

    @allure.step("Логин пользователя")
    def login(self, username: Optional[str] = None, password: Optional[str] = None) -> 'LoginPage':
        if username:
            self._base_page.fill(selector=LoginPageLocators.USERNAME_INPUT, value=username)
        if password:
            self._base_page.fill(selector=LoginPageLocators.PASSWORD_INPUT, value=password)
        self._base_page.click(selector=LoginPageLocators.LOGIN_BTN)

        return self

    @allure.step("Проверка сообщения об ошибке")
    def check_error_msg(self):
        self._base_page.expect(selector=LoginPageLocators.ERROR_MSG).to_be_attached()
        actual_text = self._base_page.get_text(selector=LoginPageLocators.ERROR_MSG)
        assert_eq(actual_value=actual_text, expected_value=INVALID_CREDS_ERROR_MSG,
                  allure_title="Проверка сообщения об ошибке", )
