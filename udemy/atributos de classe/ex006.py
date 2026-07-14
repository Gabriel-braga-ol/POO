# Atributos de classe - se alterar esse atributo, será alterado para todas as intâncias

class Pessoa:
    ano_atual = 2026 # Atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def nascimento(self):
        return Pessoa.ano_atual - self.idade #Sempre prefira usar o nome da clase

p1 = Pessoa('Gabriel', 27)
p2 = Pessoa('Maria', 15)
p3 = Pessoa('Luiz', 35)
print(Pessoa.ano_atual)
print(p1.nascimento())
print(p2.nascimento())
print(p3.nascimento())
