#Grasping inheritance first
class Duck(object):
    def __init__(self, flyBehavior, quackBehavior, displayBehavior):#behaviors need to be classes for strat pattern?
        self.flyBehavior = flyBehavior
        self.quackBehavior = quackBehavior
        self.displayBehavior = displayBehavior


class MallardDuck(Duck):
    def __init__(self, flyBehavior, quackBehavior, displayBehavior):
        super().__init__()
