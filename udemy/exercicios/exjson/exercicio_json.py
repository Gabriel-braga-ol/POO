# Salve os dados da sua classe em json
# e depois crie as intâncias da classe 
# novamente com os dados salvos
# Faça em arquivos separados
import json

CAMINHO_ARQUIVADO = 'exercicio_jsonb'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('Gabriel', 27)
p2 = Pessoa('Maria', 35)
p3 = Pessoa('João', 18)

bd = [vars(p1),p2.__dict__,vars(p3)]

with open(CAMINHO_ARQUIVADO, 'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)


