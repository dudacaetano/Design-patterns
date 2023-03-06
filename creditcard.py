from __future__ import annotations
from abc import ABC, abstractmethod


class AbstractCard(ABC):

    @abstractmethod
    def create_limite(self) -> AbstractLimite:
        pass 

    @abstractmethod
    def create_pontos(self) -> AbstractPontos:
        pass

'''Fabricas concretas criam familias de produtos de uma variante 
   específica.O metodo da fabrica concreta retornam um produto abstrato
   enquanto dentro do método é intanciado um produto concreto'''
class CardAmex(AbstractCard):

    def create_limite(self) -> AbstractLimite:
        return LimiteAmex()

    def create_pontos(self) -> AbstractPontos:
        return PontosAmex()


class CardItaublack(AbstractCard):

    def create_limite(self) -> AbstractLimite:
        return LimiteItaublack()

    def create_pontos(self) -> AbstractPontos:
        return PontosItaublack()

'''Cada produto de uma familia deve ter uma classe base(interface)'''
class AbstractLimite(ABC):

    @abstractmethod
    def credit_limit(self) -> float:
        pass

'''Produtos concretos sao criados por suas correspondentes fabricas concretas'''
class LimiteAmex(AbstractLimite):

    def credit_limit(self) -> float:
        return "90.000"
    
class LimiteItaublack(AbstractLimite):

    def credit_limit(self) -> float:
        return "50.000"


class AbstractPontos(ABC):

    @abstractmethod
    def pontos_acumulados(self) -> float:
        pass

    
class PontosAmex(AbstractPontos):

    def pontos_acumulados(self) -> float:
        return "2.2"
        


class PontosItaublack(AbstractPontos):

    def pontos_acumulados(self) -> float:
        return "1.8"
        
    
'''B1 pode colaborar com qualquer instancia da clsse  ProdutoAbstrato_A
   recebida como argumento embora trabalhe corretamente apenas com A1
   (A1 possui todas as instância, etc...) '''
    
def card(factory: AbstractCard) -> None:

    limite = factory.create_limite()
    pontos = factory.create_pontos()
    print("O limite do cartao eh:"+limite.credit_limit())
    print("A cada 1 dolar gasto voce acumula essa quantidade de pontos:" + pontos.pontos_acumulados()) 


'''o codigo cliente pode trabalhar com qualquer classe de fabrica concreta'''

if __name__ == "__main__":

    print("Cartao Amex ")
    card(CardAmex())

    print("\n")

    print("Cartao Itau uniclass black")
    card(CardItaublack())
