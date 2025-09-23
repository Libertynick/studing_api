import http
from typing import Optional

import allure
from requests import Response


@allure.step("Проверка валидности ответа")
def validate_response(response: Response, expected_status_code: http.HTTPStatus,
                      expected_text: Optional[str] = None) -> None:
    # если нужно можно добавить еще какие-то проверки, например на хедеры и тд

    with allure.step("Проверка статус кода"):
        assert response.status_code == expected_status_code, \
            f"Получен некорректный код ответа: ожидаемый={expected_status_code}, фактический={response.status_code}"

    if expected_text:
        with allure.step("Проверка текста"):
            assert response.text == expected_text, \
                f"Получен некорректный текст ответа: ожидаемый={expected_text}, фактический={response.text}"
