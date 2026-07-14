# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

# class Produto:
#     def __init__(self, preco):
#         self.preco = preco   # já chama o setter aqui embaixo!

#     @property
#     def preco(self):
#         return self._preco

#     @preco.setter
#     def preco(self, valor):
#         if valor < 0:
#             raise ValueError("Preço não pode ser negativo")
#         self._preco = valor

# p = Produto(100)
# print(p.preco)    # 100 (chama o getter)

# p.preco = 150     # OK, chama o setter, passa na validação
# print(p.preco)    # 150

# p.preco = -50     # ValueError: Preço não pode ser negativo

class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)