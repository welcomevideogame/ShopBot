
class StoreItems():

    def __init__(self, name, price, brand, category, storeOnly, inventory, id, link):
        self.name = name
        self.price = price
        self.brand = brand
        self.category = category
        self.storeOnly = storeOnly
        self.inventory = inventory
        self.id = id
        self.link = link

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

    def get_id(self):
        return self.id

    def get_link(self):
        return self.link

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
    
    def set_inventory(self, inventory):
        self.inventory = inventory
    
    def set_id(self, id):
        self.id = id

    def set_link(self, link):
        self.link = link
    
    def __str__(self):
        return f"Name: {self.name}\n\tPrice: {self.price}\n\tBrand: {self.brand}\n\tCategory: {self.category}\n\tStore Only: {self.storeOnly}\n\tInventory: {self.inventory}\n\tLink: {self.link}"