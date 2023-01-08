from bs4 import BeautifulSoup
import requests
from items import StoreItems
from utilities import Utilities

class Scraper:

    class MicroCenter:
        products = []

        def __init__(self, url):
            self.url = url

        def __init__(self):
            pass

        def set_url(self, url):
            self.url = url
    
        def scrape_items(self):
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, "html.parser")
            self.items = soup.find_all("li", class_="product_wrapper")
            self.make_items_obj()

        def make_items_obj(self):
            for item in self.items:
                storeOnly, inventory = self.clean_stock_string(item)
                div = item.find("div", class_="h2")
                a = div.find('a')
                name, price, brand, category = a['data-name'], a['data-price'], a['data-brand'], a['data-category']
                item_obj = StoreItems(name, price, brand, category, storeOnly, inventory)
                self.products.append(item_obj)
        
        def clean_stock_string(self, item):
            stock = item.find("div", class_="stock")
            inventory = stock.find('span', {'class': 'inventoryCnt'})
            if inventory:
                storeOnly = "Buy In Store" in stock.text
                inventory = inventory.text.split()[0]
                return storeOnly, inventory
            else:
                return False, 0
                

        def print_items(self, options):
            if options["Filter out store only"]:
                self.products = [product for product in self.products if not product.get_storeOnly()]
            if options["Sort by price"]:
                Utilities.sort_by_price(self.products)
            for product in self.products:
                print(product)

        def clear_items(self):
            self.products.clear()
    