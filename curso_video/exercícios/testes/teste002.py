class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2 * (self.largura + self.altura)
    
    def __str__(self):
        return (
            f'Retângulo: largura = {self.largura}, altura = {self.altura}\n'
            f'Área = {self.area()} - perimetro = {self.perimetro()}'
        )


r1 = Retangulo(5, 3)
r2 = Retangulo(10, 5)

print(r1)
print(r2)