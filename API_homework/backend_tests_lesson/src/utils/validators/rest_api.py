import http
from typing import Optional

import allure
import requests


@allure.step("Проверка валидности ответа")
def validate_response(response: requests.Response, expected_status_code: http.HTTPStatus,
                      expected_text: Optional[str] = None) -> None:
    with allure.step("Проверка статус кода"):
        assert response.status_code == expected_status_code, \
            f"Получен некорректный код ответа: ожидаемый={expected_status_code}, фактический={response.status_code}"

    if expected_text:
        with allure.step("Проверка текста ответа"):
            assert response.text == expected_text, \
                f"Получен некорректный текст ответа : ожидаемый={expected_text}, фактический={response.text}"
