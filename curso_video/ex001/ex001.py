# Declaração de classes:
class Gafanhoto:
    def __init__(self): #Método construtor
        #Atributos de instância
        self.nome = ''
        self.idade = 0

    #Métodos de instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade' 
    
# Declaração de objetos:
g1 = Gafanhoto()
g1.nome = 'Gabriel'
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Maria'
g2.idade = 20
g2.aniversario()
print(g2.mensagem())