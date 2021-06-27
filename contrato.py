from datetime import date

# padrão de projetos chamado memento

class Contrato(object):
    def __init__(self, data, cliente, tipo) -> None:
        self.__data = data
        self.__cliente = cliente
        self.__tipo = tipo

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data) -> None:
        self.__data = data

    @property
    def cliente(self) -> str:
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente) -> None:
        self.__cliente = cliente

    @property
    def tipo(self) -> None:
        return self.__tipo

    def avanca(self) -> None:
        if self.__tipo == 'NOVO':
            self.__tipo = 'EM ANDAMENTO'
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO':
            self.__tipo = 'CONCLUIDO'

    def salva_estado(self) -> None:
        return Estado(Contrato(data=self.__data,
                               cliente=self.__cliente,
                               tipo=self.__tipo))

    def restaura_estado(self, estado) -> None:
        self.__cliente = estado.contrato.cliente
        self.__data = estado.contrato.data
        self.__tipo = estado.contrato.tipo


class Estado(object):
    def __init__(self, contrato) -> None:
        self.__contrato = contrato

    @property
    def contrato(self) -> Contrato:
        return self.__contrato


class Historico(object):
    def __init__(self) -> None:
        self.__estados_salvos = []

    def obtem_estado(self, indice) -> Estado:
        return self.__estados_salvos[indice]

    def adiciona_estados(self, estado) -> None:
        self.__estados_salvos.append(estado)


if __name__ == '__main__':
    historico = Historico()
    contrato = Contrato(data=date.today(),
                        cliente='Flavio Almeida',
                        tipo='NOVO')
    contrato.avanca()
    historico.adiciona_estados(contrato.salva_estado())
    contrato.avanca()
    historico.adiciona_estados(contrato.salva_estado())
    contrato.avanca()
    historico.adiciona_estados(contrato.salva_estado())
    print(contrato.tipo)

    contrato.restaura_estado(historico.obtem_estado(1))
    print(contrato.tipo)