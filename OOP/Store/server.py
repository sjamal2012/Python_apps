class Store(object):
    def __init__(self, products, location, owner):
        self.products = []
        self.location = location
        self.owner = owner

    def add_prodcut(self, product):
        self.products.append(product)
        return self

    def remove_product(self, product):
        if product in self.products:
            self.products.pop(self.products.index(product))
        return self

    def inventory(self):
            print self.products

product_1 = {'name' :"PS4", 'price' : 200, 'weight': "2 lbs"}
product_2 = {'name' :"Xbox", 'price' : 199.99, 'weight': "2 lbs"}
store1 = Store(product_1, "LA", "Sammy")

#funtions
store1.add_product(product_1).add_prodcut(product_2)
store1.remove_product(product_1)
#display data
print store1.inventory()
