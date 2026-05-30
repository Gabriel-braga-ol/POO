class Aluno:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota
       
    def __str__(self):
         return f'O(a) aluno(a) {self.nome} de {self.idade} anos possui nota {self.nota}'
    
    def __getstate__(self):
        return f'Estado: nome = {self.nome} ; idade = {self.idade} ; nota = {self.nota}' 

    def aprovado(self):
        if self.nota > 7:
            return f'O(a) aluno(a) {self.nome} está aprovado'
        else:
            return f'O(a) aluno(a) {self.nome} está reprovado'

a1 = Aluno(nome= 'Gabriel', idade= 18, nota= 8)
a2 = Aluno(nome= 'Maria', idade= 19, nota= 5)
print(a1)
print(a2)
print(a1.__getstate__())
print(a2.__getstate__())
print(a1.aprovado())
print(a2.aprovado())