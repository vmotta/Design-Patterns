from impostos_novos_POO import *
# passagem de algorítmo para implementação da lógica (estratégias) 
# como parâmetro é o padrão de projetos Strategy
class CalculadorDeImpostos(object):
    # funções podem ser passadas como parâmetros, colocadas em variáveis
    # pois são cidadãs de primeira classe em python
    def realiza_calculo(self, orcamento, imposto):
        # Estratégia de duck typing se o objeto tem o método calcula 
        # não tem problema -> se anda como pato, voa como pato 
        # e nada como pato é um pato 
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento
    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)
    # função passada como parâmetro para cálculo dos impostos
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, IKCV())
    calculador.realiza_calculo(orcamento, ICPP())
