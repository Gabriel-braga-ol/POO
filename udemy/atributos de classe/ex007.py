# __dict__ e vars para atributos de instâncias

class Pessoa:
    ano_atual = 2026 # Atributo da classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def nascimento(self):
        return Pessoa.ano_atual - self.idade #Sempre prefira usar o nome da clase

p1 = Pessoa('Gabriel', 27)

# p1.nome = 'EITA'
# print(p1.nome) # alterando o nome

# print(p1.__dict__) # retém os valores do objetos em dicionário

p1.__dict__['outra'] = 'coisa' # cria uma nova chave no dicionário
p1.__dict__['nome'] = 'Carlos' # altera o valor da chave nome
print(p1.__dict__)


