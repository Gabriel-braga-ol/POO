from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, lado=0):
        self.lado = lado

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(lado)

    def area(self, qtd):
        self.lado += qtd
        return f'Área: {self.lado * 2}'

    def perimetro(self, valor):
        self.lado += valor
        return f'Perimetro: {4 * self.lado}'

p1 = Quadrado(12)
print(p1.area(12))
print(p1.perimetro(12))
    