
class StoreItems():

    def __init__(self, name, price, brand, category):
        self.name = name
        self.price = price
        self.brand = brand
        self.category = category

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

    def get_brand(self):
        return self.brand
    
    def get_category(self):
        return self.category
    
    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price
    
    def set_brand(self, brand):
        self.brand = brand
    
    def set_category(self, category):
        self.category = category
    
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Brand: {self.brand}, Category: {self.category}"