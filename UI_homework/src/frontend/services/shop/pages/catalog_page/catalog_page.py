import allure
from .....src.base_page.base_page import BasePage


class CatalogPageLocators:
    ITEM_CARD = '//div[@data-id="item-card"]'
    ADD_TO_CART_BTN = '//button[text()="Добавить в корзину"]'
    BRAND_FILTER = '//input[@placeholder="Фильтр по бренду"]'
    CATALOG_LINK = '//a[text()="Каталог"]'


class CatalogPage:

    def __init__(self, base_page: BasePage):
        self._base_page = base_page

    @allure.step("Открытие страницы каталога")
    def open_catalog(self):
        self._base_page.click(selector=CatalogPageLocators.CATALOG_LINK)

    @allure.step("Получение всех товаров")
    def get_all_items(self):
        items_elements = self._base_page.get_all_elements(selector=CatalogPageLocators.ITEM_CARD)
        items_data = []
        for item_element in items_elements:
            item_text = item_element.text_content()
            items_data.append(item_text)
        return items_data

    @allure.step("Добавление первого товара в корзину")
    def add_first_item_to_cart(self):
        first_add_btn = self._base_page.get_all_elements(selector=CatalogPageLocators.ADD_TO_CART_BTN)[0]
        first_add_btn.click()

    @allure.step("Поиск товаров по бренду")
    def filter_by_brand(self, brand_name: str):
        self._base_page.fill(selector=CatalogPageLocators.BRAND_FILTER, value=brand_name)

    @allure.step("Получение количества товаров на странице")
    def get_items_count(self):
        items = self._base_page.get_all_elements(selector=CatalogPageLocators.ITEM_CARD)
        return len(items)