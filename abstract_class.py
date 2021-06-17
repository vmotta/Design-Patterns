# importação da biblioteca abc que contém a meta-classe para usar na classe abstrata
import abc

# classe abstrata
class ClasseAbstrata:
    # usando a metaclasse para criar uma classe abstrata
    __metaclass__ = abc.ABCMeta
    # defininco o método abstrato
    @abc.abstractclassmethod
    def metodo_a_ser_implementado(self, input):
        pass

class ClasseConcreta(ClasseAbstrata):
    # implementando o método abstrato
    def metodo_a_ser_implementado(self, input):
        print(input)

a = ClasseConcreta()
print(a.metodo_a_ser_implementado('oi'))    