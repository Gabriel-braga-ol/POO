"""
    🟢 NÍVEL 1 - BÁSICO
    ===================
    Exercício: Classe Cachorro

    Conceitos trabalhados:
    ✅ __init__ com parâmetros
    ✅ Métodos de ação (latir, correr, dormir, comer)
    ✅ Estado interno do objeto
    ✅ __str__ e representação
"""

class Cachorro:
    """Representa um cachorro com nome, raça, idade e estados de humor/ação."""

    def __init__(self, nome, raca, idade):
        """
        Construtor do cachorro.

        Parâmetros:
            nome (str): Nome do cachorro
            raca (str): Raça do cachorro
            idade (int): Idade em anos
        """
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 100       # 0 a 100
        self.fome = 0            # 0 a 100 (0 = satisfeito)
        self.acordado = True
        self.feliz = True

    def __str__(self):
        """Representação amigável do cachorro."""
        estado = 'acordado' if self.acordado else 'dormindo'
        humor = '😊 feliz' if self.feliz else '😠 irritado'
        return (f'🐶 {self.nome} ({self.raca}, {self.idade} anos) | '
                f'Energia: {self.energia}% | Fome: {self.fome}% | '
                f'{estado} | {humor}')

    def latir(self):
        """Faz o cachorro latir (gasta energia)."""
        if not self.acordado:
            print(f'😴 {self.nome} está dormindo e não pode latir.')
            return

        if self.energia < 10:
            print(f'😫 {self.nome} está muito cansado para latir.')
            return

        self.energia -= 5
        self.fome += 5
        print(f'🐕 {self.nome} late: Au! Au! Au!')

    def correr(self):
        """Faz o cachorro correr (gasta bastante energia)."""
        if not self.acordado:
            print(f'😴 {self.nome} está dormindo e não pode correr.')
            return

        if self.energia < 20:
            print(f'😫 {self.nome} está muito cansado para correr.')
            return

        self.energia -= 20
        self.fome += 15
        self.feliz = True
        print(f'🏃 {self.nome} está correndo feliz!')

    def comer(self, quantidade=30):
        """
        Faz o cachorro comer.

        Parâmetros:
            quantidade (int): Quanto a fome diminui (default 30)
        """
        if not self.acordado:
            print(f'😴 {self.nome} está dormindo. Acorde-o para comer.')
            return

        self.fome = max(0, self.fome - quantidade)
        self.energia += 10
        print(f'🍖 {self.nome} comeu deliciosamente! Fome: {self.fome}%')

    def dormir(self):
        """Faz o cachorro dormir e recuperar energia."""
        if not self.acordado:
            print(f'😴 {self.nome} já está dormindo.')
            return

        self.acordado = False
        self.energia = min(100, self.energia + 40)
        print(f'💤 {self.nome} foi dormir... Zzzz')

    def acordar(self):
        """Acorda o cachorro."""
        if self.acordado:
            print(f'{self.nome} já está acordado.')
            return

        self.acordado = True
        self.feliz = True
        print(f'☀️ {self.nome} acordou! Bom dia!')

    def brincar(self):
        """Brinca com o cachorro."""
        if not self.acordado:
            print(f'😴 {self.nome} está dormindo.')
            return

        if self.energia < 15:
            print(f'😫 {self.nome} está exausto para brincar.')
            return

        self.energia -= 15
        self.fome += 10
        self.feliz = True
        print(f'🎾 {self.nome} adora brincar! Rabinho abanando!')

    def esta_cansado(self):
        """Verifica se o cachorro está cansado."""
        return self.energia < 20

    def esta_com_fome(self):
        """Verifica se o cachorro está com fome."""
        return self.fome > 70


# =============================================
# TESTES / EXEMPLOS DE USO
# =============================================
if __name__ == '__main__':
    print('=' * 50)
    print('🐶 TESTE DA CLASSE CACHORRO')
    print('=' * 50)

    # Criando cachorros
    rex = Cachorro('Rex', 'Pastor Alemão', 3)
    bidu = Cachorro('Bidu', 'Vira-lata', 1)

    print('\n--- Cachorros criados ---')
    print(rex)
    print(bidu)

    print('\n--- Interagindo com o Rex ---')
    rex.latir()
    rex.correr()
    rex.brincar()
    rex.comer()
    print(rex)

    print('\n--- Rex cansado? ---')
    if rex.esta_cansado():
        print(f'{rex.nome} precisa descansar!')
        rex.dormir()
        rex.acordar()

    print('\n--- Estado final ---')
    print(rex)
    print(bidu)

