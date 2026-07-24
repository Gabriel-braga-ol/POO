from abc import ABC, abstractmethod

class BebidaQuente():

    def ferver_agua(self):
        print('1. ferverndo água a 100 graus Celsius')

    @abstractmethod
    def preparar(self):
        pass

    @abstractmethod
    def servir(self):
        pass

class cafe(BebidaQuente):
    def preparar(self):
        self.ferver_agua()
        print('2. Passando água pressurizada pelo pó moído.')

    def servir(self):
        print('3. Servindo em xícara pequena')

class cha(BebidaQuente):
    def preparar(self):
        self.ferver_agua()
        print('2. Mergulhando o sachê de ervas na água.') 

    def servir(self):
        print('3. Servindo na caneca de porcelana com limão.')


class leite(BebidaQuente):
    def preparar(self):
        self.ferver_agua()
        print('2. Passando água pressurizada pelo bico do leite.')

    def servir(self):
        print('3. Servindo na caneca grande')

def main():
    b1 = cafe()
    b1.preparar()
    b1.servir()

    print()

    b2 = cha()
    b2.preparar()
    b2.servir()

    print()

    b3 = leite()
    b3.preparar()
    b3.servir()

if __name__ == '__main__':
    main()