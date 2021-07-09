# keep only object and offer one global acces in a point
# create object one turn and no more after this


class Singleton(object):

    def __new__(cls):
        """ Control for the instanciate objects

        Returns:
            cls.instance: instance of this object
        """

        # verify if this attribute 'instance' already exists 
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

class LazySingleton(object):

    __instance = None

    def __init__(self) -> None:
        if not LazySingleton.__instance:
            print('Method __init__ was called')
        else:
            print('One instance was already created', self.obter_instancia())
    
    @classmethod
    def obter_instancia(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

class MonoStateSingleton(object):
    __estado_compartilhado = {'1': '2'}

    def __init__(self):
        self.x = 1
        # use __dict__ to store all states of one class
        self.__dict__ = self.__estado_compartilhado


if __name__ == '__main__':
    b1 = MonoStateSingleton()
    b2 = MonoStateSingleton()
    b1.x=5
    b2.x=10
    print(b1)
    print(b2)
    print(b1.__dict__)
    print(b2.__dict__)

    # s1 = Singleton()
    # print(s1)
    # s2 = Singleton()
    # print(s2)
    # l1 = LazySingleton()
    # LazySingleton.obter_instancia()
    # print('Objeto criado: ', l1.obter_instancia())
    # l2 = LazySingleton()
    #print(l2)
