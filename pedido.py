from abc import abstractmethod, ABCMeta
from datetime import date

# padrão de projeto command

class Pedido(object):

    def __init__(self, cliente, valor) -> None:
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self) -> None:
        self.__pago = 'PAGO'

    def finaliza(self) -> None:
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self) -> None:
        return self.__cliente

    @property
    def valor(self) -> float:
        return self.__valor

    @property
    def status(self) -> str:
        return self.__status

    @property
    def data_finalizacao(self) -> date:
        return self.__data_finalizacao


class Comando(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class ConcluiPedido(Comando):
    def __init__(self, pedido) -> None:
        self.__pedido = pedido

    def executa(self) -> None:
        self.__pedido.finaliza()

class PagaPedido(Comando):
    def __init__(self, pedido) -> None:
        self.__pedido = pedido

    def execute(self) -> None:
        self.__pedido.paga()


class FilaDeTrabalho(object):

    def __init__(self) -> None:
        self.__comandos = []

    def adiciona(self, comando) -> None:
        self.__comandos.append(comando)

    def processa(self) -> None:
        for comando in self.__comandos:
            comando.executa()

if __name__ == '__main__':
    pedido1 = Pedido('Flavio', 200)
    pedido2 = Pedido('Almeida', 400)

    fila_de_trabalho = FilaDeTrabalho()

    comando1 = ConcluiPedido(pedido1)
    comando2 = PagaPedido(pedido1)
    comando3 = ConcluiPedido(pedido2)

    fila_de_trabalho.adiciona(comando1)
    fila_de_trabalho.adiciona(comando2)
    fila_de_trabalho.adiciona(comando3)

    fila_de_trabalho.processa()


