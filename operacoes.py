class Numero(object):
    
    def __init__(self, numero) -> None:
        self.__numero = numero

    def avalia(self) -> float:
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)

class Subtracao(object):

    # Domain Specif Language - DSL e design pattern interpreter

    def __init__(self, expressao_esquerda, expressao_direita) -> None:
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self) -> float:
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda

    @property
    def expressao_direita(self):
        return self.__expressao_direita


class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita) -> None:
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self) -> float:
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()

    def aceita(self, visitor):
        visitor.visita_soma(self)

    @property
    def expressao_esquerda(self) -> Numero:
        return self.__expressao_esquerda

    @property
    def expressao_direita(self) -> Numero:
        return self.__expressao_direita





if __name__ == '__main__':
    from impressao import Impressao

    # expressao_esquerda = Soma(Numero(10), Numero(20))
    # expressao_direita = Soma(Numero(5), Numero(2))
    # expressao_conta = Soma(expressao_direita, expressao_esquerda)
    impressao = Impressao()
    # expressao_conta.aceita(impressao)

    # expressao_conta2 = Subtracao(Numero(100), Numero(70))

    soma = Soma(Numero(10), Numero(20))
    soma.aceita(impressao)
