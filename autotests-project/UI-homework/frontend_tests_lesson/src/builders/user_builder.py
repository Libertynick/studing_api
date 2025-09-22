import random
import string
from dataclasses import dataclass
from typing import Optional

import allure
from faker import Faker

MIN_PASSWORD_LENGTH = 8
MIN_USERNAME_LENGTH = 6


@dataclass
class User:
    username: str
    password: str

    @classmethod
    @allure.step("Генерация пользователя")
    def build(cls, username: Optional[str] = None, password: Optional[str] = None,
              min_username_length: int = MIN_USERNAME_LENGTH, min_password_length: int = MIN_PASSWORD_LENGTH) -> 'User':
        faker = Faker()

        if not username:
            allowed_chars = string.ascii_letters
            length = random.randint(min_username_length, min_username_length + random.randint(0, 20))

            username = "".join(random.choices(allowed_chars, k=length))

        if not password:
            password = faker.password(
                length=random.randint(min_password_length, min_password_length + random.randint(0, 20)),
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,

            )

        return cls(username=username, password=password)
