from abc import ABC, abstractmethod

class Fighter:
    def __init__(self, kick=None):
        self.kick = kick

    def setKickBehavior(self, obj):
        self.kick = obj

    def getKickBehavior(self):
        return self.kick

    def contextInterface(self):
        print('------------contextInterface method accessed: class Fighter()-----------------')
        self.kick.kickBehavior()

class kick(ABC):
    @abstractmethod
    def kickBehavior(self):
        ''' abstract method because it doesnt have a definition only a declaration '''
        raise NotImplementedError('kickBehavior() must be defined in subclass')

class tornadoKick(kick):
    print('------------tornadoKick class accessed------------------')
    def kickBehavior(self):
        print('Tornado keeeeeick!')

class lightningKick(kick):
    print('------------lightningKick class accessed----------------')
    def kickBehavior(self):
        print('Lightning Keeeeeick!')

Instance_obj_chun_li = Fighter(tornadoKick())
#Instance_obj_chun_li.contextInterface()

attack = tornadoKick()
#Instance_obj_chun_li.setKickBehavior(attack)
Instance_obj_chun_li.contextInterface()

attack = lightningKick()
Instance_obj_chun_li.setKickBehavior(attack)
Instance_obj_chun_li.contextInterface()


ryu = Fighter()

attack = tornadoKick()
ryu.setKickBehavior(attack)
ryu.contextInterface()

