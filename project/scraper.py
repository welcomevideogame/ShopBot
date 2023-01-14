from bs4 import BeautifulSoup
import requests
from items import StoreItems
from utilities import Utilities

from urllib.parse import urlparse, parse_qs
import urllib

class Scraper:

    class MicroCenter:
        products = []
        items = []

        def __init__(self, url):
            self.url = url

        def __init__(self):
            pass

        def set_url(self, url):
            self.url = url
    
        def scrape_items(self, pagination):
            url_list = [self.url]
            if pagination:
                url = urlparse(self.url)
                query_params = parse_qs(url.query)
                current_page = int(query_params['page'][0])
                left, right = current_page, 100
                mid = 0
                while left <= right:
                    mid = (left + right) // 2
                    query_params['page'] = mid
                    new_url = url._replace(query=urllib.parse.urlencode(query_params, doseq=True))
                    response = requests.get(new_url.geturl())
                    soup = BeautifulSoup(response.content, "html.parser")
                    temp_items = soup.find_all("li", class_="product_wrapper")
                    if temp_items:
                        left = mid + 1
                    else:
                        right = mid - 1
                for i in range(current_page, mid):
                    query_params['page'] = i
                    new_url = url._replace(query=urllib.parse.urlencode(query_params, doseq=True))
                    url_list.append(new_url.geturl())
            for url in url_list:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, "html.parser")
                temp_items = soup.find_all("li", class_="product_wrapper")
                if temp_items:
                    self.items.extend(temp_items)
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
            if options["Filter out of stock"]:
                self.products = [product for product in self.products if product.get_inventory() != 0]
            if options["Sort by price"]:
                Utilities.sort_by_price(self.products)
            if options["Simple view"]:
                self.products = Utilities.clean_item_name(self.products)
            for product in self.products:
                print(product)

        def clear_items(self):
            self.products.clear()
    