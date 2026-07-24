"""
    🟢 NÍVEL 1 - BÁSICO
    ===================
    Exercício: Classe Livro

    Conceitos trabalhados:
    ✅ __init__ (construtor)
    ✅ __str__ (representação em string)
    ✅ Métodos de instância
    ✅ Atributos de instância
"""

class Livro:
    """Representa um livro com título, autor, número de páginas e estado de leitura."""

    def __init__(self, titulo, autor, paginas):
        """
        Construtor do livro.

        Parâmetros:
            titulo (str): Título do livro
            autor (str): Nome do autor
            paginas (int): Número total de páginas
        """
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.pagina_atual = 0  # Começa na página 0 (fechado)
        self.aberto = False

    def __str__(self):
        """Representação amigável do livro."""
        status = 'aberto' if self.aberto else 'fechado'
        return (f'📖 "{self.titulo}" por {self.autor} | '
                f'{self.pagina_atual}/{self.paginas} páginas | '
                f'Status: {status}')

    def abrir(self):
        """Abre o livro para leitura."""
        if self.aberto:
            print(f'O livro "{self.titulo}" já está aberto.')
            return
        self.aberto = True
        print(f'📖 Você abriu "{self.titulo}". Boa leitura!')

    def fechar(self):
        """Fecha o livro."""
        if not self.aberto:
            print(f'O livro "{self.titulo}" já está fechado.')
            return
        self.aberto = False
        print(f'📕 Você fechou "{self.titulo}".')

    def ler_pagina(self):
        """Avança uma página se o livro estiver aberto."""
        if not self.aberto:
            print(f'❌ O livro "{self.titulo}" está fechado. Abra-o primeiro!')
            return

        if self.pagina_atual >= self.paginas:
            print(f'🏁 Você já terminou "{self.titulo}"!')
            return

        self.pagina_atual += 1
        print(f'📄 Página {self.pagina_atual} lida...')

    def voltar_pagina(self):
        """Volta uma página se o livro estiver aberto."""
        if not self.aberto:
            print(f'❌ O livro "{self.titulo}" está fechado. Abra-o primeiro!')
            return

        if self.pagina_atual <= 0:
            print('⏮️ Você já está na primeira página.')
            return

        self.pagina_atual -= 1
        print(f'⏪ Voltou para a página {self.pagina_atual}')

    def progresso(self):
        """Retorna o percentual de leitura."""
        if self.paginas == 0:
            return 0
        return (self.pagina_atual / self.paginas) * 100


# =============================================
# TESTES / EXEMPLOS DE USO
# =============================================
if __name__ == '__main__':
    print('=' * 50)
    print('📚 TESTE DA CLASSE LIVRO')
    print('=' * 50)

    # Criando um livro
    livro1 = Livro('O Pequeno Príncipe', 'Antoine de Saint-Exupéry', 96)
    livro2 = Livro('1984', 'George Orwell', 328)

    print('\n--- Livros criados ---')
    print(livro1)
    print(livro2)

    print('\n--- Interagindo com o livro 1 ---')
    livro1.abrir()
    livro1.ler_pagina()
    livro1.ler_pagina()
    livro1.ler_pagina()
    print(f'Progresso: {livro1.progresso():.1f}%')
    livro1.fechar()

    print('\n--- Tentando ler com livro fechado ---')
    livro1.ler_pagina()  # Deve dar erro

    print('\n--- Estado final ---')
    print(livro1)
    print(livro2)

