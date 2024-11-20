class Quadrado:
    def __init__(self, lado):
        self.lado = lado
    def calcular_area(self):
        return self.lado ** 2
    def calcular_perimetro(self):
        return 4 * self.lado
quadrado1 = Quadrado(7)
print("A área do quadrado é: ",quadrado1.calcular_area())
print("O perímetro do quadrado é:",quadrado1.calcular_perimetro())