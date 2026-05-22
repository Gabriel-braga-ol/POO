# Métodos em instâncias de classes python
# Instância e objeto geralmente são a mesma coisa
# Hard coded - é algo que foi escrito diretamente no código
# Self - é uma covenção utilizada para referênciar a própria istância - SEMPRE é o primeiro parâmetro

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
