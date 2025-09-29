import allure


@allure.feature("Тесты логина")
class TestLogin:

    @allure.title("Тест успешного логина")
    def test_successful_login(self, shop_pages_manager_clean, prepared_user):
        shop_pages_manager_clean.login_page.login(
            username=prepared_user["username"],
            password=prepared_user["password"]
        )

        # Проверяем успешный логин - URL изменился
        current_url = shop_pages_manager_clean.login_page._base_page.page.url
        assert "login" not in current_url.lower(), f"Остались на странице логина: {current_url}"

    @allure.title("Тест логина с неправильным паролем")
    def test_login_wrong_password(self, shop_pages_manager_clean, prepared_user):
        shop_pages_manager_clean.login_page.login(
            username=prepared_user["username"],
            password="wrong_password"
        )

        error_message = shop_pages_manager_clean.login_page.get_error_message()
        assert "Invalid credentials" in error_message, f"Неверное сообщение об ошибке: '{error_message}'"

    @allure.title("Тест логина с неправильным логином")
    def test_login_wrong_username(self, shop_pages_manager_clean, prepared_user):
        shop_pages_manager_clean.login_page.login(
            username="wrong_username",
            password=prepared_user["password"]
        )

        error_message = shop_pages_manager_clean.login_page.get_error_message()
        assert "Invalid credentials" in error_message, f"Неверное сообщение об ошибке: '{error_message}'"

    @allure.title("Тест логина с пустым логином")
    def test_login_empty_username(self, shop_pages_manager_clean):
        shop_pages_manager_clean.login_page.login(
            username="",
            password="somepassword"
        )

        error_message = shop_pages_manager_clean.login_page.get_error_message()
        assert "Invalid credentials" in error_message, f"Неверное сообщение об ошибке: '{error_message}'"

    @allure.title("Тест логина с пустым паролем")
    def test_login_empty_password(self, shop_pages_manager_clean, prepared_user):
        shop_pages_manager_clean.login_page.login(
            username=prepared_user["username"],
            password=""
        )

        error_message = shop_pages_manager_clean.login_page.get_error_message()
        assert "Invalid credentials" in error_message, f"Неверное сообщение об ошибке: '{error_message}'"

    @allure.title("Тест логина с пустыми полями")
    def test_login_empty_fields(self, shop_pages_manager_clean):
        shop_pages_manager_clean.login_page.login(username="", password="")

        error_message = shop_pages_manager_clean.login_page.get_error_message()
        assert "Invalid credentials" in error_message, f"Неверное сообщение об ошибке: '{error_message}'"