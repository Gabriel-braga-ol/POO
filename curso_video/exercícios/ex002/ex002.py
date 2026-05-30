class Gafanhoto:
    def __init__(self, nome = '', idade = 0): #Método construtor
        """
    Essa classe cria um gafanhoto, que é uma pessoa qu epossui nome e idade
    Para criar um novo gafanhot, use:
    variável = Gafanhoto(nome, idade)
        """
        #Atributos de instância
        self.nome = nome
        self.idade = idade

    #Métodos de instância
    def aniversario(self):
        self.idade += 1    

    def __str__(self): # Dunder method
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade' 
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade}'
    
# Declaração de objetos:
g1 = Gafanhoto('Gabriel', 27)
g1.aniversario()
# print(g1)
# print(g1.__dict__) #Atributo
print(g1.__getstate__()) #Método
print(g1.__class__)