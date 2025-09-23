import random

import allure
from faker.proxy import Faker

pytestmark = [allure.feature("Тесты на логин")]


def test_login_valid_creds(register_user, login_page):
    login_page.login(username=register_user.username, password=register_user.password)


def test_login_no_valid_username(register_user, login_page):
    login_page.login(username=Faker().user_name(), password=register_user.password)
    login_page.check_error_msg()


def test_login_no_valid_password(register_user, login_page):
    login_page.login(username=register_user.username, password=Faker().password(length=random.randint(1, 10_000)))
    login_page.check_error_msg()


def test_login_empty_creds(login_page):
    login_page.login()
    login_page.check_error_msg()
