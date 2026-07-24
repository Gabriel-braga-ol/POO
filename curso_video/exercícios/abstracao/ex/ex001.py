from abc import ABC, abstractmethod
import math

class Poligono(ABC):
    def __init__(self, lado):
        self.lado = lado

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def area(self):
        return f'Área: {self.lado ** 2:.1f}'

    def perimetro(self):
        return f'Perimetro: {4 * self.lado:.1f}'

class Retangulo(Poligono):
    def __init__(self, base = 1, altura = 1):
        super().__init__(4)
        self.base = base
        self.altura = altura

    def area(self):
        resp = self.altura * self.base
        return f'Área: {resp}mm2'

    def perimetro(self):
        return f'Perimetro: {2 * (self.base + self.altura)}mm2'

class Circulo(Poligono):
    def __init__(self, raio = 1):
        super().__init__(0)
        self.raio = raio

    def area(self):
        return f'Área: {math.pi * self.raio ** 2:.2f}Cm2'

    def perimetro(self):
        return f'Perimetro: {2 * math.pi * self.raio:.2f}Cm2'

def main():
    p1 = Retangulo(25, 10)
    print(p1.area())
    print(p1.perimetro())

    c1 = Circulo(12)
    print(c1.area())
    print(c1.perimetro())
    
if __name__ == '__main__':
    main()
        