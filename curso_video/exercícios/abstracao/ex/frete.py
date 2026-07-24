# fretes para veículos diferentes
from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete():
        pass


class Moto(Transporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)
        
    def calc_frete(self):
        self.frete = self.distancia * Moto.fator
        return f'R${self.frete:.2f}'

class Caminhao(Transporte):
    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 50:
            self.frete = 0
            return f'Raio minímo 50Km'
        else:
            self.frete = self.distancia * Caminhao.fator
            return f'R${self.frete:.2f}'


class Drone(Transporte):
    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 10:
            self.frete = 0
            return f'Raio máximo de 10Km'
        else:
            self.frete = self.distancia * Drone.fator
            return f'R${self.frete:.2f}'

def main():
    dist = 5
    t1 = Drone(dist)
    print(f'Frete de {type(t1).__name__} para {dist}Km = {t1.calc_frete()}')

if __name__ == '__main__':
    main()