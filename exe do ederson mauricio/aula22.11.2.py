class Quadrado:
    def __init__(self,lado):
        self.lado=lado

    def mostra_area(self):
        resp=self.lado**2
        print("a area e ",resp)
    
    def mudar_valor_lado(self):
        self.lado=int(input("Dgt o novo lado "))
        resp=self.lado**2
        print("a area e ",resp)

quadrado1=Quadrado(10)
quadrado1.mostra_area()
quadrado1.mudar_valor_lado()
        