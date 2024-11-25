class Retangulo:
    def __init__(self,ladoA,ladoB):
        self.ladoA=ladoA
        self.ladoB=ladoB

    def mostra_area(self):
        resp=self.ladoA*self.ladoB
        print("a area e ",resp)
    
    def mudar_valor_lado(self):
        self.ladoA=int(input("Dgt o novo ladoA "))
        self.ladoB=int(input("Dgt o novo ladoB "))
        resp=self.ladoA*self.ladoB
        print("a area e ",resp)

    def rodape(self):
        rodape=(self.ladoA*2)+(self.ladoB*2)
        print("o rodape e ",rodape)


comprimento=int(input("Dgt o comprimento "))
largura=int(input("Dgt o largura "))

quadrado1=Retangulo(comprimento,largura)
quadrado1.mostra_area()
quadrado1.mudar_valor_lado()
quadrado1.rodape()