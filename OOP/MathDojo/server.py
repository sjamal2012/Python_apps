from animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150


    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170


    def fly(self):
        self.health -= 10
        return self

    def display_health(self, animal):
        print Animal.display_health(animal)
        print "I am a dragon!"

animal1 = Animal("Cougar")
print animal1.walk().walk().walk().run().run().display_health()

animal2 = Dog("Skippy")
print animal2.walk().walk().walk().run().run().pet().display_health()

animal3 = Dragon("Sleepy")
print animal3.fly().display_health(animal3)
