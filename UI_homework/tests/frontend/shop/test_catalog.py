import allure


@allure.feature("Тесты каталога")
class TestCatalog:

    @allure.title("Тест отображения товаров в каталоге")
    def test_catalog_shows_items(self, shop_pages_manager_logon):
        shop_pages_manager_logon.catalog_page.open_catalog()
        items_count = shop_pages_manager_logon.catalog_page.get_items_count()

        assert items_count > 0, f"Каталог пустой, товаров: {items_count}"

    @allure.title("Тест добавления товара в корзину")
    def test_add_item_to_cart(self, shop_pages_manager_logon):
        shop_pages_manager_logon.catalog_page.open_catalog()
        shop_pages_manager_logon.catalog_page.add_first_item_to_cart()

    @allure.title("Тест фильтра по бренду Apple")
    def test_filter_by_apple_brand(self, shop_pages_manager_logon):
        shop_pages_manager_logon.catalog_page.open_catalog()
        all_items_count = shop_pages_manager_logon.catalog_page.get_items_count()

        shop_pages_manager_logon.catalog_page.filter_by_brand("Apple")
        filtered_items_count = shop_pages_manager_logon.catalog_page.get_items_count()

        assert filtered_items_count <= all_items_count, "Фильтр должен уменьшить или оставить количество товаров"

    @allure.title("Тест фильтра по несуществующему бренду")
    def test_filter_by_nonexistent_brand(self, shop_pages_manager_logon):
        shop_pages_manager_logon.catalog_page.open_catalog()
        shop_pages_manager_logon.catalog_page.filter_by_brand("НесуществующийБренд123")

        filtered_items_count = shop_pages_manager_logon.catalog_page.get_items_count()
        assert filtered_items_count == 0, f"Должно быть 0 товаров, найдено: {filtered_items_count}"