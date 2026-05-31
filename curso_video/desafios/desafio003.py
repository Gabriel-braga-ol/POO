class churrasco:
    def __init__(self, titulo, qtd):
        self.nome = titulo
        self.qtd = qtd
        
    def __str__(self):
        return f'Analisando o {self.nome} para {self.qtd} pessoas'
    
    def analisar(self, qtd):
        for qtd in self.qtd:
            resp = self.qtd * 400
            print(resp)
        
    


c1 = churrasco(titulo='Churrasco dos amigos', qtd=15)
print(c1)
c1.analisar()