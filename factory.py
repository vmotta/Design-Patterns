from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def sound(self):
        pass

class Cachorro(Animal):
    def sound(self) -> None:
        print("au au au")

class Gato(Animal):
    def sound(self) -> None:
        print("miau miau")

class Factory(object):
    def get_sound(self, object_type) -> str:
        return eval(object_type)().sound()

if __name__ == '__main__':
    f = Factory()
    f.get_sound('Gato')
    f.get_sound('Cachorro')