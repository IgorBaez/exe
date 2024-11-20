class Circulo:
    def __init__(self,raio):
        self.raio=raio
      
    def __str__(self):
        pi = 3.14159
        return 2*pi*self.raio
    
pessoa1=Circulo(5)
print(pessoa1.__str__())
