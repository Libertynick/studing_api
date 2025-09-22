import random
import time

import allure

pytestmark = [allure.feature("Тесты на каталог")]


def test_get_all_catalog(shop_service_pages_manager_logon):
    all_goods = shop_service_pages_manager_logon.catalog_page.get_all_goods()
    time.sleep(5)
    shop_service_pages_manager_logon.catalog_page.add_good_to_cart(random.choice(all_goods))
    time.sleep(5)
    card_page = shop_service_pages_manager_logon.card_page.open()
    card_page.navbar_elem.open_catalog_page()
    shop_service_pages_manager_logon.catalog_page.open()

    time.sleep(5)


def test_filter_by_existed_brand(shop_service_pages_manager_logon):
    pass


def test_filter_by_no_existed_brand(shop_service_pages_manager_logon):
    pass
