import allure

@allure.title("Тест на успешный вход и наличие токена")
def test_login_success_returns_token(shop_adapter, unique_creds):
    with allure.step("Регистрируем пользователя"):
        result_reg = shop_adapter.register(**unique_creds)
        assert result_reg.status_code == 200
    with allure.step("Логинимся и проверяем наличие токена"):
        result = shop_adapter.login(**unique_creds)
        assert result.status_code == 200, result.text
        assert "token" in result.json()

@allure.title("Тест на логин несуществующего пользователя без токена")
def test_login_nonexistent_user(shop_adapter, unique_creds):
    with allure.step("Логинимся под несуществующим пользователем"):
        result = shop_adapter.login(**unique_creds)

    with allure.step("Проверяем 401 и отсутствие токена"):
        assert result.status_code == 401
        assert not result.json().get("token")

@allure.title("Тест на логин с неверным паролем")
def test_login_wrong_password(shop_adapter, unique_creds):
    bad = {
        "username": unique_creds["username"],
        "password": unique_creds["password"] + "X"
    }
    with allure.step("Регистрируем пользователя"):
        result_reg = shop_adapter.register(**unique_creds)
        assert result_reg.status_code == 200
    with allure.step("Логинимся под неверным паролем"):
        result = shop_adapter.login(**bad)
    assert result.status_code == 401
    assert not result.json().get("token")