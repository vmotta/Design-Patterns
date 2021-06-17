# -*- coding: UTF-8 -*-
from orcamento_2 import Orcamento, Item
from descontos import DescontoPorCincoItens, DescontoPorMaisDeQuinhentosReais, SemDesconto
class CalculadorDeDescontos(object):
    def calcula(self, orcamento) -> float:
        desconto = DescontoPorCincoItens(
            DescontoPorMaisDeQuinhentosReais(SemDesconto())
        ).calcula(orcamento)

        return desconto

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adciciona_item(Item('Item - 1', 100))
    orcamento.adciciona_item(Item('Item - 2', 50))
    orcamento.adciciona_item(Item('Item - 3', 400))

    print(f" O valor do orçamento é: {orcamento.valor}")

    calculador = CalculadorDeDescontos()
    desconto_calculado = calculador.calcula(orcamento)

    print(f" O valor do desconto é: {desconto_calculado}")

    orcamento.adciciona_item(Item('Item - 4', 100))
    orcamento.adciciona_item(Item('Item - 5', 50))
    orcamento.adciciona_item(Item('Item - 6', 400))

    print(f" O valor do orçamento é: {orcamento.valor}")

    calculador = CalculadorDeDescontos()
    desconto_calculado = calculador.calcula(orcamento)

    print(f" O valor do desconto é: {desconto_calculado}")