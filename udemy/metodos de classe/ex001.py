

class Pessoa:
    ano = 2026 

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', 23)
    
p1 = Pessoa('Gabriel', 27)
p2 = Pessoa.criar_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(27)
# print(p2.nome, p2.idade)
# print(p3.nome, p3.idade)
# print(p4.nome, p4.idade)
# print(Pessoa.ano)
# print(p1.nome, p1.idade)
# Pessoa.metodo_de_classe()



