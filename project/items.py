
class StoreItems():

    def __init__(self, name, price, brand, category, storeOnly, inventory):
        self.name = name
        self.price = price
        self.brand = brand
        self.category = category
        self.storeOnly = storeOnly
        self.inventory = inventory

    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

    def get_brand(self):
        return self.brand
    
    def get_category(self):
        return self.category
    
    def get_storeOnly(self):
        return self.storeOnly
    
    def get_inventory(self):
        return self.inventory

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price
    
    def set_brand(self, brand):
        self.brand = brand
    
    def set_category(self, category):
        self.category = category
    
    def set_storeOnly(self, storeOnly):
        self.storeOnly = storeOnly
    
    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Brand: {self.brand}, Category: {self.category}, Store Only: {self.storeOnly}, Inventory: {self.inventory}"