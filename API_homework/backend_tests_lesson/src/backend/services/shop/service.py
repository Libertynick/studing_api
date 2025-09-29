from API_homework.backend_tests_lesson.src.backend.services.shop.adapter import ShopAdapter


class ShopService:
    def __init__(self, adapter: ShopAdapter):
        self._adapter = adapter

    def get_token(self, username: str, password: str):
        self._adapter.register(username, password)
        resp = self._adapter.login(username, password)
        assert resp.status_code == 200, f"Не удалось залогиниться"
        token = resp.json().get("token")
        assert token, "Нет токена"
        return token