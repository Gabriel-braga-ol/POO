class Estudante:

    cont = 0
    nota_total = 0

    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
        Estudante.cont += 1
        Estudante.nota_total += nota


    def get_info(self):
        return f'{self.nome} {self.nota}'

    @classmethod
    def avg_info(cls):
        if cls.cont == 0:
            return 0
        else:
            return f'Média dos alunos: {cls.nota_total / cls.cont:.2f}'
        
    @property
    def total_alunos(self):
        return f'O total de alunos é: {self.cont}'
    
    

s1 = Estudante('Gabriel', 3.2)     
s2 = Estudante('Maria', 2.0)     
s3 = Estudante('Carlos', 4.0)     
s4 = Estudante('Carlos', 8.2)     
s5 = Estudante('Carlos', 4.0)     
s6 = Estudante('Carlos', 4.0)     

print(Estudante.get_info(s1))
print(Estudante.get_info(s2))
print(Estudante.get_info(s3))
print(Estudante.avg_info())
print(s1.total_alunos)

# class Cachorro:
#     total_cachorros = 0   # atributo de classe

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         Cachorro.total_cachorros += 1

#     @classmethod
#     def contar(cls):
#         return cls.total_cachorros   # acessa o atributo da CLASSE, não de uma instância

# rex = Cachorro("Rex", 3)
# bidu = Cachorro("Bidu", 2)

# print(Cachorro.contar())  # 2 — chamado na classe, sem precisar de uma instância

