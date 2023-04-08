# utilities.pyx
from cpython cimport array
from items cimport StoreItems
import os
import configparser
from typing import Optional, List
cimport cython

cdef class Utilities:

    @staticmethod
    @cython.boundscheck(False)
    @cython.wraparound(False)
    cpdef list[StoreItems] sort_by_price(list[StoreItems] items) -> list[StoreItems]:
        cdef StoreItems item
        for item in items:
            item.set_price(float(item.get_price().replace('$', '')))
        items.sort(key=lambda x: x.get_price())
        for item in items:
            item.set_price(f"${item.get_price():.2f}")
        return items

    @staticmethod
    cpdef Optional[int] try_parse_int(str value) -> Optional[int]:
        try:
            return int(value)
        except ValueError:
            return None

    @classmethod
    cpdef save_to_csv(cls, str filename, list[StoreItems] data):
        cls.check_for_exports()
        with open(f"exports/{filename}.csv", "w") as file:
            file.write("Name,Price,Brand,Category,Store Only,Inventory")
            for item in data:
                file.write(f"\n{item.get_name()},{item.get_price()},{item.get_brand()},{item.get_category()},{item.get_storeOnly()},{item.get_inventory()}")

    @staticmethod
    cpdef check_for_exports():
        if not os.path.exists("exports"):
            os.makedirs("exports")

    @classmethod
    cpdef str clean_item_name(cls, str products) -> str:
        cdef StoreItems i
        for i in products:
            category = i.get_category()
            if category == "Graphics Cards":
                i = cls.clean_graphics_cards(i)
        return products

    @staticmethod
    cpdef clean_graphics_cards(StoreItems product):
        cdef str name = product.get_name()
        cdef list[str] elements = name.split(" ")
        product.set_name(f"{product.get_brand()} {elements[2]} {elements[3]}")

    @staticmethod
    cpdef str make_product_link(str name, int id) -> str:
        return f"https://www.microcenter.com/product/{id}/{name}".replace(" ", "-").lower()

    @staticmethod
    cpdef dict[str, str] get_login_config() -> dict[str, str]:
        cdef configparser.ConfigParser config = configparser.ConfigParser()
        config.read("./configuration/config.ini")
        cdef dict[str, str] config_dict = {}
        cdef str key, value
        for key, value in config.items("login"):
            config_dict[key] = value
        return config_dict