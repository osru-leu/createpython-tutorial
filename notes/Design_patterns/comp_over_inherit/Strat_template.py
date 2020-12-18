#http://www.youtube.com/watch?v=xFOnFjoJBb8 Code below
#https://www.youtube.com/watch?v=sRuem-JQZRE Separate video but outlines the below

class Context:
    def __init__(self):
        self.strategy = None

    def SetStrategy(self, obj):
        self.strategy = obj

    def GetStrategy(self):
        return self.strategy

    def ContextInterface(self):
        self.strategy.AlgorithmInterface()

class Strategy:
    def AlgortihmInterface(self):
        raise NotImplementedError('AlgorithmInterface() must be defined in subclass')

class ConcreteStrategyA(Strategy):
    ''' Agorithm encapsalated by its own strategy class '''
    def AlgorithmInterface(self): 
        print('Inside ConcreteStrategyA: AlgorithmInterface()')

class ConcreteStrategyB(Strategy):
    def AlgorithmInterface(self):
        print('Inside ConcreteStrategyB: AlgorithmInterface()')

class ConcreteStrategyC(Strategy):
    def AlgorithmInterface(self):
        print('Inside ConcreteStrategyC: AlgorithmInterface()')

context = Context() # setting class Context() to var context. Context() Instance object/instantiating an object

conStratA = ConcreteStrategyA() #setting class ConcreteStrategyA to var conStrata
context.SetStrategy(conStratA) # (var)context.(method)SetStragey(var conStratA referencing class ConcreteStrategyA())
context.ContextInterface()

conStratB = ConcreteStrategyB()# concrete strategy object, "conStratB"
context.SetStrategy(conStratB)
context.ContextInterface()

conStratC = ConcreteStrategyC()
context.SetStrategy(conStratC)
context.ContextInterface()