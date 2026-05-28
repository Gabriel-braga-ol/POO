# Atributos de classe

class Pessoa:
    ano_atual = 2026 # Atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def nascimento(self):
        return Pessoa.ano_atual - self.idade

p1 = Pessoa('Gabriel', 27)
p2 = Pessoa('Maria', 15)
print(Pessoa.ano_atual)
print(p1.nascimento())
print(p2.nascimento())
