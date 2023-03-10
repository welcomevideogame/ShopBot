from items import StoreItems
import os
import configparser

class Utilities:

    @staticmethod
    def sort_by_price(items: list[StoreItems]) -> list[StoreItems]:
        for item in items:
            item.set_price(float(item.get_price().replace('$', '')))
        items.sort(key=lambda x: x.get_price())
        for item in items:
            item.set_price(f"${item.get_price():.2f}")
        return items

    @staticmethod
    def try_parse_int(value: str) -> int:
        try:
            return int(value)
        except ValueError:
            return None

    @classmethod
    def save_to_csv(cls, filename: str, data: list[StoreItems]):
        cls.check_for_exports()
        with open(f"exports/{filename}.csv", "w") as file:
            file.write("Name,Price,Brand,Category,Store Only,Inventory")
            for item in data:
                file.write(f"\n{item.get_name()},{item.get_price()},{item.get_brand()},{item.get_category()},{item.get_storeOnly()},{item.get_inventory()}")

    @staticmethod
    def check_for_exports():
        if not os.path.exists("exports"):
            os.makedirs("exports")

    @classmethod
    def clean_item_name(cls, products: str) -> str:
        for i in products:
            category = i.get_category()
            if category == "Graphics Cards":
                i = cls.clean_graphics_cards(i)
        return products
    
    @staticmethod
    def clean_graphics_cards(product):
        name = product.get_name()
        elements = name.split(" ")
        product.set_name(f"{product.get_brand()} {elements[2]} {elements[3]}")

    @staticmethod
    def make_product_link(name, id):
        return f"https://www.microcenter.com/product/{id}/{name}".replace(" ", "-").lower()

    @staticmethod
    def get_login_config():
        config = configparser.ConfigParser()
        config.read("./configuration/config.ini")
        config_dict = {}
        for key, value in config.items("login"):
            config_dict[key] = value
        return config_dict