import json
from typing import Any, Optional

import allure


def assert_eq(
        actual_value: Any,
        expected_value: Any,
        allure_title: str,
        error_msg: Optional[str] = None,

):
    with allure.step(allure_title):
        try:
            assert actual_value == expected_value, error_msg or f"Сравниваемые значения не равны"
        except AssertionError:
            attach_response = {
                "Actual_value": str(actual_value),
                "Expected_value": str(expected_value),
            }
            _allure_attach_error(attach_response, "Values comparison error")
            raise


def _allure_attach_error(attach_response: dict, error_name: str):
    allure.attach(
        json.dumps(
            attach_response,
            indent="\t",
            separators=(",", ": "),
            ensure_ascii=False,
        ),
        error_name,
        attachment_type=allure.attachment_type.JSON,
    )
