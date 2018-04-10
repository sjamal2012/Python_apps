class Bike(object):
    def __init__(self, price, max_speed, miles = 0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        print "The price of this bike is " + str(self.price) + ", its max speed is " + str(self.max_speed) + " and it has "+ str(self.miles) + " miles on it."

    def ride(self):
        print "Riding"
        self.miles += 10
        print self.miles
        return self

    def reverse(self):
        print "Reversing"
        self.miles -= 5
        print self.miles
        return self

bike1 = Bike(200, "30mph")
print bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(100, "20mph")
print bike2.ride().ride().reverse().reverse().displayInfo()

bike2 = Bike(300, "60mph")
print bike2.reverse().reverse().reverse().displayInfo()

#could implement an if function that grabs the value of self.miles to prevent negative numbers
