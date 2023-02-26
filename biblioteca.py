"The Factory Concept"
from abc import ABCMeta, abstractmethod

class LivrosID:
    "A Hypothetical Class Interface (Product)"

    @classmethod
    @abstractmethod
    def create_object(cls):
        "An abstract interface method"
        pass

class manga(LivrosID):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.nome="Berserk"
        self.formato = "ebook"
        self.preco = 30
        
    def create_object(self):
        return self

class HQs(LivrosID):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.nome= "Lanterna Verde"
        self.formato = "fisico"
        self.preco = 15

    def create_object(self):
        return self

class ficcao(LivrosID):
    "A Concrete Class that implements the IProduct interface"

    def __init__(self):
        self.nome="materia escura"
        self.formato = "ebook"
        self.preco = 6

    def create_object(self):
        return self 

class Creator:
    "The Factory Class"

    @classmethod
    def create_object(cls, some_property):
        "A class method to get a concrete product"
        if some_property == 'manga':
            return manga()
        if some_property == 'HQs':
            return HQs()
        if some_property == 'ficcao':
            return ficcao()
        return None



print("==================")
manga= manga()
print("Nome:", manga.nome)
print("Formato:", manga.formato)
print("Preço:", manga.preco)

print("==================")
hqs = HQs()
print("Nome:", hqs.nome)
print("Formato:", hqs.formato)
print("Preço:", hqs.preco)

print("==================")

ficcao = ficcao()
print("Nome:", ficcao.nome)
print("Formato:", ficcao.formato)
print("Preço:", ficcao.preco)