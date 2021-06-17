# Padrão de projeto Chain of Responsibility, 
# cada nó da cadeia tem a responsabilidade de chamar o proximo 
# até chamar o último que retornará zero
class DescontoPorCincoItens(object):

    def __init__(self, proximo_desconto) -> None:
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento) -> float:
        if orcamento.total_de_itens() > 5:
            return float(orcamento.valor * 0.1)
        else:
            return self.__proximo_desconto.calcula(orcamento)
        
class DescontoPorMaisDeQuinhentosReais(object):

    def __init__(self, proximo_desconto) -> None:
        self.__proximo_desconto = proximo_desconto

    def calcula(self, orcamento) -> float:
        if orcamento.valor > 500:
            return float(orcamento.valor * 0.07) 
        else:
            return self.__proximo_desconto.calcula(orcamento)

class SemDesconto(object):

    def calcula(self) -> int:
        return 0