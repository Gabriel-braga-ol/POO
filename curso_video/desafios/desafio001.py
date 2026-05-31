class Funcionario:
    #Atributos de classe
    empresa = 'curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        #Atributos de instância 
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f'Olá, me chamo {self.nome} e sou {self.cargo} no setor de {self.setor} da empresa {Funcionario.empresa}'
    

f1 = Funcionario(nome='Maria', setor='administração', cargo='diretora')
print(f1.apresentacao())

f2= Funcionario(nome='João', setor='finanças', cargo='estagiário')
print(f2.apresentacao())