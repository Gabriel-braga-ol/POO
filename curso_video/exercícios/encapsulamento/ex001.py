class ContaBancaria:
    def __init__(self, id, nome, saldo):
        """
        Cria uma conta bancária e permite fazer saques e depósitos
        """
        self.id = id
        self._titular = nome
        self.__saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.__saldo:,.2f}')

    def __str__(self):
        # return f'A conta {self.id} de nome {self.titular} possui saldo de R${self.saldo:,.2f}'
        return f'Estado atual da conta: {self.__dict__}'

    def __getstate__(self):
        return f'Estado: id = {self.id} ; titular = {self._titular} ; saldo = {self.__saldo}'
   
    def depositar(self, valor):
        valor = abs(valor)
        self.__saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}')

    def sacar(self, valor):
        valor = abs(valor)
        if valor > self.__saldo:
            print(f'Saque de {valor:.2f} não autorizado. Valor insificiente')
        else:
            self.__saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')

