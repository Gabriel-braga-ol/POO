from abc import ABC, abstractmethod

class Funcionario():
    sal_minímo = 1612
    desconto_inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0
    
    @abstractmethod
    def calc_sal():
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.sal_minímo
        print(f'O saláario de {self.nome} é de R${self.salario:.2f} e corresponde a {base:.2f} salários mínimo.')

class Horista(Funcionario):
    def __init__(self, nome, valor_hora = 7.37, qtd_hora = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = qtd_hora
        self.sal_bruto = self.valor_hora * self.horas_trabalhadas

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desconto_inss / 100)
        return self.salario

class Mensalista(Funcionario):
    def __init__(self, nome, sal_bruto = Funcionario.sal_minímo):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.desconto_inss / 100)

def main():
    f1 = Mensalista('José', 8500)
    f1.calc_sal()
    f1.analisar_sal()

if __name__ == '__main__':
    main()
