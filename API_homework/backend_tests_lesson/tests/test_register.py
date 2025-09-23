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

@pytest.mark.parametrize("username, password, expected_message",
    [
        ("ab", "QaTest123", "Username does not match the criteria"),
        ("validuser", "123", "Password does not match the criteria"),
        ("", "QaTest123", "Username does not match the criteria"),
        ("validuser", "", "Password does not match the criteria"),
    ])
@allure.title("Тест на регистрацию пользователя с коротким логином")
def test_register_short_login_and_password(shop_adapter, username, password, expected_message):
    result = shop_adapter.register(username=username, password=password)
    assert result.status_code == 400
    assert result.json().get("message") == expected_message

@pytest.mark.parametrize("username, password, expected_message",
     [
         # Граничные значения для логина
         ("user1", "QaTest123!", "Username does not match the criteria"),  # 5 символов - невалидный

         # Невалидные символы в логине
         ("user@12", "QaTest123!", "Username does not match the criteria"),  # спецсимволы в логине
         ("пользователь", "QaTest123!", "Username does not match the criteria"),  # русские буквы
         ("user 12", "QaTest123!", "Username does not match the criteria"),  # пробел в логине

         # Граничные значения для пароля
         ("validuser", "QaTest!", "Password does not match the criteria"),
         # 7 символов - невалидный

         # Пароль без обязательных символов
         ("validuser", "qatest123!", "Password does not match the criteria"),  # без заглавной
         ("validuser", "QATEST123!", "Password does not match the criteria"),  # без строчной
         ("validuser", "QaTest123", "Password does not match the criteria"),  # без спецсимвола
         ("validuser", "QaTest!!!", "Password does not match the criteria"),  # без цифр
     ])
@allure.title("Тест невалидных граничных значений для регистрации")
def test_register_invalid_boundary_values(shop_adapter, username, password, expected_message):
    result = shop_adapter.register(username=username, password=password)
    assert result.status_code == 400
    assert result.json().get("message") == expected_message