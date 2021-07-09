# keep only object and offer one global acces in a point
# create object one turn and no more after this


class Singleton(object):
    """ Singleton class 
    """

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
    """ Lazy instanciate singleton's object
    """

    __instance = None # initiate this atribute's value with None 

    def __init__(self) -> None:
        print('tipo: ',type(self))
        if not LazySingleton.__instance:
            print('Method __init__ was called')
        else:
            print('One instance was already created', self.obter_instancia())
    
    @classmethod
    def obter_instancia(cls) -> type(__instance): # this method belongs at this class else it can used without to create object, but using the name of this class 
        if not cls.__instance:
            cls.__instance = LazySingleton()
        return cls.__instance

class MonoStateSingleton(object):
    """ MonoStateSingleton store state in all objects
    """
    __estado_compartilhado = {'1': '2'} # variable that holds state

    def __init__(self) -> None:
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

    s1 = Singleton()
    print(s1)
    s2 = Singleton()
    print(s2)
    l1 = LazySingleton()
    LazySingleton.obter_instancia()
    print('Objeto criado: ', l1.obter_instancia())
    l2 = LazySingleton()
    print(l2)
