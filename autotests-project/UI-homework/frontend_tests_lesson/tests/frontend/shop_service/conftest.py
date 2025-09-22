import pytest

from frontend_tests_lesson.config import TestConfig
from frontend_tests_lesson.src.frontend.services.shop.pages.catalog_page.catalog_page import CatalogPage
from frontend_tests_lesson.src.frontend.services.shop.pages.login_page.login_page import LoginPage
from frontend_tests_lesson.src.frontend.services.shop.shop_service_pages_manager import ShopServicePagesManager
from frontend_tests_lesson.src.frontend.src.base_page.base_page import BasePage


@pytest.fixture
def shop_base_page(base_page) -> BasePage:
    base_page.open(url=TestConfig.SHOP_BASE_URL)
    return base_page


@pytest.fixture
def login_page(shop_base_page) -> LoginPage:
    return LoginPage(base_page=shop_base_page)


@pytest.fixture
def catalog_page(shop_base_page):
    return CatalogPage(base_page=shop_base_page)


@pytest.fixture
def shop_service_pages_manager_logon(register_user, shop_base_page) -> ShopServicePagesManager:
    pages_manager = ShopServicePagesManager(base_page=shop_base_page)
    pages_manager.login_page.login(username=register_user.username, password=register_user.password)
    return pages_manager
