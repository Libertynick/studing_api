import pytest
from API_homework.backend_tests_lesson.src.backend.services.shop.adapter import ShopAdapter
import uuid
import allure
import os
from dotenv import load_dotenv

from API_homework.backend_tests_lesson.src.backend.services.shop.service import ShopService

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "http://localhost:5000")

@pytest.fixture
def shop_adapter(base_url):
    return ShopAdapter(base_url)

@pytest.fixture
def shop(shop_adapter):
    return ShopService(shop_adapter)

@pytest.fixture(scope="function")
def unique_creds():
    with allure.step("Генерируем уникальные логин/пароль"):
        return {
            "username": f"user_{uuid.uuid4().hex[:8]}",
            "password": "QaTest123"
        }