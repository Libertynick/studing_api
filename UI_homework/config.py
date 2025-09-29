import os


class UIConfig:
    PLAYWRIGHT_WAIT_TIMEOUT = 3000


class TestConfig:
    BASE_URL = os.getenv("BASE_URL", "http://localhost:5000")
    SHOP_UI_URL = os.getenv("SHOP_UI_URL", "http://localhost")
    UI_CONFIG = UIConfig