from rich import print

class Caneta:
    def __init__(self, cor, destampada=False):
        escolha = ''
        match cor.lower().strip():
            case 'azul':
                escolha = '[blue]'
            case 'vermelho' | 'vermelha':
                escolha = '[red]' 
            case 'verde':
                escolha = '[green]'

        self.caneta = cor
        self.destampada = destampada

    def escrever(self, msg):
        print(f'{self.caneta}{msg}[/]', end='')
        
    def destampar(self):
        if not self.destampada:
            print(f'A {self.caneta} está tampada')
            return
        

c1 = Caneta('azul')
c1.escrever('Olá, mundo!')