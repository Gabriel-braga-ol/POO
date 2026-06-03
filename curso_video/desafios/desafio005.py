class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = []

    def add_favoritos(self, jogos):
        self.favoritos.append(jogos)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Jogador: {self.nick}\n'
        conteudo += f'Nome real: {self.nome}\n'
        conteudo += f'Jogos favoritos:\n'
        for num, game in enumerate(self.favoritos):
            conteudo += f'{game}\n'
        print(conteudo)

g1 = Gamer('Gabriel Braga', 'Samurai')
g1.add_favoritos('Cyberpunk')
g1.add_favoritos('CoD')
g1.add_favoritos('The Witcher 3')
g1.add_favoritos('God of War')
g1.ficha()

g2 = Gamer('Maria Rodrigues', 'peach_raivosa')
g2.add_favoritos('Sonic')
g2.add_favoritos('The Sims')
g2.add_favoritos('GTA')
g2.add_favoritos('Mario Bros')
g2.ficha()