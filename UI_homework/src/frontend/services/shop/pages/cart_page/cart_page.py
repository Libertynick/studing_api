import allure
from .....src.base_page.base_page import BasePage


class CartPageLocators:
    CART_LINK = '//a[text()="Корзина"]'
    CART_ITEMS = '//div[@data-id="cart-item"]'
    REMOVE_BTN = '//button[text()="Удалить"]'
    CHECKOUT_BTN = '//button[text()="Оформить заказ"]'
    TOTAL_PRICE = '//div[@class="total-price"]'


class CartPage:

    def __init__(self, base_page: BasePage):
        self._base_page = base_page

    @allure.step("Открытие корзины")
    def open_cart(self):
        self._base_page.click(selector=CartPageLocators.CART_LINK)

    @allure.step("Получение количества товаров в корзине")
    def get_cart_items_count(self):
        items = self._base_page.get_all_elements(selector=CartPageLocators.CART_ITEMS)
        return len(items)

    @allure.step("Получение информации о товарах в корзине")
    def get_cart_items_info(self):
        items_elements = self._base_page.get_all_elements(selector=CartPageLocators.CART_ITEMS)
        items_info = []
        for item_element in items_elements:
            item_text = item_element.text_content()
            items_info.append(item_text)
        return items_info

    @allure.step("Удаление первого товара из корзины")
    def remove_first_item(self):
        first_remove_btn = self._base_page.get_all_elements(selector=CartPageLocators.REMOVE_BTN)[0]
        first_remove_btn.click()

    @allure.step("Оформление заказа")
    def checkout(self):
        self._base_page.click(selector=CartPageLocators.CHECKOUT_BTN)

    @allure.step("Получение общей суммы заказа")
    def get_total_price(self):
        return self._base_page.get_text(selector=CartPageLocators.TOTAL_PRICE)