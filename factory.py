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
    def create_object(self, object_type) -> str:
        return eval(object_type)()

if __name__ == '__main__':
    f = Factory()
    f.create_object('Gato').sound()
    f.create_object('Cachorro').sound()