from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca=100):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            alvo.receber_dano(forca)
            return f'{self.nome} atacou {alvo.nome} com um {golpe} de força {forca}'

        else:
            return f'O ataque {self.nome} -> {alvo.vida} não pode acontecer.'

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        return f'O {self.nome} recebeu um dano de {fator}'

    @abstractmethod
    def curar(self):
        pass

class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Lâmina cortante', 'Golpe de machado', 'Golpe supersônico']

    
    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator

        return f'O {self.nome} enrolou uma atadura no ferimento e recuperou {fator} de vida'


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bola de fogo', 'Golpe de gelo', 'Eletrificar']
    

    def curar(self):
        fator = random.randint(0, 100)
        self.vida += fator
        
        return f'O {self.nome} lançou uma magia no ferimento e recuperou {fator} de vida'

def main():
    p1 = Guerreiro('Pikachu', 1000)
    p2 = Guerreiro('Mario', 1000)
    p3 = Mago('Gandalf', 1000)
    print(p1.atacar(p2, 100))
    print(p2.atacar(p3, 100))
    print(p2.receber_dano(100))
    print(p3.receber_dano(100))
    print(p2.curar())
    print(p3.curar())

if __name__ == '__main__':
    main()
