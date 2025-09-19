import allure
import pytest


@allure.title("Тест на успешную регистрацию")
def test_register_success(shop_adapter, unique_creds):
    result = shop_adapter.register(**unique_creds)
    assert result.status_code == 200
    assert result.json().get("message") == 'Registration successful'

@allure.title("Тест на регистрацию такого же юзера")
def test_register_duplicate_user(shop_adapter, unique_creds):
    result1 = shop_adapter.register(**unique_creds)
    assert result1.status_code == 200
    result2 = shop_adapter.register(**unique_creds)
    assert result2.status_code == 400

@pytest.mark.parametrize("username, password, expected_code",
    [
        ("ab", "QaTest123", 400),        # короткий логин
        ("validuser", "123", 400),       # короткий пароль
        ("", "QaTest123", 400),          # пустой логин
        ("validuser", "", 400),          # пустой пароль
    ])
@allure.title("Тест на регистрацию пользователя с коротким логином")
def test_register_short_login_and_password(shop_adapter, username, password, expected_code):
    result = shop_adapter.register(username=username, password=password)
    assert result.status_code == expected_code
