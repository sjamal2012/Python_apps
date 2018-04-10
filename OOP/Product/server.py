class Product(object):
    def __init__(self, price, item_name, weight, brand, status = "for sale"):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status

    def Sell(self):
        self.status = "sold"
        return self

    def Add_tax(self, tax):
        self.tax = 0.09
        self.price = self.price + (0.09*self.price)
        return self

    def Return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
            return self
        elif reason == "opened":
            self.status = "used"
            self.price = self.price*0.80
            return self
        else:
            self.status = "for sale"
            return self

    def Display_info(self):
            print "Price: $" + str(self.price)
            print "Name: " + str(self.item_name)
            print "Weight: " + str(self.weight)
            print "Brand: " + str(self.brand)
            print "Satus: " + str(self.status)

product1 = Product(200, "PS4", "2 lbs", "Sony")
print product1.Sell().Display_info()

print product1.Return("defective").Display_info()

product2 = Product(199.00, "xbox", "2 lbs", "Microsoft")
print product2.Add_tax(0.8).Sell().Display_info()

print product2.Return("opened").Display_info()
