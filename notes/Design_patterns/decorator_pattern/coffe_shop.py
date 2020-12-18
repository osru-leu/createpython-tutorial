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

addons = [WhipCreamAddon, CaramelAddon, WhipCreamAddon]
base = Espresso()
for addon in addons:
    base = addon(base)
print(f'result={base.cost()}')

#type this out
# maybe do a new one 
# do a recursions tut