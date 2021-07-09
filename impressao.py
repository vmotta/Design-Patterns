class Impressao(object):

    def visita_soma(self, soma) -> None:
        print('(', soma.expressao_esquerda.aceita(self),
         '+', soma.expressao_direita.aceita(self), ')')

    def visita_subtracao(self, subtracao) -> None:
        print('(', subtracao.expressao_esquerda.aceita(self),
              '-', subtracao.expressao_direita.aceita(self), ')')


    def visita_numero(self, numero) -> None:
        print(numero.avalia())
