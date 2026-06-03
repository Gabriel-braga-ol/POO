class Churrasco:
    #Atributos de classe
    consumo_padrao:float = 0.400 
    preco_por_kg:float = 82.40 

    def __init__(self, titulo, qtd):
        #Atributos de instância
        self.nome = titulo
        self.qtd = qtd
        
    def __str__(self):
        return f'Esse é o {self.nome} com {self.qtd} pessoas participando'

    def consumo(self):
        return self.qtd * Churrasco.consumo_padrao 
    
    def custo_total(self):
        return Churrasco.preco_por_kg * self.consumo()
    
    def preco_por_pessoa(self):
        return self.custo_total() / self.qtd
       
    def analisar(self):
        conteudo = f'Analisando o {self.nome} para {self.qtd} pessoas\n'
        conteudo += f'Cada pessoa consumirá {Churrasco.consumo_padrao}Kg e cada Kg custa R${Churrasco.preco_por_kg:.2f}\n'
        conteudo += f'Recomendo comprar {self.consumo():.3f}Kg de carne\n'
        conteudo += f'O custo total será de R${self.custo_total():,.2f}\n'
        conteudo += f'Cada pessoa deverá pagar R${self.preco_por_pessoa():.2f}'
        print(conteudo)
         
c1 = Churrasco(titulo='Churrasco dos amigos', qtd=15)
c1.analisar()
print(' ')
c2 = Churrasco(titulo='Festa dos crias', qtd=80)
c2.analisar()