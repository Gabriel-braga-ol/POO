class ContaBancaria:
    def __init__(self, id, nome, saldo):
        """
        Cria uma conta bancária e permite fazer saques e depósitos
        """
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}')

    def __str__(self):
        return f'A conta {self.id} de nome {self.titular} possui saldo de R${self.saldo:,.2f}'

    def __getstate__(self):
        return f'Estado: id = {self.id} ; titular = {self.titular} ; saldo = {self.saldo}'
   
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de {valor:.2f} não autorizado. Valor insificiente')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')



c1 = ContaBancaria(id=112, nome='Gabriel', saldo=5000)
c1.depositar(500)
c1.sacar(6000)
print(c1)
# print(c1.__doc__)
# print(c1.__getstate__())