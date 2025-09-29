import json
from datetime import datetime

import allure
import pytest
from playwright.sync_api import Browser, sync_playwright, Response, ConsoleMessage, Request

from UI_homework.src.backend.clients.http_client.constants import BINARY_TYPES
from UI_homework.src.frontend.src.base_page.base_page import BasePage
from UI_homework.src.utils.helpers import truncate_body


@pytest.fixture(scope="session")
def browser() -> Browser:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture()
def base_page(browser) -> BasePage:
    context = browser.new_context()
    page = context.new_page()
    yield BasePage(page=page)
    context.close()


@pytest.fixture
def ui_base_url():
    """URL куда заходит браузер"""
    return "http://localhost"


@pytest.fixture
def prepared_user(shop, unique_creds):
    """Создаем пользователя через API для UI тестов"""
    with allure.step("Подготавливаем пользователя для UI тестов"):
        shop.get_token(**unique_creds)  # регистрируем через твое API
        return unique_creds


@allure.step("Сбор логов консоли, запросов и ответов")
@pytest.fixture(scope="function", autouse=True)
def ui_report(base_page, request: pytest.FixtureRequest, tmp_path):
    # Списки для логов
    console_logs = []
    network_logs = []

    # "Сырая" Playwright-страница из вашего BasePage
    playwright_page = base_page.page

    def current_timestamp():
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S.%f")

    def on_console(msg: ConsoleMessage):
        console_logs.append({
            "timestamp": current_timestamp(),
            "type": msg.type,
            "text": msg.text
        })

    def on_request(req: Request):
        data = "binary"
        if req.headers.get("Content-Type") not in BINARY_TYPES:
            data = req.post_data
        if data:
            data = truncate_body(data)
        network_logs.append({
            "timestamp": current_timestamp(),
            "event": "REQUEST",
            "method": req.method,
            "headers": req.headers,
            "resource_type": req.resource_type,
            "data": data,
            "url": req.url
        })

    def on_response(res: Response):
        content_type = res.headers.get("content-type", "").lower()

        if "application/json" in content_type:
            try:
                response_body = res.json()
            except Exception:
                response_body = None
        elif "text/" in content_type:
            try:
                response_body = res.text()
                response_body = truncate_body(str(response_body))
            except Exception:
                response_body = None
        else:
            response_body = None

        network_logs.append({
            "timestamp": current_timestamp(),
            "event": "RESPONSE",
            "status": res.status,
            "url": res.url,
            "response_content_type": content_type,
            "response_body": response_body
        })

    playwright_page.on("console", on_console)
    playwright_page.on("request", on_request)
    playwright_page.on("response", on_response)

    failed_tests_count = request.session.testsfailed
    yield

    if request.session.testsfailed > failed_tests_count:
        screenshot_path = tmp_path / "failure.png"
        base_page.attach_screenshot(path_to_save=str(screenshot_path))

    console_log_path = tmp_path / "console_logs.json"
    with allure.step("Лог консоли"):
        with open(console_log_path, "w", encoding="utf-8") as f:
            json.dump(console_logs, f, ensure_ascii=False, indent=2)

        allure.attach(
            console_log_path.read_text(encoding="utf-8"),
            name="console_logs.json",
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Логи сети"):
        network_log_path = tmp_path / "network_logs.json"
        with open(network_log_path, "w", encoding="utf-8") as f:
            json.dump(network_logs, f, ensure_ascii=False, indent=2)

        allure.attach(
            network_log_path.read_text(encoding="utf-8"),
            name="network_logs.json",
            attachment_type=allure.attachment_type.JSON
        )

    playwright_page.remove_listener("console", on_console)
    playwright_page.remove_listener("request", on_request)
    playwright_page.remove_listener("response", on_response)


@pytest.fixture
def shop_pages_manager_clean(base_page, ui_base_url):
    """Менеджер страниц БЕЗ автологина - для тестов логина"""
    from ...src.frontend.services.shop.shop_pages_manager import ShopPagesManager

    base_page.open(ui_base_url)
    return ShopPagesManager(base_page=base_page)

@pytest.fixture
def shop_pages_manager_logon(base_page, ui_base_url, prepared_user):
    """Менеджер страниц с залогиненным пользователем"""
    from ...src.frontend.services.shop.shop_pages_manager import ShopPagesManager

    with allure.step("Логинимся в UI"):
        base_page.open(ui_base_url)
        pages_manager = ShopPagesManager(base_page=base_page)
        pages_manager.login_page.login(
            username=prepared_user["username"],
            password=prepared_user["password"]
        )
    return pages_manager