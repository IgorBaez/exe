class Retangulo:
    def __init__(self, largura, altura):
        self.lar = largura
        self.alt = altura

    def calcular_area(self):
        print( self.lar * self.alt)
retangulo1 = Retangulo(5, 10)
retangulo1.calcular_area()