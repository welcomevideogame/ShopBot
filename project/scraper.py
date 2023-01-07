from bs4 import BeautifulSoup
import requests
from items import StoreItems

class Scraper:

    class MicroCenter:
        products = []

        def __init__(self, url):
            self.url = url

        def set_url(self, url):
            self.url = url
    
        def scrape_items(self):
            response = requests.get(self.url)
            soup = BeautifulSoup(response.content, "html.parser")
            self.items = soup.find_all("li", class_="product_wrapper")
            self.make_items_obj()

        def make_items_obj(self):
            for item in self.items:
                div = item.find("div", class_="h2")
                a = div.find('a')
                name, price, brand, category = a['data-name'], a['data-price'], a['data-brand'], a['data-category']
                print
                item_obj = StoreItems(name, price, brand, category)
                self.products.append(item_obj)
        
        def print_items(self):
            for product in self.products:
                print(product)

    