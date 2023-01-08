from items import StoreItems

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