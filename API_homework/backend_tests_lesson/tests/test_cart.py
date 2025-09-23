import allure
import pytest


@allure.title("Тест на получение корзины c поврежденным токеном")
def test_get_cart_with_broken_token(shop_adapter):
    result = shop_adapter.get_cart(token="broken.token")
    assert result.status_code == 401

@allure.title("Тест на добавление в корзину товара с поврежденным токеном")
def test_add_to_cart_with_broken_token(shop_adapter):
    result = shop_adapter.add_item(token="broken.token", item_id=1, quantity=1)
    assert result.status_code == 401

@allure.title("Тест на добавление товара в корзину и проверку наличия товара в корзине")
def test_cart_add_item(shop, shop_adapter, unique_creds):
    token = shop.get_token(**unique_creds)
    with allure.step("Получаем каталог"):
        catalog = shop_adapter.get_catalog(token=token)

    with allure.step("Добавляем в корзину первый товар из полученного каталога"):
        item_id = catalog.json()[0]["id"]
        add = shop_adapter.add_item(token=token, item_id=item_id, quantity=1)
        assert add.status_code == 200

    with allure.step("Получаем корзину и проверяем наличие ранее добавленного товара"):
        cart = shop_adapter.get_cart(token=token)
        items = cart.json()["items"]
        assert any(i.get("item_id") == item_id for i in items)

    with allure.step("Чистим корзину"):
        shop_adapter.remove_item(token=token, item_id=item_id)

@allure.title("Тест на отображение 2х добавленных товаров в корзине")
def test_cart_add_quantity_two(shop, shop_adapter, unique_creds):
    token = shop.get_token(**unique_creds)

    with allure.step("Получаем каталог"):
        catalog = shop_adapter.get_catalog(token=token)

    with allure.step("Добавляем 2шт первого товара в полученном ранее каталоге"):
        item_id = catalog.json()[0]["id"]
        shop_adapter.add_item(token=token, item_id=item_id, quantity=2)

    with allure.step("Получаем корзину с лежащими в ней товарами"):
        cart = shop_adapter.get_cart(token=token)
        items = cart.json()["items"]

    with allure.step("Проверяем наличие 2шт выбранного товара в корзине"):
        qty = next(i["quantity"] for i in items if i["item_id"] == item_id)
        assert qty == 2

@allure.title("Тест на удаление из корзины товара")
def test_cart_check_removes_item(shop, shop_adapter, unique_creds):
    token = shop.get_token(**unique_creds)

    with allure.step("Получаем каталог"):
        catalog = shop_adapter.get_catalog(token=token)

    with allure.step("Добавляем товар первый товар из полученного каталога"):
        item_id = catalog.json()[0]["id"]
        shop_adapter.add_item(token=token, item_id=item_id, quantity=1)

    with allure.step("Очищаем корзину"):
        remove = shop_adapter.remove_item(token=token, item_id=item_id)
        assert remove.status_code == 200

    with allure.step("Получаем корзину и проверяем, что нет добавленного раннее товара"):
        cart = shop_adapter.get_cart(token=token)
        items = cart.json()["items"]
        assert all(i["item_id"] != item_id for i in items)

@allure.title("Добавление товара с невалидным количеством")
@pytest.mark.skip(reason="BUG: приходит 200 код вместо 400")
@pytest.mark.parametrize("bad_qty", [0, -1])
def test_cart_add_bad_quantity_item(shop, shop_adapter, unique_creds, bad_qty):
    token = shop.get_token(**unique_creds)
    catalog = shop_adapter.get_catalog(token=token)
    item_id = catalog.json()[0]["id"]

    result = shop_adapter.add_item(token=token, item_id=item_id, quantity=bad_qty)
    assert result.status_code == 400

@allure.title("Добавление товара с несуществующим айди")
@pytest.mark.skip(reason="BUG: приходит 500 код вместо 400")
@pytest.mark.parametrize("bad_id", [0, -1, 999999])
def test_cart_add_bad_id_item(shop, shop_adapter, unique_creds, bad_id):
    token = shop.get_token(**unique_creds)

    result = shop_adapter.add_item(token=token, item_id=bad_id, quantity=2)
    assert result.status_code == 400



