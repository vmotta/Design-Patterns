class Orcamento(object):

    def __init__(self, valor) -> None:
        self.__valor = valor
        
    # criando uma property
    @property
    def valor(self) -> float:
        return float(self.__valor)

if __name__ == '__main__':
    orcamento = Orcamento(500)
    print(orcamento.valor)