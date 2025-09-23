import os


class UIConfig:
    PLAYWRIGHT_WAIT_TIMEOUT = 3000


class TestConfig:
    PET_STORE_BASE_URL = os.getenv("PET_STORE_BASE_URL", "https://petstore.swagger.io")
    SHOP_BASE_URL = os.getenv("SHOP_BASE_URL", "http://127.0.0.1")
    SHOP_API_URL = os.getenv("SHOP_API_URL", "http://127.0.0.1:5000")

    UI_CONFIG = UIConfig
