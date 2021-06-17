class Orcamento(object):

    def __init__(self) -> None:
        self.__itens = []
        
    # criando uma property
    @property
    def valor(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return float(total)

    def obter_itens(self) -> list:
        return self.__itens

    def total_de_itens(self) -> int:
        return int(len(self.__itens))

    def adciciona_item(self, item) -> None:
        self.__itens.append(item)

class Item(object):
    def __init__(self, nome, valor) -> None:
        self.__nome = nome
        self.__valor = valor

    # criando uma property
    @property
    def valor(self) -> float:
        return float(self.__valor)

if __name__ == '__main__':
    orcamento = Orcamento(500)
    print(orcamento.valor)