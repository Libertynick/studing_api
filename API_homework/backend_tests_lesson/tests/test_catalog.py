import allure


@allure.title("Тест на существование в каталоге товаров")
def test_catalog_have_items(shop,shop_adapter, unique_creds):
    token = shop.get_token(**unique_creds)
    with allure.step("Получаем каталог"):
        result = shop_adapter.get_catalog(token=token)
        assert result.status_code == 200, result.text
    with allure.step("Проверяем наличие в каталоге товаров"):
        data = result.json()
        assert len(data) > 0
        assert all("id" in i for i in data)


@allure.title("Тест на невозможность получения каталога с битым токеном")
def test_catalog_with_invalid_token(shop_adapter):
    result = shop_adapter.get_catalog(token="invalid.token.here")
    assert result.status_code == 401

@allure.title("Тест на невозможность получения каталога без токена")
def test_catalog_without_token(shop_adapter):
    result = shop_adapter.get_catalog()
    assert result.status_code == 401
