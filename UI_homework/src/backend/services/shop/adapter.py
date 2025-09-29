import requests
from .routes import Route


class ShopAdapter:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def register(self, username: str, password: str):
        return requests.post(f"{self.base_url}{str(Route.REGISTER)}", json={
            "username": username,
            "password": password
        })

    def login(self, username: str, password: str):
        return requests.post(f"{self.base_url}{Route.LOGIN}", json={
            "username": username,
            "password": password
        })

    def get_cart(self, token: str):
        return requests.get(
            f"{self.base_url}{Route.GET_CART}",
            headers={"Authorization": f"Bearer {token}"}
        )

    def add_item(self, token: str, item_id: int, quantity: int):
        return requests.post(
            f"{self.base_url}{Route.ADD_ITEM}",
            headers={"Authorization": f"Bearer {token}"},
            json={"item_id": item_id, "quantity": quantity}
        )

    def remove_item(self, token: str, item_id: int):
        return requests.post(
            f"{self.base_url}{Route.REMOVE_ITEM}",
            headers={"Authorization": f"Bearer {token}"},
            json={"item_id": item_id}
        )

    def get_catalog(self, token: str = None):
        headers = {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        return requests.get(f"{self.base_url}/catalog/", headers=headers)
