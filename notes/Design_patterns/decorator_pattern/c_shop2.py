class Beverage():
    def cost(self):
        return 0

class Espresso(Beverage):
    def cost(self):
        return 2

class Addon(Beverage):
    def __init__(self, bev, cnt = 1):
        self.beverage = bev
        self.count = cnt
    def cost(self):
        pass

class CaramelAddon(Addon):
    def cost(self):
        return self.beverage.cost() + (3 * self.count)

class WhipCreamAddon(Addon):
    def cost(self):
        return self.beverage.cost() + (1 * self.count)

print(WhipCreamAddon(CaramelAddon(Espresso())).cost())

choc = 'chocolate'
print(CaramelAddon(choc)) # prints object: <__main__.CaramelAddon object at 0x010AE628>

base = 'coffee'

new_drink = CaramelAddon(choc).cost()
print(new_drink.cost())