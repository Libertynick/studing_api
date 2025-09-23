from enum import StrEnum
from typing import Optional

import allure
from requests import Response

from UI_homework.frontend_tests_lesson.src.backend.clients.http_client.client import HTTPClient


class Route(StrEnum):
    __BASE = "/auth"
    REGISTER = f"{__BASE}/register"


class ShopAuthAdapter:

    def __init__(self, host: str, route: Route = Route):
        self.__http_client = HTTPClient(host=host)
        self._route = route

    @allure.step("Регистрация нового пользователя {username}")
    def register(self, username: Optional[str] = None, password: Optional[str] = None) -> Response:
        data = {}
        if username:
            data["username"] = username
        if password:
            data["password"] = password

        return self.__http_client.post(route=self._route.REGISTER, json=data)
