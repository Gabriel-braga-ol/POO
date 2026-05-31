class Livro:
    def __init__(self, livro, pagina=0):
        self.nome = livro
        self.pagina = pagina

    def passando_paginas(self, paginas):
        for paginas in self.pagina:
            if self.pagina > paginas:
                print('Você não pode mais avançar paginas')
            else:
                self.pagina += 1




l1 = Livro(livro='Python', pagina=20)
l1.passando_paginas(5)