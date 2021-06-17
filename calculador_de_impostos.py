from impostos import calcula_ISS, calcula_ICMS
# passagem de algorítmo para implementação da lógica (estratégias) 
# como parâmetro é o padrão de projetos Strategy
class CalculadorDeImpostos(object):
    # funções podem ser passadas como parâmetros, colocadas em variáveis
    # pois são cidadãs de primeira classe em python
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto(orcamento)
        print(imposto_calculado)

if __name__ == '__main__':
    from orcamento import Orcamento
    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)
    # função passada como parâmetro para cálculo dos impostos
    calculador.realiza_calculo(orcamento, calcula_ISS)
    calculador.realiza_calculo(orcamento, calcula_ICMS)
    calculador.realiza_calculo(orcamento, calcula_ICMS)
