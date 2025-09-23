import pytest

from UI_homework.frontend_tests_lesson.config import TestConfig
from UI_homework.frontend_tests_lesson.src.backend.services.shop.auth.service import ShopAuthService
from UI_homework.frontend_tests_lesson.src.builders.user_builder import User


@pytest.fixture
def shop_auth_service() -> ShopAuthService:
    return ShopAuthService(host=TestConfig.SHOP_API_URL)


@pytest.fixture
def register_user(shop_auth_service) -> User:
    user = shop_auth_service.register_user()
    return user
