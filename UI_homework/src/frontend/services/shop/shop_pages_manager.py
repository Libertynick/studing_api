from .pages.login_page.login_page import LoginPage
from .pages.catalog_page.catalog_page import CatalogPage
from .pages.cart_page.cart_page import CartPage
from ...src.base_page.base_page import BasePage


class ShopPagesManager:

    def __init__(self, base_page: BasePage):
        self.login_page = LoginPage(base_page=base_page)
        self.catalog_page = CatalogPage(base_page=base_page)
        self.cart_page = CartPage(base_page=base_page)