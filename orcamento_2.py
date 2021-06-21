from abc import ABCMeta, abstractmethod

class EstadoDeUmOrcamento(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass

    @abstractmethod
    def aprova(self, orcamento):
        pass

    @abstractmethod
    def reprova(self, orcamento):
        pass

    @abstractmethod
    def finaliza(self, orcamento):
        pass

class EmAprovacao(EstadoDeUmOrcamento):

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()

    def finaliza(self, orcamento):
        raise Exception('Orçemento em aprovação não pode ser finalizado! ')

    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)

class Aprovado(EstadoDeUmOrcamento):

    def aprova(self, orcamento):
        raise Exception('Orçemento já foi aprovado! ')

    def reprova(self, orcamento):
        raise Exception('Orçemento aprovado não pode ser reprovado! ')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()


    def aplica_desconto_extra(self, orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)


class Reprovado(EstadoDeUmOrcamento):

    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado! ')

    def reprova(self, orcamento):
        raise Exception('Orçamento já reprovado! ')

    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    def aplica_desconto_extra(self, orcamento):
            raise Exception('Orçamento reprovados não recebem desconto extra')

class Finalizado(EstadoDeUmOrcamento):

    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser aprovado! ')

    def reprova(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser reprovado! ')

    def finaliza(self, orcamento):
        raise Exception('Orçamento finalizado não pode ser finalizado! ')

    def aplica_desconto_extra(self, orcamento):
            raise Exception('Orçamento finalizados não recebem desconto extra')

class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = EmAprovacao()
        self.__desconto_extra = 0

    def aprova(self):
        self.estado_atual.aprova(self)

    def reprova(self):
        self.estado_atual.reprova(self)

    def finaliza(self):
        self.estado_atual.finaliza(self)

    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)


    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto 
    
    # criando uma property
    @property
    def valor(self) -> float:
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return float(total - self.__desconto_extra)

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
    orcamento = Orcamento()
    orcamento.adciciona_item(Item('Item - 1', 100))
    orcamento.adciciona_item(Item('Item - 2', 50))
    orcamento.adciciona_item(Item('Item - 3', 400))

    print(f" O valor do orçamento é: {orcamento.valor}")


    orcamento.aprova()
    orcamento.aprova()
    orcamento.aplica_desconto_extra()
    print(f" O valor do orçamento é: {orcamento.valor}")
