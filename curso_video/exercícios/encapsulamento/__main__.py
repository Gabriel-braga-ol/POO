from ex001 import ContaBancaria

def main():
    c1 = ContaBancaria(111, 'Maria', 5000)
    c1.depositar(1000)
    c1.sacar(-100)
    c1.titular = 'Pedro'
    c1.saldo = 0
    print(c1)
if __name__ == '__main__':
    main()