from datetime import date
from observadores import *

# design pattern observer


class Item(object):
    """
    Item Classe que reperesenta um item da nota fiscal

    Args:
        object ([object]): [description]
    """

    def __init__(self, descricao, valor) -> str:
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self) -> str:
        return self.__descricao

    @property
    def valor(self) -> float:
        return self.__valor


class NotaFiscal(object):
    """
    NotaFiscal classe de representação de uma nota Fiscal
    """

    def __init__(self, razao_social='', cnpj='', itens=[], data_de_emissao=date.today(), detalhes='', observadores=[]) -> None:
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception(
                "Detalhes da Nota Fiscal não pode ser maiores que 20 caracteres!")
        self.__detalhes = detalhes
        self.__itens = itens

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self) -> str:
        return self.__razao_social

    @property
    def cnpj(self) -> str:
        return self.__cnpj

    @property
    def data_de_emissao(self) -> str:
        return self.__data_de_emissao

    @property
    def detalhes(self) -> str:
        return self.__detalhes


if __name__ == '__main__':

    from criador_de_nota_fiscal import CriadorDeNotaFiscal

    itens = [
        Item('Item A', 100),
        Item('Item B', 200),
    ]

    nota_fiscal = NotaFiscal(
        razao_social='FHSA limitada',
        cnpj='01231456789',
        itens=itens,
        data_de_emissao=date.today(),
        detalhes='',
        observadores=[imprime, envia_por_email, salva_no_banco]
    )

    # nota_fiscal_builder = (CriadorDeNotaFiscal()
    #                        .com_razao_social('FHSA limitada')
    #                        .com_cnpj('01231456789')
    #                        .com_itens(itens)
    #                        .com_data_de_emissao(date.today())
    #                        .constroi())
