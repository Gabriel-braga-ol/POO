from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome = '', idade = 0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1

    @abstractmethod
    def estudar(self):
        pass


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f'O aluno {self.nome} acabou de fazer matricula')

    def estudar(self):
        print(f'{self.nome} está estudando {self.curso} na turma {self.turma}')


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f'O professor {self.nome} acabou de dar aula')

    def estudar(self):
        print(f'O professor {self.nome} é especialista em {self.especialidade} no nível {self.nivel}.')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print(f'A funcionária {self.nome} acabou de bater ponto')

    def estudar(self):
        print(f'A funcionário {self.nome} atua como {self.cargo} no setor {self.setor}')


def main():
    a1 = Aluno('Gabriel', 17, 'Informática', 'T01')
    a1.fazer_aniversario()
    a1.fazer_matricula()
    a1.estudar()
    # inspect(a1, methods=True)

    p1 = Professor('Samuel', 35, 'Biologia', 'Mestrado')
    p1.fazer_aniversario()
    p1.dar_aula()
    p1.estudar()
    # inspect(p1, methods=True)

    f1 = Funcionario('Maria', 28, 'Secretária', 'Diretoria')
    f1.fazer_aniversario()
    f1.bater_ponto()
    f1.estudar()
    # inspect(f1, methods=True)


if __name__ == '__main__':
    main()