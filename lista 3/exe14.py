
class Eletrodomestico:
    def __init__(self, nome, potencia):
        self.nome = nome  
        self.potencia = potencia 
        self.ligado=False
    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print(self.nome,'está ligado e consome',self.potencia,'watts.')

eletrodomestico1 = Eletrodomestico("Geladeira", 150)
eletrodomestico1.ligar()  

eletrodomestico2 = Eletrodomestico("Micro-ondas", 1200)
eletrodomestico2.ligar()  
