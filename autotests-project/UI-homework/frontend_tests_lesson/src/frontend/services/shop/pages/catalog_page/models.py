import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class Good:
    title: str  # Название или модель продукта, например, "Iphone14 1024GB"
    brand: str  # Бренд, например, "Apple"
    price: int  # Цена в рублях, например, 165000
    memory: str  # Объём памяти, например, "1024GB"
    screen_size: float  # Размер экрана в дюймах, например, 6.1
    color: str  # Цвет, например, "White"
    index: Optional[int] = None

    @classmethod
    def from_string(cls, text: str) -> 'Good':
        """
        Парсит строку с описанием продукта и возвращает экземпляр Product.

        Пример входной строки:
        "Iphone14 1024GBБренд: Apple165000 руб.Memory: 1024GB. Screen: 6.1 inch. Color: White.Добавить в корзину"
        """
        # Определяем название до ключевого слова "Бренд:"
        parts = text.split("Бренд:")
        if len(parts) > 1:
            title = parts[0].strip()
            remaining_text = "Бренд:" + parts[1]
        else:
            title = ""
            remaining_text = text

        # Извлекаем бренд (после "Бренд:")
        brand_match = re.search(r"Бренд:\s*([A-Za-z]+)", remaining_text)
        brand = brand_match.group(1) if brand_match else ""

        # Извлекаем цену (число перед "руб")
        price_match = re.search(r"(\d+)\s*руб", remaining_text)
        price = int(price_match.group(1)) if price_match else 0

        # Извлекаем объём памяти после "Memory:" до точки
        memory_match = re.search(r"Memory:\s*([^\.]+)\.", remaining_text)
        memory = memory_match.group(1).strip() if memory_match else ""

        # Извлекаем размер экрана после "Screen:" (ожидается число с плавающей точкой)
        screen_match = re.search(r"Screen:\s*([\d\.]+)\s*inch", remaining_text)
        screen_size = float(screen_match.group(1)) if screen_match else 0.0

        # Извлекаем цвет после "Color:" до точки
        color_match = re.search(r"Color:\s*([^\.]+)\.", remaining_text)
        color = color_match.group(1).strip() if color_match else ""

        return cls(
            title=title,
            brand=brand,
            price=price,
            memory=memory,
            screen_size=screen_size,
            color=color
        )
