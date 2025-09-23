## [register] При регистрации неверное сообщение об ошибке выдается

- **Тест**: `test_register_short_login_and_password`
- **Ожидаемо**: Username does not match the criteria
- **Фактически**: Invalid data
- **Параметры**: ("ab", "QaTest123", "Username does not match the criteria"),
        ("validuser", "123", "Password does not match the criteria"),
        ("", "QaTest123", "Username does not match the criteria"),
        ("validuser", "", "Password does not match the criteria"),
- **Статус**: ❗️Баг при регистрации, сообщение об ошибке не соответсвет требованиям


## [register] Ошибка при регистрации невалидных занчений

- **Тест**: `test_register_invalid_boundary_values`
- **Ожидаемо**: Username does not match the criteria
- **Фактически**: User exists
- **Параметры**:   # Граничные значения для логина
         ("user1", "QaTest123!", "Username does not match the criteria"),  # 5 символов - невалидный

         # Невалидные символы в логине
         ("user@12", "QaTest123!", "Username does not match the criteria"),  # спецсимволы в логине
         ("пользователь", "QaTest123!", "Username does not match the criteria"),  # русские буквы
         ("user 12", "QaTest123!", "Username does not match the criteria"),  # пробел в логине

         # Граничные значения для пароля
         ("validuser", "QaTest!", "Password does not match the criteria"),
         # 7 символов - невалидный

         # Пароль без обязательных символов
         ("validuser", "qatest123!", "Password does not match the criteria"),  # без заглавной
         ("validuser", "QATEST123!", "Password does not match the criteria"),  # без строчной
         ("validuser", "QaTest123", "Password does not match the criteria"),  # без спецсимвола
         ("validuser", "QaTest!!!", "Password does not match the criteria"),  # без цифр
- **Статус**: ❗️Баг при регистрации, как может существовать невалидный пользователь ?! 


## [cart] Ошибка при добавлении товара с несуществующим ID

- **Тест**: `test_cart_add_bad_id_returns_400`
- **Ожидаемо**: 400 Bad Request
- **Фактически**: 500 Internal Server Error
- **Параметры**: `item_id` = 0, -1, 999999
- **Статус**: ❗️Баг на стороне сервера



## [cart] Ошибка при добавлении количества товара 0, -1

- **Тест**: `test_cart_add_bad_quantity_returns_400`
- **Ожидаемо**: 400 Bad Request
- **Фактически**: 200
- **Параметры**: 'bad_qty' = 0, -1
- **Статус**: ❗️Баг при создании приложения

