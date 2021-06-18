# criando uma classe abstrata
from abc import ABCMeta, abstractmethod

# implementação do template method onde é criada uma classe 
# concreta e métodos abstratos para serem implementados pela 
# classe filha
class TamplateDeImpostoCondicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod 
    def deve_usar_maxima_taxacao(self,orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(self,orcamento):
        pass

    @abstractmethod
    def minima_taxacao(self,orcamento):
        pass

class ISS(object):
    def calcula(self, orcamento) -> float:
        return orcamento.valor * 0.1

class ICMS(object):
    def calcula(self, orcamento) -> float:
        return orcamento.valor * 0.06

class ICPP(TamplateDeImpostoCondicional):

    def deve_usar_maxima_taxacao(self,orcamento):
        if orcamento.valor > 500:
            return True
        else:
            return False
    
    def maxima_taxacao(self,orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self,orcamento):
        return orcamento.valor * 0.05

class IKCV(TamplateDeImpostoCondicional):
    
    def __tem_item_maior_que_cem_reais(self,orcamento):
        for item in orcamento.obter_itens():
           if item.valor > 100:
               return True
        return False

    def deve_usar_maxima_taxacao(self,orcamento):
        if orcamento.valor > 500 and self.__tem_item_maior_que_cem_reais():
            return True
        else:
            return False
    
    def maxima_taxacao(self,orcamento):
        return orcamento.valor * 0.01

    def minima_taxacao(self,orcamento):
        return orcamento.valor * 0.06
