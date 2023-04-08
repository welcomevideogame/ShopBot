# items.pyx
cdef class StoreItems:
    cdef str name
    cdef str price
    cdef str brand
    cdef str category
    cdef str storeOnly
    cdef str inventory
    cdef int id
    cdef str link

    def __init__(self, str name, str price, str brand, str category, str storeOnly, str inventory, int id, str link):
        self.name = name
        self.price = price
        self.brand = brand
        self.category = category
        self.storeOnly = storeOnly
        self.inventory = inventory
        self.id = id
        self.link = link

    cpdef str get_name(self):
        return self.name

    cpdef str get_price(self):
        return self.price

    cpdef str get_brand(self):
        return self.brand

    cpdef str get_category(self):
        return self.category

    cpdef str get_storeOnly(self):
        return self.storeOnly

    cpdef str get_inventory(self):
        return self.inventory

    cpdef int get_id(self):
        return self.id

    cpdef str get_link(self):
        return self.link

    cpdef set_name(self, str name):
        self.name = name

    cpdef set_price(self, str price):
        self.price = price

    cpdef set_brand(self, str brand):
        self.brand = brand

    cpdef set_category(self, str category):
        self.category = category

    cpdef set_storeOnly(self, str storeOnly):
        self.storeOnly = storeOnly

    cpdef set_inventory(self, str inventory):
        self.inventory = inventory

    cpdef set_id(self, int id):
        self.id = id

    cpdef set_link(self, str link):
        self.link = link

    def __str__(self):
        return f"Name: {self.name}\n\tPrice: {self.price}\n\tBrand: {self.brand}\n\tCategory: {self.category}\n\tStore Only: {self.storeOnly}\n\tInventory: {self.inventory}\n\tLink: {self.link}"
