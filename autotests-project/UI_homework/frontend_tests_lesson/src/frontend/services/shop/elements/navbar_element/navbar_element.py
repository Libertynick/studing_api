import allure

from UI_homework.frontend_tests_lesson.src.frontend.src.base_page.base_page import BasePage


class NavbarLocators:
    CATALOG_BTN = '//a[text()="Каталог"]'
    CARD_BTN = '//a[text()="Корзина"]'


class NavbarElement:

    def __init__(self, base_page: BasePage):
        self._base_page = base_page

    @allure.step("Открытие страницы каталога")
    def open_catalog_page(self) -> None:
        self._base_page.click(selector=NavbarLocators.CATALOG_BTN)

    @allure.step("Открытие страницы корзины")
    def open_card_page(self) -> None:
        self._base_page.click(selector=NavbarLocators.CARD_BTN)

    @allure.step("Логаут")
    def logout(self):
        pass
