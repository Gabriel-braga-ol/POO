import time

class Livro:
    def __init__(self, livro, pagina):
        self.nome = livro
        self.pagina = pagina
        self.pagina_atual = 1

        print(f'Você acabou de abrir o livro {self.nome} que tem {self.pagina} paginas no total. Você está na pagina {self.pagina_atual}.')

    def passando_paginas(self, qtd= 1):
        cont = 0
        for pagina in range(0, qtd, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} >', end=' ')
                time.sleep(0.2)
                cont += 1
        print(f'Você avançou {cont} páginas e agora está na página {self.pagina_atual}')
        if self.fim_do_livro():
            print(f'Você chegou no fim do livro "{self.nome}"')

    def fim_do_livro(self):
        if self.pagina_atual == self.pagina:
            return True
        else:
            return False

l1 = Livro(livro='Aprendendo Python', pagina=20)
l1.passando_paginas(10)
l1.passando_paginas(5)
l1.passando_paginas(10)
l1.passando_paginas(10)
