

class Animal:
    #escopo da classe

    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor' #escopo do __init__
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal(nome='Simba')
print(leao.nome)
print(leao.comendo('banana'))
print(leao.executar('carne'))