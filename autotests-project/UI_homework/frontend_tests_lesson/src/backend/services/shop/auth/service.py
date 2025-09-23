import http
from typing import Optional

from UI_homework.frontend_tests_lesson.src.backend.services.shop.auth.adapter import ShopAuthAdapter
from UI_homework.frontend_tests_lesson.src.builders.user_builder import User
from UI_homework.frontend_tests_lesson.src.utils.validations.rest_api import validate_response


class ShopAuthService:
    def __init__(self, host: str):
        self._adapter = ShopAuthAdapter(host=host)

    def register_user(self, username: Optional[str] = None, password: Optional[str] = None) -> User:
        user = User.build(username=username, password=password)
        response = self._adapter.register(username=user.username, password=user.password)
        validate_response(response=response, expected_status_code=http.HTTPStatus.OK)
        return user
