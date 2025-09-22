from frontend_tests_lesson.src.frontend.services.shop.elements.navbar_element.navbar_element import NavbarElement
from frontend_tests_lesson.src.frontend.src.base_page.base_page import BasePage


class CardPage:

    def __init__(self, base_page: BasePage):
        self._base_page = base_page
        self.navbar_elem = NavbarElement(self._base_page)

    def open(self) -> 'CardPage':
        self.navbar_elem.open_card_page()
        return self
