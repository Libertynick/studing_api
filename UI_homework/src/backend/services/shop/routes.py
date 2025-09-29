from enum import StrEnum

class Route(StrEnum):
    REGISTER = "/auth/register"
    LOGIN = "/auth/login"
    GET_CART = "/cart/"
    ADD_ITEM = "/cart/add"
    REMOVE_ITEM = "/cart/remove"
    GET_CATALOG = "/catalog/"
